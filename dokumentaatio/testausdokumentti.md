# Testausdokumentti

## Kattavuusraportti
Ohjelman yksikkötestien kattavuusraportin saa luotua komennolla `poetry run invoke coverage-report`, minkä lisäksi testikattavuutta voi tarkastella [Codecovin](https://app.codecov.io/gh/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo) kautta.

![Codecov icicle graph](https://codecov.io/gh/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo/graphs/icicle.svg?token=YMC46OV14B)

## Testatut asiat
Ohjelman toimintaa on testattu Pythonin unittest-sovelluskehyksen avulla. Testit voi ajaa komennolla `poetry run invoke test`.

HuffmanCoder-luokkaa on kehitetty testivetoisesti ja sille on kirjoitettu yksikkötestejä. Osa yksikkötesteistä testaa useamman metodin yhteistoimintaa ja sitä, miten luokka suoriutuu tekstipätkän pakkaamisesta ja pakkaamisen purkamisesta.
