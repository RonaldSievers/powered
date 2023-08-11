import logging

# create logger
logger = logging.getLogger("leditbe")
logger.setLevel(logging.INFO)

# create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# create file logger for longer term logging
file_handler = logging.FileHandler("logs.txt")
file_handler.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to both handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# add all handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
