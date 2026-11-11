import time

import requests

from common.logger import get_logger

logger = get_logger(__name__)

# 这些字段在日志中会被脱敏，避免账号密码泄露到日志文件
SENSITIVE_KEYS = {"password", "pwd", "passwd", "token", "csrf_token"}


def _mask(data):
    """对字典中的敏感字段打码，其他类型原样返回"""
    if isinstance(data, dict):
        return {
            key: "***" if str(key).lower() in SENSITIVE_KEYS else value
            for key, value in data.items()
        }
    return data


class RequestUtil():
    session_util = requests.session()

    def send_request(self, method, url, **kwargs):
        method = method.upper()
        logger.info("请求 %s %s | 参数: %s", method, url, _mask(kwargs.get("data")))
        start = time.perf_counter()
        try:
            res = RequestUtil.session_util.request(method=method, url=url, **kwargs)
        except requests.RequestException as e:
            cost_ms = (time.perf_counter() - start) * 1000
            logger.error("请求失败 %s %s | %s: %s | 耗时: %.0fms",
                         method, url, type(e).__name__, e, cost_ms)
            raise

        cost_ms = (time.perf_counter() - start) * 1000
        if res.status_code >= 400:
            # 非 2xx 时打印响应体片段，方便排查服务端返回的错误原因
            logger.warning("响应异常 %s %s | 状态码: %s | 耗时: %.0fms | 响应体: %s",
                           method, url, res.status_code, cost_ms, res.text[:300])
        else:
            logger.info("响应 %s %s | 状态码: %s | 耗时: %.0fms",
                        method, url, res.status_code, cost_ms)
        return res
