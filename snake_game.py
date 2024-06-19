from tkinter import *
import random as rd


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"

BTN_WIDTH = 20
BTN_HEIGHT = 5


class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)
        


class Food:

    def __init__(self):
        x = rd.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = rd.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")




def next_turn(snake, food):
    x, y = snake.coordinates[0]
    
    if direction == 'up':
        y -= SPACE_SIZE

    elif direction == 'down':
        y += SPACE_SIZE

    elif direction == 'left':
        x -= SPACE_SIZE

    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square)


    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text = "Score:{:}".format(score))

        canvas.delete('food')
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]


    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction

    elif new_direction == 'right' and direction != 'left':
        direction = new_direction

    elif new_direction == 'up' and direction != 'down':
        direction = new_direction

    elif new_direction == 'down' and direction != 'up':
        direction = new_direction




def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:

        if x == body_part[0] and y == body_part[1]:
            return True

    return False
        


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/3, font = ('consolas', 70),
                       text = "GAME OVER", fill = "red", tag = "gameover")


    #Retry
    button1.place(x = GAME_HEIGHT / 2 - BTN_WIDTH * BTN_HEIGHT , y = GAME_WIDTH / 1.5)
    


def retry():
    global score, snake, food, direction
    
    direction = 'down' 
    score = 0
    label.config(text = "Score:{:}".format(score))
    canvas.delete("gameover")

    button1.place(x = -100, y = -100)
 

    snake = Snake()  
    food = Food()


    next_turn(snake, food)
    
    



  
def main():
    
    global window, score, canvas, direction, window, label, button1, snake, food
    score = 0
    direction = 'down'

    window = Tk()
    window.title("Snake Game")
    window.resizable(False, False)
    window.iconphoto(False, PhotoImage(file='snake.png'))
    
    #score label
    label = Label(window, text = "Score:{:}".format(score), font = ('consolas', 40))
    label.pack()

    #bg canvas
    canvas = Canvas(window, bg = BG_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
    canvas.pack(expand = 'yes')

    #Retry button
    button1 = Button(window, text = "RETRY", width = BTN_WIDTH, height = BTN_HEIGHT, command = retry)
    button1.place(x = GAME_HEIGHT * 2 - BTN_WIDTH , y = GAME_WIDTH * 2)



    window.update()


    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))


    snake = Snake()
    food = Food()

    next_turn(snake, food)



main()
window.mainloop()










