from math import pi


def luas_balok(panjang, lebar, tinggi):
    return 2*(panjang*lebar) + 2*(panjang*tinggi) + 2*(lebar*tinggi)


def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


def volume_kubus(rusuk):
    return rusuk * rusuk * rusuk


def luas_volume(rusuk):
    return 6 * rusuk * rusuk


def luas_bola(radius):
    return 4 * 3.14 * radius**2


def volume_bola(radius):
    return (4/3) * 3.14 * radius**3


def luas_selimut_kerucut(radius, s):
    return 3.14 * radius * s


def luas_permukaan_kerucut(radius, s):
    return 3.14 * radius * s + 3.14 * radius**2


def volume_kerucut(radius, s):
    return 3.14 * radius * s + 3.14 * radius**2


def luas_limas_segiempat(panjang, tinggi):
    ls = 0.5 * panjang * tinggi
    la = panjang**2
    return ls * 5


def volume_limas_segiempat(panjang, tinggi):
    ls = 0.5 * panjang * tinggi
    la = panjang**2
    return (1/3) * la * tinggi


def luas_limas_segitiga(alas, tinggi):
    ls = 0.5 * alas * tinggi
    return ls * 4\



def volume_limas_segitiga(alassegitiga, tinggilimas, tinggisegitiga):
    return (1/6) * alassegitiga * tinggilimas * tinggisegitiga


def volume_prisma_segitiga(alas, tinggi, tinggiprisma):
    return 0.5 * alas * tinggi * tinggiprisma


def luas_prisma_segitiga(a, t, tinggi):
    kel_segitiga = 3 ** a
    return kel_segitiga * tinggi + a * t


def luas_sisi_prisma_segitiga(a, tinggi):
    kel_segitiga = 3**a
    return kel_segitiga * tinggi\



def luas_permukaan_selinder(radius, tinggi):
    return 2 * 3.14 * radius * tinggi + 2 * 3.14 * radius ** 2


def luas_selimut_selinder(radius, tinggi):
    return 2 * 3.14 * radius * tinggi


def volume_selinder(radius, tinggi):
    return 3.14 * radius**2 * tinggi