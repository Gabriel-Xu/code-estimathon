import os
filedir = "complete_list_bytes(admin).txt"  

num_files = 0 
with open(filedir, 'r', encoding='utf-8') as file: 
    for i in file: 
        a, b = i.split(" ") 
        if int(b) > 1100: 
            num_files += 1 
print(f"Number of files with more than 1100 words: {num_files}")   