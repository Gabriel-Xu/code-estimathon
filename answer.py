import os
filedir = "txtFiles (1 - 10000)"

num_files = 0
for i in range(1, 10001):
    filename = f"FILE-{i:06d}.txt"
    with open(os.path.join(filedir, filename), 'r', encoding='utf-8') as file:
        content = file.read()
        if len(content.split()) > 1100:
            num_files += 1
print(f"Number of files with more than 1100 words: {num_files}")