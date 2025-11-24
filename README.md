# inventory_manager.py
This Python script is a simple inventory management system that allows a user to track items and their quantities in a CSV file.
This Python script is a basic inventory management system designed to store and manage items and their quantities efficiently. The program uses a CSV file for persistent storage, allowing users to maintain an up-to-date record of inventory across sessions. It is intended for small-scale inventory tracking, educational purposes, or introductory programming projects.

Overview

The system provides a menu-driven interface that allows users to perform the following operations:
Add Items – Input an item name and quantity. If the item already exists, its quantity is updated.
Remove Items – Delete an item entirely from the inventory.
Update Quantities – Modify the quantity of an existing item.
Search Items – Find a specific item and display its details.
View Inventory – Display all items and quantities in a structured format.
Save and Load Inventory – Inventory data is saved to and loaded from a CSV file (inventory.csv), ensuring persistence between sessions.

Technical Details

The program is implemented in Python 3 and uses the pandas library for data handling.
Data is stored in a CSV file, which simplifies reading, writing, and updating inventory records.
User input is handled through a text-based menu, with input validation to ensure numeric quantities are correctly processed.
The program includes basic error handling for file operations and input validation.

Key Features

Easy-to-use, menu-driven interface.
Persistent storage using CSV files.
Supports adding, removing, updating, and searching inventory items.
Built using standard Python libraries and pandas.

Use Cases

Tracking small business or personal inventory.
Learning basic Python programming concepts such as file I/O, data handling with pandas, and menu-driven applications.

Serving as a foundational project for further development of more advanced inventory systems.
