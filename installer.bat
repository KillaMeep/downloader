@echo off
mkdir Downloader
cd Downloader
curl --output yt-dlp.exe https://raw.githubusercontent.com/KillaMeep/downloader/main/yt-dlp.exe
curl --output downloader.py https://raw.githubusercontent.com/KillaMeep/downloader/main/downloader.py
mkdir ffmpeg_install
cd ffmpeg_install
curl --output ffmpeg.zip https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-5.1.2-essentials_build.zip
tar -xf ffmpeg.zip
del /s /q ffmpeg.zip
for /D %%i in (ffmpeg-*) do ren %%i ffmpeg
move ffmpeg .. > nul
cd ..
del /s /q ffmpeg_install
pip install tk
pip install pyinstaller
exit
