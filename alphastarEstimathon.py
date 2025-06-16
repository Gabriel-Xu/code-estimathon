import os
import random

INPUT_FILENAME = "combined.txt"  
OUTPUT_DIR = "txtFiles (1 - 88140)"   
SUMMARY_FILE = "complete_list_bytes.txt" 
MIN_BYTES = 200
MAX_BYTES = 25000
MAX_FILES = 100000
ENCODING = 'utf-8'
STARTFILE = 88141

def parse_wiki_lines(filename):
    lines = []
    with open(filename, 'r', encoding=ENCODING) as f:
        started = False
        for line in f:
            if not started:
                if line.strip() == "":
                    started = True
                continue
            if line.strip():  # Non-empty lines only
                lines.append(line.strip())  # Remove trailing newlines
    return lines

def write_chunks(lines):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear or create the summary file
    with open(SUMMARY_FILE, 'w') as f:
        pass

    i = STARTFILE
    idx = 0

    while idx < len(lines) and i <= MAX_FILES:
        max_bytes = random.randint(MIN_BYTES, MAX_BYTES)
        buffer = ""
        current_bytes = 0

        while idx < len(lines):
            candidate = lines[idx]
            new_buffer = buffer + candidate
            new_size = len(new_buffer.encode(ENCODING))

            if new_size > max_bytes:
                break

            buffer = new_buffer
            current_bytes = new_size
            idx += 1

        if not buffer:
            idx += 1
            continue

        filename = f"{i}.txt"
        out_path = os.path.join(OUTPUT_DIR, filename)
        with open(out_path, 'w', encoding=ENCODING) as out_file:
            out_file.write(buffer)

        # Get exact file size from disk (safer than buffer size)
        file_size = os.path.getsize(out_path)

        # Append to summary file
        with open(SUMMARY_FILE, 'a') as summary:
            summary.write(f"{filename} - {file_size}\n")

        i += 1

    print(f"Finished writing {i-1} files to '{OUTPUT_DIR}'")
    print(f"File sizes logged in '{SUMMARY_FILE}'")

if __name__ == "__main__":
    lines = parse_wiki_lines(INPUT_FILENAME)
    write_chunks(lines)





