DICTIONARY_LENGTH = 128

class LZWCoder:
    def __init__(self) -> None:
        pass

    def encode(self, data: str) -> list:
        dictionary = {chr(i): i for i in range(DICTIONARY_LENGTH)}
        output = []
        p = ''
        c = ''
        code = DICTIONARY_LENGTH
        p += data[0]
        for i in range(len(data)):
            if i != len(data)-1:
                c += data[i+1]
            if p+c in dictionary:
                p = p+c
            else:
                output.append(dictionary[p])
                dictionary[p+c] = code
                code += 1
                p = c
            c = ''
        if p:
            output.append(dictionary[p])
        return output

    def decode(self, encoded: list) -> str:
        dictionary = {i: chr(i) for i in range(DICTIONARY_LENGTH)}
        output = ''
        old = encoded[0]
        output += dictionary[old]
        code = DICTIONARY_LENGTH
        s = ''
        c = ''
        for i in range(len(encoded)-1):
            new = encoded[i+1]
            if new in dictionary:
                s = dictionary[new]
            else:
                s = dictionary[old]
                s = s+c
            output += s
            c = s[0]
            dictionary[code] = dictionary[old]+c
            code += 1
            old = new
        return output


if __name__ == "__main__":
    coder = LZWCoder()
    print()
    encoded = coder.encode('Testing this test thing here')
    print(encoded)
    print()
    decoded = coder.decode(encoded)
    print(decoded)
