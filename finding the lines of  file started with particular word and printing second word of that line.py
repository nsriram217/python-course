fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    a=line.rstrip()
    b=line.split()
    if len(line)<3 or b[0]!="From": continue
    else:
        print(b[1])
        count = count+1
       
print("There were", count, "lines in the file with From as the first word")
