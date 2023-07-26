from functools import lru_cache, reduce


# We are using memorization here to improve performance
@lru_cache(maxsize=None)
def calc_fibo(n):
    if n < 2:
        return n
    else:
        return calc_fibo(n - 1) + calc_fibo(n - 2)


fibo_sequence = list(map(calc_fibo, range(10)))
fibo_sequence_sum = reduce(lambda x, y: x + y, fibo_sequence)

print(fibo_sequence_sum)

# Output is 88
