import requests
import treelib as tree

class registry:
    def __init__(self, dir_ = False, file_ = False, name = '', size = 0):
        self.dir_ = dir_
        self.file_ = file_
        self.name = name
        self.size = size


if __name__ == '__main__':
    cookies = {"session":"53616c7465645f5fa47cbb0ca4ce9e975c6fbc56ff99561f9f1f6dbe1cb36bae80ae8b12bc4da49f76fdcbab19ed1c0f3f764f75d0f699cd9f7fffc2b26e7cac"}
    arr = requests.get('https://adventofcode.com/2022/day/7/input', cookies=cookies).text.split('\n')
    buffer = tree.Tree()
    buffer.create_node("/", "/", data=registry(dir_=True))
    current = buffer.get_node("/")
    for line in arr:
        if line.startswith('$'):
            if line.split(" ")[1] == 'cd':
                if line.split(" ")[2] == '..':
                    if current.identifier != "/":
                        current = buffer.parent(current.identifier)
                elif line.split(" ")[2] == '/':
                    current = buffer.get_node("/")
                else:
                    print(line.split(" ")[2])
                    current = buffer.get_node(current.identifier + "/" + (line.split(" ")[2]))
            elif line.split(" ")[1] == 'ls':
                continue
        else:
            if line.split(' ')[0].isnumeric():
                if buffer.get_node((line.split(" ")[1])) is not None:
                    continue
                buffer.create_node(line.split(" ")[1], current.identifier + "/" + line.split(" ")[1],
                                   data=registry(file_=True, size=int(line.split(' ')[0]), name=line.split(" ")[1]),
                                   parent=current.identifier)

            elif line.split(' ')[0] == "dir":
                if buffer.get_node((line.split(" ")[1])) is not None:
                    continue
                buffer.create_node(line.split(" ")[1], current.identifier + "/" + line.split(" ")[1],
                                   data=registry(dir_=True, name=line.split(" ")[1]),
                                   parent=current.identifier)

    for i in buffer.all_nodes().__reversed__():
        if buffer.parent(i.identifier) is not None:
            buffer.parent(i.identifier).data.size += i.data.size

    out = []
    max = 30000000 - (70000000 - buffer.get_node("/").data.size)
    for i in buffer.all_nodes():
        if i.data.dir_ and max - i.data.size <= 0:
            out.append(i.data.size)
        # if i.data.dir_ and i.data.size <= 100000: # part one
        #     out.append(i.data.size)

    print(min(out))

    #print(sum(i.data.size for i in buffer.all_nodes() if i.data.dir_ and i.data.size <= 100000)) # part one
