# This program maintains a bookstore

#List for catalogue Book, Author, price

catalogue = [["Harry Potter" , "JK Rowlling", "19.99"]]

#lists for menu option
menu_option = [["View", "view"], ["Add","add"] , ["Edit","edit"] , ["Delete", "delete"], ["Exit Program", "exit"]]

def menu_select (menu_number):
        start_option = (menu_option[menu_number - 1][1])
        if start_option == "exit":
                return "0"
        else:
                return start_option
#display menu options
def display_menu():
        for i in range(len(menu_option)):
                print ((i+1), "." , menu_option[i][0]);       
                
#display catalogue
def display_catalogue():
        print (" NAME, AUTHOR, PRICE")
        for i in range (len(catalogue)):
                print (catalogue [i]);

#function for add:

        
menu = True

while menu == True:
        
        display_catalogue()
        
        display_menu()
              
        menu_number = int(input("Enter number of what you want to do: "))
        
        menu_select(menu_number)
        
        if menu_select == 0:
                menu = False
                
        else: 
        
                start_option = True
                
                add = False
                
                while add == True:
                        new_title = input("Enter new book's title: ")
                        new_author = input("Enter new book's author: ")
                        new_price = str(input("Enter new book's price: "))
                                        
                        new_book = [new_title, new_author, new_price]
                        
                        catalogue.append(new_book)
