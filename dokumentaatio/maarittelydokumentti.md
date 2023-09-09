# Määrittelydokumentti

- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)
- Ohjelmointikieli: Python
    - Pystyn tarvittaessa lukemaan Javaa, mutta edellisestä kerrasta on muutama vuosi
- Toteutettavat algoritmit:
    - [Huffmanin koodaus](https://fi.wikipedia.org/wiki/Huffmanin_koodaus) [(englanniksi)](https://en.wikipedia.org/wiki/Huffman_coding)
        - Tietorakenteina binääripuu Huffman-puuta varten ja prioriteettijono puun rakentamista varten
    - [Lempel-Ziv 78 (LZ78)](https://en.wikipedia.org/wiki/LZ77_and_LZ78)
        - Tietorakenteina n-ary-puu algoritmin tarvitsemaa sanakirjaa varten
- Dokumentaation kieli: englanti
    - Koodin ja kommenttien kieli on englanti, ellei toisin vaadita

## Valittu ongelma ja perustelut valituille algoritmeille ja tietorakenteille?
Sovellus pakkaa tekstitiedostoja kahdella vaihtoehtoisella häviöttömällä algoritmilla. Huffmanin koodaus vaikuttaa melko yksinkertaiselta, mutta sitä käytetään osana monien nykyäänkin käytettyjä pakkausmenetelmiä. Lempel-Ziv 78 on hieman monimutkaisempi, mutta manuaalisesti testattaessa hyvin mielenkiintoinen ja se pystyy ilmeisesti hieman parempaan pakkaukseen. Se kuuluu LZ-algoritmien perheeseen, jossa on myös muita mielenkiintoisia vaihtoehtoja. LZ78 saattaa vaihtua kun ehdin tutustua hieman enemmän vaihtoehtoihin (esim. LZW-algoritmi vaikuttaa hieman monimutkaisemmalta, mutta ei mahdottomalta). Toisaalta jos Huffmanin koodaus ja Pythonin käyttö tiedostojen pakkaamiseen tuottaa liikaa ongelmia, niin sitten keskityn vain yhteen algoritmiin.

## Syötteet
Sovelluksen avulla voidaan pakata tekstitiedostoja ja purkaa pakattuja tiedostoja takaisin tekstitiedostoiksi. Ensimmäisessä tapauksessa se saa syötteenä tekstitiedoston, jonka se pakkaa käyttäjän valitsemalla algoritmilla ja tallentaa uudeksi tiedostoksi. Jälkimmäisessä se ottaa syötteenä aiemmin pakkaamansa tiedoston, jonka se pakkaa ja tallentaa ihmisen luettavaksi tekstitiedostoksi.

## Aika- ja tilavaativuudet
- Huffmanin koodauksen tuottama pakattu tekstitiedosto on lyhyempi tai korkeintaan yhtä pitkä kuin alkuperäinen koodattava tekstitiedosto. Huffman-puun luominen on aikavaativuudeltaan O(nlogn). BPC (bits per character) -arvo on keskimäärin 5,27.
- LZ78-algoritmin aikavaativuus on O(n), koska jokainen koodattavan tiedoston merkki n luetaan koodauksen aikana kerran. BPC-arvo on keskimäärin 4,26.

## Lähteet
- Huffman D. 1952. A Method for the Construction of Minimum-Redundancy Codes. Proceedings of the IRE. 40 (9): 1098–1101.
- Senthil S & Robert L. 2011. Text Compression Algorithms - A Comparative Study. ICTACT Journal on Communication Technology. 2 (4): 444-451.
- Ziv J & Lempel A. 1978. Compression of Individual Sequences via Variable-Rate Coding. IEEE Transactions on Information Theory. 24 (5): 530–536.
- Wikipedia. Huffman coding. https://en.wikipedia.org/wiki/Huffman_coding. Haettu 9.9.2023
- Wikipedia. Huffmanin koodaus. https://fi.wikipedia.org/wiki/Huffmanin_koodaus. Haettu 9.9.2023
- Wikipedia. LZ77 and LZ78. https://en.wikipedia.org/wiki/LZ77_and_LZ78. Haettu 9.9.2023
