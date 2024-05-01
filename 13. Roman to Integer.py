class Solution:
    def romanToInt(self, s: str) -> int:
        integer_roman = 0
        roman_symbol = ["I", "V", "X", "L", "C", "D", "M"]
        roman_to_integer = [1,5,10,50,100,500,1000]

        firstStrSymbolIndex = 0
        secondStrSymbolIndex = 0
        while(len(s)>0):
            firstStrSymbolIndex = roman_symbol.index(s[0])
            if((firstStrSymbolIndex ==0 or firstStrSymbolIndex == 2 or firstStrSymbolIndex == 4) and len(s) > 1):
                secondStrSymbolIndex = roman_symbol.index(s[1])
                if(secondStrSymbolIndex == firstStrSymbolIndex + 1 or secondStrSymbolIndex == firstStrSymbolIndex + 2):
                    integer_roman += roman_to_integer[secondStrSymbolIndex] - roman_to_integer[firstStrSymbolIndex]
                    s= s[2:]
                    continue
            integer_roman+=roman_to_integer[firstStrSymbolIndex]
            if(len(s) > 1):
                s=s[1:]
            else:
                s = ""
        return integer_roman
