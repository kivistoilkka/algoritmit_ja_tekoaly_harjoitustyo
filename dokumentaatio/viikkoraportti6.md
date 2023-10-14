# Viikkoraportti, viikko 6

## Päivittäinen edistyminen
Maanantai 9.10. *4h*
- Testien korjaamista bittikäsittelyssä
    - branchissa *working-with-bytes*
- Huffmanin koodauksella tuotettujen tiedostojen käsittely (täyttöbittien huomiointi)
    - branchissa *working-with-bytes*

Torstai 12.10. *5h*
- LZW toimimaan biteillä
    - branchissa *working-with-bytes*
- Bittitoiminnallisuuden tuominen main-branchiin ja osaksi varsinaisen sovelluksen toiminnallisuutta
- Lisää testejä LZWCoderille ja TextCompressorServicelle
- Lisää integraatiotestejä

Perjantai 13.10 *2h*
- Testien kirjoittamista
- LZWCoderille sanakirjan välityhjennys suurien tiedostojen pakkauksessa
- Koodin refaktorointia

Lauantai 14.10. *5h*
- UTF-8 tuki LZWCoderille (käsittelee vain tavuja, ei ota kantaa tekstin merkistökoodaukseen)
- Koodin refaktorointia
- Eri testimuotojen ajamiselle omat Invoke-komennot
- Suorituskykytestien luominen

## Mitä opin?
Merkistökoodaukset ovat varsin sotkuinen aihealue. UTF-8 on nerokas merkistökoodaustapa, mutta koska merkit ovat vaihtelevan pituisia, niin niiden käsittely kokonaisina merkkeinä vaatii hieman tavujen ja bittien tarkempaa lukemista.

## Mikä jäi epäselväksi?
Työ alkaa olla aika mukavasti kasassa. Ensi viikolla ehdin vielä selvitellä miksi Huffman ei pakkaa kaikkia tiedostoja häviöttömästi. ASCII-merkkejä sisältävät tiedostot toimivat, mutta sellaisia suuria tiedostoja, jotka ovat ASCII-enkoodattuja ja vapaalla lisenssillä jaettavissa, en vielä löytänyt, joten en voinut sisällyttää niitä käsitteleviä testejä vielä projektiini.

## Mitä teen seuraavaksi?
- Virheiden käsittely tiedostokäsittelyssä (FileIO)
- Tarkastelen olisiko Huffmanin koodaus mahdollista saada häviöttömäksi myös UTF-8:n kanssa
- Lisää testejä (erittäin suuret tiedostot, erittäin pienet tiedostot)
- Peräkkäinen pakkaus molempia pakkausalgoritmeja hyödyntäen (jos sattuu helposti toimimaan)
- Mahdollisesti yksinkertainen GUI tkinterillä
