@echo off
mkdir Downloader
cd Downloader
curl --output downloader.py https://raw.githubusercontent.com/KillaMeep/downloader/main/downloader.py
curl -L -O https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
mkdir ffmpeg_install
cd ffmpeg_install
curl --output ffmpeg.zip https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-5.1.2-essentials_build.zip
tar -xf ffmpeg.zip
del /s /q ffmpeg.zip
for /D %%i in (ffmpeg-*) do ren %%i ffmpeg
move ffmpeg .. > nul
cd ..
rmdir /s /q ffmpeg_install
pip install tk
pip install pyinstaller
start /b "" cmd /c del "%~f0"&exit /b