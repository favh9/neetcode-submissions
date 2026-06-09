class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Approach
        Create helper functions to traverse a given row, column and subbox:
            Search individual rows and columns by traversing the row/column.
            Search subboxes by traversing the rows and columns of it.
                Rows and columns can be searched with a given index like 0-8
                Subboxes can be searched with a given position like box 0-8
                Using a set, add all elements until a duplicate is found or not.

        Using the helper functions, use booleans to immediately get feedback if a row,
        column, or subbox contains a duplicate.
            search every row
            search every column
            search every subbox
        return True after exhausting all prior searches.
        """

        for i in range(len(board)):
            if not self.isRowValid(i, board):
                return False
            if not self.isColValid(i, board):
                return False
            if not self.isBoxValid(i, board):
                return False
        return True

    """ Helper function 1
    @param row - the index at which the row is at on the board
    @param board - the complete board
    """
    def isRowValid(self, row: int, board: List[List[str]]):

        nums = set()

        for i in range(len(board)):
            element = board[row][i]
            if element == ".":  # empty
                continue
            if element not in nums:
                nums.add(element)
            else:
                return False  # duplicate detected

        return True

    """ Helper function 2
    @param col - the index at which the column is at on the board
    @param board - the complete board
    """
    def isColValid(self, col: int, board: List[List[str]]):

        nums = set()

        for i in range(len(board)):
            element = board[i][col]
            if element == ".":  # empty
                continue
            if element not in nums:
                nums.add(element)
            else:
                return False  # duplicate detected

        return True

    """ Helper function 3
    @param box - the box index or position on the board
    @param board - the complete board
    """
    def isBoxValid(self, pos: int, board: List[List[str]]):

        nums = set()

        row, col = self.getRowAndColAt(pos)
        for i in range(row, row + 3, 1):
            for j in range(col, col + 3, 1):
                element = board[i][j]
                if element == ".":  # empty
                    continue

                if element not in nums:
                    nums.add(element)
                else:
                    return False  # duplicate detected

        return True

    def getRowAndColAt(self, pos: int):

        row = 0
        col = 0

        # top
        if pos == 0:
            row = 0
            col = 0
        elif pos == 1:
            row = 0
            col = 3
        elif pos == 2:
            row = 0
            col = 6
        # middle
        elif pos == 3:
            row = 3
            col = 0
        elif pos == 4:
            row = 3
            col = 3
        elif pos == 5:
            row = 3
            col = 6
        # bottom
        elif pos == 6:
            row = 6
            col = 0
        elif pos == 7:
            row = 6
            col = 3
        elif pos == 8:
            row = 6
            col = 6

        return row, col
