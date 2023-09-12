from collections import Counter

class HuffmanCoder:
    def __init__(self) -> None:
        pass

    def encode(self, input_string: str) -> str:
        return input_string

    def calculate_frequencies(self, input_string: str) -> dict:
        output = Counter(input_string)
        for symbol in output:
            output[symbol] = output[symbol]/len(input_string)
        return output

if __name__ == "__main__":
    coder = HuffmanCoder()
    result = coder.calculate_frequencies('How to code this string with Huffman coding?')
    print(result)
