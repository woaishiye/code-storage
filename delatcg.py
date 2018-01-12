with open ('1024.ldb.geno')as f:
    for line in f:
        n = line.split()
        if len(n[0])>20:
            print(line.strip())
