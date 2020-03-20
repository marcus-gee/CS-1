'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        self.board = [[0] * 9 for i in range(9)]
        self.moves = []

    def load(self, filename):
        '''This function loads the board to play sudoku'''
        f = open(filename, 'r')
        lines = 0
        digits = 0
        line_count = 0
        digit_count = 0
        for line in f:
            line_count += 1
            digit_count = len(line)
            if digit_count != 9 and digit_count != 10:
                raise IOError('There is an incorrect number of numbers in \
                the line')
            if line_count > 9:
                raise IOError('Board must have 9 lines')
            for num in line[0:9]:
                if num not in '0123456789':
                    raise IOError('Number must be between 0 an 9')
                self.board[lines][digits] = int(num)
                digits += 1
            digits = 0
            lines += 1
        f.close()

    def save(self, filename):
        '''This function saves the board'''
        f = open(filename, 'w')
        for row in range(9):
            for column in range(9):
                f.write(self.board[row][column])
            f.write('\n')
        f.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print() 
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        '''This function takes a value and puts it at the specified row and 
        column coordinates''' 
        
         
        row_new = (row - 1) / 3
        col_new = (col - 1) / 3

        if row_new < 1:
            row_start = 0
            
        elif row_new >= 1 or row_new < 2:
            row_start = 3
            
        elif row_new >= 2:
            row_start = 6
    
        if col_new < 1:
            col_start = 0
            
        elif col_new >= 1 or row_new < 2:
            col_start = 3
            
        elif col_new >= 2:
            col_start = 6
            
        if type(val) is not int:
            raise SudokuMoveError('Value must be an integer')
        
        if val < 1 or val > 9:
            raise SudokuMoveError('Value must be between 1 and 9')
        
        if type(row) is not int and type(col) is not int:
            raise SudokuMoveError('Rows and columns must be integers')
        
        if row < 1 or row > 9:
            raise SudokuMoveError('Row must be between 1 and 9')
        
        if col < 1 or col > 9:
            raise SudokuMoveError('Column must be between 1 and 9')  
        
        for i in range(9):
            if self.board[row - 1][i] == val:
                raise SudokuMoveError('Row conflict. Please try again')
            
            if self.board[i][col - 1] == val:
                raise SudokuMoveError('Column conflict. Please try again')
            
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == val:
                    raise SudokuMoveError('Box conflict. Please try again')
                
        if self.board[row - 1][col - 1] == 0:
            self.board[row - 1][col - 1] = val
            self.moves.append((row, col, val))

    def undo(self):
        '''This function undoes the previous move'''
        self.move.pop(len(self.moves) - 1)
        

    def solve(self):
        '''This function handles user interactions'''
        while True:
            try:
                move = str(input('sudoku> '))
                total = 0
                if len(move) == 3:
                    for i in move:
                        if i in '123456789':
                            total += 1
                if move == 'q':
                    return
                elif move == 'u':
                    self.undo()
                    self.show()
                elif total == 3:
                    self.move(int(move[0]), int(move[1]), int(move[2]))
                    self.show()
                elif move[0] == 's':
                    self.save(move[1:])
                    self.show()
                else:
                    raise SudokuCommandError('Input is invalid. Must be a q, \
                    u, s, or a three-digit sequence')
            except SudokuMoveError as x:
                print(str(x))
                print('\n')
                self.show()
            except SudokuCommandError as x:
                print(str(x))
                print('\n')
                self.show()
                    
                             

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError as e:
            print(e)

    s.show()
    s.solve()

