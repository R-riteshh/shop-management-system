#***************************start of 2nd file********************************************
#this is main file which contains the main function to call the functions from the first file
import project_part_1

l=["item_id","item_name","item_price","item_quantity"]

while True:
    print("1. add item")
    print("2. delete item")
    print("3. update item")
    print("4. view items")
    print("5. view item")
    print("6. exit")

    choice=input("enter your choice :")
    
    if choice=="1":
        l=project_part_1.add_item(l)
    elif choice=="2":
        l=project_part_1.del_item(l)
    elif choice=="3":
        l=project_part_1.update_item(l)
    elif choice=="4":
        project_part_1.view_items(l)
    elif choice=="5":
        project_part_1.view_single_item(l)
    elif choice=="6":
        break
    else:
        print("invalid choice")
