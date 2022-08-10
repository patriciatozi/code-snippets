import logging

# Define the format including time, type of log and the message
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(
    filename='example.log', level=logging.INFO, filemode='w', format=FORMAT
)

# DEBUG has severity level 10
logging.debug('This is a debug message')

# INFO has severity level 20
logging.info('This is an info message')

# WARN has severity level 30
logging.warning('This is a warning message')

# ERROR has severity level 40
logging.error('This is an error message')

# CRITICAL has severity level 50
logging.critical('This is a critical message')


a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.exception(f'Exception occurred: {e}')