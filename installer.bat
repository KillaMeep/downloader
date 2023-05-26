@echo off
mkdir Downloader
cd Downloader
start /b "" cmd /c pip install pipreqs && pipreqs && pip install -r requirements.txt && del /s /q requirements.txt
start /b "" cmd /c curl -L -s -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
start /b "" cmd /c curl -s -o downloader.py https://raw.githubusercontent.com/KillaMeep/downloader/main/downloader.py
mkdir ffmpeg_install
cd ffmpeg_install
curl -s -o ffmpeg.zip https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-5.1.2-essentials_build.zip
tar -xf ffmpeg.zip
del /s /q ffmpeg.zip
for /D %%i in (ffmpeg-*) do ren %%i ffmpeg
move ffmpeg .. > nul
cd ..
rmdir /s /q ffmpeg_install
start /b "" cmd /c del "%~f0"&&exit /b
