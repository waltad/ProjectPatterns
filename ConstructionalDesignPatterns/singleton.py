""""Zadanie 1 - Singleton
Używając wzorca Singleton stwórz prostą klasę loggera, zapisującą do pliku łańcuchy znakowe oraz datę i godzinę.
 Wykorzystaj zagnieżdżoną klasę gromadzącą funkcjonalność instancji oraz przeciążenie metody new."""
import datetime
import time


class Logger:
    class __Singleton:
        def __init__(self, file_name):
            self.file_name = file_name

        def log(self, log_msg):
            with open(self.file_name, 'a') as file:
                file.write(f'{datetime.datetime.now()}: {log_msg}\n')

    __instance = None

    def __new__(cls, file_name):
        if not Logger.__instance:
            Logger.__instance = Logger.__Singleton(file_name)
        return Logger.__instance


def main():
    logger = Logger('test.log')
    logger.log('message 1')
    time.sleep(1)
    logger.log('message 2')
    time.sleep(1.5)
    logger.log('message 3')


if __name__ == '__main__':
    main()
