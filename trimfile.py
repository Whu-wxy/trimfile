
with open('c:/Users/Administrator/Desktop//trimfile2.txt', 'w', encoding='gbk') as f:
    with open('c:/Users/Administrator/Desktop//trimfile.txt', 'r', encoding='gbk') as f2:
        lines = f2.readlines()
        for line in lines:
            line = line.replace('\n', '').replace('\r', '').strip()
            if line.endswith('#'):
                # print(line)
                f.write('\n'+line.replace('#', '\n'))
            else:
                f.write(line.replace('\n', '').replace('\r', '').strip()) 