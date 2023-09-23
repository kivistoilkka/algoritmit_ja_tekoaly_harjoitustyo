# Viikkoraportti, viikko 3

## Päivittäinen edistyminen
Tiistai 19.9. *2h*
- Huffmanin puun ja koodin luonnin debuggausta
    - Miten käsitellä kahta tai useampaa samalla frekvenssillä lisättävää kirjainta, vaikuttaa puun rakenteeseen ja siitä luotavaan koodiin

Keskiviikko 20.9. *2h*
- Huffmanin koodaus: enkoodaus ja dekoodaus toimiviksi

Lauantai 23.9. *2h*
- GitHub Actions ja Codecov käyttöön
- Testausraportin kirjoitus
- Tutustumista Unicode-standardiin
- Huffmanin koodauksen algoritmin muuttaminen bittejä ja tavuja käsitteleväksi aloitettu
    - Työstetään branchissa working-with-bytes, koska muutokset tulevat hajottamaan testit

## Mitä opin?
Debuggauksen tuloksena en onnistunut keksimään miten keko on tarkalleen toteutettu Pythonissa. Erityisesti miten se käsittelee samanarvoisia solmuja ja miten solmujen poisto on toteutettu. Lopulta totesin, että vaikka en voikaan tarkalleen ennustaa millaisia koodaustauluja algoritmi tuottaa, niin voin ainakin päätellä kunkin symbolin koodaukseen käytetyn bittijonon pituudet. Näin sain kirjoitettua jonkinlaisen testin ja jatkettua enkoodaamisen ja dekoodaamisen toteuttamiseen, jolloin totesin algoritmin toimivan ainakin lyhyillä syötteillä.

Tutustuin myös alustavasti Unicode-standardiin. ASCII-muotoisen tekstin käsittely olisi helpointa, koska kutakin merkkiä vastaa yksi tavu. Toisaalta koska Unicode-standardin mukaisissa koodauksissa kutakin symbolia vastaavat "codepointit" koostuvat yhdestä tai useammasta kokonaisesta tavusta, niin tavujen käyttäminen Huffmanin koodauksessa olisi todennäköisesti mahdollista. Tällöin ohjelmaa monimutkaistaisi se, että pakattuun tiedostoon pitäisi tallentaa myös alkuperäisessä tekstissä käytetty merkistö.

## Mikä jäi epäselväksi?
Ei varsinaisia epäselvyyksiä, projekti etenee.

## Mitä teen seuraavaksi?
Seuraavaksi yritän saada bittikäsittelyn toimimaan. Lisäksi tiedostojen luku ja tallennus olisi hyvä saada valmiiksi, kuten myös jonkinlainen käyttöliittymä vertaisarviointia varten.
