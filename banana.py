def banana(s):
    text = ""
    i = 0

    for ch in s:
        if i < 6 and ch == 'banana'[i]:
            text += ch
            i += 1
        else:
            text += "_"
    return text


if __name__ == '__main__':
    x = "bbananana"
    print(banana(x))
