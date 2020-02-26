'''Program is a travel price system'''


depart_location = [["Auckland", 0], ["Wellington", 50], ["Chirstchurch", 75]]

destination = [["Sydney", 326], ["Tonga", 378], ["Shanghai", 1436], ["London", 2376]]

def display_depart():
    '''Function to display departure location list'''
    for i in range (len(depart_location)):
        print (i+1,".", depart_location[i][0])
        
def display_arrival():
    '''Function to display list of departure location'''
    for i in range (len(destination)):
        print (i+1, ".", destination[i][0])

def find_depart_price(user_depart):
    '''Function to find cost of departure'''
    total_cost += (depart_location[(user_depart - 1)][1]);

total_cost = 0

final_depart = (depart_location[user_depart - 1][0])
     
display_depart()
user_depart = int(input("Type number of desired departure location: "))

find_depart_price(user_depart)
print (total_cost)

display_arrival()

user_arrival = int(input("Type number of desired arrival location: "))
    

    








    
    
    