python
import csv
import os
from datetime import datetime

FILE_NAME = "attendance_records.csv"

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Student ID", "Student Name", "Status"])

def mark_attendance():
    """Records attendance for a student with the current date."""
    date_today = datetime.now().strftime("%Y-%m-%d")
    student_id = input("Enter Student ID: ").strip()
    student_name = input("Enter Student Full Name: ").strip()
    
    print("Status options: [P] Present | [A] Absent | [L] Late")
    status_choice = input("Enter status (P/A/L): ").strip().upper()
    
    status_map = {"P": "Present", "A": "Absent", "L": "Late"}
    status = status_map.get(status_choice, "Present")
    
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_today, student_id, student_name, status])
        
    print(f"\n[SUCCESS] Attendance recorded: {student_name} ({status}) on {date_today}\n")

def view_attendance():
    """Displays all saved attendance records."""
    if not os.path.exists(FILE_NAME):
        print("\nNo attendance records found.\n")
        return
        
    print("\n" + "=" * 60)
    print(f"{'DATE':<12} | {'ID':<10} | {'STUDENT NAME':<22} | {'STATUS':<10}")
    print("=" * 60)
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        records_found = False
        for row in reader:
            if row:
                records_found = True
                print(f"{row[0]:<12} | {row[1]:<10} | {row[2]:<22} | {row[3]:<10}")
        if not records_found:
            print("No records entered yet.")
    print("=" * 60 + "\n")

def search_student():
    """Searches attendance history by Student ID or Name."""
    query = input("Enter Student ID or Name to search: ").strip().lower()
    found = False
    
    print("\n--- Search Results ---")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row and (query in row[1].lower() or query in row[2].lower()):
                print(f"Date: {row[0]} | ID: {row[1]} | Name: {row[2]} | Status: {row[3]}")
                found = True
                
    if not found:
        print("No matching records found.")
    print("----------------------\n")

def main():
    initialize_file()
    while True:
        print("=== STUDENT ATTENDANCE MONITORING SYSTEM ===")
        print("1. Mark Student Attendance")
        print("2. View All Attendance Records")
        print("3. Search Student Record")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
