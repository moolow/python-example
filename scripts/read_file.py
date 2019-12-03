filepath = '../data/greeting.txt'

# Read a file line-by-line - 1
with open(filepath, 'r') as f:
    print("Start Read a file line-by-line - 1")
    while True:
        line = f.readline()
        if line is None:
            print('line is None')
            break

        print(line.strip())

# Read a file line-by-line - 2
with open(filepath, 'r') as f:
    print("Start Read a file line-by-line - 2")
    for line in f:
        print(line.strip())