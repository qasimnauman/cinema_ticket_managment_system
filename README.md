# **Movie Management System**
## **Project Description**
Our project refers to a program used by the cinema staff to reserve tickets in accordance to the customer’s demand, which would later be printed and handed over to the customer. 
Firstly, the task was to make a program in which user was limited to only three records and  four attributes only , in this phase we were only restricted to while loop.
Secondly we were told to use functions, lists and modules in the program, which would give the user full control to add records till he wanted to do so.  
### **Program working (Modules and Entities):**
This program handles the information of movies, customers and their reservations.
In the beginning it shows the menu to the user, asking the user what to do. It shows the following options
1.	Add record
1.	View Record
1. Search Record
1.	Update Record
1.	Exit  

If user selects **_addition_** or **_viewing_** of record it shows the following option
1.	Add/View Customer 
1.	Add/View Movie
1.	Add/View Reservation  

If user selects the search or update it asks for the id, if the id of movie is entered it automatically moves to the movie section. If CNIC is entered it moves to customer section and also if reservation is made previously it would automatically be displayed along this.

Following are the details of modules
### **Module 1**  
First module is customer details. It contains a global list named contact. It contains four functions
1.	Addcontact
1.	Viewcontact
1.	Seacrhcontact
1.	Updatecontact  

Which are called in the **main module**.
**Addcontact** takes in the name, contact number and CNIC of the customer. **Viewcontact** views the all  record entered by the user. **Searchcontact** and updatecontact searches and updates against the CNIC of the customer which is asked in the main function respectively. For that a parameter is passed to both the functions.

### **Module 2**
Second module is of movie details and is almost identical to module 1. It contains a global list named movie It contains four functions
1.	Addmovie
1.	Viewmovie
1.	Seacrhmovie
1.	Updatemovie  

Which are called in the **main module**.
**Addmovie** takes in the name, id and genre of movie. **Viewmovie** views the all  record entered by the user. **Searchmovie** and **updatemovie** searches and updates against the movie id which is asked in the main function respectively. For that a parameter is passed to both the functions.  
### **Module 3**  
Third module is of reservation details and is almost identical to module 1 and module 2. Module 1 and  2 are imported in this module which allows it to use the elements of both the modules. It contains a global list named reservation. It contains four functions
1.	Addreservation
1.	Viewreservation
1.	Seacrhreservation  

Which are called in the **main module**.
**Addreservation** first validates if the customer CNIC is present in the record, then validates if the movie id is present in the record. If both are found it asks for the number of seats and reserves them against the CNIC of the customer. **Viewreservation** displays the reservations done by the customer. If the reservation is found against the CNIC searched, it would automatically displays the reservation along with the contact information.
