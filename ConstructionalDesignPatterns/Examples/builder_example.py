""""Builder
Wzorzec ten oddziela konstrukcję obiektów złożonych do ich reprezentacji, umożliwiając tym samym powstawanie w jednym
 procesie konstrukcyjnym różnych reprezentacji.

Wzorca Budowniczy używamy, gdy:

Algorytm tworzenia obiektu złożonego powinien być niezależny od części składowych tego obiektu i sposobu ich
zestawiania. Proces konstruowania musi uwzględniać różne reprezentacje konstruowanego obiektu.
Konstrukcja
Builder

Uczestnicy:

Builder - abstrakcyjny interfejs do tworzenia docelowych obiektów
ConcreteBuilder - konkretny builder tworzący i łączący składniki tworzonego obiektu
Director - zarządza tworzeniem obiektu
Product - generowany obiekt złożony
Współpraca:

Klient tworzy obiekt Director i konfiguruje go za pomocą pożądanego obiektu ConcreteBuilder
Director informuje ConcreteBuilder o potrzebie zbudowania części produktu
ConcreteBuilder przetwarza żądania od Director i dodaje części do produktu
Klient odbiera produkt od ConcreteBuilder
Konsekwencje:

Umożliwienie zmiany wewnętrznej reprezentacji produktu
Oddzielenie kodu służącego do konstruowania od reprezentacji
Lepsza kontrola procesu konstruowania"""


class Cook:
    '''
    Director - zarządza tworzeniem obiektu
    '''
    def __init__(self):
        self._builder = None

    def prepare(self, builder):
        self._builder = builder
        self._builder.prepare_dough()
        self._builder.add_extras()
        self._builder.bake()


class PizzaBuilder:
    '''
    Builder - abstrakcyjny interfejs do tworzenia docelowych obiektów
    '''
    def __init__(self):
        self.pizza = Pizza()

    def prepare_dough(self): pass

    def add_extras(self): pass

    def bake(self): pass


class MargeritaBuilder(PizzaBuilder):
    '''
    ConcreteBuilder - konkretny builder tworzący i łączący składniki tworzonego obiektu
    '''
    def prepare_dough(self): pass

    def add_extras(self): pass

    def bake(self): pass


class PepperoniBuilder(PizzaBuilder):
    def prepare_dough(self): pass

    def add_extras(self): pass

    def bake(self): pass


class Pizza:
    '''
    generowany obiekt złożony
    '''
    pass


def main():
    cook = Cook()
    # wybieramy buildera
    baking = PepperoniBuilder()
    print(baking)
    cook.prepare(baking)
    pizza = baking.pizza
    print(pizza)


if __name__ == '__main__':
    main()
