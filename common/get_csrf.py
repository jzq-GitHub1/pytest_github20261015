from common.request_util import RequestUtil
from common.write_yaml import WriteYaml
from common.find_file import find_path
from common.logger import get_logger

logger = get_logger(__name__)


def get_csrf_token():

    url = "http://47.107.116.139/phpwind/"
    csrf_token_data = RequestUtil().send_request(method="get", url=url).cookies.get("csrf_token")
    if csrf_token_data is None:
        logger.error("获取 csrf_token 失败：响应 Cookie 中没有 csrf_token")
        return None

    csrf_token = {"csrf_token": csrf_token_data}
    write_path = find_path("yaml_file", "new_write_data.yaml")
    WriteYaml(write_path=write_path, write_data=csrf_token).write_yaml_w()
    logger.info("获取 csrf_token 成功，已写入 %s", write_path)
    return csrf_token_data


# --------------------
# global csrf_token
# value = RequestUtil().send_request("get", url)
# csrf_token = value.cookies.get("csrf_token")
# session = requests.Session()
# # 先发起请求以获取 Cookie
# session.get(url=url)
# # 直接从 CookieJar 中获取指定 key 的值，注意：key 名称取决于后端框架，Django 默认为 'csrftoken'，其他可能为 'XSRF-TOKEN' 等
# csrf_token = session.cookies.get("csrf_token")
