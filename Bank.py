
from Customer import *
from File_handling import *
from Account import *
from Account_generator import *
import json

class Bank:

    def __init__(self):
        self.list_of_customers = []
        self.inlogged_customer = None
        self.customer_dictionary_list = []

    def __repr__(self):
        return f"Bank-bank. Who´s there?"

    def add_customer(self, name, password):
        valid_name = self.check_for_duplicated_name(name)
        if valid_name:
            self.list_of_customers.append(Customer(name, password))
            return True
        return f"Customer not added please use another name"
    
    def check_for_duplicated_name(self, name):
        if self.get_customer(name) is None:
            return True
        return False
    
    def check_for_duplicated_account_number(self, account_number):
        for customer in self.list_of_customers:
            for account in customer.list_of_accounts:
                if account_number == account.account_number:
                    return True
                return False

    def get_customers(self):
        for customer in self.list_of_customers:
            print(customer)
        return self.list_of_customers

    def get_customer(self, name):
        for customer in self.list_of_customers:
            if name == customer.name:
                return customer
        return None

    def change_customer_password(self, name, new_password):
        customer = self.get_customer(name)
        if customer != None:
            customer.set_password(new_password)
            print("Password successfully changed")
            return customer
        return False

    def withdraw(self, account_number, amount):
        if self.inlogged_customer is None:
            return None
        account = self.inlogged_customer.get_account(account_number)
        if amount > account.get_saldo():
            print("Error, not enough funds")
            return False
        account.change_saldo(-amount)
        print("Successfull")
        return account

    def deposit(self, account_number, amount):
        if self.inlogged_customer is None:
            print(f"Please log in first")
            return None
        if amount < 0:
            print("Amount less than 0")
            return False
        account = self.inlogged_customer.get_account(account_number)
        if account is None:
            return f"Invalid account"
        account.change_saldo(amount)
        print("Successfull")
        return account

    def get_accounts(self):
        if self.inlogged_customer is not None:
            return self.inlogged_customer.get_accounts()
        return None

    def remove_customer(self, name):
        customer = self.get_customer(name)
        if customer is not None:
            self.list_of_customers.remove(customer)
            return customer
        return None

    def login(self, name, password_input):
        if self.inlogged_customer is not None:
            print("The line is full")
            return False
        customer = self.get_customer(name)
        if customer is None:
            return None
        self.check_is_valid_password(password_input, customer.password, customer)
        return True

    def check_is_valid_password(self, password_input, password, customer):
        if password == password_input:
            self.inlogged_customer = customer
            print(f"{customer.name} is online")
            return True
        print("Incorrect name or password")
        return False

    def logout(self):
        if self.inlogged_customer is None:
            return False
        print(f"{self.inlogged_customer.name} logged out")
        self.inlogged_customer = None
        return True

    def add_account(self):
        if self.inlogged_customer is None:
            print("Please log in first")
            return False
        new_account_number = AccountGenerator.generate_account_number()
        is_invalid_number = self.check_for_duplicated_account_number(new_account_number)
        if is_invalid_number:
            new_account_number = AccountGenerator.generate_account_number()
            new_account = (Account(new_account_number, 0))
            self.inlogged_customer.add_account(new_account)
            self.save_bank()
            self.load_bank()
            return
        new_account = (Account(new_account_number, 0))
        self.inlogged_customer.add_account(new_account)
        self.save_bank()
        self.load_bank()

    def remove_account(self, account_number):
        if self.inlogged_customer is None:
            print("Please, log in first")
            return None
        account = self.inlogged_customer.get_account(account_number)
        self.inlogged_customer.list_of_accounts.remove(account)
        return account

    def save_bank(self):
        self.customer_dictionary_list.append(AccountGenerator.save_state_of_account_number())
        for customer in self.list_of_customers:
            self.customer_dictionary_list.append(customer.make_dictionary())
        json_string = json.dumps(self.customer_dictionary_list, indent=2)
        File.write_to_file(self.customer_dictionary_list)

    def load_bank(self):
        self.list_of_customers.clear()
        self.customer_dictionary_list.clear()
        with open("mappmapp\database.json", "r") as file:
            try:
                dictionary = json.load(file)
                slice_of_list = dictionary[0]
                AccountGenerator.available_accounts_from = slice_of_list["current_accountnumber"]
                dictionary.pop(0)
                for customer_dictionary in dictionary:
                    customer = Customer(customer_dictionary["name"], customer_dictionary["password"])
                    self.list_of_customers.append(customer)
                    for account_dictionary in customer_dictionary["accounts"]:
                       account = Account(account_dictionary["account_number"], account_dictionary["saldo"])
                       customer.list_of_accounts.append(account)
            except BaseException as error:
                return f"Nothing to load"






