def fib(n):
    return fib_mem(n, dict())


def fib_mem(n, mem):
    """
    Memoized fibonacci function. Accumulates results as they
    are calculated.
    """
    if n in mem:
        return mem[n]

    if (n == 0 or n == 1):
        mem[n] = 1
        return 1

    val = fib_mem(n - 1, mem) + fib_mem(n - 2, mem)
    mem[n] = val
    return val
