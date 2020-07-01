g = open('wasteland', mode='rt', encoding='utf-8')
g.read() # entire file
g.seek(0) # points to the start of the file

g.readline() # reads a single line
g.seek(0)

l = g.readlines()
print(l)
g.close()