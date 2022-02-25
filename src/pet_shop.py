# WRITE YOUR FUNCTIONS HERE

from os import remove
from webbrowser import get


def get_pet_shop_name(shop_info):
    return shop_info['name']

def get_total_cash(shop_info):
    return shop_info["admin"]["total_cash"]

def add_or_remove_cash(shop_info, cash):
    shop_info["admin"]["total_cash"] += cash

def get_pets_sold(shop_info):
    return shop_info["admin"]["pets_sold"]

def increase_pets_sold(shop_info, quantity):
    shop_info["admin"]["pets_sold"] += quantity

def get_stock_count(shop_info):
    return len(shop_info["pets"])

def get_pets_by_breed(shop_info, breed):
    pets = []
    for pet in shop_info["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
        else:
            continue
    return pets

def find_pet_by_name(shop_info, name):
    
    for pet in shop_info["pets"]:
        if pet["name"] == name:
            return pet
        else: continue

def remove_pet_by_name(shop_info, name):
    for pet in shop_info["pets"]:
        if pet["name"] == name:
            shop_info["pets"].remove(pet)
        else: continue

def add_pet_to_stock(shop_info, new_pet):
    shop_info["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]



# grab price -> remove cash from customer -> add cash to shop ->
# -> Retrieve pet data and give to customer -> Remove pet data from shop

def sell_pet_to_customer(shop_info, pet, customer):
    if customer_can_afford_pet(customer, pet) == False:
        print(f"Sorry, {customer}. I can't give credit. Come back when you're a little... mmmmm... richer!")
        #morshu reference from "Link: The Faces of Evil"
    else:
        cash = pet["price"]
        remove_customer_cash(customer, cash)
        add_or_remove_cash(shop_info, cash)
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(shop_info, pet)
