import tkinter as tk
from tkinter import ttk
import os
import subprocess
import time
os.system('if exist downloads del /s /q downloads')
def clear_progress(progress_label,root):
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
        
        subprocess.run(f'yt-dlp.exe {urls[x]}')

    files = os.listdir(os.getcwd())
    convert_files = []
    final_names = []
    
    # Check for webms
    for x in range(0, len(files)):
        if '.webm' in files[x]:
            final_names.append(files[x].split(' [')[0].split(".webm")[0])
            convert_files.append(files[x])

    # If there are any webm files, convert them
    if convert_files:
        clear_progress(progress_label,root)
        # Update the prompt to show progress
        for x in range(0, len(convert_files)):
            progress_label.config(text=f'Converting {x+1}/{len(convert_files)} | {final_names[x]}')
            root.update()  # Update the GUI
            
            os.system(f'ffmpeg -fflags +genpts -i "{convert_files[x]}" -r 24 "{final_names[x]}.mp4" > nul 2>&1')
    clear_progress(progress_label,root)
    for x in range(0, len(final_names)):
        progress_label.config(text=f'Copying file(s) {x+1}/{len(final_names)} | {final_names[x]}')
        root.update()
        os.system(f'copy "{final_names[x]}.mp4" .. > nul 2>&1')

    os.chdir('..')
    os.remove('downloads')
    clear_progress(progress_label,root)
    for x in range(0,5):
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
