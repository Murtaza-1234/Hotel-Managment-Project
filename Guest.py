import extra
from datetime import datetime
def view_rooms(hotels):

    print("Available Rooms:")
    for room in hotels['rooms']:
        print(f"Room Number: {room['roomNumber']}, Type: {room['type']}, Price Per Night: {room['pricePerNight']}, Status: {room['status']}")
    extra.log_action(hotels, "guest", "View Rooms", "successful")

def view_own_booking(hotels):
    guest_id = input("Enter your Guest ID: ")
    found = False
    for booking in hotels['bookings']:
        if booking['guestId'] == guest_id:
            print(f"Booking ID: {booking['bookingId']}, Room Number: {booking['roomNumber']}, Check-In Date: {booking['checkInDate']}, Check-Out Date: {booking['checkOutDate']}, Total Amount: {booking['totalAmount']}, Status: {booking['status']}")
            found = True
            extra.log_action(hotels, "guest", f"View Booking {booking['bookingId']}", "successful")
    if not found:
        extra.log_action(hotels, "guest", f"View Booking for Guest ID {guest_id}", "failed")
        print("No bookings found for this Guest ID")


def book_room(hotels):
    room_number = input("Enter Room Number to book: ")
    for room in hotels['rooms']:
        if room['roomNumber'] == room_number:
            
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            phone = input("Enter Your Phone: ")
            check_in_date = input("Enter Check-In Date (DD-MM-YYYY): ")
            check_out_date = input("Enter Check-Out Date (DD-MM-YYYY): ")  
            status = 'confirmed'        

            check_in = datetime.strptime(check_in_date, "%d-%m-%Y")
            check_out = datetime.strptime(check_out_date, "%d-%m-%Y")
            days = (check_out - check_in).days
            total_amount = room['pricePerNight'] * days

            booking_id = extra.generate_booking_id(hotels['bookings'])
            guest_id = extra.generate_guest_id(hotels['guests'])

            new_guest = {
                    "guestId": guest_id,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "role": "guest"
                }

            if room['status'] == 'available':
                new_booking = {
                    "bookingId": booking_id,
                    "guestId": guest_id,
                    "roomNumber": room_number,
                    "checkInDate": check_in_date,
                    "checkOutDate": check_out_date,
                    "totalAmount": total_amount,
                    "status": "confirmed"
                    
                }
                room['status'] = 'occupied'
               
                hotels['bookings'].append(new_booking)
                hotels['guests'].append(new_guest)

                print("Room booked successfully")
                print(f"Your Booking ID is {booking_id} and Guest ID is {guest_id}")
                print(f"Total Amount to be paid: {total_amount}")
                extra.log_action(hotels, "guest", f"Book Room {room_number} with Booking ID {booking_id}", "successful")
                return
              

            else:
                print("Room is not available for booking")
                ch = input("Want to wait (yes/no): ")
                if ch == "yes":
                    new_booking = {
                    "bookingId": booking_id,
                    "guestId": guest_id,
                    "roomNumber": room_number,
                    "checkInDate": check_in_date,
                    "checkOutDate": check_out_date,
                    "totalAmount": total_amount,
                    "status": "Waiting"
                    
                }
                    hotels['guests'].append(new_guest)
                    hotels['bookings'].append(new_booking)
                    extra.log_action(hotels, "guest", f"Wait for Room {room_number}", "successful")
                    print("You are now on the waiting list for this room.")
                else:
                    return
    else:
        extra.log_action(hotels, "guest", f"Book Room {room_number}", "failed")
        print("Room not found")
        return
    
    