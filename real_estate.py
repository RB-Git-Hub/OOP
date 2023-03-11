import os

class PropertyListing():
    '''
    The PropertyListing class sets the format for each property listing.

    '''
    def __init__(self, property_details, is_available, property_viewed, 
property_type, property_agent, rent_or_sale):
        self.property_details = property_details
        self.is_available = True
        self.property_viewed = False
        self.property_type = property_type
        self.property_agent = property_agent
        self.rent_or_sale = rent_or_sale
                  
    def mark_as_viewed(self, obj):
        obj.property_viewed = True  

    def mark_as_not_available(self, obj):
        obj.is_available = False      

class Storage():
    '''
    Storage class holds the property listings formed in in
    a list called listings. 
    
    The functions are accessed using the main menu and are used to read and
    modifying the listings.

    '''
    
    listings= []

    # Adds a property to listings using PropertyListing class to format
    def add_property (self, property_details, property_agent, rent_or_sale,
 property_type):
             
        self.listings.append(PropertyListing(property_details, True, False,
 property_type, property_agent, rent_or_sale))
        
    # Counts all properties 
    def get_count(self):
        count = 0
        for obj in self.listings:
            if  obj.is_available is True:
                count += 1    
        print(f"\nThe total number of listings is {count}")

    # Shows a list of all properties with index 
    def get_property(self, rofs):
        count = -1
        for obj in self.listings:
            if obj.is_available is True:
                # This lists properties for rent/ sale as selected
                if rofs == obj.rent_or_sale:
                    count += 1
                    bcount = 0    
                    for obj in obj.property_details.split(","):
                        if bcount == 0:
                            ob = obj.replace("'", "").replace("(", "")  
                            print(f"{count}      {ob}")
                        bcount = 1
                # This lists all available properties
                elif rofs =="a":
                    count += 1
                    bcount = 0    
                    for obj in obj.property_details.split(","):
                        if bcount == 0:
                            ob = obj.replace("'", "").replace("(", "")  
                            print(f"{count}      {ob}")
                        bcount = 1
            # This lists all the unavailable properties for deletion
            elif rofs =="d":
                count += 1
                bcount = 0    
                for obj in obj.property_details.split(","):
                    if bcount == 0:
                        ob = obj.replace("'", "").replace("(", "")  
                        print(f"{count}      {ob}")
                    bcount = 1
            else:
                pass

    # Shows property detail selected by index
    def get_detail(self, rofs, index):
        count = 0
        for obj in self.listings:
            if obj.is_available is True:
                # If for sale or rent selected then it only shows those
                if rofs == obj.rent_or_sale:
                    try:
                        detail= ""
                        for line in obj.property_details.split(","):
                            ob = line.replace("'", "").replace("(", "")\
.replace(")", "")    
                            detail += line+"\n"
                            
                        if count == int(index):  
                            os.system("cls")
                            print(f"\n{detail}Property Type : {obj.property_type}\nAgent:\
 {obj.property_agent}")
                            PropertyListing.mark_as_not_available(
PropertyListing, obj)
                        count +=1    
                    except:
                        pass
                elif rofs =="a":
                    try:
                        detail= ""
                        for line in obj.property_details.split(","):
                            ob = line.replace("'", "").replace("(", "")\
.replace(")", "")    
                            detail += ob+"\n"
                        if count == int(index):  
                            os.system("cls")
                            print(f"\n{detail}Property Type : {obj.property_type}\nAgent:\
 {obj.property_agent}")
                            PropertyListing.mark_as_not_available(
PropertyListing, obj)
                        count+= 1
                    except:
                        pass

    # Shows a list of properties For sale
    def get_properties_for_sale(self):
        Storage.get_property(Storage,"f")

    # Shows a list of properties For rent
    def get_properties_for_rent(self):
        Storage.get_property(Storage,"r")

    # Deletes properties that have been leased or sold (not available)
    def delete(self, index):
        count = -1
        for obj in self.listings:
            if obj.is_available is False:
                count += 1
                #Try used to protect against selection of non int
                try:
                    if count == int(index): 
                        self.listings.remove(obj) 
                except:
                    pass

# Menu
message = '''Main Menu

a  - add property
t  - total number of available properties
v  - view property detail
gs - get properties for sale
gr - get properties for rent
d  - delete a property
e  - exit this program
'''

user_choice = ""

# Menu selection
while True:
    os.system("cls")
    user_choice = input(message).strip().lower()
    
    # a - Adds a property to list
    if user_choice == "a":
        os.system("cls")
        address1 = input("First line of address\t: ")
        city = input("City\t\t\t: ")
        zipcode = input("Zipcode\t\t\t: ")
        while True:
            p_type = input("Property type\n\tHouse\t\t- h\n\tLinked House\
\t- l\n\tAppartment\t- a\n\t\t\t: ").lower()
            if p_type == "h":
                property_type="House"   
                break     
            elif p_type == "l":
                property_type="Linked House"        
                break
            elif p_type == "a":
                property_type="Appartment"        
                break
            else:
                print("Try again")
        size = input("Size ㎡\t\t\t: ")
        bed = input("Bedrooms\t\t: ")
        bath = input("Bathrooms\t\t: ")
        features = input("Features\t\t: ")
        agent = input("Property Agent\t\t: ")
        property_details= (f"{address1},{city},{zipcode}\n,Size ㎡: {size},\
Number of bedrooms: {bed},Number of bathrooms: {bath},Features: {features}")
        while True:
            rent_or_sale = input("Offered\n\tFor sale\t- f\n\tFor rent\t- r\
\n\t\t\t: ").lower()
            if rent_or_sale == "f" or rent_or_sale == "r":
                break
            else:
                print("Try again")
        Storage.add_property(Storage, property_details, agent, rent_or_sale,
 property_type)
        print("\nProperty has been added")
        input("\nPress enter to go back to main menu")

    
    # t - Displays the total count of available properties   
    elif user_choice == "t":
        Storage.get_count(Storage)
        input("\nPress enter to go back to main menu")

    elif user_choice == "v":  
        # Lists all properties then allows the user to
        # view the contents of a property listing
        os.system("cls")
        Storage.get_property(Storage,"a")

        # Displays property detail selected by index
        choice = (input("\nPlease enter the index of the property to\
 view\n:"))
        Storage.get_detail(Storage, "a", choice)
        input("\nPress enter to go back to main menu")

    # Lists all properties For sale
    elif user_choice == "gs":  
        os.system("cls")
        Storage.get_properties_for_sale(Storage)
        input("\nPress enter to go back to main menu")

    # Lists all properties For rent
    elif user_choice == "gr":  
        os.system("cls")
        Storage.get_properties_for_rent(Storage)
        input("\nPress enter to go back to main menu")
  
    # d - Deletes a specific listing
    elif user_choice == "d":
        os.system("cls")
        # Displays leased or sold listings 
        Storage.get_property(Storage, "d")

        # Listing selected by index deleted
        property_index = (input("\nPlease enter the index of the property to \
be deleted\n: "))
        Storage.delete(Storage, property_index)
        print("Property has been deleted")

    # e - Exit
    elif user_choice == "e":
        print("\nGoodbye")
        break

    # Incorrect selection message
    else:
        input("Incorrect input please try again")