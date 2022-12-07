import requests

if __name__ == '__main__':
    cookies = {"session" : ""}
    arr = requests.get('https://adventofcode.com/2022/day/3/input', cookies=cookies).text.split("\n")
    max = 0
    for i in arr:
        for j in range(0, len(i)//2):
            if i[j] in i[len(i)//2:len(i)] and i[j].isupper():
                max += ord(i[j]) % ord("A") + 27
                break
            elif i[j] in i[len(i)//2:len(i)] and i[j].islower():
                max += ord(i[j]) % ord("a") + 1
                break

    max = 0
    for num, i in enumerate(arr):
        if (num+1) % 3 == 0 and num != 0:
            for j in i:
                if j in arr[num-1] and j in arr[num-2]:
                    if j.isupper():
                        max += ord(j) % ord("A") + 27
                        break
                    elif j.islower():
                        max += ord(j) % ord("a") + 1
                        break
# 2497

    print(max)
