def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

# Decora a funcao say_hello
say_hello = my_decorator(say_hello)
say_hello()

print()

# Decora a funcao say_goodbye porem usando a sintaxe @
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()

