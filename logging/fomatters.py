"""
Log using different formatters for different handlers
"""


import logging

def log(path):
    """Log to multiple locations if multipleLocs is True"""
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    # log to file
    fh = logging.FileHandler(path)
    formatter = logging.Formatter('%(asctime)s - %(name)s %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # log to stdout
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    logger.info("This is an informational message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("You can't do that !")
    logger.critical("THIS IS A SHOW STOPPER!!!")

if __name__ == "__main__":
    log("sample.log")


