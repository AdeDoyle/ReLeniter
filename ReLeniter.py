"""Takes Irish text and replaces lenition shown by means of a letter "h" following a lenitable character with lenition
   shown by a punctum delens"""

lenitables = ["b", "c", "d", "f", "g", "m", "p", "s", "t", "B", "C", "D", "F", "G", "M", "P", "S", "T"]
leniteDict = {"b":"ḃ", "c":"ċ", "d":"ḋ", "f":"ḟ", "g":"ġ", "m":"ṁ", "p":"ṗ", "s":"ṡ", "t":"ṫ",
              "B":"Ḃ", "C":"Ċ", "D":"Ḋ", "F":"Ḟ", "G":"Ġ", "M":"Ṁ", "P":"Ṗ", "S":"Ṡ", "T":"Ṫ"}

"""finds h-lenition in string and replaces it with punctum-delens-lenition. returns result"""
def relenite(string):
    hrep = "REPLACEMELATER"
    for letter in string:
        if letter == "h" or letter == "H":
            """retains "h" where it appears as the first character in the string"""
            if string.index(letter) == 0:
                if letter == "h":
                    letonerep = (hrep + "1")
                elif letter == "H":
                    letonerep = (hrep + "2")
                string = (letonerep + string[1:])
                """replaces lenitable consonant and "h" with equivalent punctum-delens-lenition"""
            elif string.index(letter) > 0:
                place = string.index(letter)
                lenCheck = place - 1
                letCheck = (string[lenCheck])
                if letCheck in lenitables:
                    letReplace = leniteDict.get(letCheck)
                    string = (string[:lenCheck] + letReplace + string[place + 1:])
                    """retains "h" where it appears following a non-lenitable character"""
                else:
                    if letter == "h":
                        letanotherrep = (hrep + "1")
                    elif letter == "H":
                        letanotherrep = (hrep + "2")
                    letReplace = letanotherrep
                    string = (string[:place] + letReplace + string[place + 1:])
    """replaces all "REPLACEMELATER" markers left from earlier steps with the original "h" which was removed"""
    if hrep in string:
        h1 = "REPLACEMELATER1"
        h2 = "REPLACEMELATER2"
        if h1 in string:
            string = string.replace(h1, "h")
        if h2 in string:
            string = string.replace(h2, "H")
    return string


input_string = input("Paste Text Here: ")
print(relenite(input_string))
