movie = []
def addmovie():
    confirm = "y"
    while confirm == "y":
        movie.append(input("Enter movie's name: "))
        movie.append(input("Enter movie's id number: "))
        movie.append(input("Enter movie's genre: "))
        confirm = input("Enter y to add more record: ")
    return movie

def viewmovie(r2):
    if r2 == 0:
        print("No record found! ")
    else:
        print("MOVIE DETAILS: ")
        for i in range(0, len(movie), 3):
            print(movie[i],"\t",movie[i+1],"\t",movie[i+2])

def searchmovie(s):
    for i in range(1, len(movie), 3):
        if s == movie[i]:
            print("Movie: ",movie[i-1])
            print("Genre: ",movie[i+1])

def updatemovie(s):
    for i in range(1, len(movie), 3):
        if s == movie[i]:
            movie[i-1] = input("Enter Movie's name: ")
            movie[i+1] = input("Enter movie's genre: ")
