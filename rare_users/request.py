import sqlite3
import json
from models.rare_user import Rare_User
from datetime import date

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
        "created_on": date.today()
    },{
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
        "created_on": date.today()
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
        "created_on": date.today()
    },{
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
        "created_on": date.today()
    }
]


def get_all_rare_users():
    """this is getting all users"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

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
        FROM Rare_User r
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
            rare_user = Rare_User(row['id'], row['bio'], row['profile_image_url'],# pylint:disable=(too-many-function-args)
                            row['created_on'], row[1], row['first_name'],
                            row['last_name'], row['email'], row['username'], row['password'], row['is_admin'])

            # Create a Location instance from the current row
            # location = Location(
            #     row['location_id'], row['location_name'], row['location_address'])
            # # Add the dictionary (like an object on an object) representation of the location to the users
            # users.location = location.__dict__
            # # Create a Customer instance from the current row
            # customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'],
            #                     row['customer_email'], row['customer_password'])
            # users.customer = customer.__dict__

            # turns users object into a dictionary
            rare_users.append(rare_user.__dict__)

            row ['active'] = 1
            row ['is_admin'] = 1
    # Use `json` package to properly serialize list as JSON
    return json.dumps(rare_users)  # converts Python object into a json string

def get_single_rare_user(id):
    """this is getting a single rare_user by its id"""
    with sqlite3.connect("./kennel.db") as conn:
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
        FROM Rare_User r
                """, (id, ))  # replaces the question mark with an id  uses a sequal query

        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an rare_user instance from the current row
        rare_user = Rare_User(data['id'], data['bio'], data['profile_image_url'],# pylint:disable=(too-many-function-args)
                            data['created_on'], data['active'], data['first_name'],
                            data['last_name'], data['email'], data['username'], data['password'], data['is_admin'])

        data ['active'] = 1
        data ['is_admin'] = 1

        return json.dumps(rare_user.__dict__)