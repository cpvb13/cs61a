# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value
        self.next_val = 1

    def next(self):

    #self is start, which is an instance of Fib()
    #have to return something that is another instance, so I can call next() method
    # calling next on self needs a generator!

        result = Fib(self.next_val) #result is a new instance of Fib() where result.value is set to self.value
        result.next_val = result.value + self.value
        return result 

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10) 
    >>> v.vend() 
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.stock = 0
        self.balance = 0

    def is_stocked(self):
        return self.stock or False #or returns either the first Truthy value or the last Falsey value 
  
    def withdraw(self):
        self.balance = 0
        self.stock -=1     
  
    def vend(self):

        if self.is_stocked():
            if self.balance > self.price:
                change = self.balance-self.price
                self.withdraw()
                return 'Here is your {0} and ${1} change.'.format(self.name, change)
                
            elif self.balance == self.price:
                self.withdraw()
                return 'Here is your {0}.'.format(self.name)
                
            else:
                return 'You must deposit ${0} more.'.format(self.price-self.balance)

        else:
            return 'Machine is out of stock.'

    def restock(self, amount):
        self.stock += amount
        return 'Current {0} stock: {1}'.format(self.name,self.stock)


    def deposit(self,payment):
        if self.is_stocked():
            self.balance += payment
            return 'Current balance: ${0}'.format(self.balance)
        else:
            return 'Machine is out of stock. Here is your ${}.'.format(payment)



