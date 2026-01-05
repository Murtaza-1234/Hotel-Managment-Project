import extra

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
                booking['checkInDate'] = new_check_in
            elif choice == 2:
                new_check_out = input("Enter new Check-Out Date (DD-MM-YYYY): ")
                booking['checkOutDate'] = new_check_out
            elif choice == 3:
                new_total_amount = input("Enter new Total Amount: ")
                booking['totalAmount'] = new_total_amount
            elif choice == 4:
                new_status = input("Enter new Status: ")
                booking['status'] = new_status
            print("Booking updated successfully")
            return
    else:
        print("Booking not found")

def cancel_booking(hotels):
    booking_id = input("Enter Booking ID to cancel: ")
    for booking in hotels['bookings']:
        if booking['bookingId'] == booking_id:
            hotels['bookings'].remove(booking)
            print("Booking cancelled successfully")
            extra.log_action(hotels, "admin", f"Cancel Booking {booking_id}", "successful")
            extra.log_action(hotels, "admin", f"Cancel Booking {booking_id}", "successful")
            return
    else:
        extra.log_action(hotels, "admin", f"Cancel Booking {booking_id}", "failed")
        print("Booking not found")

def view_rooms(hotels):
    print("Available Rooms:")
    for room in hotels['rooms']:
        print(f"Room Number: {room['roomNumber']}, Type: {room['type']}, Price Per Night: {room['pricePerNight']}, Status: {room['status']}")
    extra.log_action(hotels, "admin", "View Rooms", "successful")

