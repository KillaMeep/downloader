@echo off
pip install tk
pyinstaller --noconfirm --onefile --console downloader.py
cd dist
cp downloader.exe ..
cd ..
rmdir /s /q dist
rmdir /s /q build
del /s /q downloader.spec
exit