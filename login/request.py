import sqlite3
import json
from models import Login
from datetime import datetime



def login_auth(email, password):
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
		SELECT 
			r.email,
			r.password
		FROM Rare_Users r
		WHERE r.email = ?
		AND r.password = ?
		""", (email, password))

        data = db_cursor.fetchone()
        try:
            rare_user = Login(data['email'], data['password'] , True)# pylint:disable=(too-many-function-args)
        except:
            print("Please Register Below")
            rare_user = Login("", "", 0)

        return json.dumps(rare_user.__dict__)


def register_rare_user(new_rare_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
				INSERT INTO Rare_Users
						( first_name, last_name, email, password, created_on, active )
				VALUES
						( ?, ?, ?, ?, ?, ? );
				""", (new_rare_user['first_name'], new_rare_user['last_name'],
          new_rare_user['email'], new_rare_user['password'], datetime.now(), new_rare_user['active']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_rare_user['id'] = id

        new_rare_user['active'] = 1

    return json.dumps(new_rare_user)
