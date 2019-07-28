"""
Some scalable code patterns.
"""


""" --------- generator function ----------
You know this is a generator function because it has yield instead of return. It’s a kind of function, 
but behaves differently, because it’s completely scalable.
"""
def fetch_squares(limit):
    for root in range(limit):
        yield root*root

def generator_func():
    LIMIT = 5
    for sq in fetch_squares(LIMIT):
        print(sq)


""" ----------- High Level Collections -----------
List comprehension is a way to create a list. It’s a high-level and _declarative_ way to create a new list.
"""
def get_squares(limit):
    squares = []
    for root in range(limit):
        squares.append(root*root)
    return squares

def list_comprehension():
    limit = 5
    #sq = get_squares(limit)
    sq = [x*x for x in range(limit)]
    print(sq)

def list_comprehension_adv():
    # multi for
    colors = ["orange", "purple", "pink"]
    toys = ["bike", "basketball", "skateboard", "doll"]
    gifts = [
        color + " " + toy
        for color in colors
        for toy in toys
    ]
    print(gifts)

    # multi if
    numbers = [ 9 , -1 , -4 , 20 , 11 , -3 ]
    positive_evens = [
        num for num in numbers
        if num > 0
        if num % 2 == 0
    ]
    print(positive_evens)

def generator_comprehension():
    squares = (num*num for num in range(5))
    print(type(squares))
    for sq in squares:
        print(sq)

""" ------ OOP -----------
@property is a built-in Python decorator. By default Python properties are read only.
To make it settable, define .setter method
"""
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return self.first + " " + self.last

    @full_name.setter
    def full_name(self, new_name):
        first, last = new_name.split()
        self.first = first
        self.last = last

def oop_person():
    guy = Person('John', 'Smith')
    print(guy.full_name)

""" ------ Factory ---------
A factory is a function that helps you create an object.
"""
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @classmethod
    def from_string(cls, amount):
        # amount is $123.23
        import re
        match = re.search(r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
        if match is None:
            raise ValueError('Invalid amount: {}'.format(amount))
        dollars = int(match.group('dollars'))
        cents = int(match.group('cents'))
        return cls(dollars, cents)

class TipMoney(Money):
    pass

def factory():
    tip = TipMoney.from_string("$123.57")
    print(tip)
    print(tip.dollars, tip.cents)


if __name__ == '__main__':
    #generator_func()
    #list_comprehension_adv()
    #generator_comprehension()
    #oop_person()
    factory()
