class Pojazd:

    def __init__(self, rokProdukcji, rodzajSilnika, kolor, masa):
        self.rokProdukcji = rokProdukcji
        self.rodzajSilnika = rodzajSilnika
        self.kolor = kolor
        self.masa = masa

    def uruchomSilnik(self):
        # dodano kod wyświetlający napis “Silnik uruchomiono” + 'model' oraz wszystkie pola
        print('Silnik uruchomiony, model:', self.rokProdukcji, self.rodzajSilnika, self.kolor, self.masa, sep=', ')