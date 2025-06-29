import csv
import sqlite3
import random
from datetime import datetime, timedelta
import os

# === Setup ===
csv_path = "data/attendance.csv"
db_path = "data/attendance.db"
names = ["Aarav", "Diya", "Ishaan", "Sneha", "Rohan", "Meera", "Aditya", "Sara", "Kiran", "Tara", 
         "Neha", "Ayaan", "Nisha", "Kabir", "Riya", "Dev", "Priya", "Arjun", "Anaya", "Varun"]

# === Create DB if not exists ===
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT,
        name TEXT,
        timestamp TEXT
    )
''')
conn.commit()

# === Create CSV with header if it doesn't exist ===
if not os.path.exists(csv_path):
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['UID', 'Name', 'Timestamp'])

# === Generate random timestamp within last 30 days ===
def random_timestamp():
    now = datetime.now()
    days_ago = random.randint(0, 30)
    random_time = now - timedelta(days=days_ago, hours=random.randint(0, 23), minutes=random.randint(0, 59))
    return random_time.strftime("%Y-%m-%d %H:%M:%S")

# === Simulate Attendance Logs ===
def simulate_attendance(n=100):
    for _ in range(n):
        uid = "UID" + str(random.randint(1000, 9999))
        name = random.choice(names)
        timestamp = random_timestamp()

        # Save to CSV
        with open(csv_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([uid, name, timestamp])

        # Save to SQLite
        c.execute("INSERT INTO attendance (uid, name, timestamp) VALUES (?, ?, ?)", (uid, name, timestamp))
        conn.commit()

    print(f"✅ Simulated {n} attendance records!")

# === Run Logger ===
if __name__ == "__main__":
    simulate_attendance(100)
