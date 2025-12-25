class DecimalToRoman:
    def convert(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

class RomanToDecimal:
    def convert(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]
        return res

d2r = DecimalToRoman()
r2d = RomanToDecimal()

print("--- Перетворення: Десяткове число -> Римське")

print(f"Число 14 -> {d2r.convert(14)}")
print(f"Число 19 -> {d2r.convert(19)}")

print("\n--- Перетворення: Римське -> Десяткове число")

print(f"Римське XIV -> {r2d.convert('XIV')}")
print(f"Римське XIX -> {r2d.convert('XIX')}")