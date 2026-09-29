#***************************start of 1st file********************************************
#this file contains functions to add, delete, update ,view one itemand view items in the list

def add_item(l):
    try:
        n=int(input("enter no of items :"))
    except ValueError:
        print("please enter a valid integer5")
    for i in range(n):
        try:
            item_id=input("enter item :")
            item_name=input("enter name :")
            item_price=int(input("enter price :"))
            item_quantity=int(input("enter quantity :"))
            item={"id":item_id,"name":item_name,"price":item_price,"quantity":item_quantity}
            l.append(item)
        except ValueError:
            print("please enter a valid integer")    
    return l
def del_item(l):
    try:
        n=int(input("enter no of items to delete :"))
    except ValueError:
        print("please enter a valid integer")
    
    item_id=input("enter item id to delete :")
    for i in l:

        if i["id"]==item_id:
            l.remove(i)
            print("item deleted successfully")
            return l
    print("item not found")
    return l
def update_item(l):
    try:
        n=int(input("enter no of items to update :"))
    except ValueError:
        print("please enter a valid integer")  
    item_id=input("enter item id to update :")
    for i in l:
        if i["id"]==item_id:
            item_name=input("enter new name :")
            item_price=float(input("enter new price :"))
            item_quantity=int(input("enter new quantity :"))
            i["name"]=item_name
            i["price"]=item_price
            i["quantity"]=item_quantity
    print("item not found")
    return l

def view_items(l):
    if len(l)==0:
        print("no items to display")
    else:
        for i in l:
            print("id:",i["id"],"name:",i["name"],"price:",i["price"],"quantity:",i["quantity"])    

def view_single_item(l):
    try:
        n=int(input("enter no of items to view :"))
    except ValueError:
        print("please enter a valid integer")
    item_id=input("enter item id to view :")
    for i in l:
        if i["id"]==item_id:
            print("id:",i["id"],"name:",i["name"],"price:",i["price"],"quantity:",i["quantity"])
    
