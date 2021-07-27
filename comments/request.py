import sqlite3
import json
from models import Post
from models import Rare_User

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
            p.id rare_user,
            u.username username,
            u.is_admin is_admin
        FROM comment com
        JOIN POST p
            ON p.id = p.rare_user
            """)

        posts = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            # Create an post instance from the current row
            post = Post(row['id'], row['content'], row['created_on'], row['post_id'],
                        row['author_id'], row['image_url'], row['content'], row['approved'])
            rare_user = Rare_User(row['id'], row['bio'], row['profile_image_url'],  # pylint:disable=(too-many-function-args)
                                  row['created_on'], row[1], row['first_name'],
                                  row['last_name'], row['email'], row['username'], row['password'], row[1])
            post.rare_user = rare_user.__dict__
            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)
            # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)