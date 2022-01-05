class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def __init__(self):
        if not self.__instance:
            print("Wspólna instancja nie została jeszcze stworzona - nie jestem Sigletonem!")
        self.val = 0

    def function(self):
        print(self.val)


if __name__ == '__main__':
    a = Singleton.get_instance()
    a.function()
    a.val = 10
    a.function()


    b = Singleton.get_instance()
    b.function()