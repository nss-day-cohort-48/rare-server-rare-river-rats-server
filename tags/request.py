import sqlite3
import json
from models.tag import Tag


def get_all_tags():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tag t
            """)

        tags = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            tag = Tag(row['id'], row['label'])
            tags.append(tag.__dict__)
            # Use `json` package to properly serialize list as JSON
    return json.dumps(tags)


def get_single_tag(id):
    """this is getting a single tag by its id"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            SELECT
            t.id,
            t.label
        FROM Tag t
                """, (id, ))  # replaces the question mark with an id  uses a sequal query

        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an rare_user instance from the current row
        tag = Tag(data['id'], data['label'])
        return json.dumps(tag.__dict__)
