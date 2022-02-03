"""Zadanie 1 - Command
Napisz program symulujący robota przemieszczającego się po płaszczyźnie. Poleceniami będą przesunięcia o zadaną
odległość w kierunkach: dół, góra, lewo i prawo.
Uzupełnij program o funkcjonalność undo/redo.
Uzupełnij program o interakcję z użytkownikiem, który będzie podawał polecenia do wykonania."""


class Robot:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return f"({self.pos.x}, {self.pos_y})"


class Command:
    def execute(self, robot):
        pass

    def undo(self, robot):
        pass


class MoveUp(Command):
    def __init__(self, steps):
        self.steps = steps

    def execute(self, robot):
        robot.pos_y += self.steps

    def undo(self, robot):
        robot.pos_y -= self.steps


class MoveDown(Command):
    def __init__(self, steps):
        self.steps = steps

    def execute(self, robot):
        robot.pos_y -= self.steps

    def undo(self, robot):
        robot.pos_y += self.steps


class MoveRight(Command):
    def __init__(self, steps):
        self.steps = steps

    def execute(self, robot):
        robot.pos_x += self.steps

    def undo(self, robot):
        robot.pos_x -= self.steps


class MoveLeft(Command):
    def __init__(self, steps):
        self.steps = steps

    def execute(self, robot):
        robot.pos_x -= self.steps

    def undo(self, robot):
        robot.pos_x += self.steps


class Commander:
    def __init__(self, robot):
        self._robot = robot
        self._undo_stack = []
        self._redo_stack = []

    def execute(self, cmd):
        cmd.execute(self._robot)
        self._undo_stack.append(cmd)
        self._redo_stack.clear()

    def undo(self):
        if self._undo_stack:
            cmd = self._undo_stack.pop()
            cmd.undo(self._robot)
            self._redo_stack.append(cmd)

    def redo(self):
        if self._redo_stack:
            cmd = self._redo_stack
            cmd.execute(self._robot)
            self._undo_stack(cmd)
