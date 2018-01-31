def generateTrueRandom(byteCount) :
    with open("dev/random", 'rb') as f:
            return f.read(byteCount)
