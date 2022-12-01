import requests

if __name__ == '__main__':
    cookies = {'_ga' :'', '_gid' : "", "session" : ""}
    arr = requests.get('https://adventofcode.com/2022/day/1/input', cookies=cookies).text.split("\n\n")
    max = 0
    maxes = []
    for num, i in arr:
        a = sum([int(j) for j in i.split("\n") if j != ''])
        maxes.append(a)
        max = a if max < a else max

    print(max)
    maxes.sort(reverse=True)
    print(sum(maxes[0:3]))
