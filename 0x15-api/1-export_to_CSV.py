#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_user_info(user_id):
    """Fetches the user information from the API."""
    response = requests.get(f"{BASE_URL}users/{user_id}")
    response.raise_for_status()
    return response.json()


def get_user_todos(user_id):
    """Fetches the to-do list for the user from the API."""
    params = {"userId": user_id}
    response = requests.get(f"{BASE_URL}todos", params=params)
    response.raise_for_status()
    return response.json()


def export_to_csv(user_id, username, todos):
    """Exports the user's to-do list to a CSV file."""
    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            data = [
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ]
            writer.writerow(data)


def main():
    user_id = sys.argv[1]
    user = get_user_info(user_id)
    todos = get_user_todos(user_id)
    export_to_csv(user_id, user.get("username"), todos)


if __name__ == "__main__":
    main()
