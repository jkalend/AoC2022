import requests

if __name__ == '__main__':
    cookies = {"session" : ""}
    arr = requests.get('https://adventofcode.com/2022/day/5/input', cookies=cookies).text.split("\n")
    crates = [[] for _ in range(9)]
    for i in arr:
        if "1" in i:
            break
        for j in range(9):
            if i[1 + j*4] != " ":
                crates[j].append(i[1 + j*4])

    for i in crates:
        i.reverse()

    for i in arr:
        if "move" not in i:
            continue
        i = i.split(" ")
        tmp = [[] for _ in range(9)]
        for _ in range(int(i[1])):
            # crates[int(i[5])-1].append(crates[int(i[3]) - 1].pop()) part 1
            tmp[int(i[5]) - 1].append(crates[int(i[3]) - 1].pop())
        tmp[int(i[5]) - 1].reverse()
        for j in range(int(i[1])):
            crates[int(i[5]) - 1].append(tmp[int(i[5]) - 1][j])


    for i in crates:
        print(i[-1], end="")
