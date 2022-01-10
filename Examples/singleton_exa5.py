""""Najbardziej polecana implementacja singletona w Pythone opiera się o metaklasę.
Metaklasa jest wołana automatycznie gdy deklaracja klasy używająca metaklasy się skończy, innymi słowy: - jeśli nie ma
 słowa kluczowego metaclass po klasach bazowych wołane jest type() (a dokładnie metoda __call__ z type) - jeśli jest
  słowo kluczowe metaclass, klasa do niego przypisana jest wołana (jej __call__)"""


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonType):
    pass


if __name__ == '__main__':
    x = SingletonClass()
    y = SingletonClass()

    print(x == y)
