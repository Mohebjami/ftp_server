# FTP Server GUI Application

This is a simple FTP server application with a graphical user interface (GUI) built using Python, Tkinter, and pyftpdlib. The application allows users to share directories and view/download files from an FTP server in an easy-to-use GUI environment.

## Features

- **Share Directory**: Select and share a directory over an FTP server for others to view and download files.
- **View & Download Files**: View the list of shared files on the server and download selected files to your local machine.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `pyftpdlib` (for FTP server functionality)
- `ftplib` (for FTP client functionality)

## Installation

1. **Clone the repository or download the files**:
    ```bash
    git clone https://github.com/Mohebjami/ftp_server.git
    cd <your-repository-folder>
    ```

2. **Install required packages**:
    Install the necessary Python packages using pip:
    ```bash
    python3.13 -m venv myenv
    source myenv/bin/activate
    pip install pyftpdlib
    pip install pyftpdlib
    ```

3. **Run the application**:
    To start the GUI, run:
    ```bash
    python gui.py
    ```

## How to Use

1. **Sharing a Directory**:
   - Click on the "Share Directory" button.
   - Select a folder you wish to share through the FTP server.
   - The selected directory will be shared, and the server will start running on `localhost` at port `8080`.

2. **Viewing and Downloading Files**:
   - Click the "View & Download Files" button to connect to the FTP server and load the list of files in the shared directory.
   - Select a file from the list and click "Download Selected File" to download it to your local system.
   - You will be prompted to choose the save location for the downloaded file.

## File Structure

```bash
.
├── gui.py             # Main GUI application
├── ftp_server.py      # FTP server logic
├── file_handler.py    # FTP client logic
└── README.md          # Documentation