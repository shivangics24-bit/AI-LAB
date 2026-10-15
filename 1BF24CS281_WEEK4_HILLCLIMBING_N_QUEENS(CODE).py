def calculate_cost(board):
    cost = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


def hill_climbing(board):
    n = len(board)

    while True:
        current_cost = calculate_cost(board)

        if current_cost == 0:
            return board

        best_board = board[:]
        best_cost = current_cost

        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    neighbor = board[:]
                    neighbor[col] = row
                    cost = calculate_cost(neighbor)

                    if cost < best_cost:
                        best_cost = cost
                        best_board = neighbor

        if best_cost == current_cost:
            return None

        board = best_board


def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


n = 4
board = [2, 2, 2, 2]

solution = hill_climbing(board)

if solution is not None:
    print("Input: N =", n)
    print("Output:")
    print_board(solution)
    print("Cost:", calculate_cost(solution))
else:
    print("Local minimum reached")