import logging
import requests


logging.basicConfig(level="DEBUG")
logger = logging.getLogger()


for key in logging.Logger.manager.loggerDict:  # see all loggers
    print(key)


def main(name):
    logger.debug(f"Enter in the main function: name = {name}")

    r = requests.get("https://www.google.com")


if __name__ == "__main__":
    main("paul")
