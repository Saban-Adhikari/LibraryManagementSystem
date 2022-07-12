import datetime #importing the date and time
def file_read():
    '''Function to open and read the text file '''
    file = open("books.txt","r")
    print("The books that are available in the library are as follows: ")
    print(file.read())
    file.close

                
def borrow(a):
    '''Function to borrow books from the library '''
    #Creating a list to store and update the quantity of books
    list_book = []

    #Creating a list to store the prices of books
    list_price = []
    print ("\n"
        "You are now borrowing books ")


    continuity = True
    while continuity == True:

        #Error handling
        correctb_id = False
        while correctb_id == False:
            try:
                book_id = int(input("\n"
                    "Enter the Book ID of the book: "))
                correctb_id = True
            except:
                print("\n**************************************************************************************\n" 
                          " \t \t Please ONLY enter integer/correct id!\n"
                          "*************************************************************************************\n")

        '''While loop for valid number and available book id '''
        while book_id <= 0 or book_id>len(dicts):
            print("\n**********************************************************************************\n" 
                          " \t \t  Please ONLY enter the Book ID shown in the screen!\n"
                         "**********************************************************************************\n")

            #Error handling
            correctb_ids = False
            while correctb_ids == False:
                try:
                    book_id = int(input("Enter the Book ID of the book: "))
                    correctb_ids = True
                except:
                    print("\n------------------------------------------------------------------------------------\n" 
                          " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                          "-------------------------------------------------------------------------------------\n")

        '''Checking if the book is available or not!'''
        #If the book is unavailable
        if (int(dicts[book_id][2])) == 0:
            print("\n"
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  "\t \t Book is out of stock!\n"
                  "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            
        #If the book is available
        else :
            print("\n"
                "----------------------------------------------------------------------------------\n"
                  "\t \t Book is in stock!\n"
                 "----------------------------------------------------------------------------------\n")
            
            name = input("\n"
                "Please enter the name of the borrower: ")
            list_price.append(dicts[book_id][3]) #adding the price of the book to the list list_price
            list_book.append(dicts[book_id][0])#adding the name of the book to the list list_book
            print ("The price of the book is $",(dicts[book_id][3]))
            datetime1 = datetime.datetime.now()#date and time of the borrowing of book/books

            '''Total price of books borrowed '''
            total = list(map(int,list_price))
            Sum_price = sum(total)
            print("The date and time of book borrowed is: ", datetime1)

            #Updating the list after book is borrowed
            dicts[book_id][2] = int(dicts[book_id][2]) - 1

            #Calling function to write updated values in the dictionary and text file
            write_dictionary()

            '''For displaying the library after book/books is borrowed '''
            print("\n"
                "The library after the book borrowed is: ")
            dictionary_print()
            continuity = False

        '''Code to ask user for borrowing another book'''
        continu_ = True
        while continu_ == True:

            '''Function to ask user if they want to borrow another book'''
            Another = input("\n"
                        "Do you wish to buy any other book as well? \n"
                        "If Yes enter 'Yes' or else other value: ")
            if Another == "y" or Another == "Y" or Another == "Yes" or Another == "yes":

                #Error handling for the input of bookID & for other books
                Another_correct = False
                while Another_correct == False:
                    try:
                        bid_ = int(input("Enter the book ID of another book you wish to borrow: "))
                        Another_correct = True
                            
                    except:
                        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                              " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                              "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                #Checking the availability of book          
                while bid_ <= 0 or bid_>len(dicts):
                    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                          " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                    #Error handling for input
                    Check_correct = False
                    while Check_correct == False:
                        try:
                            book_id = int(input("Enter the book ID of the book you want to return: "))
                            Check_correct = True
                            
                        except:
                            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                              " \t \t Please ONLY enter the Book ID shown in the screen\n"
                              "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                #Condition to check the availability of book
                if (int(dicts[bid_][2])) == 0:
                    print("\n"
                        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                          "\t \t Book is out of stock!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                #Condition if the book is in stock   
                else :
                    print("\n"
                    "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                      "\t \t Book is in stock!\n"
                     "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                    list_price.append(dicts[bid_][3])#adding the price of the book to the list list_price
                    list_book.append(dicts[bid_][0])#adding the name of the book to the list list_book

                    '''Calculating the total price of books borrowed'''
                    total = list(map(int,list_price))
                    Sum_price = sum(total)

                    #Updating the availability of books after borrowing
                    dicts[bid_][2] = int(dicts[bid_][2]) - 1

                    #Calling function to write updated values in the dictionary and text file
                    write_dictionary()

                    '''Displaying the library after the process of borrowing is completed'''
                    print("\n"
                    "Library after borrowing is: ")
                    dictionary_print()
                
            else:
                '''Creating a receipt for the books borrowed'''
                continu_ = False
                print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                       "\t \t A receipt has been generated for the books you have borrowed \n"
                       "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                file = open("borrow_"+name+randoms+".txt","w")
                file.write("The name of the borrower is: "+ str(name)+"\n")
                file.write("The total price of the book/books: $"+ str(Sum_price)+ "\n")
                file.write("Date and time of book/books borrowed is: "+ str(datetime1)+ "\n")
                file.write("The book/books borrowed are: ")
                for i in range(len(list_book)):
                    file.write(str(list_book[i])+"\n")
                file.close()

    #Calling the function "Welcome" to bring the main interface back
    Welcome()


def write_dictionary():
    file = open("books.txt","w")
    for values in dicts.values():
        file.write(str(values[0]) + ","+ str(values[1])+ ","+str(values[2])+","+ str(values[3]))
        file.write("\n")
    file.close()

def number_random():
    '''A function to generate random numbers '''
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    micro = str(datetime.datetime.now().microsecond)

    random = minute + second + micro

    return random

randoms = number_random()
    
def returning(a):
    '''Function for returning book to the library'''
    #Creating a list to store and update data after the return
    list_return=[]

    #Creating a list to store data of fine after the return is late
    list_fine =[]
    print ("\n"
        "You are now returning book/books")

    '''For the bookid of the book that is being returned'''
    #Error Handling of the input value from the user
    Return_correct = False
    while Return_correct == False:
        try:
            book_return = int(input("Enter the BookID of the book you want to return: "))
            Return_correct = True

        except:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                    " \t \t Please ONLY enter integer/correct id!\n"
                  "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    
    while book_return <= 0 or book_return>len(dicts):
        #Checking if the availability of the books
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                          " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

        '''Asking the user for BookID after wrong value input'''
        #Error handling
        correctRet = False
        while correctRet == False:
            try:
                book_return = int(input("Enter the Book ID of the book: "))
                correctRet = True
            except:
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                          " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
              
    dicts[book_return][2] = int(dicts[book_return][2]) + 1 #Updating the dictionary after the return of a book
    list_return.append(dicts[book_return][0]) #adding the name of the book to the list_return

    #Calling function to write updated values in the dictionary and text file.
    write_dictionary()
    
    name = input("Please enter the name of the person returning the book: ") #Asking user for their name.

    '''Asking the user for the number of days they borrowed the book'''
    #Error handling for the input from the user.
    correctFine = False
    while correctFine == False:
        try:  
            fine = int(input("Enter the number of days you have had the book for: "))
            correctFine = True

        except:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                    " \t \t Please enter an integer/number value!\n"
                 "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    '''Calculating fine if the user has kept book for mmore than 10 days'''
    if fine > 10:
        fine_amount = (fine-10)*0.10*int(dicts[book_return][3])
        list_fine.append(fine_amount) #Adding the fine to the list list_fine
        totalfine = sum(list_fine) #Calculating the total sum of fine
        print("Your fine for not returning book in time is: $", totalfine)

    else:
        totalfine = 0
    datetime_return = datetime.datetime.now() #date and time of return of the book.

    '''Displaying the library after the process of borrow is completed to the user'''
    print("\n"
    "The library after return is: ")
    dictionary_print()

    '''Code to ask user for borrowing another book'''
    continu_ = True
    while continu_ == True:

        #Asking the user if they want to return any other books.
        Another = input("\n"
                "Do you want to return another book as well? \n"
                        "If Yes please enter 'Yes' or else provide any other value: ")
        if Another == "y" or Another == "Y" or Another == "Yes" or Another == "yes":

            #Error handling for input of bookID for other books.
            Return_correct_ = False
            while Return_correct_ == False:
                try:
                    return_book_ = int(input("Enter bookID of the book you want to return: "))
                    Return_correct_ = True

                except:
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                    " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                      "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

            while return_book_ <= 0 or return_book_>len(dicts):
                #Checking if the book is available or not 
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                                  " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                                  "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                #Error handling for input of bookID for other books after wrong valid input.
                correctRetr = False
                while correctRetr == False:
                    try:
                        return_book_ = int(input("Enter the Book ID of the book: "))
                        correctRetr = True
                    except:
                        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                                  " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                                  "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

            #Error handling for input of number of days the user has borrowed the book for.
            correctFine = False
            while correctFine == False:
                try:
                    fines = int(input("Enter the number of days you have had the book/books: "))
                    correctFine = True

                except:
                    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                             " \t \t Please ONLY enter the Book ID shown in the screen!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                            
            dicts[return_book_][2] = int(dicts[return_book_][2]) + 1 #Updating the dictionary after return of a book.
            list_return.append(dicts[return_book_][0]) #adding the name of the book to the list_return.

            if fines > 10:
                fineamounts = (fines -10)*0.10*int(dicts[return_book_][3])
                list_fine.append(fineamounts)#Adding the fine to the list list_fine.
                totalfine = sum(list_fine)#Calculating the total sum of fine.
                print("The total fine you need to pay is: $", totalfine)

            #Calling function to write updated values in the dictionary and text file.
            write_dictionary()
            
            '''Displaying the library after the process of borrow is completed to the user.'''
            print("\n"
            "Library after return is: ")
            dictionary_print()

        else:
            '''Writing note to generate the outcome of the purchase/borrow.'''
            continu_ = False
            print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                       "\t \t A receipt has been generated for your return of the books.\n"
                       "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

            file = open("return_"+name+randoms+".txt","w")
            file.write("The name of the returner is: "+ str(name)+"\n")
            file.write("The date and time of book borrowed is: "+ str(datetime_return)+ "\n")
            file.write("The books returned are: ")
            for i in range(len(list_return)):
                file.write(str(list_return[i])+"\n")
            file.write("The total fine due is : $" + str(totalfine))
            file.close()
           

def exit(a):
    '''Creating a function to display the user has exited the library management system.'''
    print ("\n"
        "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
      "\t \t Thank you for using the library management system. You have exited the system. Adios!!!.\n"
      "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

def Welcome():
    print("\n"
        "*************************************************************************************\n"
          "\t \tWelcome to the library management system!\n"
          "*************************************************************************************\n")

    #Calling the fucntion "dictionary_print" to display the books available in the dictionary.
    dictionary_print()

    #Calling the function "user" to ask input value from the user to navigate around the program.
    user()

def dictionary_print():
    '''To display the books available '''
    print("\n"
        "-------------------------------------------------------------------------------------")
    print("Book ID " + " Book-Name \t"  + " Author \t" + "   Quantity  " + "  Price($) " )
    print("-------------------------------------------------------------------------------------")

    #Creating a dictionary to extract and store values from the text value
    dictionary ={}
    
    '''Code to generate the table of books and its details.'''
    file = open("books.txt","r")
    n = 0
    for line in file:
        n = n + 1
        line = line.replace("\n","")
        dictionary [n] = line.split(',')
        line = line.replace(",", " \t")
        
        print(n, "\t", line) 
    print("\n-------------------------------------------------------------------------------------\n")
    file.close()
    
def dictsbook():
    dictionary ={}
    file = open("books.txt","r")
    n = 0
    for line in file:
        n = n + 1
        line = line.replace("\n","")
        dictionary [n] = line.split(',')
        line = line.replace(",", " \t")

    file.close()
    return dictionary

#Assigning the function "dictbook" to a variable.
dicts = dictsbook()

def user():
    '''function to help user navigate around the program'''

    #Error handling
    properUserInput = False
    while properUserInput == False:
        try:
            #Asking the user input value to navigate with different functions of the program.
            User_Input = int(input("\n"
                            "Enter '1' to borrow a book\n"
                            "Enter '2' to return a book\n"
                            "Enter '3' to exit\n"
                            "Please enter a value: "))
            properUserInput = True

        except:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" 
                          " \t \t Error! Please ONLY enter a valid input that is 1, 2, 3!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    #Function after the user has entered a valid input.
    if User_Input == 1:
                borrow(User_Input) #The user will be redirected to the borrowing section.

    elif User_Input == 2:
                returning(User_Input)#The user will be redirected to the returning section.
                Welcome()

    elif User_Input == 3:
                exit(User_Input)#User will exit the system.
 
    else:
        #Redirects the user to the main interface if any value other than 1, 2, & 3 is provided.
        print ("\n"
                "Invalid input. Please only input numbers shown on the screen.")
        Welcome()

    return User_Input 
