import sqlite3
import json
from models import Post
from models import Rare_User


def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.rare_user,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id rare_user,
            u.username username,
            u.is_admin is_admin
        FROM post p
        JOIN Rare_User u
            ON u.id = p.rare_user
            """)

        posts = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            # Create an post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['content'], row['approved'])
            rare_user = Rare_User(row['id'], row['bio'], row['profile_image_url'],  # pylint:disable=(too-many-function-args)
                                  row['created_on'], row[1], row['first_name'],
                                  row['last_name'], row['email'], row['username'], row['password'], row[1])
            post.rare_user = rare_user.__dict__
            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)
            # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def get_single_post(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
        FROM Post p
        WHERE p.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an post instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                    data['publication_date'], data['image_url'], data['content'], data['approved'])
        return json.dumps(post.__dict__)
