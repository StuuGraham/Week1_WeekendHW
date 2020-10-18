# Function 1;
def get_pet_shop_name(shop):
    return shop["name"]
# This block of code looks through a list denoted as shop and looks for the "name".

# Functon 2;
def get_total_cash(shop):
    return int(shop["admin"]["total_cash"])
# This block calls the shop list again, this time looking for the info stored under "total_cash"within the "admin" part of the 
# list and converts the returned value into an integer.

#Function 3 (Test 3 & 4);
def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash
# This requires two arguments, the shop list and the cash value to be added or subtracted, the second line calls the place in 
# the specified list to be amended and the += adds the cash value This works for adding and subtracting here as the "remove_cash"
# example has a negative integer.

# Function 4 (Test 5);
def get_pets_sold(shop):
    return int(shop["admin"]["pets_sold"])
# This is the same as get_total_cash above, just calling on a different place in the dictionary.

# Function 5 (Test 6);
def increase_pets_sold(shop, sales):
    shop["admin"]["pets_sold"] += sales
# This again the same as adding/removing cash, just in a different place in the dictionary.

# Function 6 (Test 7);
def get_stock_count(shop):
    return len(shop["pets"])
# This returns the "length" of the called dictionary pets within the shop dictionary by length, this just means the number of 
# items.

# Function 7 (Test 8 & 9);
def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet["breed"])
    return pets
# This block of code opens a new empty list, pets. The for line tells the code where to look and then says if the breed of the 
# pet matches in input argument breed, then append this pet to the empty list. Finally the list is returned and the length can 
# be checked in the test code.

# Function 8 (Test 10 & 12);
def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if name == pet["name"]:
            return pet
# This is similar to Function 7, we have just changed to comparing the pets name and then returned the pet if the name matches 
# rather than append it to a list.

# Fuction 9 (Test 13);
def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)
# This is the same as above again, however now we are using the for loop, to remove the pet from the  list if the variable 
# matches the information in the list.

# Function 10 (Test 14);
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)
    return len(shop["pets"])
# Here we append the argument variable new_pet to the list and then return the length of the list.

# Function 11 (Test 15);
def get_customer_cash(customer):
    return customer["cash"]
# This is the same as function 1, we are now accessing a different dictionary in the test code.

# Function 12 (Test 16);
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
# This is the same as function 3, just in a different dictionary.  

# Function 13 (Test 17);
def get_customer_pet_count(customer):
    return len(customer["pets"])

# Function 14 (Test 18);
def add_pet_to_customer(customer, new_pet):
        customer["pets"].append(new_pet)
        return len(customer["pets"])
# Here I have appended the new pet which is defined in the test code, to the dictionary of the  customers pets and then 
# returned the length of that dictionary.

# Additional Tests, Section 1

# Function 1 (Test 19);
def customer_can_afford_pet(customer, price):
    for money in customer["cash"]:
        if money > can_buy_pet:
            return True
        elif money < can_buy_pet:
            return False
        elif money == can_buy_pet:
            return True

# Got stuck at this point... :(