@echo off
echo '' > IsEXE
pyinstaller --noconfirm --onefile --console --add-data "yt-dlp.exe;." --add-data "ffmpeg;ffmpeg/" "downloader.py"
del /s /q IsEXE
del /s /q downloader.spec
rmdir /s /q build
cd dist
copy downloader.exe ..
cd ..
rmdir /s /q dist
