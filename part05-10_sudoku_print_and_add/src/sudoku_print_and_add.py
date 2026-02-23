# Write your solution here
def print_sudoku(sudoku: list):
    for r in range(9):           
        if r == 3 or r == 6 :
            print()
        for c in range(9):
            square = sudoku[r][c]
            if c == 3 or c == 6:
                print(" ", end="") 
            if square == 0:
               square = "_"
            print(square, end= " ")
        print()
            
    
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
        sudoku[row_no][column_no] = number

        


