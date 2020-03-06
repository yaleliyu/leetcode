def Repeat(s):
    finalstr = ""
    state = "Norm"
    repeat = ""
    repeatnum = 0
    bodystr = ""
    braket = 0
    for idx, n in enumerate(s):
        if state == "Norm" and n.isdigit():
            state = "digit"
            repeat += n
        elif state == "digit" and n.isdigit():
            repeat += n
        elif state == "Norm" and n.isalpha():
            finalstr += n
        elif state == "digit" and n == '[':
            state = "body"
            repeatnum = int(repeat)
            repeat = ""
            bodystr = ""
        elif state == "body" and n not in ['[', ']']:
            bodystr += n
        elif state == "body" and n == '[':
            braket += 1
            bodystr += n
        elif state == "body" and n == ']':
            if braket:
                braket -= 1
                bodystr += n
            else:
                state = "Norm"
                repeatstr = Repeat(bodystr)
                finalstr += repeatstr * repeatnum
        else:
            raise Exception(f"Incorrect input {n} at {idx}")
    return finalstr


print(Repeat('3[p2[d]e]'))
