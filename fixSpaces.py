import os
import re

pattern = re.compile(r"[.!?]\S*?\w")

filedir = "txtFiles (1 - 100000)"
outputdir = "txtFiles (1 - 100000) (fixed)"
os.makedirs(outputdir, exist_ok=True)

admin_filename = "complete_list_bytes(admin)(fixed).txt"
student_filename = "complete_list_bytes(student)(fixed).txt"

admin_file = open(admin_filename, 'w', encoding='utf-8')
student_file = open(student_filename, 'w', encoding='utf-8')

def fix_spaces(num):
    filename = os.path.join(filedir, f"FILE-{num:06d}.txt")
    outname = os.path.join(outputdir, f"FILE-{num:06d}.txt")

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

        new_content = list(content)
        for x in re.finditer(pattern, content):
            new_content[x.end()-2] += "\n\n"
        
        new_content = ''.join(new_content)
        with open(outname, 'w', encoding='utf-8') as file:
            file.write(new_content)

        file_size = os.path.getsize(outname)
        admin_file.write(f"FILE-{num:06d}.txt - {file_size}\n")
        student_file.write(f"{file_size}\n")



for i in range(1, 100001):
    if i % 1000 == 0:
        print(f"Processing file {i}...")
    fix_spaces(i)
