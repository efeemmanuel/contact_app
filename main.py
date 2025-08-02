# main.py
import contact_manager
from contact_manager import welcome, add_contact, saved_contact, contact_book, search_contact, delete_contact



def main():

    welcome()
    user_input = input('Select an option: a/b/c/d/e:   ')

    while True:
        if user_input.lower() == 'a':
            name = input('Enter recepient name: ')
            phone_number = int(input('Enter recepient phone number: '))
            email = input('Enter recepient email: ')
            add_contact(name, phone_number, email)
            print('successfully added........')
            welcome()
            user_input = input('Select an option: a/b/c/d/e:   ')
        elif user_input.lower() == 'b':
            print('here are you saved contacts......')
            saved_contact()
            welcome()
            user_input = input('Select an option: a/b/c/d/e:   ')
        elif user_input.lower() == 'c':
            print('Search for a contact....')
            name = input('Enter recepient name: ')
            search_contact(name)
            welcome()
            user_input = input('Select an option: a/b/c/d/e:   ')
        elif user_input.lower() == 'd':
            print('Enter the name of the contact to delete......')
            name = input('Enter recepient name: ')
            delete_contact(name)
            welcome()
            user_input = input('Select an option: a/b/c/d/e:   ')
        elif user_input.lower() == 'e':
            print('Goodbye....')
            break
        else:
            welcome()
            user_input = input('Select an option: a/b/c/d/e:   ')
            

    
 







if __name__ == '__main__':
    main()

