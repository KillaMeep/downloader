@echo off
timeout /t 5 /nobreak > NUL
del /s /q downloader.exe
curl -L  -o downloader.exe https://github.com/killameep/downloader/releases/latest/download/downloader.exe 
