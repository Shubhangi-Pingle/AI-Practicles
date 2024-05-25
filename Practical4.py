def issafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 'Q':
            return False
    row = x
    col = y
    # Checking diagonal attack
    while row >= 0 and col >= 0:
        if arr[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 'Q':
            return False
        row -= 1
        col += 1

    return True

def nQueen(arr, x, n):
    if x >= n:
        print("\nSolution:")
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
            print()
        print()
        return True

    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 'Q'
            print("\nQueen placed at row:", x + 1, "column:", col + 1)
            for i in range(n):
                for j in range(n):
                    print(arr[i][j], end=" ")
                print()
            if nQueen(arr, x + 1, n):
                return True
            arr[x][col] = '.'
            print("\nBacktrack. Removed queen from row:", x + 1, "column:", col + 1)
            for i in range(n):
                for j in range(n):
                    print(arr[i][j], end=" ")
                print()
    return False

def main():
    n = int(input("Enter number of Queens: "))
    arr = [['.' for i in range(n)] for i in range(n)]

    if not nQueen(arr, 0, n):
        print("No solution exists.")

main()
