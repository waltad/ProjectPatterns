"""Zadanie 1 - Command
Napisz program symulujący robota przemieszczającego się po płaszczyźnie. Poleceniami będą przesunięcia o zadaną
odległość w kierunkach: dół, góra, lewo i prawo.
Uzupełnij program o funkcjonalność undo/redo.
Uzupełnij program o interakcję z użytkownikiem, który będzie podawał polecenia do wykonania."""


class Robot:
    def __init__(self):
        pass


class Command:
    def execute(self, robot):
        pass

    def undo(self, robot):
        pass


class MoveUp(Command):
    def __init__(self, steps):
        pass

    def execute(self, robot):
        pass

    def undo(self, robot):
        pass


class Commander:
    def __init__(self, robot):
        pass

    def execute(self, cmd):
        pass

    def undo(self):
        pass

    def redo(self):
        pass
