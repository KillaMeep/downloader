@echo off
mkdir Downloader
cd Downloader
curl --output yt-dlp.exe https://github.com/KillaMeep/downloader/raw/main/yt-dlp.exe
curl --output downloader.py https://raw.githubusercontent.com/KillaMeep/downloader/main/downloader.py
pip install tk
pyinstaller --noconfirm --onefile --console downloader.py
cd dist
cp downloader.exe ..
cd ..
rmdir /s /q dist
rmdir /s /q build
del /s /q downloader.spec
exit
