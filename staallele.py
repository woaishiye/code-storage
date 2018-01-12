allele = [] 
with open('outn(w).txt')as f:
    for line in f:
        n = line.split()
        myset = set(n)
        v = list(myset)
        q = len(v)
        allele.append(q)
    print(allele)

myset1 = set(allele)
for i in myset1:
    print('%s have %d'%(i,allele.count(i)))
