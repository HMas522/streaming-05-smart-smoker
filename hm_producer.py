"""
Student: Hayley M
Date: 01Jun24

Message sender / emitter /producer

Description:
This script reads messages from a CSV file and sends them to a named queue
every 1-3 seconds. 

Remember:
- Use the up arrow to recall the last command executed in the terminal.
"""

# Import from Standard Library
import sys
import csv
import time
import random

# Import External packages used
import pika

# Configure logging
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

# ---------------------------------------------------------------------------
# Define program functions (bits of reusable code)
# ---------------------------------------------------------------------------

def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """
    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))

        # use the connection to create a communication channel
        ch = conn.channel()

        # use the channel to declare a queue
        ch.queue_declare(queue=queue_name)

        # use the channel to publish a message to the queue
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)

        # log a message for the user
        logger.info(f" [x] Sent {message}")

    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        if conn.is_open:
            conn.close()

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    host = "localhost"
    queue_name = "tasks"
    csv_file_path = "C:\\Users\\Hayley\\Documents\\streaming-05-smart-smoker\\smoker-temps.csv"

    try:
        # Open the CSV file and read data
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                message = ','.join(row)
                send_message(host, queue_name, message)
                time.sleep(random.uniform(1, 3))

    except FileNotFoundError:
        logger.error(f"CSV file not found: {csv_file_path}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")