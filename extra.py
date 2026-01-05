from datetime import datetime


def generate_booking_id(bookings):
    if not bookings:
        return "B001"
    last_id = bookings[-1]['bookingId']
    numeric_part = int(last_id[1:]) + 1
    return f"B{numeric_part:03d}"

def generate_staff_id(staffs):
    if not staffs:
        return "S001"
    last_id = staffs[-1]['staffId']
    numeric_part = int(last_id[1:]) + 1
    return f"S{numeric_part:03d}"

def generate_guest_id(guests):
    if not guests:
        return "G001"
    last_id = guests[-1]['guestId']
    numeric_part = int(last_id[1:]) + 1
    return f"G{numeric_part:03d}"

def log_action(hotels, role, action, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "logId": f"L{len(hotels['activityLogs']) + 1:03d}",
        "timestamp": timestamp,
        "userRole": role,
        "action": action,
        "status": status
    }
    hotels['activityLogs'].append(log_entry)