import sqlite3
import json
from models import Post
from models import Rare_User
from models import Comment

COMMENTS =[]

def view_comments_on_post():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            com.id,
            com.content,
            com.created_on,
            com.post_id,
            com.author_id,
            p.id post_id
        FROM comment com
        JOIN post_id p
            ON p.id = com.post_id
            """)

        comments = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            # Create an post instance from the current row
            comment = Comment(row['id'], row['content'], row['created_on'], row['post_id'],
                        row['author_id'])
            post_id = post_id(row['id'], row['bio'], row['profile_image_url'],  # pylint:disable=(too-many-function-args)
                                  row['created_on'], row[1], row['first_name'],
                                  row['last_name'], row['email'], row['username'], row['password'], row[1])
            post.rare_user = post_id.__dict__
            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)
            # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)
