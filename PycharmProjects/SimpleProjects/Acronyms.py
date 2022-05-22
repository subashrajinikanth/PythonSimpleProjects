# input : world health organization
#output : WHO

name = input("Enter the String : ")
print(type(name))
print("Given string : ", name)
splitName = name.split()
print("After split : ", splitName)
acronym = ""
for i in splitName:
    print(i, " - ",i[0].upper())
    acronym = acronym + i[0].upper()
print("******Result*****")
print(acronym," - ",name)
