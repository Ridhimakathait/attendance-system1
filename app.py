import sqlite3

# View attendance records
def view_attendance():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()

    print("\nAttendance Records:")
    print(f"{'ID':<5}{'Name':<20}{'Timestamp':<30}")
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<20}{row[2]:<30}")

if __name__ == "__main__":
    print("Welcome to the Automatic Attendance System!")
    view_attendance()