file=open("file4.txt","r")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("others.txt","w")
for data in file:
    
    if "delhi" in data:
        f1.write(data)
    elif "shimla" in data:
        f2.write(data)
    else:
        f3.write(data)
f1.close()
f2.close()
f3.close()

