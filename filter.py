words = ['Lorem','Ipsum','dummy']

file1 = open('text.txt','r')
fl = file1
newText = []


for line in fl:
    line.split()
    for w in words:
        line = line.replace(w,'****')
    newText.append(line)
    
print("===============")
print(newText)

