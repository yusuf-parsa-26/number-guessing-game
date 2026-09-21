# Number Guessing Game

A polished desktop number guessing game built with Python and Tkinter.

## Features

- Easy, Normal, and Hard difficulty levels
- Attempt counter and progress bar
- Higher/lower and distance hints
- Duplicate-guess detection
- Previous-guess history
- Score based on attempts used
- Instant restart with the **New Game** button

## Run locally

You need Python 3 with Tkinter. Tkinter is included with the standard Windows and macOS Python installers.

```bash
git clone https://github.com/yusuf-parsa-26/number-guessing-game.git
cd number-guessing-game
python app.py
```

On some systems, use `python3 app.py` instead.

## Windows executable

Every push to `main` runs the included GitHub Actions workflow and builds a standalone Windows executable.

1. Open the repository's **Actions** tab.
2. Select the latest successful **Build Windows executable** run.
3. Download the `NumberGuessingGame-Windows` artifact.
4. Extract the ZIP and run `NumberGuessingGame.exe`.

## Build the executable yourself

```bash
python -m pip install pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name NumberGuessingGame app.py
```

The executable will be created inside the `dist` folder.

## Project structure

```text
.
├── .github/workflows/build-windows.yml
├── .gitignore
├── app.py
└── README.md
```

## Note

This is a native desktop GUI application. GitHub Pages hosts websites, so it cannot run this Tkinter interface in a browser.
