import sqlite3
import json
from models import Category

CATEGORIES = []


def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            cat.id,
            cat.label
        FROM Categories cat
        """)

        # Initialize an empty list to hold all category representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an category instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Category class above.
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(categories)


def get_single_category(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            cat.id,
            cat.label
        FROM category cat
        WHERE cat.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        category = Category(data['id'], data['label'])

        return json.dumps(category.__dict__)


def create_category(category):
    # Get the id value of the last category in the list
    max_id = CATEGORIES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the category dictionary
    category["id"] = new_id

    # Add the category dictionary to the list
    CATEGORIES.append(category)

    # Return the dictionary with `id` property added
    return category


def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM category
        WHERE id = ?
        """, (id, ))


def update_category(id, new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Category
            SET
                label = ?
        WHERE id = ?
        """, (new_category['label'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
