import requests

if __name__ == '__main__':
    cookies = {"session" : ""}
    arr = requests.get('https://adventofcode.com/2022/day/4/input', cookies=cookies).text.split("\n")
    max = 0
    for num, i in enumerate(arr):
        if i == "":
            break
        i = i.strip().split(",")
        if int(i[0].split("-")[0]) >= int(i[1].split("-")[0]) and int(i[0].split("-")[1]) <= int(i[1].split("-")[1]):
            max += 1
        elif int(i[0].split("-")[0]) <= int(i[1].split("-")[0]) and int(i[0].split("-")[1]) >= int(i[1].split("-")[1]):
            max += 1

    max = 0
    r = ["90-90,80-80"]
    a = ["5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
    for num, i in enumerate(arr):
        if i == "":
            break
        i = i.strip().split(",")
        if int(i[0].split("-")[1]) >= int(i[1].split("-")[0]) and int(i[0].split("-")[0]) <= int(i[1].split("-")[1]):
            max += 1
        # if int(i[0].split("-")[0]) >= int(i[1].split("-")[0]) or int(i[0].split("-")[1]) <= int(i[1].split("-")[1]):
        #     if int(i[0].split("-")[1]) >= int(i[1].split("-")[0]):
        #         max += 1
        # elif int(i[0].split("-")[0]) <= int(i[1].split("-")[0]) or int(i[0].split("-")[1]) >= int(i[1].split("-")[1]):
        #     if int(i[0].split("-")[1]) <= int(i[1].split("-")[1]):
        #         max += 1

    print(max)
