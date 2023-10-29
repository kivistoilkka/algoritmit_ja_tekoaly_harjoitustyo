# Käyttöohje
## Asennusohjeet

1. Kloonaa repositorio
2. Asenna riippuvuudet komennolla `poetry install`
3. Käynnistä sovellus komennolla `poetry run invoke start`

## Ohjelman käyttö graafisella käyttöliittymällä
Ohjelma käynnistyy graafisella käyttöliittymällä komennolla `poetry run invoke start`. Ylempään kenttään kirjoitetaan polku tiedostoon, jota halutaan käsitellä. Alempaan kenttään kirjoitetaan tiedostopolku, johon käsitelty tiedosto halutaan tallentaa. Haluttu pakkausmenetelmä valitaan kolmesta vaihtoehdosta, jonka jälkeen käyttöliittymän alaosan napeilla joko pakkaus (Compress) tai purku (Decompress) -toiminnallisuus.

### Hyväksytyt tiedostomuodot
Ohjelmaa on testattu raakojen tekstitiedostojen häviöttömään pakkaamiseen. Sovelluksen pitäisi olla tässä suhteessa myös merkistöriippumaton, eli sekä ASCII että UTF-8 muotoiset tekstitiedostot toimivat. Myös muita tiedostomuotoja voi pakata, sillä ohjelma käsittelee saamiaan syötteitä tavuina, mutta muilla tiedostomuodoilla ei päästä kovinkaan hyviin pakkausprosentteihin.

## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman suoritus tapahtuu komennolla `poetry run invoke start`, jolloin ohjelma suoritetaan graafisella käyttöliittymällä. Komennolla `poetry run invoke start-cli` ohjelma suoritetaan komentorivillä. Poetry shellin sisällä voi käyttää myös komentoja `python3 src/index.py --ui gui` ja `python3 src/index.py --ui cli`.

### Testaus
Ohjelman kaikki testit ajetaan komennolla `poetry run invoke test`. Pelkät yksikkötestit ajetaan komennolla `poetry run invoke unit-test` ja pelkät integraatiotestit komennolla `poetry run invoke integration-test`.

### Testikattavuus
Ohjelmasta voi luoda HTML-muotoisen testikattavuusraportin komennolla `poetry run invoke coverage-report`. Raportti luodaan _htmlcov_-hakemistoon.

### Suorituskykytestaus
Suorituskykytestit ajetaan komennolla `poetry run invoke performance-test`.

### Pylint
Tiedostossa .pylintrc määritellyt tarkistukset ajetaan komennolla `poetry run invoke lint`.

### Autopep8
Koodin voi automaattiformatoida noudattamaan PEP 8 -tyyliä komennolla `poetry run invoke format`.
