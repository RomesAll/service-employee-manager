import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(module)s - %(levelname)s: (%(message)s)',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'stdout':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'mode': 'a',
            'formatter': 'standard',
        },
    },
    'loggers': {'root': { 'handlers': ['stdout', 'file'], 'level': 'DEBUG',}}
}

logging.config.dictConfig(LOGGING_CONFIG)