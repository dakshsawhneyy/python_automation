import logging

# Configure the root logger: set the level to DEBUG and define the output format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# if want to output logs to a file
logging.basicConfig(
    filename='deploy.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
