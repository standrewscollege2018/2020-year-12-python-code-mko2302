'''Program is a travel price system'''

#list of depart location / connection price / connection needed
depart_location = [["Auckland", 0, "No"], ["Wellington", 50, "Yes"], ["Chirstchurch", 75, "Yes"]]

#list for destination / flight price / accomodation for 1 night price
destination = [["Sydney", 326, 120], ["Tonga", 378, 40], ["Shanghai", 1436, 60], ["London", 2376, 80]]

#list for user's selections for breakdown
selection_order = ["Departure location: ", "Connecting flight needed: ", "Departure price (return): $", "Destination: ", "Airfare cost: $", "Nights stayed: ","Cost for 1 night: $", "Accommodation sub-total: $", "Discount applied: ", "Accommodation total: $", "Subtotal (GST Excl): $", "GST: $", "Final cost: $"]


def display_depart():
    '''Function to display departure location list'''
    for i in range (len(depart_location)):
        print (i+1,".", depart_location[i][0] + " - Connection flight needed: " + str(depart_location[i][2]) + " - $" + str(depart_location[i][1]), "One way")
        
def display_destination():
    '''Function to display list of departure location'''
    for i in range (len(destination)):
        print (i+1, ".", destination[i][0], "- $" + str(destination[i][1]), "Return")

def find_depart_price(user_depart):
    '''Function to find cost of departure'''
    depart_cost = (depart_location[(user_depart - 1)][1]);
    return depart_cost

def find_depart_name(user_depart):
    '''Function to find the name of departure location'''
    depart_name = (depart_location[(user_depart - 1)][0]);
    return depart_name    


def find_destination_price(user_destination):
    '''Function to find cost of arrival'''
    destination_cost = (destination[(user_destination - 1)][1]);
    return destination_cost

def find_destination_name(user_destination):
    '''Function to find the name of the selected destination'''
    destination_name = (destination[(user_destination - 1)][0]);
    return destination_name

def display_sub_total():
    '''Displays the subtotal'''
    print ("Sub-total: $" + str(total_cost))

    
def night_cost(user_nights, user_destination):
    '''Finds the cost for one night'''
    one_night = (destination[user_destination - 1][2])
    return one_night
 
def accommodation_discount(accommodation_total, user_nights):
    '''Sees if number of nights is eligable for discount'''
    if user_nights >= 3:
        accomodaiton_final = accommodation_total * 0.8
        user_selection.append("YES")
        return accomodaiton_final
    else:
        accomodaiton_final = accommodation_total
        user_selection.append("NO")
        return accomodaiton_final

#loop to redo the program
running = True

while running == True:
#empty list for user selectinos
    user_selection = []    
    
#prices added for total cost
    total_cost = 0
    
    
    '''Departure code'''
#For finding depart location     
    display_depart()
    
    depart = True
    
    while depart == True:    
        try:
            user_depart = int(input("Type number of desired departure location: "))
            if user_depart in range(1, len(depart_location)+1):
                depart = False
            else:
                print ("ERROR: PLEASE ENTER VALID NUMBER")
            
        except: print ("ERROR: PLEASE ENTER VALID NUMBER")
    
#calculate cost for depart
    depart_cost = find_depart_price(user_depart)
    
    total_cost += (depart_cost * 2)
    
#find name for depart
    depart_name = find_depart_name(user_depart)
    
#adds to list for later
    user_selection.append(depart_name)
    
    if depart_cost == 0:
        user_selection.append("No")
    else:
        user_selection.append("Yes")
        
    user_selection.append(depart_cost)
    
#total
    display_sub_total()
    
    '''Destinaion code'''
    
    display_destination()
    
#finding destination
    
    find_destination = True
    
    while find_destination == True:    
        try:
            user_destination = int(input("Type number of desired arrival location: "))
            if user_destination in range(0, len(destination)+1):
                find_destination = False
            else:
                print ("ERROR: PLEASE ENTER VALID NUMBER")
            
        except: print ("ERROR: PLEASE ENTER VALID NUMBER")
    
#destination price
    destination_cost = find_destination_price(user_destination)
    
    total_cost += destination_cost 
    
#destination name
    destination_name = find_destination_name(user_destination)
    
    user_selection.append(destination_name)
    
    user_selection.append(destination_cost)
    
    display_sub_total()
    
    '''Nights'''
    
    nights = True
    
    while nights == True:
        try:
            user_nights = int(input("How many nights are you wanting to stay in " + str(destination_name) + " for: "))
            if user_nights > 1:
                nights = False
            else: 
                print ("ERROR: Please enter a valid number (min 1)")
            
        except: print ("ERROR: Please enter a valid number (min 1)")            
                
    user_selection.append(user_nights)
    
#finds one night
    one_night_total = night_cost(user_nights, user_destination)
    
#adds one night cost to list
    user_selection.append(one_night_total)
    
    accommodation_total = (one_night_total * user_nights)
    
    user_selection.append(accommodation_total)
    
    accommodation_final = accommodation_discount(accommodation_total,user_nights)
    
    total_cost += accommodation_final
    
    user_selection.append(accommodation_final)
    
#Calculations for subtotals
    
    gst_excl = round((total_cost / 1.15),0)
    
    user_selection.append(gst_excl)
    
    gst = round(total_cost - gst_excl)
    
    user_selection.append(gst)
    
    user_selection.append(total_cost)
    
    print ("")
    print ("COST BREAKDOWN")
    print ("")
    
    for i in range(len(user_selection)):
        print (str(selection_order[i]) + str(user_selection[i]))
    
    print("")
    
#confirm booking
    confirm = str(input("Would you like to confirm your booking? Type 'yes' or 'no' "))

    if confirm.lower() == "yes":
        running = False
        
    else: 
        print("")
        print("Resetting booking...")
        print("")
    
print("Your booking is now confirmed")    
        
        
        



    

    








    
    
    