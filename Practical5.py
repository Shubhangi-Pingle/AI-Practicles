import datetime
import webbrowser

user_details = {
    123456789: {'password': 1234, 'salary': 50000,'name':'Shubhangi'},
    987654321: {'password': 5678, 'salary': 60000,'name':'Shruti'}
}


def greet_user():
    current_time = datetime.datetime.now()
    if 6 <= current_time.hour < 12:
        print("Good morning!")
    elif 12 <= current_time.hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")


def display_menu():
    print("\nMenu:\n1. Bank Details\n2. Account Holder Information\n3. Balance Inquiry\n4. Home Loan\n5. Quit")

def bank_details():
    print("Bank Details:\n1.Bank detail 1 \n2.Bank detail 2")


def account_holder_info():
    account_no = int(input("Enter your account number: "))
    password = int(input("Enter your password: "))
    
    
    if account_no in user_details and password == user_details[account_no]['password']:
        print("Account Holder Information:\nAccount Number:",{account_no})
        print("\nAccount Holder Name:",user_details[account_no]['name'])
        print("\nSalary:",user_details[account_no]['salary'])
    else:
        print("Invalid account number or password. Please try again.")

def balance_inquiry():
    account_no = int(input("Enter your account number: "))
    password = int(input("Enter your password: "))
    
    
    if account_no in user_details and password == user_details[account_no]['password']:
        print(f"Balance Inquiry:\nAccount Number: {account_no}\nBalance: ${user_details[account_no]['salary']}")
    else:
        print("Invalid account number or password. Please try again.")

def home_loan():
    hdfc_home_loan_url = "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiS7oGHwuyEAxVobA8CHbCEA4YYABABGgJ0Yg&ase=2&gclid=CjwKCAjw17qvBhBrEiwA1rU9wya2HEmUOGuEg486z-CSNj61rM8HKkQgQ7h6ZeOldj2LYwHsTQd7ERoCKQgQAvD_BwE&ohost=www.google.com&cid=CAESVeD2eLL5f1Qb9dXHB-7JSd_fCGXitiX8A3vGIxsWwq1JQdhBaR8JVEDuPP_oRaqLfq4hniU33SwaBFmXqQv_TOs4jcuni534p0fMp1hZl_Ntky6jvQU&sig=AOD64_1VplDmQfP-4SCLucjofp3JEjVt7g&q&nis=4&adurl&ved=2ahUKEwivqvaGwuyEAxVdr1YBHWmvDWIQ0Qx6BAgHEAE"
    webbrowser.open(hdfc_home_loan_url)
    print("Home Loan: Opening HDFC Bank home loan page in your default web browser.")


def initialize_chatbot():
    user_name = input("Enter your name: ")
    greet_user()
    print(user_name + "!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            bank_details()
        elif choice == '2':
            account_holder_info()
        elif choice == '3':
            balance_inquiry()
        elif choice == '4':
            home_loan()
        elif choice == '5':
            feedback=input("Enter Your feedback:")
            print("Thank you for using our bank chat bot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


initialize_chatbot()
