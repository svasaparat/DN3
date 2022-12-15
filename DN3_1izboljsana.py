import datetime


def izracun_starosti():

    emso = input("VNESITE EMŠO OSEBE ZA KATERO ŽELITE IZVEDETI NJENO STAROST! \n")


# VNESEN EMŠO SPREMENIMO V LIST, DA BOMO LAHKO OPERILALI S POSAMEZNIMI ŠTEVKAMI
    emso = list(emso)

# IZ EMŠE VZAMEMO RELEVANTNO ŠTEVKO PREKO KATERE BOMO UGOTIVILI TISOČLETJE, PRAV TAKO JO IZ STRINGA PRETVORIMO V INTTIGER, DA BOMO Z NJO LAHKO MATEMATIČNO OPERIRALI
    števka_stoletja = int(emso[4])

# DEFINIRAMO ŠE OSTALE ŠTEVKE
    letnica_ena = emso[4]
    letnica_dva = emso[5]
    letnica_tri = emso[6]

# DEFINIRAMO ŠE TRENUTNI DATUM (LETNICO), SAJ JO BOMO KANEJE UPORABILI PRI IZRAČUNU STAROSTI UPORABNIKA
    datum = datetime.datetime.now()


# POGOJ DA JE TIŠOČLETJE 1000 (STR ŠTEVKE ZLEPIMO SKUPAJ IN JIH PRETVORIMO V INT)
    if števka_stoletja <= 9 and števka_stoletja > 0:

        letnica_pre_dva_tisoč = "1" + letnica_ena + letnica_dva + letnica_tri
        letnica_pre_dva_tisoč = int(letnica_pre_dva_tisoč)
        print("STAROST OSEBE, KI JI PRIPADA VNESENA EMŠA = ", datum.year - letnica_pre_dva_tisoč)

#VSE OSTALO JE 2000 LETJE (STR ŠTEVKE ZLEPIMO SKUPAJ IN JIH PRETVORIMO V INT)
    else:

        letnica_post_dva_tisoč = "2" + letnica_ena + letnica_dva + letnica_tri
        letnica_post_dva_tisoč = int(letnica_post_dva_tisoč)
        print("STAROST OSEBE, KI JI PRIPADA VNESENA EMŠA = ", datum.year - letnica_post_dva_tisoč)
    # 3007995500103

izracun_starosti()
