#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
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


def export_to_json(user_id, username, todos):
    """Exports the user's to-do list to a JSON file."""
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)


def main():
    user_id = sys.argv[1]
    user = get_user_info(user_id)
    todos = get_user_todos(user_id)
    export_to_json(user_id, user.get("username"), todos)


if __name__ == "__main__":
    main()
