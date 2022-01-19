"""Zadanie 1 - Adapter
Korzystając z wzorca Adapter napisz wrapper na listę tak, żeby interfejs dla klienta składał się z metod push, pop
i is_empty.

Stwórz dwie implementacje:
opartą o adapter obiektowy - wykorzystaj składanie obiektów
opartą o adapter klasowy - wykorzystaj wielodziedziczenie do dostosowania interfejsu listy do oczekiwanego interfejsu
stosu.
Stworzone implementacje wykorzystaj do obliczenia wyrażeń podanych w odwrotnej notacji polskiej (ONP):
https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska
'2 7 + 3 / 14 3 - 4 * + 2 /'
'12 2 3 4 * 10 5 / + * +'
'5 1 2 + 4 * + 3 -'"""


# adapter klasowy
class StackInterface:
    def push(self, data):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass


class Stack(StackInterface, list):
    def push(self, data):
        list.append(self, data)

    def pop(self):
        return list.pop(self)

    def is_empty(self):
        return not list.__len__(self)


def main():
    expr = '2 7 + 3 / 14 3 - 4 * + 2 /'
    # expr = '12 2 3 4 * 10 5 / + * +'
    # expr = '5 1 2 + 4 * + 3 -'
    stack = Stack()

    for el in expr.split():
        if el.isnumeric():
            stack.push(float(el))
        else:
            a = stack.pop()
            b = stack.pop()
            if el == '+':
                stack.push(a + b)
            elif el == '-':
                stack.push(b - a)
            elif el == '*':
                stack.push(a * b)
            else:
                stack.push(b / a)

    print(stack.pop())
    print(stack.is_empty())


if __name__ == '__main__':
    main()
