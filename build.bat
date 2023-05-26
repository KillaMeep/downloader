@echo off
echo '' > IsEXE
pyinstaller --noconfirm --onefile --console --add-data "F:/Coding/File-Downloader/yt-dlp.exe;." --add-data "F:/Coding/File-Downloader/ffmpeg;ffmpeg/" "F:/Coding/File-Downloader/downloader.py"
del /s /q IsEXE
del /s /q downloader.spec
rmdir /s /q build
cd dist
copy downloader.exe ..
cd ..
rmdir /s /q dist