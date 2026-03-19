with open('/tmp/ppay', 'r') as f:
    lines = f.readlines()

new_lines = []

for i,line in enumerate(lines):
    new_lines.append(line)
    if (i+1) % 2 == 0:
        new_lines.append("peter\n")

with open('/tmp/ppay', 'w') as f:
    f.writelines(new_lines)

