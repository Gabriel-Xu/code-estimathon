import os
filedir = "txtFiles (1 - 100000) (fixed)"

num_files = 0
for filename in os.listdir(filedir):
    if filename.endswith(".txt"):
        with open(os.path.join(filedir, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            if len(content.split()) > 1100:
                num_files += 1
print(f"Number of files with more than 1100 words: {num_files}")