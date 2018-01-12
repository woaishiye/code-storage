with open('1024ldbnew.geno')as f:
    for line in f:
        n = line.split()
        v = n[0]
        a = n[4:450]
        print(v + '\t' + '\t'.join('%s'%j for j in a))
