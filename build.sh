poetry run pyinstaller --onefile --paths ./src/ src/main.py
poetry run pyinstaller --onefile --paths ./src/ src/lipsum.py

rm -rf ./build
rm *.spec
