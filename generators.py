def create_cubes(n):
    for x in range(n):
        yield x**3

def gen_ribbon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        yield a
        a,b = b,a+b
    return output

# for number in gen_ribbon(10):
#     print(number)

def simple_gen():
    for x in range(3):
        yield x

# for x in simple_gen():
#     print(x)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

s = 'Hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))