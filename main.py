f = open("this.txt","r")
data = f.read()

f = open("copy.txt","w")
data = f.write(data)
print(data)
f.close()