"""
Author: Christopher Reid
Description: This program is calculates my monthly bills, bills totals, and the amount each roommate would owe.
"""


def main():
    print(' _______________________________ ')
    print('|                               |')
    print('|        CHOOSE A COMMAND       |')
    print('|_______________________________|')
    print('SET: Default preset bills (Current as of October 2022).')
    print('CUSTOM: Customize bill input.')
    print(' _______________________________ ')
    command = input('Enter your command: ')
    print()
    if command.upper() == 'CUSTOM':
        bills_custom()
    elif command.upper() == 'SET':
        bills_preset()

    again = input('Would you like to run this again? (Y/N): ')
    if again.upper() == 'Y':
        main()
    elif again.upper() == 'N':
        exit()


def bills_preset():
    """Bill presets current as of October 2022."""
    rent = 1338.10
    cars = 108.98
    internet = 102.05
    cell = 80.00
    Bills_PRESET(rent, cars, internet, cell)


def bills_custom():
    """Returns a dictionary of bills as determined by user input."""

    bills = {'rent': 0, 'car insurance': 0, 'internet': 0, 'cell phone': 0}
    for expense in bills:
        bills[expense] = float(input(f'How much was the {expense} bill this month?: \n'))
    Bills_CUSTOM(bills)


class Bills_CUSTOM:
    def __init__(self, bills):
        """Passed a dictionary containing the bills as an argument."""
        self.bills = bills
        self.bills['electricity'] = self.set_electricity()

        self.bills_list()
        self.print_total()

    def set_electricity(self):
        """Prompts user for electric bill because it can vary."""
        return float(input('How much was the electric bill this month?:\n'))

    def bills_list(self):
        """Prints each bill from the dictionary."""
        for name, amount in self.bills.items():
            print('________________________')
            print(f'{name}: ${amount}')
        print('________________________')

    def print_total(self):
        """Prints the total for the month."""
        total = 0
        for amount in self.bills.values():
            total += amount
        print(f'The total amount for this month is: ${round(total, 2)}')
        print()
        self.split_bills(total)

    def split_bills(self, total):
        """Prints the amount based on the number of roommates. """
        roommates = float(input('How many roommates are splitting the bill?:\n'))
        split = round((total / roommates), 2)
        print(f'Each roommate pays ${split} this month.')


class Bills_PRESET:
    def __init__(self, rent, cars, internet, cell):
        """Passed preset values for bills as arguments."""
        self.rent = rent
        self.cars = cars
        self.internet = internet
        self.cell = cell
        self.electricity = self.set_electricity()

        self.bills = {
            'Rent': self.rent,
            'Car Insurance': self.cars,
            'Internet': self.internet,
            'Cell Phone': self.cell,
            'Electricity': self.electricity
        }
        self.bills_list()
        self.print_total()

    def set_electricity(self):
        """Prompts user for electric bill because it can vary."""
        return float(input('How much was the electric bill this month?:\n'))

    def bills_list(self):
        """Prints each bill from the dictionary."""
        for name, amount in self.bills.items():
            print('________________________')
            print(f'{name}: ${amount}')
        print('________________________')

    def print_total(self):
        """Prints the total for the month."""
        total = 0
        for amount in self.bills.values():
            total += amount
        print(f'The total amount for this month is: ${round(total, 2)}')
        print()
        self.split_bills(total)

    def split_bills(self, total):
        """Prints the amount based on the number of roommates. """
        roommates = float(input('How many roommates are splitting the bill?:\n'))
        split = round((total / roommates), 2)
        print(f'Each roommate pays ${split} this month.')


main()
