#imports
import pygame
import time
from sudoku import Sudoku

background_color = ('light gray')
original_grid_element_color = ('dark green')
buffer = 5
size = 9

# Cell class that holds the attributes needed for each cell in the sudoku
class Cell:
    def __init__(self,current,row,column,found,value,domain) -> None:
        self.current = current
        self.row = row
        self.column = column
        self.found = found
        self.value = value
        self.domain = domain

# Hidden Singles function
def hidden_singles(sudoku,win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(size):
        for j in range(size):
            temp_list = sudoku[i][j].domain
            if len(temp_list) == 1:
                sudoku[i][j].found = True
                sudoku[i][j].value = temp_list[0]
                pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                value = myfont.render(str(sudoku[i][j].value), True, 'black')
                win.blit(value, ((j+1)*50 +15,(i+1)*50))
                pygame.display.update()
                pygame.time.delay(70)
                sudoku[i][j].domain.clear()
    return sudoku
            
# eliminate function
def eliminate(sudoku):
    
    # to check every cell
    for row in range(size):
        for col in range(size):

            # if the cell is not found
            if sudoku[row][col].found == False:
                not_in_domain = [] #an array to put all the values that cannot be apart of our domain

                # checking the row
                for k in range(size):
                    if sudoku[row][k].found == True:
                        if not not_in_domain.count(sudoku[row][k].value):
                            not_in_domain.append(sudoku[row][k].value)
                
                # checking the column
                for k in range(size):
                    if sudoku[k][col].found == True:
                        if not not_in_domain.count(sudoku[k][col].value):
                            not_in_domain.append(sudoku[k][col].value)

                # checking the box
                box_row = row // 3 * 3
                box_col = col // 3 * 3
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if sudoku[i][j].found == True:
                            if not not_in_domain.count(sudoku[i][j].value):
                                not_in_domain.append(sudoku[i][j].value)

                # delete the numbers collected from the domains
                for k in not_in_domain:
                    if k in sudoku[row][col].domain:
                        sudoku[row][col].domain.remove(k)
                
                # clear the not possible domain list 
                not_in_domain.clear()

    return sudoku

# Only choice functions
def only_choice_box(sudoku, win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for row in range(size):
        for col in range(size):

            can_continue_1 = True

            if sudoku[row][col].found == False:

                sudoku[row][col].current = True
                for k in range(len(sudoku[row][col].domain)):

                    if can_continue_1:
                        box_row = row // 3 * 3
                        box_col = col // 3 * 3
                        can_continue_2 = True
                        for i in range(box_row, box_row + 3):
                            for j in range(box_col, box_col + 3):

                                if can_continue_2:
                                    if sudoku[i][j].found == False and sudoku[i][j].current == False:
                                        if(sudoku[i][j].domain.count(sudoku[row][col].domain[k])):
                                            can_continue_2 = False
                                            break
                                    
                                    if i == box_row + 2 and j == box_col +2:
                                        sudoku[row][col].curent = False
                                        sudoku[row][col].found = True
                                        sudoku[row][col].value = sudoku[row][col].domain[k]
                                        pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                                        value = myfont.render(str(sudoku[row][col].value), True, 'black')
                                        win.blit(value, ((col+1)*50 +15,(row+1)*50))
                                        pygame.display.update()
                                        pygame.time.delay(70)
                                        sudoku[row][col].domain.clear()
                                        can_continue_1 = False
                    else:
                        break
                sudoku[row][col].current = False
    return sudoku

def only_choice_row(sudoku, win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for row in range(size):
        for col in range(size):

            can_continue = True

            if sudoku[row][col].found == False:

                sudoku[row][col].current = True
                for k in range(len(sudoku[row][col].domain)):

                    if can_continue:
                        
                        for i in range(size):
                            if sudoku[row][i].found == False and sudoku[row][i].current == False:
                                if(sudoku[row][i].domain.count(sudoku[row][col].domain[k])):
                                    break
                                    
                            if i == 8:
                                sudoku[row][col].curent = False
                                sudoku[row][col].found = True
                                sudoku[row][col].value = sudoku[row][col].domain[k]
                                pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                                value = myfont.render(str(sudoku[row][col].value), True, 'black')
                                win.blit(value, ((col+1)*50 +15,(row+1)*50))
                                pygame.display.update()
                                pygame.time.delay(70)
                                sudoku[row][col].domain.clear()
                                can_continue = False
                    else:
                        break
                sudoku[row][col].current = False
    return sudoku

def only_choice_col(sudoku, win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for row in range(size):
        for col in range(size):

            can_continue = True

            if sudoku[row][col].found == False:

                sudoku[row][col].current = True
                for k in range(len(sudoku[row][col].domain)):

                    if can_continue:
                        
                        for i in range(size):
                            if sudoku[i][col].found == False and sudoku[i][col].current == False:
                                if(sudoku[i][col].domain.count(sudoku[row][col].domain[k])):
                                    break
                                    
                            if i == 8:
                                sudoku[row][col].curent = False
                                sudoku[row][col].found = True
                                sudoku[row][col].value = sudoku[row][col].domain[k]
                                pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                                value = myfont.render(str(sudoku[row][col].value), True, 'black')
                                win.blit(value, ((col+1)*50 +15,(row+1)*50))
                                pygame.display.update()
                                pygame.time.delay(70)
                                sudoku[row][col].domain.clear()
                                can_continue = False
                    else:
                        break
                sudoku[row][col].current = False
    return sudoku

# checking the sudoku
def check_sudoku(sudoku):
    if check_row(sudoku) and check_column(sudoku):
        return True
    else:
        return False

def check_row(sudoku):
    for row in range(size):
        temp_list = []
        for i in range(size):
            if sudoku[row][i].value in temp_list:
                return False
            else:
                temp_list.append(sudoku[row][i].value)
    return True

def check_column(sudoku):
    for col in range(size):
        temp_list = []
        for i in range(size):
            if sudoku[i][col].value in temp_list:
                return False
            else:
                temp_list.append(sudoku[i][col].value)
    return True

# check if game over
def game_over(sudoku):
    for row in range(size):
        for col in range(size):
            if sudoku[row][col].found == False:
                return False
    return True


def main():
    pygame.init()
    win = pygame.display.set_mode((550, 550))
    pygame.display.set_caption("Constraint Propogation Solution")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, 'black', (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, 'black', (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, 'black', (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, 'black', (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()

    test_sudoku = [
        [5,0,1,0,0,0,6,0,4],
        [0,9,0,3,0,6,0,5,0],
        [0,0,0,0,9,0,0,0,0],
        [4,0,0,0,0,0,0,0,9],
        [0,0,0,1,0,9,0,0,0],
        [7,0,0,0,0,0,0,0,6],
        [0,0,0,0,2,0,0,0,0],
        [0,8,0,5,0,7,0,6,0],
        [1,0,3,0,0,0,7,0,2],
    ]

    for i in range(0, len(test_sudoku[0])):
        for j in range(0, len(test_sudoku[0])):
            if test_sudoku[i][j] != 0 and 0 < test_sudoku[i][j] < 10:
                value = myfont.render(str(test_sudoku[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()

    solved_sudoku = []

    for row in range(0,size):
        cell_row = []
        for column in range(0,size):
            if test_sudoku[row][column] == 0:
                temp_list = [1,2,3,4,5,6,7,8,9]
                temp_cell = Cell(False,row,column,False,0,temp_list)
                cell_row.append(temp_cell)
            else:
                empty_list = []
                temp_cell = Cell(False,row,column,True,test_sudoku[row][column],empty_list)
                cell_row.append(temp_cell)
        solved_sudoku.append(cell_row)

    iteration_counter = 0

    start_time = int(round(time.time() * 1000))

    while not game_over(solved_sudoku):
        iteration_counter += 1

        eliminate(solved_sudoku)
        hidden_singles(solved_sudoku,win)
        eliminate(solved_sudoku)

        only_choice_row(solved_sudoku,win)

        eliminate(solved_sudoku)
        hidden_singles(solved_sudoku,win)
        eliminate(solved_sudoku)

        only_choice_col(solved_sudoku,win)

        eliminate(solved_sudoku)
        hidden_singles(solved_sudoku,win)
        eliminate(solved_sudoku)

        only_choice_box(solved_sudoku,win)

        eliminate(solved_sudoku)
        hidden_singles(solved_sudoku,win)
        eliminate(solved_sudoku)

    end_time = int(round(time.time() * 1000))
    run_time = end_time - start_time

    check_sudoku(solved_sudoku)

    print('\nSudoku solved in : ' + str(run_time) + ' ms')

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()