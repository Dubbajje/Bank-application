from Account import *
from Bank import *
from Account_generator import *


class Customer:
    def __init__(self, name: object, password: object) -> object:
        self.name = name
        self.password = password
        self.list_of_accounts = []

    def __repr__(self):
        return f"{self.name}, {self.password}"

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_account(self, account_number):
        for account in self.list_of_accounts:
            if account.account_number == account_number:
                return account
        return None

    def get_accounts(self):
        print(f"{self.name}'s accounts:")
        for account in self.list_of_accounts:
            print(account)
        return None

    def add_account(self, account):
        self.list_of_accounts.append(account)
        print("Successfully added")

    def remove_account(self, account):
        self.list_of_accounts.remove(account)

    def make_dictionary(self):
        dictionary = {}
        dictionary["name"] = self.name
        dictionary["password"] = self.password
        dictionary["accounts"] = []
        for account in self.list_of_accounts:
            dictionary["accounts"].append(account.make_dictionary())
        return dictionary



