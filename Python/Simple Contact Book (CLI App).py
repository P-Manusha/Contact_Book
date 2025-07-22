contacts={}
while True:
    print("Contact Menu\n 1.Add Number\n 2.View Contacts\n 3.Search Contact\n 4.Delete Contact \n 5.Exit")
    option=input("Enter a option")
    if option=="1":
        name=input("Enter the name").lower()
        if name not in contacts:
            number=input(f"Enter the number of {name}")
            contacts[name]=number
            print("✅ Contact Added Successfully")
        else:
            print("⚠️Contact Already Existed !")
    elif option=="2":
        if contacts:
            for name in contacts:
                print(f"{name}--{contacts[name]}")
        else:
            print("No Contacts Added")
    elif option=="3":
        searches=input("Enter a Name to Search ")
        if searches in contacts:
            print(f"contact found {searches}--{contacts[searches]}")
        else:
            print("Contact Not Found")
    elif option=="4":
        delete=input("enter the name to be deleted")
        if delete in contacts:
            del contacts[delete]
            print("✅Contact Deleted Successfully!")
        else:
            print("Contact is Not Found")
    elif option=="5":
        print("exit")
        break
    else:
        print("Enter a Correct Option")