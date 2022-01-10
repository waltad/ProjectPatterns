""""Użycie dekoratora skutecznie i elegancko rozdziela implementację klasy singletona od "mechaniki:"""


def Singleton(class_):
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    return get_instance


@Singleton
class FirstClass:
    def __init__(self):
        self.val = 0


@Singleton
class SecondClass:
    def __init__(self):
        self.val = 0


if __name__ == '__main__':
    a = FirstClass()
    print(a.val)
    a.val = 10
    b = FirstClass()
    print(b.val)

    c = SecondClass()
    print(c.val)
    c.val = 20
    d = SecondClass()
    print(d.val)
