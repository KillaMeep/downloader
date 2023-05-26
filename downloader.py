import tkinter as tk
from tkinter import ttk
import os
import time
import subprocess
import requests
import hashlib
from tkinter import messagebox

def update(local_file_path, github_file_url):
    # Read the local file
    with open(local_file_path, 'rb') as file:
        local_data = file.read()

    # Calculate the hash of the local file
    local_hash = hashlib.sha256(local_data).hexdigest()

    # Fetch the content of the GitHub file
    response = requests.get(github_file_url)
    github_data = response.content

    # Calculate the hash of the GitHub file
    github_hash = hashlib.sha256(github_data).hexdigest()

    # Compare the hashes
    if local_hash == github_hash:
        print("Up to date")
    else:
        result = messagebox.askquestion("Update Available", "New version detected. Update?")
        print(result)
        if result == 'yes':
            print('User chose to update.')
            subprocess.run('curl --output updater.bat https://raw.githubusercontent.com/KillaMeep/downloader/main/updater.bat')
            os.system('start updater.bat')
            time.sleep(10)
            exit(1)
        if result == 'no':
            print('User chose not to update.')

# Check for updates
update('downloader.py','https://raw.githubusercontent.com/KillaMeep/downloader/main/downloader.py')
abs_path = os.path.abspath(os.getcwd())
os.system('if exist downloads del /s /q downloads')
if os.path.exists(r'ffmpeg/bin/'):
    # local ffmpeg install
    ffmpeg_path = abs_path + r'\ffmpeg\bin\ffmpeg.exe'
    print(ffmpeg_path)
else:
    # hoping ffmpeg is in the path :/
    ffmpeg_path = 'ffmpeg.exe'
yt_dlp_path = abs_path + r'\yt-dlp.exe'

def clear_progress(progress_label, root):
    progress_label.config(text='                                  ')
    root.update()

def download():
    os.system('if not exist downloads mkdir downloads')
    os.chdir('downloads')
    text = text_entry.get("1.0", "end-1c")
    urls = text.split('\n')  # Split the text into an array at every '\n'

    # Loop through and download from each url
    for x in range(0, len(urls)):
        # Update the prompt to show progress
        progress_label.config(text=f'Downloading {x+1}/{len(urls)}')
        root.update()  # Update the GUI
        subprocess.run(fr'{yt_dlp_path} {urls[x]}')

    files = os.listdir(os.getcwd())
    print(files)
    convert_files = []
    final_names = []
    # Check for webms
    for x in range(0, len(files)):
        if '.webm' in files[x]:
            print(f'Found webm: "{files[x]}"')
            final_names.append(files[x].split(' [')[0].split(".webm")[0])
            convert_files.append(files[x])
        elif '.mov' in files[x]:
            print(f'Found mov: "{files[x]}"')
            final_names.append(files[x].split(' [')[0].split(".mov")[0])
            convert_files.append(files[x])
    # If there are any webm files, convert them
    if convert_files:
        clear_progress(progress_label, root)
        # Update the prompt to show progress
        for x in range(0, len(convert_files)):
            progress_label.config(text=f'Converting {x+1}/{len(convert_files)} | {final_names[x]}')
            root.update()  # Update the GUI
            subprocess.run(f'"{ffmpeg_path}" -i "{convert_files[x]}" "{final_names[x]}.mp4"')
    clear_progress(progress_label, root)
    for x in range(0, len(files)):
        print('copying')
        if final_names != []:
            progress_label.config(text=f'Copying file(s) {x+1}/{len(final_names)} | {final_names[x]}')
            os.system(f'copy "{final_names[x]}.mp4" .. > nul 2>&1')

        else:
            print(f'filename: "{files[x]}"')
            progress_label.config(text=f'Copying file(s) {x+1}/{len(files)} | {files[x]}')
            os.system(f'copy "{files[x]}" .. > nul 2>&1')
        root.update()

    os.chdir('..')
    os.system('rmdir /s /q downloads')
    clear_progress(progress_label, root)
    for x in range(0, 5):
        progress_label.config(text=f'Complete! Closing in {5-x}')
        root.update()
        time.sleep(1)
    exit(1)

root = tk.Tk()
root.title("Downloader")
root.config(bg="#1f1f1f")  # Set background color to dark gray

# Configure the style for the GUI elements
style = ttk.Style()
style.configure("TLabel", background="#1f1f1f", foreground="#ffffff", font=("Arial", 12))
style.configure("TButton", background="#4a4949", foreground="#4a4949", font=("Arial", 12))
style.configure("TEntry", background="#808080", font=("Arial", 12))

# Create the text entry box
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=20)

# Create the submit button
submit_button = ttk.Button(root, text="Download", command=download)
submit_button.pack(pady=10)

# Create the label for progress
progress_label = ttk.Label(root, text="")
progress_label.pack()

root.mainloop()
