class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

#USERS
logan = User("Logan Awesome's", "slayincode@gmail.com")
jac = User("Jac Gunna", "gunnajacuup@gmail.com")
dave = User("Dave Naugler", "davenaugler@gmail.com")
anna = User("Anna Kendrick", "annagunnabenicenow@gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
logan.make_deposit(1000)
logan.make_deposit(500)
logan.make_deposit(100)
print(logan.account_balance)
#Account Balance = 1600

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
jac.make_deposit(1000)
jac.make_deposit(2000)
jac.make_withdrawal(50)
jac.make_withdrawal(50)
print(jac.account_balance)
#Account Balance = 2900

dave.make_deposit(1000)
dave.make_withdrawal(200)
dave.make_withdrawal(500)
dave.make_withdrawal(500)
print(dave.account_balance)
#Account Balance = -200

logan.make_deposit(1000)
print(logan.account_balance)

jac.transfer_money(logan, 100)
jac.display_user_balance()
logan.display_user_balance()























