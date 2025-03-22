class BankAccount:
    def __init__(self):
        self.__salary = 5000 #private Attributes
    def salary(self):   
        return self.__salary 
obj=BankAccount()
print(obj.salary())