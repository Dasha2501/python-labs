def check_truth(a, b, c):
    return (a and b) or c
#print(check_truth(True, False, True)) # True

def logical_equivalence(a, b):
    return bool(a) == bool(b)

#print(logical_equivalence(True, True)) # True
#print(logical_equivalence(True, False)) # False

def xor(a, b):
    return (a and not b) or (not a and b)
#print(xor(True, False)) # True
#print(xor(True, True)) # False

def greet(is_hello):
    if is_hello:
        return "Hello, World!"
    else:
        return "Goodbye, World!"
#print(greet(True)) # Hello, World!
#print(greet(False)) # Goodbye, World!

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"
#print(nested_condition(3, 3, 3)) # All same
#print(nested_condition(3, 4, 5)) # All different  

def count_true(bool_list):
    true_count = 0
    for value in bool_list:
        if value:
            true_count += 1
    return true_count
#print(count_true([True, False, True, False, True])) # 3

def parity(n):
    binary_str = bin(n)[2:]
    count_ones = binary_str.count('1')
    return count_ones % 2 == 0

#print(parity(15))


def majority_vote(a, b, c):
    true_count = a + b + c  
    return true_count > 1   
#print(majority_vote(True, True, False)) # True

def switch(value):
    return bool(1 - int(value))
#print(switch(True)) # False

def ternary_check(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
#print(ternary_check(True, "Yes", "No")) # Yes

def validate(x, y, z):
    return x or (y and z)
#print(validate(True, False, True)) # True

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"
#print(chain_check(1, 2, 3)) # Increasing
#print(chain_check(3, 2, 1)) # Decreasing
  
def filter_true(bool_list):
    true_values = []
    for value in bool_list:
        if value:
            true_values.append(value)
    return true_values
#print (filter_true([True, False, True, False])) # [True, True]

def multiplexer(bool1, bool2, bool3, num):
    if bool1:
        return num * 2
    elif bool2:
        return num * 3
    elif bool3:
        return num - 5
    else:
        return num
#print(multiplexer(False, False, True, 10)) # 5