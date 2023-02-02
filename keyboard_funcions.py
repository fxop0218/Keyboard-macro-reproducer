import sys
import csv
import threading
import datetime
from pynput import keyboard


# def replicate(file_name: str = "key_logger.csv"):
#     with open(file_name) as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             simulate_key_press(row[0])
