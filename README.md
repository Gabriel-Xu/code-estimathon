# Code Estimathon

A small PHP web application for browsing a collection of numbered text files and viewing each file's size and contents. The repository also includes Python utilities for generating and querying word-count metadata for the text collection.

## Project Structure

- `index.php` — Web interface for loading files numbered `1` through `10000`.
- `txtFiles (1 - 10000)/` — Input text files named `FILE-000001.txt` through `FILE-010000.txt`.
- `fixer.py` — Processes the text files, counts alphabetic words in each file, and writes the results to a metadata file.
- `answer.py` — Reads `complete_list_bytes(admin).txt` and counts entries whose recorded value is greater than `1100`.
- `complete_list_bytes(admin).txt` — Generated metadata for the text files.
- `complete_list_bytes(student).txt` — Additional metadata associated with the text files.

## Requirements

- PHP 7 or newer
- Python 3.6 or newer

No external PHP or Python packages are required.

## Running the Web App

From the repository root, start PHP's built-in development server:

```bash
php -S localhost:8000
```

Open [http://localhost:8000](http://localhost:8000) in a browser. Enter a file number between `1` and `10000` to view the corresponding text file and its size in bytes.

The application expects the data directory and filenames to remain unchanged:

```text
txtFiles (1 - 10000)/FILE-000001.txt
txtFiles (1 - 10000)/FILE-000002.txt
...
```

## Running the Python Utilities

To regenerate the administrator metadata from the text files:

```bash
python fixer.py
```

To count metadata entries greater than `1100`:

```bash
python answer.py
```

Run both commands from the repository root so the relative file paths resolve correctly. `fixer.py` overwrites `complete_list_bytes(admin).txt`.

## How It Works

1. `index.php` accepts a file number through a GET request.
2. The number is validated and converted to a six-digit filename.
3. The matching text file is read and displayed safely in the browser.
4. The file size is calculated in bytes and shown above the contents.
5. `fixer.py` scans each file, counts tokens made entirely of alphabetic characters, and saves one result per file.
6. `answer.py` reads those results and counts values above the configured threshold.

## Notes

- The text-file collection is required for the PHP application and Python scripts to work.
- Invalid file numbers, missing files, and unreadable files are reported by the web interface.
- Generated metadata files may change when `fixer.py` is run.
