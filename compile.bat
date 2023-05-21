@echo off
F:
cd F:\Coding\File-Downloader
pyinstaller --noconfirm --onefile --console  "F:\Coding\File-Downloader\downloader.py"
cd dist
cp downloader.exe ..
cd ..
rmdir /s /q dist
rmdir /s /q build
del /s /q downloader.spec
cd F:\Coding\bin
if exist downloader.exe del /s /q downloader.exe
cd F:\Coding\File-Downloader
cp downloader.exe F:\Coding\bin
del /s /q downloader.exe
echo Updated!
echo ctrl+c to close!
exit