# Install dependencies
python -m pip install pyinstaller
python -m pip install requests
# Build Python script
pyinstaller -F vld.py
# Move build to bin
mv dist/vld $HOME/bin
# Delete other files
rm -rf build
rm -rf dist
rm vld.spec


