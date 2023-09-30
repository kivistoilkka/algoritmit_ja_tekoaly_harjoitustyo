# Viikkoraportti, viikko 4

## Päivittäinen edistyminen
Sunnuntai 24.9. *2h*
- Huffmanin koodauksen algoritmin muuttaminen bittejä ja tavuja käsitteleväksi jatkui
    - branchissa *working-with-bytes*

Maanantai 25.9. *2h*
- Huffmanin koodauksen algoritmin muuttaminen bittejä ja tavuja käsitteleväksi jatkui
    - branchissa *working-with-bytes*
    - Enkoodaus ja dekoodaus toimivat ilman virheilmoituksia, mutta tulokset ovat väärin

Torstai 28.9. *2h*
- Tiedostojen lukemiseen ja luomiseen käytettävän FileIO-luokan luonti

Perjantai 29.9. *3h*
- TextCompressorService-luokan luonti, ensimmäisiä integraatiotestejä
- Komentorivikäyttöliittymän luonti

Lauantai 30.9. *3h*
- Lisää bittikäsittelyn opiskelua
- LZW-pakkauksen toteuttavan LZWCoder-luokan luominen, ensimmäinen iteraatio enkoodauksesta ja dekoodauksesta
- Ensimmäiset Docstring-dokumentaatiot

## Mitä opin?
Opin hieman lisää Pythonin sisäisestä maailmasta Real Pythonin tutoriaalista. Päädyin valitsemaan Lempel-Ziv algoritmiksi Lempel-Ziv-Welchin, koska sen nimi on tullut vastaan GeoTIFF-kuvien kanssa työskennellessä. Tuo LZW oli myös yllättävän helppo toteuttaa.

## Mikä jäi epäselväksi?
Huffmanin koodaus tuottaa niin eripituisia bittijaksoja, mutta koska Python työskentelee mielummin kokonaisten tavujen kanssa, niin näiden bittijaksojen käsittely on edelleen tuottanut vaikeuksia. Törmäsin tällä viikolla jo muutamiin esimerkkeihin, miten luodaan oma bittivirran käsittelijä, joten tällainenkin täytynee toteuttaa jotta enkoodatun datan tallennus onnistuu niin, että tiedosto oikeasti pakkaantuu.

## Mitä teen seuraavaksi?
Kirjoitan testejä LZW-pakkauksen toteuttavalle luokalle ja optimoin sen suoritusta. Kytken LZW-toiminnallisuuden osaksi käyttöliittymää. Jatkan bittien ja tavujen kanssa työskentelyä, LZW-algoritmin kanssa tämä on luultavasti helpompaa kuin Huffmanin koodauksen kanssa.
