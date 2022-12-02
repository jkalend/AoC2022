import requests

if __name__ == '__main__':
    cookies = {"session" : ""}
    arr = requests.get('https://adventofcode.com/2022/day/2/input', cookies=cookies).text.split("\n")
    out = 0
    for i in arr:
        first = (ord(i.split(" ")[0]) if " " in i else ord("A")-1) % ord("A")
        second = (ord(i.split(" ")[1]) if " " in i else ord("X")-1) % ord("X")
        if first == 0:
            out += 1 + 3 if second == 0 else 0
            out += 6 + 2 if second == 1 else 0
            out += 3 if second == 2 else 0
        elif first == 1:
            out += 1 if second == 0 else 0
            out += 2 + 3 if second == 1 else 0
            out += 6 + 3 if second == 2 else 0
        elif first == 2:
            out += 6 + 1 if second == 0 else 0
            out += 2 if second == 1 else 0
            out += 3 + 3 if second == 2 else 0
    print(out)

    out = 0
    for i in arr:
        first = (ord(i.split(" ")[0]) if " " in i else ord("A")-1) % ord("A")
        second = (ord(i.split(" ")[1]) if " " in i else ord("X")-1) % ord("X")
        if first == 0: #rock
            out += 3 if second == 0 else 0 #lose
            out += 1 + 3 if second == 1 else 0 #draw
            out += 2 + 6 if second == 2 else 0 #win
        elif first == 1: #paper
            out += 1 if second == 0 else 0
            out += 2 + 3 if second == 1 else 0
            out += 6 + 3 if second == 2 else 0
        elif first == 2: #scissors
            out += 2 if second == 0 else 0
            out += 3 + 3 if second == 1 else 0
            out += 1 + 6 if second == 2 else 0

    print(out)

