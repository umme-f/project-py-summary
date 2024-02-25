
# parent class
class User():
    def __init__(self,name, age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("details")
        print("")
        print("Name ", self.name)
        print("gender", self.gender)

# child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance+ amount
        print("Account balance updated", self.balance)
        