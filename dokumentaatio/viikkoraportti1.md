# Viikkoraportti, viikko 1

## Päivittäinen edistyminen
Perjantai 8.9. *3h*
- Aiheideoihin tutustumista
- Tarkempaa tutustumista pakkausalgoritmeihin
- Pythonin binääridatan käsittelykykyihin tutustumista
- Huffmanin koodaukseen ja Lempel-Ziv-algoritmeihin tutustumista ja kokeilemista paperilla

Lauantai 9.9. *3h*
- Projektirungon luominen ja vieminen GitHubiin
- Määrittelydokumentin kirjoittaminen

## Mitä opin?
Pakkausalgoritmit itsessään olivat täysin uusi aihepiiri. Run-length Encoding oli sellainen intuitiivinen pakkausmenetelmä, jonka olisin voinut jollain tavalla kuvailla ennen aihepiiriin tutustumista. Päädyin valitsemaan kurssin aiheideoissa mainitun Huffman vs. Lempel Ziv -vertailun, koska näitä oli melko helppo testata paperilla ja harjoitustyöhön tulee jo lähtökohtaisesti lisää vaikeutta sillä, että lähden tekemään bittioperaatioita Pythonilla. Onnistuin jonkin aikaa väännettyäni lukemaan tekstitiedostoja binääriluvuiksi Pythonin sisällä, eli luultavasti binäärilukujen tallentaminen tiedostoksi onnistuu lopulta. Pienen kokeilun ja sekalaisten hakutulosten lukemisen jälkeen selvitin myös, että tekstitiedostot ovat hyvin pelkistettyjä, eli niissä ei taida olla mitään otsakkeita tai muita tietoja varsinaisen merkkidatan lisäksi.

## Mikä jäi epäselväksi?
Kurssin laajuus on hieman häilyvästi määritelty, mutta valitsin työn aiheeksi sellaisen asian, minkä on mainittu kurssin ohjeistuksessa olevan ainakin riittävän. Pakkausalgoritmeihin liittyi paljon sellaista terminologiaa, jota ei ole tullut aiemmin opinnoissa vastaan, kuten entropiakoodaus (ja siihen liittyvä informaatioteorian määritelmä entropialle). Myös Pythonin bittimanipulaatiot ja muu binäärilukujen kanssa työskentely on hakusessa ja siihen etsin vielä hyviä materiaaleja ja tutoriaaleja. Bittimanipulaatioita käsiteltiin kyllä Tietokoneen toiminnassa, mutta siellä käytettiin leikkiohjelmointikieltä varsinaisen ohjelmointikielen sijaan, joten syntaksin yms. opiskeluun tulee menemään hetki.

## Mitä teen seuraavaksi?
- Kirjoitan alustavan version Huffmanin koodausta hyödyntävästä algoritmista testeineen
    - Aluksi ohjelma voisi ottaa syötteen, koodata datan, tulostaa koodatun datan, dekoodata datan ja tulostaa dekoodatun datan
    - Koodatun datan tallentaminen tiedostoon lisätään myöhemmin, ensin täytyy päättää käytetäänkö tiivistetyn datan tallennukseen tekstitiedostoa vai yritänkö tehdä binääritiedoston
- Jos aika riittää, niin lisään tekstitiedostojen lukemisen ja kirjoittamisen
