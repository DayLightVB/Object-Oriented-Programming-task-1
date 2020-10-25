from typing import final
# from accessify import protected, private
from ClassPojazd import Pojazd


# sprawdzilem wpływ dodania słowa private przed klasą Pojazd. Otrzymalem blad w projecie, poniewaz
# private - to modyfikator dostempu ktory robie metody dostępne tylko wewnątrz klasy, zakomentowalem to wszystko
# dlatego ze project nie dziala z @private nad classa Pojazd
# @private
# dodalem słowo protected zamiast private z zadania 13 i sprawdzilem ze program nie dziala.
# wyskakuje taki blad 'function() argument 'code' must be code, not str'
# poniewaz protected - pracuje tylko w glownej klasie i w klassach podrzędnych.
# @protected
# kiedy nie ma modyfikatora dostepu to project dziala.
# przypissalem do klas wspólny pakiet, sprawdzilem zachowanie programu w sytuacji gdy klasa Pojazd nie posiada
# informacji o modyfikatorze dostępu. W tej sytuacji program dziala bez bledow


class Kolowe(Pojazd):

    def __init__(self, rozmiarOpony, rokProdukcji, rodzajSilnika, kolor=None, masa=None):
        super().__init__(rokProdukcji, rodzajSilnika, kolor, masa)
        self.rozmiarOpony = rozmiarOpony

    def uruchomSilnik(self):
        print('Uruchomiono silnik:', self.rodzajSilnika)
        # do klasy Kołowe dodalem metodę uruchomSilnik(String rodzajSilnika) która wypisuje rodzaj uruchomionego silnika
        # na podstawie przesłanej wartości do metody


class Cierzarowka(Kolowe):

    def __init__(self, udzwig, rozmiarOpony, rokProdukcji, rodzajSilnika, kolor, masa):
        super().__init__(rozmiarOpony, rokProdukcji, rodzajSilnika, kolor, masa)
        self.udzwig = udzwig

    def podniesSkrzynie(self):
        pass


class Osobowy(Kolowe):

    def __init__(self, iloscOsob, rozmiarOpony, rokProdukcji, rodzajSilnika, kolor, masa):
        super().__init__(rozmiarOpony, rokProdukcji, rodzajSilnika, kolor, masa)
        self.iloscOsob = iloscOsob


class Sedan(Osobowy):
    model = None
    symbol = None
    # do klasy Sedan dodalem pola: model, symbol

    def __init__(self, model, symbol, iloscOsob, rozmiarOpony, rokProdukcji, rodzajSilnika, kolor, masa):
        super().__init__(iloscOsob, rozmiarOpony, rokProdukcji, rodzajSilnika, kolor, masa)
        self.model = model
        self.symbol = symbol


class Skoda(Sedan):
    pass


class superB(Skoda):
    pass


@final
class Octavia(Skoda):
    pass
# dodalem do klasy Octavia słowo final, sprawdzilem co się stanie w sytuacji utworzenia nowej klasy, która dziedziczy
# po klasie Octavia.

# class newOctavia(Octavia):
# kiedy chcę utworzyc nowe classe to wyswitla mi 'Octavia' is marked as '@final' and should not be subclassed
# to oznacza że nie jest możliwe utworzyc subclass od classy Octavia


class VW(Sedan):
    pass


class Golf(VW):
    pass


class PickUp(Osobowy):
    pass


class Szynowe(Pojazd):

    def __init__(self, rokProdukcji, rodzajSilnika, kolor, masa):
        super().__init__(rokProdukcji, rodzajSilnika, kolor, masa)
        pass

    def uruchomSilnik(self):
        print('Uruchomiono silnik pojazdu szynowego')
        # dodano własną metodę uruchomSilnik(), która wyświetlała napis 'Uruchomiono silnik pojazdu szynowego'


class Pociag(Szynowe):
    wlasciciel = 'P.K.P.'
    # w klasie Pociąg dodalem pole statyczne o nazwie właściciel, przechowujące wartość 'P.K.P.'

    def __init__(self, wlasciciel, rokProdukcji, rodzajSilnika, kolor, masa):
        super().__init__(rokProdukcji, rodzajSilnika, kolor, masa)
        self.wlasciciel = wlasciciel


class Gasenicowe(Pojazd):

    def __init__(self, moc, rokProdukcji, rodzajSilnika, kolor, masa):
        super().__init__(rokProdukcji, rodzajSilnika, kolor, masa)
        self.moc = moc

    @final
    def uruchomSilnik(self):
        Pojazd.uruchomSilnik(self)
        print('Jest to pojazd gąsienicowy')
        # dodano własną metodę uruchomSilnik(), wewnątrz której wywolalem metodę z klasy nadrzędnej (Pojazd),
        # następnie wyświetlilem tekst “Jest to pojazd gąsienicowy”


class Czolg(Gasenicowe):
    pass

# def uruchomSilnik(self):
# kiedy dodalem @final do metody uruchomSilnik() w klasie Gasenicowe to kiedy chce utworzyc w klassie Czolg metode
# uruchomSilnik() wypisuje bląd 'MainPy.Gasenicowe.uruchomSilnik' is marked as '@final' and should not be overridden
# to oznacza ze ta metoda nie moze byc pszepisana (переопределенна)


class Spyhacz(Gasenicowe):
    pass


# utworzylem trzy obiekty klasy Golf nadając im wartości początkowe z listy Zadań, dodalem jescie model oraz symbol
GolfA = Golf('Golf', 'S', 4, '195/70 R15', 2019, 'elektryczny', 'biały', '1200kg')
GolfB = Golf('Golf', 'SE', 5, '185/70 R16', 2012, 'benzynowy', 'czerwony', '1500kg')
GolfC = Golf('Golf', 'GTE', 5, '195/80 R17', 2009, 'diesel', 'niebieski', '1800kg')
