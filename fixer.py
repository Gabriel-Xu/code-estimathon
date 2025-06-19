import os

filedir = "txtFiles (1 - 10000)" 
outdir = "complete_list_bytes(admin).txt" 
broski = [] 
res = 0   
admin = open("complete_list_bytes(admin).txt", 'r').readlines()[:10000] 
output = "" 
for j in range(1, 10001):
    filename = f"FILE-{j:06d}.txt"
    # copy file to outdir
    with open(os.path.join(filedir, filename), 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.split() 
        a = 0 
        alpha="abcdefghijklmnopqrstuvwxyz"
        alpha+=alpha.upper()
        alpha={c for c in alpha}
        for word in content:  
            good=True  
            for c in word:
                if c not in alpha:
                    good=False
                    break 
            if good: 
                a += 1 
        broski.append(a) 
        admin[j-1] = admin[j-1].strip().split() 
        output += admin[j-1][0] + " " + str(a) + "\n" 
        
with open(outdir, 'w', encoding='utf-8') as out_file:
    out_file.write(output)  
for i in broski: 
    if i > 1100: 
        res += 1 
print(res) 