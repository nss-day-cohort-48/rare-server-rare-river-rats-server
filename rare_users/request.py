import sqlite3
import json
from models import Rare_User
from datetime import datetime

RARE_USERS = [
    {
        "id": 1,
        "bio": "New guy",
        "profile_image_url": "profile_image_url",
        "active": 1,
        "first_name": "Nick",
        "last_name": "M",
        "email": "nick@m.com",
        "username": "Nick M",
        "password": "password",
        "is_admin": 1,
        "created_on": datetime.today()
    }, {
        "id": 2,
        "bio": "Smooth guy",
        "profile_image_url": "profile_image_url",
        "active": 1,
        "first_name": "Ben",
        "last_name": "K",
        "email": "ben@k.com",
        "username": "Ben K",
        "password": "password",
        "is_admin": 1,
        "created_on": datetime.today()
    },
    {
        "id": 3,
        "bio": "Cool guy",
        "profile_image_url": "profile_image_url",
        "active": 1,
        "first_name": "Roger",
        "last_name": "G",
        "email": "roger@g.com",
        "username": "Roger G",
        "password": "password",
        "is_admin": 1,
        "created_on": datetime.today()
    }, {
        "id": 4,
        "bio": "Young dude",
        "profile_image_url": "profile_image_url",
        "active": 1,
        "first_name": "Key",
        "last_name": "N",
        "email": "key@n.com",
        "username": "Key N",
        "password": "password",
        "is_admin": 1,
        "created_on": datetime.today()
    }
]


def get_all_rare_users():
    """this is getting all users"""
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            r.id,
            r.bio,
            r.profile_image_url,
            r.created_on,
            r.active,
            r.first_name,
            r.last_name,
            r.email,
            r.username,
            r.password,
            r.is_admin
        FROM Rare_Users r
                """)  # location table is going to be joined with the users table for line

        # Initialize an empty list to hold all users representations
        rare_users = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an users instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # users class imported above.
            rare_user = Rare_User(row['id'], row['bio'], row['profile_image_url'], row['created_on'], row['active'], row['first_name'], row['last_name'], row['email'], row['username'], row['password'], row['is_admin'])  # pylint:disable=(too-many-function-args)

            # turns users object into a dictionary
            rare_users.append(rare_user.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(rare_users)  # converts Python object into a json string


def get_single_rare_user(id):
    """this is getting a single rare_user by its id"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            r.id,
            r.bio,
            r.profile_image_url,
            r.created_on,
            r.active,
            r.first_name,
            r.last_name,
            r.email,
            r.username,
            r.password,
            r.is_admin
        FROM Rare_Users r
        WHERE r.id = ?""", (id, ))  # replaces the question mark with an id  uses a sequal query

        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an rare_user instance from the current row
        rare_user = Rare_User(data['id'], data['bio'], data['profile_image_url'], data['created_on'], data['active'], data['first_name'], data['last_name'], data['email'], data['username'], data['password'], data['is_admin']) # pylint:disable=(too-many-function-args)
        
        return json.dumps(rare_user.__dict__)

def create_rare_user(new_rare_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Rare_Users
            ( first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (new_rare_user['first_name'], new_rare_user['last_name'], new_rare_user['email'], new_rare_user['bio'], new_rare_user['username'], new_rare_user['password'], new_rare_user['profile_image_url'], datetime.now(), new_rare_user['active']))

        id = db_cursor.lastrowid

        new_rare_user['id'] = id
        new_rare_user['active'] = True

    return json.dumps(new_rare_user)


def delete_rare_user(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Rare_Users
        WHERE id = ?
        """, (id, ))

def update_rare_user(id, new_rare_user):
    """this is editing an rare_user"""
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Rare_User
            SET
                bio = ?,
                profile_image_url = ?,
                created_on = ?,
                active = ?,
                first_name = ?,
                last_name = ?,
                email = ?,
                username = ?,
                password = ?,
                is_admin = ?
        WHERE id = ?
        """, (new_rare_user['bio'], new_rare_user['profile_image_url'], datetime.now(), new_rare_user['active'], new_rare_user['first_name'], new_rare_user['last_name'], new_rare_user['email'], new_rare_user['username'], new_rare_user['password'], new_rare_user['is_admin'], id, ))
        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

