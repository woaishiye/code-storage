ldb1 = []
with open('1024ldbold.txt')as f1:
    for line1 in f1:
        n = line1.split()
        ldb1.append(n[0])

ldb2 = []
with open('1024ldbnew.geno')as f2:
    for line2 in f2:
        v = line2.split()
        ldb2.append(v[0])

ldb3 = []
for i in ldb1:
    if i in ldb2:
        ldb3.append(i)

for k in ldb3:
    if len(k)<15:
        print(k)

print(len(ldb3))
            
            
