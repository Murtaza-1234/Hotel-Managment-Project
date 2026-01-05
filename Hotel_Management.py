import json
import Admin
import Staff
import Guest


with open('Hotel_Data.json', 'r') as file:
    hotels = json.load(file)

print("Welcome to the Grand Horizon Hotel")
def login():
    print("Login")
    print("1. Admin")
    print("2. Staff")
    print("3. Guest")

    choice = input("Select your role : ")
    
    if choice == '1':
        password = input("Enter Admin Password: ")
        if password == "Admin@123":
            return "admin"
        else:
            print("Incorrect Password")
            return None
    elif choice == '2':
        for staff in hotels['staffs']:
            staff_id = input("Enter Staff ID: ")
            password = input("Enter Staff Password: ")
            if staff['staffId'] == staff_id and staff['Password'] == password:
                return "staff"  
    elif choice == '3':
        return "guest"  
    else:
        print("Invalid role selected")
        return None

try:
    while True:
        role = login()

        if role == "admin":
            print("Logged in as Admin")
            while True:
                print("MENU")
                print("1. Add Room")
                print("2. Update Room")
                print("3. Delete Room")
                print("4. Add Staff")
                print("5. Add Guest")
                print("6. Create Booking")
                print("7. Update Booking")
                print("8. Cancel Booking")
                print("9. View Logs")
                print("10. Exit")
                choice = input("Select an option: ")
                if choice == '1':
                    Admin.add_room(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                        
                elif choice == '2':
                    Admin.update_room(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '3':
                    Admin.delete_room(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '4':
                    Admin.add_staff(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '5':
                    Admin.add_guest(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '6':
                    Admin.create_booking(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '7':
                    Admin.update_booking(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '8':
                    Admin.cancel_booking(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '9':
                    Admin.view_logs(hotels)
                elif choice == '10':
                    print("Exiting...")
                    break
                else:
                    print("Invalid option selected")
                
                choice = input("Do you want to perform another operation? (y/n): ")
                if choice.lower() != 'y':
                    break

        elif role == "staff":
            print("Logged in as Staff")
            while True:
                print("MENU")
                print("1. Add Guest")
                print("2. Create Booking")
                print("3. Update Booking")
                print("4. Cancel Booking")
                print("5. View Rooms")
                print("6. Exit")
                choice = input("Select an option: ")
                if choice == '1':
                    Staff.add_guest(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '2':
                    Staff.create_booking(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '3':
                    Staff.update_booking(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '4':
                    Staff.cancel_booking(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '5':
                    Staff.view_rooms(hotels)
                elif choice == '6':
                    print("Exiting...")
                    break
                else:
                    print("Invalid option selected")

                choice = input("Do you want to perform another operation? (y/n): ")
                if choice.lower() != 'y':
                    break

        elif role == "guest":
            print("Logged in as Guest")
            while True:
                print("MENU")
                print("1. View Rooms")  
                print("2. View Own Booking")
                print("3. Book Room")
                print("4. Exit")
                choice = input("Select an option: ")
                if choice == '1':
                    Guest.view_rooms(hotels)
                elif choice == '2':
                    Guest.view_own_booking(hotels)
                elif choice == '3':
                    Guest.book_room(hotels)
                    with open('Hotel_Data.json', 'w') as file:
                        json.dump(hotels, file, indent=4)
                elif choice == '4':
                    print("Exiting...")
                    break
                else:
                    print("Invalid option selected")

                choice = input("Do you want to perform another operation? (y/n): ")
                if choice.lower() != 'y':
                    break
        choice = input("Do you want to login again? (y/n): ")
        if choice.lower() != 'y':
            print("Thank you for using the Hotel Management System. Goodbye!")
            break

except Exception as e:
    print(f"An error occurred: {e}")
    
