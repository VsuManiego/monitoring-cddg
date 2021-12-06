# Error Management System


print("""
*** Welcome to Error Monitoring System! ***
        Administrator/Staff Log in
    """)  # Printing Welcome message


class StoreLogin:
    def __init__(self):
        self.data = {}

    def add_user(self, user_login, password):
        if user_login in self.data:
            raise AssertionError('This User already exists.')

        self.data[user_login] = password

    def check_user(self, user_login, password):
        if user_login not in self.data:
            return False

        if self.data[user_login] != password:
            return False

        return True


class InputLogin:
    def __init__(self):
        self.store = StoreLogin()

    def ask_user(self):
        username = input("Please Enter your Username: ")
        password = input("Please Enter your Password: ")

        return username, password

    def login_check(self):
        username, password = self.ask_user()

        while not self.store.check_user(username, password):
            print("\nIncorrect username or password.\n")
            if input("Are you a new user? (Y/N): ") == "Y":
                print("\nSTARTING REGISTRATION PROCESS...\n")
                username, password = self.ask_user()
                self.store.add_user(username, password)
                print("\nRegistration successful. Try to login again.\n")
            username, password = self.ask_user()

            import json

            def menu():
                while True:
                    print("\nWelcome! How may I help you?\n")
                    print("Enter 1 : Create a Complaint")
                    print("Enter 2 : View Complaint")
                    print("Enter 3 : Update Complaint Status")
                    print("Enter 4 : Cancel a Complaint")
                    print("Enter 5 : Logout")

                    try:  # Using exception for validation
                        option_input: int = int(input("""
Please select and option above: """))  # Asks the user to input an option
                    except ValueError:
                        exit("\n This is not a Number.")  # Error message
                    else:
                        print("\n")  # Print New line

                    if option_input == 1:  # This will print option 1 which is Create a complaint
                        print("""
Add your complaint details:
---------------------------
                                """)  # Printing complaint details
                        complaint_no = (int, input("Type Complaint No. : "))  # Asks the user to input complaint number
                        name = input("Name of Complainant : ")  # Asks the user to input their name
                        date = input("Date (MM/DD/YY) : ")  # Asks the user to input the date
                        department = input("""
Choose your Department
1 : Department 1
2 : Department 2
3 : Department 3
4 : Department 4
5 : Department 5
Enter Department No. here: """)
                        complaint_des = input("Complaint/Issue Description (100 words max) : ")
                        if len(complaint_des) > 100:
                            print("Please enter only 100 characters.")
                        else:
                            print("\n")

                        value = {'Complaint No': complaint_no, 'Name': name, 'Date': date, 'Department': department,
                            'Complaint': complaint_des}

                        file_path = 'Complaint.json'
                        with open('Complaint.json', 'w') as json_file:
                            json.dump(file_path, json_file)
                        print("Complaint successfully added! Thank you for informing us.")

                    elif option_input == 2:
                        view = int(input("Enter Complaint No. to view Complaint : "))
                        data = open('Complaint.json', 'r')
                        complaint = data.readlines(view)
                        if view in data:
                            print("\n-> Record found of this Complaint {}".format(complaint))
                        else:
                            print("\n-> No Record found of this Complaint {}".format(view))

                    elif option_input == 3:
                        update = int(input("Enter Complaint No. to view Complaint Status : "))
                        data = open('Complaint.json', 'r')
                        status = data.readlines(update)
                        if update in data:
                            print("\n-> Record found of this Complaint {}".format(status))
                        else:
                            print("\n-> No Record found of this Complaint No. {}".format(update))

                    elif option_input == 4:
                        cancel = int(input("Enter Complaint No. to Cancel a Complaint : "))
                        data = open('Complaint.json', 'r')
                        if cancel in data:
                            data.remove(cancel)
                            print("\n-> Complain No. {} successfully deleted. \n")
                            for complaints in data:
                                print("-> {}".format(complaints))
                        else:
                            print("\n-> No Record found of this Complaint No. {}".format(cancel))
                    else:
                        print('''
You have successfully logged out.
Thank you for using Error Monitoring System!\n''')
                        exit()

            menu()


manager = InputLogin()
manager.login_check()
