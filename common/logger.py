import logging
import os
from logging.handlers import RotatingFileHandler

# 日志统一输出到项目根目录的 logs/ 下
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "test.log")

# 时间 | 级别 | 模块:行号 | 消息
LOG_FORMAT = "\n%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 已创建的 logger，供 set_level 批量调整级别
_LOGGERS = []


def get_logger(name=__name__, level=None):
    """
    获取一个同时输出到控制台和文件的 logger。
    同名 logger 只会初始化一次，重复调用不会重复添加 handler。

    级别优先级：level 参数 > 环境变量 LOG_LEVEL > INFO
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level or os.getenv("LOG_LEVEL", "INFO").upper())
    # 避免日志被 root logger 再输出一次造成重复
    logger.propagate = False

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 单个日志文件最大 5MB，保留 3 个历史文件，避免文件无限增长
    os.makedirs(LOG_DIR, exist_ok=True)
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    _LOGGERS.append(logger)
    return logger


def set_level(level):
    """批量调整已创建的所有 logger 的级别，供 pytest --log-level 使用"""
    for logger in _LOGGERS:
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)
