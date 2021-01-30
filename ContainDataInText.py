banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

with open('file3.txt', "w") as myfile:
        for i in banks_list:
                myfile.write( i)
                myfile.write("\n")



content = open('file3.txt')
print(content.read())