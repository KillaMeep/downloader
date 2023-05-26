@echo off
cd Downloader
echo '' > IsEXE
pyinstaller --noconfirm --onefile --console --add-data "yt-dlp.exe;." --add-data "ffmpeg;ffmpeg/" "downloader.py"
del /s /q IsEXE
del /s /q downloader.spec
rmdir /s /q build
copy dist/downloader.exe ../..
rmdir /s /q dist
exit
