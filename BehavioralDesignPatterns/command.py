"""Zadanie 1 - Command
Napisz program symulujący robota przemieszczającego się po płaszczyźnie. Poleceniami będą przesunięcia o zadaną
odległość w kierunkach: dół, góra, lewo i prawo.
Uzupełnij program o funkcjonalność undo/redo.
Uzupełnij program o interakcję z użytkownikiem, który będzie podawał polecenia do wykonania."""


class Robot:
    def __init__(self):
        self.pos_x = 0.0
        self.pos_y = 0.0

    def __str__(self):
        return f"({self.pos_x}, {self.pos_y})"


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
            cmd = self._redo_stack.pop()
            cmd.execute(self._robot)
            self._undo_stack(cmd)


def main():
    robot = Robot()
    commander = Commander(robot)

    while True:
        command = input("Podaj polecenie (U,D,R,L) i odległość lub wycofanie (u) / ponowne wykoanie (r): ")
        if command[0] in 'UDRL':
            cmd_robot, steps = command.split()
            steps = float(steps)
            if cmd_robot == 'U':
                cmd = MoveUp(steps)
            elif cmd_robot == 'D':
                cmd = MoveDown(steps)
            elif cmd_robot == 'R':
                cmd = MoveRight(steps)
            else:
                cmd = MoveLeft(steps)
            commander.execute(cmd)
        elif command[0] == 'u':
            commander.undo()
        elif command[0] == 'r':
            commander.redo()
        else:
            break

        print(robot)


if __name__ == '__main__':
    main()

