import logging


logging.basicConfig(level="DEBUG")
logger = logging.getLogger()  # default layer = 30
# print(dir(logger))
# print()
# logger.setLevel("DEBUG")  # may be digital(10)

# print(logger.level)
print(logger.handlers)


def main(name):
    logger.debug(
        f"Enter in the main function: name = {name}"
    )  # we don't see anything because layer is smaller(10 <= 10)

    # print(dir(logger))


# layer of notifications
# notset - 0
# debug - 10
# info - 20
# warning - 30
# error - 40
# critical - 50


if __name__ == "__main__":
    main("paul")
