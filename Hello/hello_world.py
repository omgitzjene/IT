print("Hello World, my name is Jenny")


# def fibonacci(x):
# #     if x == 1 or x == 2:
# #         return 1
# #     if x > 2:
# #         return fibonacci(x-1) + fibonacci(x-2)
# #
# # for x in range(1,10):
# #     print(fibonacci(4))


def fib(num):
    if num == 0:
        return num
    if num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

x = input("Value? ")
for num in range(1, x+1):
    print(fib(num))






