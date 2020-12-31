def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))

import time

# Current time before
start_time = time.time()
# Run the code
result = func_one(1000000)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)

# Current time before
start_time = time.time()
# Run the code
result = func_two(1000000)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)

import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

result2 = timeit.timeit(stmt,setup, number=1000000)

print(result2)

stmt = '''
func_two(100)
'''

setup = '''
def func_two(n):
    return list(map(str,range(n)))
'''

result3 = timeit.timeit(stmt,setup, number=1000000)

print(result3)