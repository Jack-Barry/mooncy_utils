# `mooncy_utils`

## What is it?

Utilities to assist with the moon cyanobacteria project overseen by Marguerite E Mauritz-Tozer at UTEP

## Setup

1. This project was written using Python version `3.12.1`. Make sure you have the correct version of Python installed. 
   > * It is recommended to use something like [`pyenv`](https://github.com/pyenv/pyenv) (or [`pyenv-win`](https://github.com/pyenv-win/pyenv-win) on Windows) to install Python versions to keep your environments clean.
   > * If you don't expect to run more than one version of Python, you can install it directly from [here](https://www.python.org/downloads/release/python-3121/).
2. Install dependencies by navigating to this project's root directory then running:
   ```none
   python -m pip install openpyxl
   ```

## Usage

### `move_images.py`

```none
python move_images.py --path <IMAGES_DIRS_ROOT_PATH>
```

Replace `<IMAGES_DIRS_ROOT_PATH>` in the above with the applicable relative path from the current working directory to the folder where images are being stored, e.g.:

```none
python move_images.py --path ../OneDriveContents
```