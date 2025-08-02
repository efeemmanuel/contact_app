# contact_manager.py
import csv

contact_book = {}

# CSV file name
csv_filename = "example.csv"

# Define the field names (headers)
fieldnames = ["name", "phone_number", "email"]



def welcome():
    print('Welcome to horizon Phone Book...')
    print('A. Add new contacts')
    print('B. View all saved contacts')
    print('C. Search for a contact by name')
    print('D. Delete a contact')
    print('E. Exit the app')
    









# Add new contacts (name, phone number, email)
# Fix: Change mode='w' ➝ mode='a' to append new entries
# Also use csv.DictWriter instead of writing .keys() and .values() (which is breaking the format).

def add_contact(name, phone_number, email):
    contact_book[name] = {'phone_number': phone_number, 'email': email}
    
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # If the file is empty, write header first
        file.seek(0)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'name': name,
            'phone_number': phone_number,
            'email': email
        })
    
    return contact_book


# View all saved contacts
def saved_contact():
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            print(f"{line['name']}: {line['phone_number']} | {line['email']}")


# Search for a contact by name
def search_contact(name):
    if name in contact_book:
        return print('found', name ,contact_book[name])
    else:
        if name not in contact_book:
            print(name, 'not found')


# Delete a contact
def delete_contact(name):
    contact_book.pop(name)
    return contact_book