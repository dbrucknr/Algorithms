def hello_world():
    print("Hello world")

def helloPerson(name):
    print('Hello %s' %(name))

def attempt(function, args=None):
    try:
        if args != None:
            return function(**args) # check if ** is for dicts only
        else:
            function
    except Exception as e:
        print('Error', e)
        return False

attempt(hello_world())
attempt(helloPerson('Sparky'))