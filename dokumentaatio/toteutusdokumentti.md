# Toteutusdokumentti

## Ohjelman yleisrakenne
Ohjelman ytimen muodostaa TextCompressionService-luokka, joka tarjoaa käyttöliittymäluokille metodit tiedostojen pakkaamiseen ja pakkauksen purkamiseen. Tiedostojen lukemisesta ja kirjoittamisesta vastaa FileIO-luokka. Varsinaisesta pakkauksesta vastaa kaksi luokkaa: HuffmanCoder ja LZWCoder.

## Lähteet
Työn toteutuksessa ei ole käytetty ChatGPT:tä tai muita vastaavia tekoälyjä.

Käytetyt lähteet ja esimerkit:
- Bittikäsittely: (https://realpython.com/python-bitwise-operators/)
- Huffmanin koodaus:
    - Teoria: https://fi.wikipedia.org/wiki/Huffmanin_koodaus
    - Teoria: https://en.wikipedia.org/wiki/Huffman_coding
    - Keon teoria: Laaksonen, A. 2022. Tietorakenteet ja algoritmit. Helsingin yliopisto. ISBN 978-951-51-8804-5
    - Huffmanin puun pakkaus: https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree
    - Esimerkki: https://www.rosettacode.org/wiki/Huffman_coding#Alternative_2
    - Esimerkki, enkoodaus: https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
    - Esimerkki, dekoodaus: https://www.geeksforgeeks.org/huffman-decoding/?ref=lbp
- LZW:
    - Teoria: https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
    - Esimerkki: https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
    - Esimerkki: https://www.rosettacode.org/wiki/LZW_compression#Python
