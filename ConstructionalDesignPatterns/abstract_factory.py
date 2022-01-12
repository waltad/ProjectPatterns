"""Zadanie 3 - Abstract Factory
Napisz program, w którym dwie Abstrakcyjne Fabryki samochodów (z kierownicą po lewej i po prawej stronie) produkują
3 rodzaje aut (sedan, kombi, coupe)."""


class Sedan:
    def who_am_i(self):
        pass


class LHDSedan(Sedan):
    def who_am_i(self):
        pass


class CarFactory:
    def create_sedan(self):
        pass

    def create_station_wagon(self):
        pass

    def create_coupe(self):
        pass


class LHDCarFactory(CarFactory):
    def create_sedan(self):
        pass

    def create_station_wagon(self):
        pass

    def create_coupe(self):
        pass
