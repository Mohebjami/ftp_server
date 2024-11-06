import os
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"Provided path is not a valid directory: {directory}")

    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", directory, perm="elradfmwMT")
    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("localhost", 8080), handler)
    print(f"Starting FTP server on port 8080, sharing directory: {directory}")
    server.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ftp_server.py <directory_to_share>")
        sys.exit(1)

    directory_to_share = sys.argv[1]
    start_ftp_server(directory_to_share)
