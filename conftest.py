import os
import subprocess
import time

from common.logger import get_logger, set_level

logger = get_logger(__name__)


def _decode_output(raw):
    """Windows 控制台输出可能是 GBK，这里依次尝试 utf-8 / gbk 解码，避免日志乱码或解码报错"""
    if not raw:
        return ""
    for encoding in ("utf-8", "gbk"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def pytest_configure(config):
    """支持通过 pytest --log-level=DEBUG 调整日志级别"""
    level = config.getoption("log_level", None)
    if level:
        set_level(level)
        logger.info("日志级别已设置为 %s", level)


def pytest_sessionfinish(session, exitstatus):
    """
    测试会话结束后，自动生成Allure报告并尝试在默认浏览器打开
    """
    # 定义结果目录和报告输出目录
    results_dir = r"./report"
    report_dir = r"./report/html"

    # 确保结果目录存在（虽然pytest通常会创建，但防御性编程）
    # if not os.path.exists(results_dir):
    #     return

    logger.info("测试会话结束，退出码: %s", exitstatus)
    logger.info("正在生成 Allure 报告...")

    # 执行 allure generate 命令
    # --clean: 清空输出目录后再生成，避免旧报告残留
    # -o: 指定输出目录
    cmd_generate = f"allure generate {results_dir} -o {report_dir} --clean"
    # os.system(cmd_generate) os.system() 被划线提醒：这个函数‌已过时，不推荐继续使用‌，建议改用更安全的 subprocess 模块
    result = subprocess.run(cmd_generate, shell=True, capture_output=True)
    if result.returncode == 0:
        logger.info("Allure 报告已生成至: %s", os.path.abspath(report_dir))
    else:
        # allure 未安装或路径不对时 stderr 可能为空，这里做兜底
        logger.error("Allure 报告生成失败，退出码 %s，错误输出: %s",
                     result.returncode, _decode_output(result.stderr).strip())

    # 可选：自动生成后直接在默认浏览器打开
    # 注意：os.system 在某些CI环境中可能无法打开浏览器，本地开发非常有用
    cmd_open = f"allure open {report_dir}"
    logger.info("Allure 报告正在打开...")
    subprocess.run(cmd_open, shell=True)

