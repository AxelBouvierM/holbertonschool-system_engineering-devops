#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import requests
from sys import argv
import csv

api = "https://jsonplaceholder.typicode.com/"
api_url_usr = api + "users/" + argv[1]
api_url_todos = api + "todos?userId=" + argv[1]

response = requests.get(api_url_usr).json()
todo = requests.get(api_url_todos).json()

filename = argv[1] + ".csv"
with open(filename, 'w', newline='') as csvfile:
    write_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in todo:
        write_file.writerow([argv[1], response.get("name"),
                            task.get("completed"), task.get("title")])
