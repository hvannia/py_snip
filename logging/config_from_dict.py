import logging
import logging.config

dictLogConfig  = {
    "version":1,
    "handlers":{
        "fileHandler":{
            "class":"logging.fileHandler",
            "formatter":"myFormatter",
            "filename":"dict_config.log"
        }
    },
    "loggers":{
        "exampleApp":{
            "handlers":["fileHandler"],
            "level":"INFO",
        }
    },
    "formatters":{
        "myFormatter":{
            "format":"%(asctime)s - %(name)s - %(levelname)s - %(messages)s"
        }
    }
}

logging.config.dictConfig(dictLogConfig)
logger = logging.getLogger("exampleApp")

logger.info("Program started")
logger.info("Done!")