def hello_world():
    print("Hello world")


def helloPerson(name):
    print('Hello %s' % (name))


def attempt(function, args=None):
    try:
        if args != None:
            return function(**args)  # check if ** is for dicts only
        else:
            function
    except Exception as e:
        print('Error', e)
        return False


attempt(hello_world())
attempt(helloPerson('Sparky'))


def attempt_decorator(target_function):
    def wrapper():
        try:
            target_function()
        except:
            return None
    return wrapper


@attempt_decorator
def graceful_func():
    print("We used a decorator to create a try / catch")
    return True


graceful_func()
