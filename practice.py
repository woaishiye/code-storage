with open('cutwold.txt')as f:
    for line in f:
        n = line.split()[1:]
        print('\t'.join('%s'%j for j in n))
