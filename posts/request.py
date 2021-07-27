import sqlite3
import json
from models import Post
from models import User

POSTS = []

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
            p.user_id,
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
        JOIN User u
            ON u.id = p.rare_user
            """)

        posts = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            # Create an post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['content'], row['approved'])
            # Create a Location instance from the current row
            user = User(row['id'],
                        row['username'], row['is_admin'])
            # Add the dictionary representation of the location to the post
            post.user = user.__dict__
            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)
            # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def create_post(post):
    # Get the id value of the last animal in the list
    max_id = POSTS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    post["id"] = new_id

    # Add the animal dictionary to the list
    POSTS.append(post)

    # Return the dictionary with `id` property added
    return post

def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM post
        WHERE id = ?
        """, (id, ))



def update_post(id, new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Post
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                image_url = ?,
                content = ?
                approved =?
        WHERE id = ?
        """, (new_post['user_id'], 
            new_post['category_id'],
            new_post['title'],  
            new_post['image_url'],
            new_post['content'], 
            new_post['approved'], 
            id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
