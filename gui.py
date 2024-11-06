import os
import sys
import time
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, ttk
from file_handler import FTPClient  # Assume FTPClient is implemented as described below

class FTPGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("FTP Server GUI")
        self.master.geometry("500x450")  # Adjust window size for the new button
        
        # Track the FTP server process
        self.process = None

        # Create a frame for sharing and viewing files
        self.top_frame = tk.Frame(master)
        self.top_frame.pack(pady=20)

        # Share directory button
        self.share_button = ttk.Button(self.top_frame, text="Share Directory", command=self.share_directory)
        self.share_button.grid(row=0, column=0, padx=10, pady=10)

        # View files button
        self.view_button = ttk.Button(self.top_frame, text="View & Download Files", command=self.view_files)
        self.view_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox for displaying files
        self.file_listbox = Listbox(master, height=10, width=60, font=("Arial", 10))
        self.file_listbox.pack(pady=20)

        # Create a frame for download and delete buttons
        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack()

        # Download file button
        self.download_button = ttk.Button(self.bottom_frame, text="Download Selected File", command=self.download_file)
        self.download_button.grid(row=0, column=0, padx=10, pady=10)

        # Delete selected file button
        self.delete_file_button = ttk.Button(self.bottom_frame, text="Delete Selected File", command=self.delete_selected_file)
        self.delete_file_button.grid(row=0, column=1, padx=10, pady=10)

    def share_directory(self):
        directory = filedialog.askdirectory()  # Ask the user to select a directory to share
        if directory:
            try:
                # If there is an existing server process, terminate it
                if self.process is not None:
                    self.process.terminate()
                    self.process.wait()  # Ensure the previous process is fully terminated
                
                # Use sys.executable to get the correct Python executable
                python_executable = sys.executable  # Get the Python interpreter path
                # Start the new FTP server in the background with the selected directory
                self.process = subprocess.Popen([python_executable, "ftp_server.py", directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                # Allow time for the server to start
                time.sleep(2)  # Wait 2 seconds to ensure the server has started
                messagebox.showinfo("Info", f"Successfully shared directory: {directory}")
            except subprocess.TimeoutExpired:
                messagebox.showerror("Error", "Failed to start FTP server. Please try again.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while sharing the directory: {e}")

    def view_files(self):
        self.file_listbox.delete(0, tk.END)  # Clear the current file list
        ftp_client = FTPClient()
        ftp_client.connect()

        files = ftp_client.list_files()  # List files from the FTP server
        if files:
            for file in files:
                self.file_listbox.insert(tk.END, file)  # Add files to the listbox
            messagebox.showinfo("Info", "Files loaded successfully.")
        else:
            messagebox.showwarning("Warning", "No files found or error occurred.")

        ftp_client.close()

    def download_file(self):
        try:
            selected_index = self.file_listbox.curselection()[0]  # Get the selected file
            selected_file = self.file_listbox.get(selected_index)

            local_path = filedialog.asksaveasfilename(initialfile=selected_file)  # Ask where to save the file
            if local_path:
                ftp_client = FTPClient()
                ftp_client.connect()
                ftp_client.download_file(selected_file, local_path)  # Download the selected file
                ftp_client.close()
                messagebox.showinfo("Info", f"Downloaded: {selected_file} to {local_path}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a file to download.")
    
    def delete_selected_file(self):
        try:
            selected_index = self.file_listbox.curselection()[0]  # Get the selected file
            selected_file = self.file_listbox.get(selected_index)
            
            ftp_client = FTPClient()
            ftp_client.connect()
            ftp_client.delete_file(selected_file)  # Delete the selected file from the server
            ftp_client.close()

            self.file_listbox.delete(selected_index)  # Remove the file from the listbox
            messagebox.showinfo("Info", f"Deleted: {selected_file} from server.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a file to delete.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while deleting the file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    ftp_gui = FTPGUI(root)
    root.mainloop()