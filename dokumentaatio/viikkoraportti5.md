# Viikkoraportti, viikko 5

## Päivittäinen edistyminen
Torstai 5.10. *2h*
- LZW kytketty osaksi käyttöliittymää
- Bittien käyttöön vaihdon kanssa työskentelyä
    - branchissa *working-with-bytes*

Perjantai 6.10. *4h*
- Huffman koodauksen enkoodaus toimimaan bitstring-moduulin avulla
    - branchissa *working-with-bytes*

Lauantai 7.10. *4h*
- Huffmanin koodauksen enkoodaus ja dekoodaus toimimaan biteillä
    - branchissa *working-with-bytes*
- Binääridatan käsittelyyn sopivat metodit FileIO-luokkaan
    - branchissa *working-with-bytes*
- Testien korjailua
    - branchissa *working-with-bytes*

## Mitä opin?
Gitin rebase-toiminnallisuuden kanssa on toimittava varoen, mutta sain siirrettyä working-with-bytes -branchin osoittamaan hieman myöhempään committiin main-branchissa. Tuo käyttöön ottamani bitstring-moduuli on todella erinomainen, monta ongelmaa ratkesi sen avulla. Kaikkien testien korjaaminen tämän uuden bittitoiminnallisuuden mukaisiksi on varsin työlästä, eli näin isot rakenteelliset muutokset eivät ole kovin järkeviä kun lähdetään tekemään sovelluksia kurssien ulkopuolella.

## Mikä jäi epäselväksi?
Täytyy vielä päättää miten hoidan Huffmanin koodauksella pakattujen tiedostojen käsittelyssä sen pienen ongelman, että enkoodattu data ei välttämättä ole jaettavissa tavuiksi. Ratkaisuvaihtoehtoja on ainakin kaksi: joko lisään enkoodausvaiheessa huffmanin puuhun end-of-file -merkin, jonka avulla tiedoston lukeminen voidaan lopettaa ennen täydentämiseen käytettyjä nollia, tai sitten lisään tiedoston alkuun tiedon täydennysbittien lukumäärästä.

## Mitä teen seuraavaksi?
Viimeistelen bittikäsittelyn ja tuon toiminnallisuuden osaksi varsinaista ohjelmaa. Kirjoitan testejä LZW-algoritmeille. Aloitan pakkaustehokkuuden testaamisen.
