from math import factorial, sqrt
from pprint import pprint as pp
from itertools import islice, count

words = "sometimes looks like this is just a string".split()
num_of_chars = [len(word) for word in words]
print(num_of_chars)

len_of_num = [len(str(factorial(number))) for number in range(20)]
print(len_of_num)

# Or with sets
len_of_num_set = {len(str(factorial(number))) for number in range(20)}
print(len_of_num_set)

# or dictionaries
cap_t_cou = {'UK': 'London', 'Italy': 'Rome', 'Austria': 'Vienna'}
cou_t_cap = {capital: country for country, capital in cap_t_cou.items()}
pp(cou_t_cap)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primes = [num for num in range(200) if is_prime(num)]
prime_square_divisors = {x*x:(1, x, x*x) for x in range(101) if is_prime(x)}
# pp(prime_square_divisors)

# Iteration protocols
iterable_seasons = ['spring', 'summer', 'autumn', 'winter']
iterator = iter(iterable_seasons)

def first(iterable_object):
    iterator = iter(iterable_object)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")

print(first(iterable_seasons))

# Generators
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123() # g is a generator object
print(next(g))
for value in gen123():
    print(value)

## Stateful generators
def take(cnt, iterable):
    counter = 0
    for item in iterable:
        if cnt == counter:
            return
        counter += 1
        yield item

def run_take():
    items = ['a','b','c','d','e','f','g']
    for item in take(3, items):
        print(item)

# run_take()

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_dist():
    items = [22,33,44,33,66,55,44,77]
    for item in distinct(items):
        print(item)

# run_dist()

def run_pipeline():
    items = [33,55,33,88,77,66,11,22,11,55,33,77,33]
    for item in take(4, distinct(items)):
        print(item)

# run_pipeline()

## Generator comprehensions
million_squares = (x*x for x in range(1, 1000001)) # creates a generator object
# both will print the same
print(sum(million_squares))
print(sum( x*x for x in range(1, 1000001) ))

# islice and count
thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)
print(sum(thousand_primes))