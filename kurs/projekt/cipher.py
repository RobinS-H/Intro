while True:
    text = input("Text: ")
    bokstäver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
    text_delad = list(text)
    a = 0
    for x in text:
        b = 0
        for y in bokstäver:
            if x == y and x != "ö":
                text_delad[a] = bokstäver[b + 1]
            elif x == "ö":
                text_delad[a] = bokstäver[0]
            b += 1
        a += 1
    print("".join(text_delad))