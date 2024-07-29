#!/usr/bin/python3
"""
Script to fetch and display to-do list information for a given employee ID.

This script accepts an employee ID as a command-line argument, retrieves
the corresponding user information and to-do list from the JSONPlaceholder API,
and prints the tasks completed by the employee.
"""

import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_employee_info(employee_id):
    """Fetches the employee information from the API."""
    response = requests.get(f"{BASE_URL}users/{employee_id}")
    response.raise_for_status()
    return response.json()


def get_employee_todos(employee_id):
    """Fetches the to-do list for the employee from the API."""
    params = {"userId": employee_id}
    response = requests.get(f"{BASE_URL}todos", params=params)
    response.raise_for_status()
    return response.json()


def print_completed_tasks(user, todos):
    """Prints the completed tasks for the employee."""
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print(f"Employee {user.get('name')} has completed {len(completed)} out of "
          f"{len(todos)} tasks:")
    for task in completed:
        print(f"\t {task}")


def main():
    """Main function to orchestrate the fetching
    and printing of employee task data."""
    employee_id = sys.argv[1]
    user = get_employee_info(employee_id)
    todos = get_employee_todos(employee_id)
    print_completed_tasks(user, todos)


if __name__ == "__main__":
    main()
