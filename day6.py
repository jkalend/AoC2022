import requests

if __name__ == '__main__':
    cookies = {"session" : "53616c7465645f5fa47cbb0ca4ce9e975c6fbc56ff99561f9f1f6dbe1cb36bae80ae8b12bc4da49f76fdcbab19ed1c0f3f764f75d0f699cd9f7fffc2b26e7cac"}
    arr = requests.get('https://adventofcode.com/2022/day/6/input', cookies=cookies).text
    buffer = []
    index = 0
    for i in arr:
        index += 1
        if len(buffer) == 14:
            buffer.pop(0)
        if len(buffer) != 14:
            buffer.append(i)
            if len(set(buffer)) == 14:
                print(index)
                break
