with open('same.txt')as f:
    for line in f:
        n = line.split('_')
        a = n[2]
        b = n[3]
        print(int(b)-int(a))
