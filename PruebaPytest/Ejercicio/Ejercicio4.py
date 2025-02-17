def kaprekar(num):

    res = 0

    if num >= 1000 or num < 10000:

        while res != 6174:

            i = 0
            if i == 0:
                str(num)
            else:
                str(res)

            if i == 0:
                numArray = list(num)
            else:
                numArray = list(res)

            if len(numArray) <= 3:
                numArray.append("0")

            numArray.sort(reverse=True)

            numMayor = int("".join(numArray))

            numArray.sort()

            numMenor = int("".join(numArray))

            i = i + 1

            res = numMayor - numMenor

    elif num == 6174:
        res = 0

    return res