# 2023-04-27 17:56:46

# python generators:
n= 101
square_generator = (i*i for i in range(n))

for i in square_generator:
    print(i)




# python decorators:

def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()