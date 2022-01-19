"""Zadanie 2 - Composite
Zbuduj klasy opisujące strukturę firmy: Oddział (z nazwą) i Pracownik (z nazwą, zarobkami i liczbą dni urlopu) tak,
żeby klient mógł obsługiwać drzewiastą strukturę firmy nie zwracając uwagi na typy poszczególnych węzłów. Zaimplementuj
metody zwracające poprawnie nazwę, zarobki i liczbę dni urlopu bez względu na to, na którym elemencie struktury zostaną
wywołane."""


class Element:
    def get_name(self):
        pass

    def get_salary(self):
        pass

    def get_vacation_days(self):
        pass


class Employee(Element):
    def __init__(self, name, salary, vacation_days):
        self._name = name
        self._salary = salary
        self._vacation_days = vacation_days

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def get_vacation_days(self):
        return self._vacation_days


class Departament(Element):
    def __init__(self, name):
        self._name = name
        self._elements = []

    def get_name(self):
        return self._name

    def get_salary(self):
        salary = 0.0
        for el in self._elements:
            salary += el.get_salary()
        return salary

    def get_vacation_days(self):
        vacation = 0
        for el in self._elements:
            vacation += el.get_vacation_days()
        return vacation

    def add_element(self, element):
        self._elements.append(element)


def main():
    company = Departament('ACME')
    sales = Departament('Sales')
    prod = Departament('Production')
    company.add_element(sales)
    company.add_element(prod)
    company.add_element(Employee('Maria Kowalska', 30000.0, 30))
    company.add_element(Employee('Jan Kowalski', 25000.0, 25))
    sales.add_element(Employee('Joanna Mierzyńska', 20000.0, 20))
    sales.add_element(Employee('Stefan Mierzyński', 15000.0, 15))
    prod.add_element(Employee('Anna Nowak', 10000.0, 10))
    prod.add_element(Employee('Marian Nowak', 5000.0, 5))

    print(f'Dep: {company.get_name()}, salary: {company.get_salary()}, vacation days: {company.get_vacation_days()}')
    print(f'Dep: {sales.get_name()}, salary: {sales.get_salary()}, vacation days: {sales.get_vacation_days()}')
    print(f'Dep: {prod.get_name()}, salary: {prod.get_salary()}, vacation days: {prod.get_vacation_days()}')


if __name__ == '__main__':
    main()
