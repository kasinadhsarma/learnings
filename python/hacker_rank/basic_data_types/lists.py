if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        if op == 'insert':
            i,e = int(cmd[1]), int(cmd[2])
            lst.insert(i, e)
        elif op == 'print':
            print(lst)
        elif op == 'remove':
            lst.remove(int(cmd[1]))
        elif op == 'append':
            lst.append(int(cmd[1]))
        elif op == 'sort':
            lst.sort()
        elif op == 'pop':
            lst.pop()
        elif op == 'reverse':
            lst.reverse()