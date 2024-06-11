from collections import deque
import itertools

def number_generator(numbers):
    for num in numbers:
        yield num

def even_number_generator(start, end):
    for num in range(start, end+1):
        if num % 2 == 0:
            yield num

def odd_number_generator(start, end):
    for num in range(start, end+1):
        if num % 2 != 0:
            yield num

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_number_generator(limit):
    for num in range(2, limit+1):
        if is_prime(num):
            yield num

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val

def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
            stack.extend(reversed(graph[node]))

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            yield node
            queue.extend(graph[node])

def dict_keys_generator(d):
    for key in d:
        yield key

def dict_values_generator(d):
    for value in d.values():
        yield value

def dict_items_generator(d):
    for item in d.items():
        yield item

def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def string_chars_generator(s):
    for char in s:
        yield char

def unique_elements_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item

def reverse_list_generator(lst):
    for i in range(len(lst)-1, -1, -1):
        yield lst[i]

def cartesian_product_generator(lst1, lst2):
    for x in lst1:
        for y in lst2:
            yield (x, y)

def permutations_generator(lst):
    yield from itertools.permutations(lst)

def combinations_generator(lst):
    for r in range(1, len(lst)+1):
        yield from itertools.combinations(lst, r)

def tuple_list_generator(tuples):
    for t in tuples:
        yield t

def parallel_lists_generator(*lists):
    yield from zip(*lists)

def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

def powers_of_two_generator(n):
    for i in range(n+1):
        yield 2**i

def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

def squares_generator(start, end):
    for num in range(start, end+1):
        yield num**2

def cubes_generator(start, end):
    for num in range(start, end+1):
        yield num**3
        
def factorials_generator(n):
    factorial = 1
    for i in range(n+1):
        yield factorial
        factorial *= (i+1)

def collatz_sequence_generator(n):
    while n != 1:
        yield n
        n = 3*n + 1 if n % 2 else n // 2
    yield 1

def geometric_progression_generator(a, r, limit):
    while a <= limit:
        yield a
        a *= r

def arithmetic_progression_generator(a, d, limit):
    while a <= limit:
        yield a
        a += d

def running_sum_generator(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

def running_product_generator(numbers):
    product = 1
    for num in numbers:
        product *= num
        yield product