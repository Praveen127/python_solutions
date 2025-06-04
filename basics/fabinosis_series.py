def fabinosis_series(n):
    fab = [0,1]
    if n < 0:
        return [-1]
    if n == 0:
        fab=[]
    elif n == 1:
        fab = [0]
    elif n == 2:
        fab = [0, 1]
    else:
        for i in range(n-2):
            fab.append(fab[-1]+fab[-2])

    print(fab)
    return fab

if __name__ == "__main__":
    num = int (input("enter the number for febinosis series:"))
    print(f" febinosis series ", fabinosis_series(num))
