def hello_world():
    print("Hello world")

def attempt(function, args=None):
    try:
        if args != None:
            return function(**args)
        else:
            function
    except Exception as e:
        print('Error', e)
        return False

attempt(hello_world())