def is_safe(board, row, col):

    for i in range(row):
        if board[i] == col:
            return False


    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False


    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

    backtrack(0)
    return solutions

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)

    print(f"Found {len(solutions)} solutions for {n}-queens problem:")
    for solution in solutions:
        print_board(solution)
