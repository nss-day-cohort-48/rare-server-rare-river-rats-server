import sqlite3
import json
from models import Tag

TAGS = []


def get_all_tags():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
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
        FROM Tags t
                """, (id, ))  # replaces the question mark with an id  uses a sequal query

        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an rare_user instance from the current row
        tag = Tag(data['id'], data['label'])
        return json.dumps(tag.__dict__)


def create_tag(new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the tag dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_tag['id'] = id


    return json.dumps(new_tag)


def update_tag(id, new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Tags
            SET
                label = ?
        WHERE id = ?
        """, (new_tag['label'], id, ))

        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    else:
        return True


def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Tags
        WHERE id = ?
        """, (id, ))
