# Game Ping-Pong

# Importação de biblioteca
from tkinter import *
import random
import time

# Variável que vai receber o valor digitado pelo usuário sobre o nível de jogo que ele escolher
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# Variável que vai indicar o tamanho da barra do jogo de acordo com o nível escolhido
length = 500/level

# Instância do objeto Tk
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Variável que recebe o valor da função Canvas
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável do contador
count = 0

# Variável
lost = False

# Classe bola
class Bola:
    def __init__(self, canvas, Barra, color):

        # Variáveis para a função
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # Lista
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        # Variáveis
        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Função
    def draw(self):

        # Variáveis
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # Condicional IF
        if pos[1] <= 0:

            # Variável
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        # Variável
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Condicional IF aninhada
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:

                # Variáveis
                self.y = -3
                global count
                count +=1

                # Chamada à função
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

# CLasse Barra
class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)

        # Chamada ao método
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()

    # Variável que recebe o resultado da função
    canvas.itemconfig(game, text=" ")

    # Métodos dos objetos
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Função
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# Função
def game_over():
    canvas.itemconfig(game, text="Game over!")

# Instâncias dos objetos barra e bola
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# Variáveis que recebem os resultados das funções
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

canvas.bind_all("<Button-1>", start_game)

# Executa o programa
root.mainloop()



