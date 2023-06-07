import logging

logger = logging.getLogger()
print(logger)


def main(name):
    logger.warning(f"Enter in the main function: name = {name}")

# layer of notifications
# notset - 0
# debug - 10
# info - 20
# warning - 30
# error - 40
# critical - 50


if __name__ == "__main__":
    main("paul")
