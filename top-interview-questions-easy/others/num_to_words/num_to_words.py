one = [ "", "One ", "Two ", "Three ", "Four ",
		"Five ", "Six ", "Seven ", "Eight ",
		"Nine ", "Ten ", "Eleven ", "Twelve ",
		"Thirteen ", "Fourteen ", "Fifteen ",
		"Sixteen ", "Seventeen ", "Eighteen ",
		"Nineteen "]

ten = [ "", "", "Twenty ", "Thirty ", "Forty ",
		"Fifty ", "Sixty ", "Seventy ", "Eighty ",
		"Ninety "]


def numToWords(n, s):

    str = ""

    if n == 100:
        str += "One Hundred "
        return str
    if n > 100:
        str += one[(n // 100) % 10]
        str += "Hundred "
        n = n % 100


    if (n > 19):
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]
    if (n):
        str += s

    return str


def convertToWordsInIndian(n):

    out = ""

    out += numToWords((n // 100000000000), "Kharab ")
    out += numToWords(((n // 1000000000) % 100), "Arab ")
    out += numToWords(((n // 10000000) % 100), "Crore ")
    out += numToWords(((n // 100000) % 100), "Lakh ")
    out += numToWords(((n // 1000) % 100), "Thousand ")
    out += numToWords(((n // 100) % 10), "Hundred ")
    out += numToWords((n % 100), "")

    return out

def convertToWordsInInternational(n):
    
    out = ""

    out += numToWords((n // 1000000000000), "Trillion ")
    out += numToWords(((n // 1000000000) % 1000), "Billion ")
    out += numToWords(((n // 1000000) % 1000), "Million ")
    out += numToWords(((n // 1000) % 1000), "Thousand ")
    out += numToWords(((n // 100) % 10), "Hundred ")
    out += numToWords((n % 100), "")

    return out

n = 4000000000000


print(convertToWordsInIndian(n))
print(convertToWordsInInternational(n))