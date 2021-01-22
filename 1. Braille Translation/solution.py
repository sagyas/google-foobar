def solution(str):
    dic = init_dic()
    result = ""
    for char in str:
        key = char
        if char.isupper():
            key = char.lower()
            result += dic["upper"]
        result += dic[key]
    return result

def init_dic():
    sample = "The quick brown fox jumps over the lazy dog"
    translation = ("00000101111011001010001000000011111010100101010010010010100"
                    "0000000110000111010101010010111101110000000110100101010101101000000010110101"
                    "0011011001111000111000000001010101110011000101110100000000111101100101000100"
                    "00000111000100000101011101111000000100110101010110110")
    dic = {
    	"upper": "000001",
    }
    wordSize = 6
    i = wordSize
    for char in sample:
    	key = char
    	if char.isupper():
    		key = char.lower()
    	dic[key] = translation[i : i + wordSize]
    	i += wordSize
    return dic

# Test
code = "The quick brown fox jumps over the lazy dog"
brailleTranslation = ("00000101111011001010001000000011111010100101010010010010100"
                        "0000000110000111010101010010111101110000000110100101010101101000000010110101"
                        "0011011001111000111000000001010101110011000101110100000000111101100101000100"
                        "00000111000100000101011101111000000100110101010110110")
print(solution(code) == brailleTranslation)