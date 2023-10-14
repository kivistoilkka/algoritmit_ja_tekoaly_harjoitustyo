# Testausdokumentti

## Kattavuusraportti
Ohjelman yksikkötestien kattavuusraportin saa luotua komennolla `poetry run invoke coverage-report`, minkä lisäksi testikattavuutta voi tarkastella [Codecovin](https://app.codecov.io/gh/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo) kautta.

![Codecov icicle graph](https://codecov.io/gh/kivistoilkka/algoritmit_ja_tekoaly_harjoitustyo/graphs/icicle.svg?token=YMC46OV14B)

## Testatut asiat
Ohjelman toimintaa on testattu Pythonin unittest-sovelluskehyksen avulla. Kaikki testit voi ajaa komennolla `poetry run invoke test`.

# Yksikkötestaus
Pelkät yksikkötestit voi ajaa komennolla `poetry run invoke unit-test`.

HuffmanCoder-luokkaa on kehitetty testivetoisesti ja sille on kirjoitettu yksikkötestejä. Osa yksikkötesteistä testaa useamman metodin yhteistoimintaa ja sitä, miten luokka suoriutuu tekstipätkän pakkaamisesta ja pakkaamisen purkamisesta. LZWCoder-luokalle on kirjoitettu luokan perustoiminnallisuutta testaavat yksikkötestit.

TextCompressorService-luokkaa on myös kehitetty testivetoisesti ja sitä on testattu Mock-luokkia hyödyntämällä.

# Integraatiotestaus
Pelkät integraatiotestit voi ajaa komennolla `poetry run invoke integration-test`.

TextCompressorService-luokalle on kirjoitettu integraatiotestejä, jotka hyödyntävät oikeita tiedostokäsittelyyn ja tekstidatan koodaukseen käytettäviä luokkia. Integraatiotesteissä pakataan ja puretaan kansiosta *src/tests/text_files* löytyviä eri tavoin merkistökoodattuja tekstitiedostoja. Testauksessa käytetään myös suurikokoisia tiedostoja (pg84_frankenstein_UTF8.txt, 449.0 kB)
