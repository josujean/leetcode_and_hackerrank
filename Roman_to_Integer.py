class Solution:
    def romanToInt(self, s: str) -> int:
        romdict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        ints = []
        i = 0
        while (i < len(s)):
            if s[i:].startswith(("IV", "IX", "XL", "XC", "CD", "CM")):
                ints.append(romdict[s[i:i+2]])
                i = i+2

            else:
                ints.append(romdict[s[i:i+1]])
                i = i+1
            
        return(sum(ints))
        
