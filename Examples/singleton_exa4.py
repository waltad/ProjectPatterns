""""Alex Martinelli zauważył (http://www.aleax.it/Python/5ep.html), że często potrzeba stosowania singletona wynika ze
 współdzielenia wyłącznie danych i zaproponował rozwiązanie oparte o wspólny atrybut __dict__:"""


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self):
        return self.val


if __name__ == '__main__':
    x = Singleton('jabłko')
    print(x)
    y = Singleton('gruszka')
    print(y)
    z = Singleton('śliwka')
    print(z)
    print(x)
    print(y)
