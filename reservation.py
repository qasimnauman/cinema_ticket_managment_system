from customer_detail import *
from movie_detail import *
reservation = []
cid = 0
def addreservation():
    cid = input("Enter Customers CNIC: ")
    if cid in contact:
        mid = input("Enter Movie's ID: ")
        while mid not in movie:
            print("Invalid Movie ID!")
            mid = input("Enter again: ")
        reservation.append(cid)
        reservation.append(mid)
        reservation.append(eval(input("Enter number of seats to reserve: ")))
    else:
        print(cid," not found! ")

def viewreservation(r3):
    if r3 == 0:
        print("No record found! ")
    else:
        print("RESERVATION DETAILS: ")
        print("Customer's Id \t Movie ID \t Numbe rof Seats")
        for i in range(0, len(reservation), 3):
            print(reservation[i],"\t",reservation[i+1],"\t",reservation[i+2])

def searchreservation(s):
    for i in range(0, len(reservation), 3):
        if reservation[i] == s:
            print("Customer's ID: ",reservation[i])
            print("Movie ID: ",reservation[i+1])
            print("Number of seats: ",reservation[i+2])
