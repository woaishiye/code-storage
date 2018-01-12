with open('1024.ldb.geno')as f:
    for line in f:
        n = line.split()
        if len(n[0])<15:
            print(line.strip())
        else:
            a = n[0].split('_')
            b = 'LDB'
            c = n[1:]
            print('_'.join([a[0],b,a[2],a[3]])+'\t'+'\t'.join('%s'%j for j in c))
