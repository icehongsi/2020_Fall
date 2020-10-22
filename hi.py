class Greetings:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        a = "Hello " + self.name + "!"
        b = "Good-bye " + self.name + "!"
        return {"a": a,
                "b": b}


david = Greetings("David")
aaa = david.say_hi()
print(aaa['a'])
print(aaa['b'])