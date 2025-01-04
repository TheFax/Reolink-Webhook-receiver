"""
Module: reolink_webhook_server

Description:
    This module implements a basic HTTP server in Python to receive and
    handle webhook notifications sent by Reolink IP cameras. The server
    listens for incoming POST requests and delegates content processing
    to a customizable function, allowing users to implement their own
    event handling logic.

Webhook configuration on IP CAM:
    Content: Default
    URL:     http://(ip_server):8080
    

Key Features:
    - Receives POST requests containing webhook data from Reolink cameras.
    - Provides a welcome HTML page for GET requests.
    - Sends HTTP 200 OK responses to POST requests coming from cameras.
    - Extracts the IP address of the sending client.
    - Decodes the request content from bytes to a UTF-8 string.
    - Calls a customizable function for data processing.
        - Parses the content as JSON (with error handling).
        - Handles decoding and JSON parsing errors for increased robustness.

Functions:
    - handle_post_request(client_ip, request_content): Customizable function
      for processing the content of POST requests.

Dependencies:
    - http.server
    - json

Author:  TheFax
Date:    04 Jan 2025
Version: 1.0
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def handle_post_request(client_ip, request_content):
    """
    Handles the content of incoming POST requests.

    This function attempts to parse the request_content as JSON.
    Prints the formatted JSON data if successful and provides error handling
    for parsing failures.

    Args:
        client_ip: The IP address of the client sending the request.
        request_content: The content of the POST request.
    """
    try:
        data = json.loads(request_content)
    except json.JSONDecodeError:
        print(f"Error: POST requests does not contain valid JSON data.")
    else:
        # This is the function you can customize with your logic
        # Here's an example that simply prints the data
        print(f"Received POST request from {client_ip}")
        print(f"Content:")
        print(json.dumps(data, indent=4))
        # You can add logic to process the data, save it, etc.

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Received GET request.")

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Server Webhook Reolink</h1></body></html>")

    def do_POST(self):
        print("Received POST request.")

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"OK")

        client_ip = self.client_address[0]  # Get client IP
        request_content_length = int(self.headers['Content-Length'])  # Get content length
        request_content = self.rfile.read(request_content_length).strip()  # Read content
        try:
            request_content = request_content.decode('utf-8') # Try to decode content in UTF-8
        except UnicodeDecodeError:
            print(f"Unable to decode request_content received from {client_ip}")
        else:
            # Call the customizable function with client IP and content
            handle_post_request(client_ip, request_content)

    def log_message(self, format, *args):
        # Suppress every log message coming from http.server
        return


def run(server_class=HTTPServer, handler_class=handler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting HTTPD on port %d...' % port)
    httpd.serve_forever()

run()

