BOARD_SIZE = 10
'''
[
    [., ., .],
    [., ., .],
    [., ., .]
]
'''
class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.layout = self.generate_board()

    def generate_board(self):
        row = list(" . " for i in range(BOARD_SIZE))
        layout = []
        for i in range(BOARD_SIZE):
            layout.append(row)
        return layout

    def display(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                print(self.layout[row][col], end = '')
            print("");  # newline
