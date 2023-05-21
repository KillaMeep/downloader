@echo off
mkdir Downloader
cd Downloader
curl --output yt-dlp.exe https://github.com/KillaMeep/downloader/raw/main/yt-dlp.exe
curl --output downloader.py https://raw.githubusercontent.com/KillaMeep/downloader/main/downloader.py
curl --output build.bat https://raw.githubusercontent.com/KillaMeep/downloader/main/build.bat
pip install tk
pip install pyinstaller
start /B /WAIT build.bat
exit
