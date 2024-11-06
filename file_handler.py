import ftplib

class FTPClient:
    def __init__(self):
        self.ftp = ftplib.FTP()
        self.cached_files = None  # Initialize a cache for files

    def connect(self):
        try:
            self.ftp.connect("localhost", 8080)  # Connect to the local FTP server
            self.ftp.login("user", "12345")  # Login with the correct credentials
        except Exception as e:
            print(f"Connection error: {e}")

    def list_files(self):
        # Reset cached files every time this function is called
        self.cached_files = None
        try:
            self.cached_files = self.ftp.nlst()  # List the files in the directory
            return self.cached_files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def download_file(self, filename, local_path):
        try:
            with open(local_path, "wb") as local_file:
                self.ftp.retrbinary(f"RETR {filename}", local_file.write)
        except Exception as e:
            print(f"Error downloading file: {e}")

    def clear_cache(self):
        self.cached_files = None  # Simply reset the cache
        print("File cache cleared.")

    def close(self):
        self.ftp.quit()