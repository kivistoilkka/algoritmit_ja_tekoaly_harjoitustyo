from collections import Counter
from heapq import heappush, heappop


class HuffmanCoder:
    def __init__(self) -> None:
        pass

    def encode(self, input_string: str) -> str:
        return (input_string, input_string)

    def calculate_frequencies(self, input_string: str) -> dict:
        output = Counter(input_string)
        return output

    def create_huffman_tree(self, symbols_and_weights: dict[str, int]) -> list:
        return list(symbols_and_weights.values())


if __name__ == "__main__":
    # coder = HuffmanCoder()
    # test_string = 'How to code this string with Huffman coding?'
    # print(test_string.encode())
    # result = coder.calculate_frequencies(test_string)
    # print(result)

    # keko = []
    # heappush(keko,5)
    # heappush(keko,3)
    # heappush(keko,8)
    # heappush(keko,7)
    # print(keko[0]) # 3
    # heappop(keko)
    # print(keko[0]) # 5
    # print(type(keko))

    # symbols_and_weights = {
    #     'H': 2,
    #     'o': 4,
    #     'w': 2,
    #     ' ': 7,
    #     't': 4
    # }
    # print(list(symbols_and_weights.values()))
    pass
