# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            square = sudoku[r][c]
            if square > 0 and square in numbers:
                return False
            else:
                numbers.append(square)
    return True
   
    print(sudoku[row_no][column_no])

        