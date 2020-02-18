class Account:
    """
    Attributes:
    name: The name of the person
    money: The amount of money on the account
    pin_code: The pin code needed to access the account
    transactions: a list of the latest 10 transactions
    """
    def __init__(self, name, money, pin_code):
        """
        Creates a new account
        :param name: The name of the person
        :param money: The amount of money on the account
        :param pin_code: The pin code needed to access the account
        """
        self.name = name
        self.money = money
        self.pin_code = pin_code
        self.transactions = []


    def __str__(self):
        """
        Account information for printouts
        :return: A nice string including name, money and transaction
        history of the account
        """
        return self.name + ", Amount: " + str(self.money) + ", Transactions: " + str(self.transactions)

    def deposit(self, amount):
        """
        Used to add money to the account, also updates the
        transaction history
        :param amount: the amount of money
        :return: a string confirming the successful deposit
        """
        self.money += amount
        self.transactions.append(amount)
        if len(self.transactions) > 10:
            self.transactions.pop(0)
        return "Deposit successful"

    def withdrawal(self, amount, pin):
        """
        Used to withdraw (remove) money from the account, also
        updates the transaction history.
        :param amount: the amount of money
        :param pin: the pin needed to access the account
        :return: a string confirming the successful withdrawal, or
        notifying the user of wrong pin, or lack of money
        """
        if self.ok_PIN(pin) and self.money >= amount:
            self.money -= amount
            self.transactions.append(-amount)
            if len(self.transactions) > 10:
                self.transactions.pop(0)
            return "Withdrawal successful"
        elif not self.ok_PIN(pin):
            return "Wrong pincode"
        elif self.money < amount:
            return "You don't have enough money"

    def ok_PIN(self, pin):
        """
        Used to check if pin is correct
        :param pin: The pin code needed to access the account
        :return: Boolean variable, True if new_pin is correct, False
        otherwise
        """
        return pin == self.pin_code

    def change_PIN(self, old_pin, new_pin):
        """
        Used to change pin-code
        :param old_pin: the old pin code
        :param new_pin: the desired new pin code
        :return: a string confirming the successful change, or
        notifying that the pin was wrong
        """
        if self.ok_PIN(old_pin) and len(str(new_pin)) == 4:
            self.pin_code = new_pin
            return "Change of pincode successful"
        elif not self.ok_PIN(old_pin):
            return "Wrong pincode"
        elif len(str(new_pin)) != 4:
            return "The pincode must be 4 characters long"

class PremiumAccount(Account):
    def withdrawal(self, amount, pin):
        if amount > self.money:
            if self.ok_PIN(pin):
                return "Would you like a loan?"
            else:
                return "Wrong pincode"
        else:
            return Account.withdrawal(self, amount, pin)



def get_int_input(prompt_string):
    """
    Used to get an int from the user, asks again if input is
    not convertible to int
    :param prompt_string: the string explaining what to input
    :return: the int that was asked for
    """
    while True:
        try:
            tal = int(input(prompt_string))
        except ValueError:
            print("Du måste ange ett heltal!")
        else:
            return tal

def display_accounts(account_dict):
    """
    Used to display the information on all accounts (debugging
    only, not for bank customers)
    :param account_dict: a dictionary with the accounts
    :return: (nothing)
    """
    for account in account_dict:
        print(account_dict[account])

def menu():
     """
     Used to display the menu:
     What would you like to do?
     1 - Set up a new account
     2 - Deposit
     3 - Withdrawal
     4 - Change pin
     5 - Display earlier transactions
     6 - Exit
     :return: (nothing)
     """
     print("""-------------------------------------
     What would you like to do?
     1 - Set up a new account
     2 - Deposit
     3 - Withdrawal
     4 - Change pin
     5 - Display earlier transactions
     6 - Exit      
     """)

def menu_choice():
    """
    Used to get input on what the user wants to do
    :return: an int, the chosen menu option
    """
    while True:
        choice = get_int_input("Your choice: ")
        if choice < 1 or choice > 6:
            print("Alternativet finns inte.")
        else:
            return choice

def execute(choice):
    """
    Used to execute the option that the user chose
    :param choice: an int corresponding the the chosen option
    :return: (nothing)
    """
    while True:
        try:
            if choice == 1:
                name = input("Name: ")
                pin = get_int_input("PIN-code: ")
                amount = get_int_input("Amount: ")
                account = Account(name, amount, pin)
                account_dict[name] = account
            elif choice == 2:
                name = input("Name: ")
                amount = get_int_input("Amount: ")
                print(account_dict[name].deposit(amount))
            elif choice == 3:
                name = input("Name: ")
                pin = get_int_input("PIN-code: ")
                amount = get_int_input("Amount: ")
                print(account_dict[name].withdrawal(amount, pin))
            elif choice == 4:
                name = input("Name: ")
                old_pin = get_int_input("Current PIN-code: ")
                new_pin = get_int_input("New PIN-code: ")
                print(account_dict[name].change_PIN(old_pin, new_pin))
            elif choice == 5:
                name = input("Name: ")
                pin = get_int_input("PIN-code: ")
                if account_dict[name].ok_PIN(pin):
                    print(account_dict[name])
                else:
                    print("Wrong pincode")
            elif choice == 6:
                quit()
        except KeyError:
            print("Det finns inget konto")
        else:
            break

account_dict = {}
account_dict["Lisa"] = Account("Lisa", 200, 1111)
account_dict["Kalle"] = Account("Kalle", 100, 2222)
account_dict["Kim"] = Account("Kim", 300, 3333)
account_dict["Douglas"] = PremiumAccount("Douglas", 1000, 1234)

def main():
    while True:
        menu()
        execute(menu_choice())

if __name__ == "__main__":
    main()

