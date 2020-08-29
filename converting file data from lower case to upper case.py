fname = input("Enter file name: ")
fh = open(fname)
fr=fh.read()
for line in fh:
    line=line.upper()
    line=line.rstrip()
    print(line)
