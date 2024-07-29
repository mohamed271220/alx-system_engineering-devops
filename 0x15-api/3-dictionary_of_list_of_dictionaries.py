#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API and exports the data to a JSON file.
"""

import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_all_users():
    """Fetches the information for all users from the API."""
    response = requests.get(f"{BASE_URL}users")
    response.raise_for_status()
    return response.json()


def get_user_todos(user_id):
    """Fetches the to-do list for the user from the API."""
    params = {"userId": user_id}
    response = requests.get(f"{BASE_URL}todos", params=params)
    response.raise_for_status()
    return response.json()


def fetch_user_data(users):
    """Fetches user information and to-do lists for all employees."""
    data_to_export = {}
    for user in users:
        user_id = user["id"]
        todos = get_user_todos(user_id)
        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todos
        ]
    return data_to_export


def export_to_json(data_to_export):
    """Exports the user's to-do list to a JSON file."""
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)


def main():
    users = get_all_users()
    data_to_export = fetch_user_data(users)
    export_to_json(data_to_export)


if __name__ == "__main__":
    main()
