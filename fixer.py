import os

filedir = "txtFiles (1 - 100000) (fixed)"
outdir = "txtFiles (1 - 10000)"

admin = open("complete_list_bytes(admin)(fixed).txt", 'r').readlines()[:10000]
adminout = open("complete_list_bytes(admin).txt", 'w')
studentout = open("complete_list_bytes(student).txt", 'w')

for i in range(1, 10001):
    filename = f"FILE-{i:06d}.txt"

    wc = None
    bs = admin[i-1].strip().split(" - ")[-1]
    
    # copy file to outdir
    with open(os.path.join(filedir, filename), 'r', encoding='utf-8') as file:
        content = file.read()
        wc = len(content.split())
        with open(os.path.join(outdir, filename), 'w', encoding='utf-8') as out_file:
            out_file.write(content)
    
    adminout.write(f"{bs} {wc}\n")
    studentout.write(f"{bs}\n")