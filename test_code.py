def safe_pawns(pawns):
    count = 0
    safed = ""
    for figure in pawns:
        prev_l = chr(ord(figure[0]) + 1)
        next_l = chr(ord(figure[0]) - 1)
        next_n = int(figure[1]) + 1
        # if figure[1] == "1":
        #     count += 1
        #     continue
        # elif figure[0] == "a" or figure[0] == "h":
        #     pass
        # else:
        for check in pawns:
                if check == prev_l + str(next_n) or check == next_l + str(next_n):
                    count += 1
                    if check == prev_l + str(next_n):
                        safed += prev_l + str(next_n) + " "
                    if check == next_l + str(next_n):
                        safed += next_l + str(next_n) + " "
    return (count-1, safed)

print(safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"]))