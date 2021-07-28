import os

# 项目根目录
BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)

# 日志配置字典
file_format = '[%(name)s]-[%(asctime)s]-[%(levelname)s]-[%(filename)s]-' \
              '[%(lineno)d]-[%(message)s]'
console_format = '[%(name)s]-[%(asctime)s]-[%(levelname)s]-[%(filename)s]-' \
                 '[%(lineno)d]-[%(message)s]-[%(processName)s]-[%(threadName)s]'
log_path = os.path.join(BASE_PATH, 'log', 'course_system.log')
LOGGING_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'console_logger': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'INFO',
            # 日志回滚
            # a2文件始终存放最新的日志并且大小不超过maxBytes
            # 旧的日志会被备份并且备份数量不超过backupCount
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'file',
            'filename': log_path,
            'backupCount': 3,
            'encoding': 'utf-8',
        },
    },
    'filters': {},
    'formatters': {
        'file': {
            'format': file_format,
            'datefmt': '%Y-%m-%d %X',
        },
        'console': {
            'format': console_format,
            'datefmt': '%Y-%m-%d %X',
        },
    },
}
