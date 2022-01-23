"""Zadanie 3 - Decorator
Do poprzedniefo programu (Composite) doimplementuj Dekoratora, który upewni się, że nazwy rozpoczynają się od wielkich
liter."""
import functools
import string


def capitalize(fn):
    @functools.wraps(fn)
    def capitalizer(*args):
        return string.capwords(fn(*args))
    return capitalizer


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

    @capitalize
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

    @capitalize
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
    company = Departament('aCME')
    sales = Departament('sales')
    prod = Departament('production')
    company.add_element(sales)
    company.add_element(prod)
    company.add_element(Employee('maria kowalska', 30000.0, 30))
    company.add_element(Employee('jan kowalski', 25000.0, 25))
    sales.add_element(Employee('joanna mierzyńska', 20000.0, 20))
    sales.add_element(Employee('stefan mierzyński', 15000.0, 15))
    prod.add_element(Employee('anna nowak', 10000.0, 10))
    prod.add_element(Employee('marian nowak', 5000.0, 5))
    emp = Employee('marek markotny', 50000.0, 50)

    print(f'Dep: {company.get_name()}, salary: {company.get_salary()}, vacation days: {company.get_vacation_days()}')
    print(f'Dep: {sales.get_name()}, salary: {sales.get_salary()}, vacation days: {sales.get_vacation_days()}')
    print(f'Dep: {prod.get_name()}, salary: {prod.get_salary()}, vacation days: {prod.get_vacation_days()}')
    print(f'Emp: {emp.get_name()}, salary: {emp.get_salary()}, vacation days: {emp.get_vacation_days()}')


if __name__ == '__main__':
    main()
