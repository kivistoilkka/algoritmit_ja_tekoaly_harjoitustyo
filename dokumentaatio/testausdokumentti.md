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

TextCompressorService-luokalle on kirjoitettu integraatiotestejä, jotka hyödyntävät oikeita tiedostokäsittelyyn ja tekstidatan koodaukseen käytettäviä luokkia. Integraatiotesteissä pakataan ja puretaan kansiosta *src/tests/text_files* löytyviä eri tavoin merkistökoodattuja tekstitiedostoja. Testauksessa käytetään myös suurikokoisia tiedostoja.

# Suorituskykytestaus
Suorituskykytestit voi ajaa komennolla `poetry run invoke performance-test`.

Suorituskykytestissä pakataan ja puretaan suuria tekstitiedostoja eri pakkausmenetelmillä. Pakkauksen yhteydessä lasketaan pakkaamiseen kulunut aika ja pakkausprosentti. Purkamisen yhteydessä lasketaan purkamiseen kulunut aika ja verrataan puretun tiedoston kokoa alkuperäiseen tiedostoon. Testissä käytetään seuraavia tekstitiedostoja:
- [pg84_frankenstein_UTF8.txt](../src/tests/text_files/pg84_frankenstein_UTF8.txt), 449.0 kB, [Project Gutenberg](https://www.gutenberg.org/ebooks/84)
- [pg11_alice_UTF8.txt](../src/tests/text_files/pg11_alice_UTF8.txt), 174.4 kB, [Project Gutenberg](https://www.gutenberg.org/ebooks/11)
- [pg1342_pride_and_prejudice.txt](../src/tests/text_files/pg1342_pride_and_prejudice.txt), 772.4 kB, [Project Gutenberg](https://www.gutenberg.org/ebooks/1342)

Suorituskykytestien tuloksista voi lukea lisää [toteutusdokumentista](toteutusdokumentti.md).
