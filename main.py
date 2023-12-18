from customer_detail import *
from movie_detail import *
from reservation import *
search = 0
recordc = 0
recordm = 0
recordr = 0
print("MOVIE MANAGEMENT")
print("1. Add Record")
print("2. View Records")
print("3. Search Record")
print("4. Update Record")
print("5. Exit")
check = eval(input("Enter number: "))
while not check == 5:
    while check > 5 or check < 1:
        print("Invalid Input!")
        check = eval(input("Enter number again: "))
    if check == 1:
        print("1 to add customer")
        print("2 to add movie")
        print("3 to add reservation")
        add = eval(input("Enter "))
        while add < 1 or add > 3:
            add = eval(input("Invalid Input!\nEnter again: "))
        if add == 1:
            recordc += 1
            addcontact()
        elif add == 2:
            recordm += 1
            addmovie()
        else:
            recordr += 1
            addreservation()
    elif check == 2:
        print("1 to view customer")
        print("2 to view movie")
        print("2 to view reservation")
        view = eval(input("Enter "))
        while view < 1 or view > 3:
            view = eval(input("Invalid Input!\nEnter again: "))
        if view == 1:
            viewcontact(recordc)
        elif view == 2:
            viewmovie(recordm)
        else:
            viewreservation(recordr)
    elif check == 3:
        search = input("Enter Id number: ")
        searchcontact(search)
        searchmovie(search)
        searchreservation(search)
    else:
        search = input("Enter Id number: ")
        updatecontact(search)
        updatemovie(search)
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Exit")
    check = eval(input("Enter number: "))
