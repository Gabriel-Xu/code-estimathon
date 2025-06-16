import re

input_filename = "complete_list_bytes(admin).txt"
output_filename = "complete_list_bytes(admin).txt"  # Overwrite same file

pattern = re.compile(r"^FILE-(\d+)\.txt - (\d+)$")

with open(input_filename, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

with open(output_filename, "w", encoding="utf-8") as outfile:
    for line in lines:
        line = line.strip()
        match = pattern.match(line)
        if match:
            number = int(match.group(1))
            size = match.group(2)
            padded_number = f"{number:06d}"
            new_line = f"FILE-{padded_number}.txt - {size}"
            outfile.write(new_line + "\n")
        else:
            outfile.write(line + "\n")  # Leave unmatching lines unchanged
