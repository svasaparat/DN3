

data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}


def najvecje_vrednosti():

# KLJUČ "PRICES" SHRANIM V NOV LIST POD IMENOM kljuc_prices_lista TER POTEM LAHKO Z FUNKCIJO MAX PRIDOBIM NAJVEČJO VREDNOST LISTA
    kljuc_prices_lista = data["prices"]
    print(max(kljuc_prices_lista))

# PODOBNO KOT PREJ NAREDIM ŠE ZA KLJUČ "volume"
    kljuc_volume_lista = data["volume"]
    print(max(kljuc_volume_lista))


najvecje_vrednosti()
