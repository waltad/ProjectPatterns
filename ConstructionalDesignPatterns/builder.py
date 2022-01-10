""""Zadanie 2 - Builder
Napisz program, który dane odczytane z pliku tekstowego, znak po znaku, przekształci przy pomocy Budowniczych do postaci:
wartości heksadecymalnych
wielkich znaków
małych znaków
licznika znaków"""


class Builder:
    def build_part(self, element):
        pass

    def get_result(self):
        pass


class HexBuilder(Builder):
    def __init__(self):
        pass

    def build_part(self, element):
        pass

    def get_result(self):
        pass


class Director:
    def __init__(self, file_name):
        pass

    def construct(self):
        pass

    def set_builder(self, builder):
        pass

    def get_result(self):
        pass
