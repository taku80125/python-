def decorator_name(power):


    def any_fun():
        print("ask me")

        power()

    return any_fun


@decorator_name
def question():
    print("hello")

@decorator_name
def survive():
    print("i live long")    

question()
survive()    

