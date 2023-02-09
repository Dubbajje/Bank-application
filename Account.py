class Account:
    def __init__(self, account_number, saldo):
        self.account_number = account_number
        self.saldo = saldo

    def __repr__(self):
        return f"Account number: {self.account_number}, Saldo: {self.saldo} "

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, new_saldo):
        self.saldo = new_saldo

    def change_saldo(self, new_saldo):
        self.saldo += new_saldo

    def print_saldo(self):
        print(self.saldo)

    def make_dictionary(self):
        dictionary = {}
        dictionary["account_number"] = self.account_number
        dictionary["saldo"] = self.saldo
        return dictionary