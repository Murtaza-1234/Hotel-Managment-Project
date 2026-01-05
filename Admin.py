
import extra

def add_room(hotels):
    roomNumber = input("Enter Room Number: ")

    for room in hotels['rooms']:
        if room['roomNumber'] == roomNumber:
            print("Room already exists")
            extra.log_action(hotels, "admin", f"Add Room {roomNumber}", "failed")
            return
        
    roomType = input("Enter Room Type: ")
    pricePerNight = int(input("Enter Price Per Night: "))
    status = "available"

    
    new_room = {
            "roomNumber": roomNumber,
            "type": roomType,
            "pricePerNight": pricePerNight,
            "status": status
        }
    hotels['rooms'].append(new_room)
    extra.log_action(hotels, "admin", f"Add Room {roomNumber}", "successful")
    print("Room added successfully")

def update_room(hotels):
    room = input("Select the room number to update:")
    for r in hotels['rooms']:
        if r['roomNumber'] == room:
            print("1. Update Room Type")
            print("2. Update Price Per Night")
            print("3. Update Status")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_type = input("Enter new Room Type: ")
                r['roomType'] = new_type
                extra.log_action(hotels, "admin", f"Update Room {room} Type", "successful")
            elif choice == 2:
                new_price = input("Enter new Price Per Night: ")
                r['pricePerNight'] = new_price
                extra.log_action(hotels, "admin", f"Update Room {room} Price", "successful")
            elif choice == 3:
                new_status = input("Enter new Status (available/occupied): ")
                r['status'] = new_status
                extra.log_action(hotels, "admin", f"Update Room {room} Status", "successful")
            print("Room updated successfully")
            return
        
    else:
        extra.log_action(hotels, "admin", f"Update Room {room}", "failed")
        print("Room not found")

def delete_room(hotels):

    room = input("Select the room number to delete:")
    for r in hotels['rooms']:
        if r['roomNumber'] == room:
            hotels['rooms'].remove(r)
            print("Room deleted successfully")
            extra.log_action(hotels, "admin", f"Delete Room {room}", "successful")
            return
    else:
        extra.log_action(hotels, "admin", f"Delete Room {room}", "failed")
        print("Room not found")
        
def add_staff(hotels):

    staffId = input("Enter Staff ID: ")

    for staff in hotels["staffs"]:
        if staff["staffId"] == staffId:
            print("Staff ID already exists")
            extra.log_action(hotels, "admin", f"Adding existing Staff ID {staffId}", "failed")
            return
    name = input("Enter Staff Name: ")
    email = input("Enter Staff Email: ")
    phone = input("Enter Staff Phone: ")
    password = input("Enter Staff Password: ")

    new_staff = {
            "staffId": staffId,
            "name": name,
            "email": email,
            "phone": phone,
            "Password": password
        }
    hotels['staffs'].append(new_staff)
    extra.log_action(hotels, "admin", f"Add Staff {staffId}", "successful") 
    print("Staff added successfully")

def create_booking(hotels):
    booking_id = input("Enter Booking ID: ")
    for booking in hotels['bookings']:
        if booking['bookingId'] == booking_id:
            print("Booking ID already exists")
            extra.log_action(hotels, "admin", f"Creating existing Booking ID {booking_id}", "failed")
            return
    guest_id = input("Enter Guest ID: ")    
    room_number = input("Enter Room Number: ")
    check_in_date = input("Enter Check-In Date (DD-MM-YYYY): ")
    check_out_date = input("Enter Check-Out Date (DD-MM-YYYY): ")
    total_amount = input("Enter Total Amount: ")
    status = input("Enter Booking Status: ")

    new_booking = {
        "bookingId": booking_id,
        "guestId": guest_id,
        "roomNumber": room_number,
        "checkInDate": check_in_date,
        "checkOutDate": check_out_date,
        "totalAmount": total_amount,
        "status": status
    }
    hotels['bookings'].append(new_booking)
    extra.log_action(hotels, "admin", f"Add Booking {booking_id}", "successful")
    print("Booking created successfully")

def add_guest(hotels):
    guestId = input("Enter Guest ID: ")
    for guest in hotels["guests"]:
        if guest["guestId"] == guestId:
            print("Guest ID already exists")
            extra.log_action(hotels, "admin", f"Adding existing Guest ID {guestId}", "failed")
            return
    name = input("Enter Guest Name: ")
    email = input("Enter Guest Email: ")
    phone = input("Enter Guest Phone: ")

    new_guest = {
            "guestId": guestId,
            "name": name,
            "email": email,
            "phone": phone
        }
    hotels['guests'].append(new_guest)
    extra.log_action(hotels, "admin", f"Add Guest {guestId}", "successful")
    print("Guest added successfully")

def update_booking(hotels):
    booking_id = input("Enter Booking ID to update: ")
    for booking in hotels['bookings']:
        if booking['bookingId'] == booking_id:
            print("1. Update Check-In Date")
            print("2. Update Check-Out Date")
            print("3. Update Total Amount")
            print("4. Update Status")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_check_in = input("Enter new Check-In Date (DD-MM-YYYY): ")
                extra.log_action(hotels, "admin", f"Update Booking {booking_id} Check-In Date", "successful")
                booking['checkInDate'] = new_check_in
            elif choice == 2:
                new_check_out = input("Enter new Check-Out Date (DD-MM-YYYY): ")
                extra.log_action(hotels, "admin", f"Update Booking {booking_id} Check-Out Date", "successful")
                booking['checkOutDate'] = new_check_out
            elif choice == 3:
                new_total_amount = input("Enter new Total Amount: ")
                extra.log_action(hotels, "admin", f"Update Booking {booking_id} Total Amount", "successful")
                booking['totalAmount'] = new_total_amount
            elif choice == 4:
                new_status = input("Enter new Status: ")
                extra.log_action(hotels, "admin", f"Update Booking {booking_id} Status", "successful")
                booking['status'] = new_status
            print("Booking updated successfully")
            return
    else:
        extra.log_action(hotels, "admin", f"Update Booking {booking_id}", "failed")
        print("Booking not found")

def cancel_booking(hotels):
    booking_id = input("Enter Booking ID to cancel: ")
    for booking in hotels['bookings']:
        if booking['bookingId'] == booking_id:
            hotels['bookings'].remove(booking)
            for room in hotels['rooms']:
                if room['roomNumber'] == booking['roomNumber']:
                    room['status'] = 'available'
                    break
            print("Booking cancelled successfully")
            extra.log_action(hotels, "admin", f"Cancel Booking {booking_id}", "successful")
            return
    else:
        extra.log_action(hotels, "admin", f"Cancel Booking {booking_id}", "failed")
        print("Booking not found")

def view_logs(hotels):
    print("Activity Logs:")
    extra.log_action(hotels, "admin", "View Logs", "successful")
    for log in hotels['activityLogs']:
        print(log)
    






