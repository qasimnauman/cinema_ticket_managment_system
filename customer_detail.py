contact = []
def addcontact():
    confirm = "y"
    while confirm == "y":
        contact.append(input("Enter customers name: "))
        contact.append(input("Enter customers contact number: "))
        contact.append(input("Enter customers CNIC: "))
        confirm = input("Enter y to add more record: ")
    return contact

def viewcontact(r1):
    if r1 == 0:
        print("No record found! ")
    else:
        print("CUSTOMER DETAILS: ")
        for i in range(0, len(contact), 3):
            print(contact[i],"\t",contact[i+1],"\t",contact[i+2])

def searchcontact(s):
    for i in range(2, len(contact), 3):
        if s == contact[i]:
            print("Name: ",contact[i-2])
            print("Phone number: ",contact[i-1])

def updatecontact(s):
    for i in range(2, len(contact), 3):
        if s == contact[i]:
            contact[i-2] = input("Enter name: ")
            contact[i-1] = input("Enter phone number")
