import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from rare_users import (get_all_rare_users, get_single_rare_user)
#    create_rare_user, delete_rare_user, update_rare_user)

#from employees import (
from posts import get_all_posts
# from animals import (
#    get_all_animals, get_single_animal, create_animal,
#    delete_animal, update_animal)
# from employees import (
#    get_all_employees, get_single_employee, create_employee,
#    delete_employee, update_employee)
# from locations import (
#    get_all_locations, get_single_location, create_location,
#    delete_location, update_location)
# from customers import (
#    get_all_customers, get_single_customer, create_customer,
#    delete_customer, update_customer, get_customers_by_email)


# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """sets the path"""
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return (resource, key, value)

        # No query string parameter
        else:
            id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response
        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was for
        # `/rare_users` or `/rare_users/2`
        if len(parsed) == 2:
            (resource, id, _) = parsed

            if resource == "rare_users":
                if id is not None:
                   response = f"{get_single_rare_user(id)}"
            else:
                   response = f"{get_all_rare_users()}"
            
            #elif resource == "customers":
            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
            # if resource == "animals":
            #    if id is not None:
            #        response = f"{get_single_animal(id)}"
            #    else:
            #        response = f"{get_all_animals()}"
            # elif resource == "customers":
            #    if id is not None:
            #        response = f"{get_single_customer(id)}"
            #    else:
            #        response = f"{get_all_customers()}"
            # elif resource == "employees":
            #    if id is not None:
            #        response = f"{get_single_employee(id)}"
            #    else:
            #        response = f"{get_all_employees()}"
            # elif resource == "locations":
            #    if id is not None:
            #        response = f"{get_single_location(id)}"
            #    else:
            #        response = f"{get_all_locations()}"

        # Response from parse_url() is a tuple with 3
        # items in it, which means the request was for
        # `/resource?parameter=value`
        elif len(parsed) == 3:
            (resource, key, value) = parsed

            # Is the resource `customers` and was there a
            # query parameter that specified the customer
            # email as a filtering value?

            # if key == "email" and resource == "customers":
            #    response = get_customers_by_email(value)

        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server
        """
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, _, _) = self.parse_url(self.path)

        # Initialize new rare_user
        new_item = None

        # Add a new rare_user to the list. Don't worry about
        # the orange squiggle, you'll define the create_rare_user
        # function next.
        
        #if resource == "rare_users":
        #    new_item = create_rare_user(post_body)
        #if resource == "employees":

        #    new_item = create_employee(post_body)
        # if resource == "locations":
        #    new_item = create_location(post_body)
        # if resource == "customers":
        #    new_item = create_customer(post_body)

        # Encode the new rare_user and send in response
        self.wfile.write(f"{new_item}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id, _) = self.parse_url(self.path)

        success = False

        #if resource == "rare_users":
        #    success = update_rare_user(id, post_body)
        #if resource == "employees":
        #    update_employee(id, post_body)
        # if resource == "locations":
        #    update_location(id, post_body)
        # if resource == "customers":
        #    update_customer(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handles DELETE requests to the server
        """
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id, _) = self.parse_url(self.path)

        # Delete a single rare_user from the list
        
        #if resource == "rare_users":
        #    delete_rare_user(id)
        #if resource == "employees":
        #    delete_employee(id)
        # if resource == "locations":
        #    delete_location(id)
        # if resource == "customers":
        #    delete_customer(id)

        # Encode the new rare_user and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
