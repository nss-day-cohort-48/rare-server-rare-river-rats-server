import sqlite3
import json
from models import Comment

COMMENTS = []


def get_all_comments():
    """Gets all users. Mainly for testing on this app"""
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            com.id,
            com.content,
            com.created_on,
            com.post_id,
            com.author_id
        FROM Comments com
        """)

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(
                row['id'], row['content'], row['created_on'], row['post_id'], row['author_id'], )

            comments.append(comment.__dict__)

    return json.dumps(comments)


def get_comments_by_post(post_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            com.id,
            com.content
            com.created_on,
            com.post_id,
            com.author_id,
        FROM Comments com
        WHERE com.post_id = ?
        """, (post_id, ))

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(
                row['id'], row['content'], row['created_on'], row['post_id'], row['author_id'])

            comments.append(comment.__dict__)

    return json.dumps(comments)


def create_comment(comment):
    # Get the id value of the last category in the list
    max_id = COMMENTS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the category dictionary
    comment["id"] = new_id

    # Add the comment dictionary to the list
    COMMENTS.append(comment)

    # Return the dictionary with `id` property added
    return comment


def delete_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))


def update_comment(id, new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                content = ?,
                created_on =?,
                post_id = ?,
                author_id = ?
        WHERE id = ?
        """, (new_comment['content'], new_comment['created_on'], new_comment['post_id'], new_comment['author_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
