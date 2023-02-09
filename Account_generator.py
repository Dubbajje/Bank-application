class AccountGenerator:
    available_account_numbers_from = 1

    @staticmethod
    def generate_account_number():
        new_account_number = AccountGenerator.available_account_numbers_from + 1
        AccountGenerator.available_account_numbers_from += 1
        return new_account_number

    @staticmethod
    def save_state_of_account_number():
        return {
            "current_accountnumber" : AccountGenerator.available_account_numbers_from
        }

