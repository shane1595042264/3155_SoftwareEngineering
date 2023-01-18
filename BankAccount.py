class BankAccount:
    def __init__(self, customer_name, balance, minimum_balance, title):
        self.customer_name = customer_name
        self.balance = balance
        self.minimum_balance = minimum_balance
        self.title = title
    def deposit(self, amount):
        self.balance += amount
        print("Added amount: ", amount)
    def withdraw(self, amount):
        self.balance -= amount
        print("Removed amount: ", amount)
    def getCustomerInformation(self):
        print("Customer Information: ", self.customer_name + "\n Balance: " + self.balance +
             "\n Bank:" + self.title  )