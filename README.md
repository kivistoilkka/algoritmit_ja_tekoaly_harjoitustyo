# Text Compressor

![GHA workflow badge](https://github.com/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo/graph/badge.svg?token=YMC46OV14B)](https://codecov.io/gh/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo)

Sovellus tekstitiedostojen pakkaamiseen käyttäen Huffman- ja LZW-pakkausalgoritmeja.

Tällä hetkellä sovelluksella voi käyttöliittymän kautta koodata ASCII (ISO8859-1) muotoisia tekstitiedostoja Huffmanin koodauksella uuteen tiedostoon ja purkaa tuollaiseen tiedostoon tallennetun tekstin takaisin luettavaan muotoon. Sovellus ei siis vielä tiivistä tietoa.

## Dokumentaatio
- [Määrittelydokumentti](dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)

## Viikkoraportit
- [Viikko 1](dokumentaatio/viikkoraportti1.md)
- [Viikko 2](dokumentaatio/viikkoraportti2.md)
- [Viikko 3](dokumentaatio/viikkoraportti3.md)
- [Viikko 4](dokumentaatio/viikkoraportti4.md)
- [Viikko 5](dokumentaatio/viikkoraportti5.md)

## Asennusohjeet

1. Kloonaa repositorio
2. Asenna riippuvuudet komennolla `poetry install`
3. Käynnistä sovellus komennolla `poetry run invoke start`

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman suoritus tapahtuu komennolla `poetry run invoke start`.

### Testaus
Ohjelman testit ajetaan komennolla `poetry run invoke test`.

### Testikattavuus
Ohjelmasta voi luoda HTML-muotoisen testikattavuusraportin komennolla `poetry run invoke coverage-report`. Raportti luodaan _htmlcov_-hakemistoon.

### Pylint
Tiedostossa .pylintrc määritellyt tarkistukset ajetaan komennolla `poetry run invoke lint`.

### Autopep8
Koodin voi automaattiformatoida noudattamaan PEP 8 -tyyliä komennolla `poetry run invoke format`.
