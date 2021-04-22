import random
import os

class board():

    def __init__(self, w, h, b):
        self.size = w*h
        self.win = False
        self.score = 0
        self.gameover = False
        self.turn = 1
        self.width = w
        self.height = h
        self.bomb_num = b
        self.visited = [[False for i in range(self.width)]for j in range(self.height)]
        self.bombs = self.plantmines(b)
        self.field = self.setfield()
        self.numbersetter()

    def flush(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def display(self):

        print(f'\tTurn: {str(self.turn)}\tScore: {self.score}',end='\n'*2)

        for h in reversed(range(self.height)):
            print(h,"\t|",end="\t")
            for w in range(self.width): 
                if self.visited[h][w]:
                    print(self.field[h][w],end="\t")
                else:
                    print("X",end="\t")
            print()
        print("   ",end="\t")
        print("________"*(w+1))

        print("\t"*2,end="")
        for n in range(w+1):
            print(n,end="\t")
        print()

    def plantmines(self,b):
        bombpairs = []
        i = 0
        while i < b:
            pair = (random.randint(0,self.width-1),random.randint(0,self.height-1))
            if pair in bombpairs:
                continue
            bombpairs.append(pair)
            i+=1
        return bombpairs

    def numbersetter(self):
        for b in (self.bombs):
            x = b[0] 
            y = b[1]
            if y != self.height-1:   
                if self.field[y+1][x] != "B":                          #up
                    self.field[y+1][x] += 1
                if x != self.width-1 and self.field[y+1][x+1] != "B":  #upright
                    self.field[y+1][x+1] += 1
                if x != 0 and self.field[y+1][x-1] != "B":             #upleft
                    self.field[y+1][x-1] += 1
            if y != 0:   
                if self.field[y-1][x] != "B":                          #down
                    self.field[y-1][x] += 1
                if x != self.width-1 and self.field[y-1][x+1] != "B":  #downright
                    self.field[y-1][x+1] += 1
                if x != 0 and self.field[y-1][x-1] != "B":             #downleft
                    self.field[y-1][x-1] += 1
            if x != self.width-1 and self.field[y][x+1] != "B":        #right
                self.field[y][x+1] += 1
            if x != 0 and self.field[y][x-1] != "B":                   #left
                self.field[y][x-1] += 1

    def setfield(self):
        field = [[0 for i in range(self.width)]for j in range(self.height)]
        for b in self.bombs:
            field[b[1]][b[0]] = "B"
        return field

    def search4mines(self,x,y):
        to_visit = [(x,y)]
        visited = []
        
        while len(to_visit)>0:
            coord = to_visit.pop(0)
            self.visited[coord[1]][coord[0]] = True
            visited.append(coord)
            if self.field[coord[1]][coord[0]] == "B":
                if self.turn == 1:
                    self.flush()
                    gameboard.display()
                    print("Weird... that bomb didn't quite explode.")
                    input()
                    break
                else:
                    self.gameover = True

                break
            
            x = coord[0] 
            y = coord[1]
            if y != self.height-1:   
                if self.field[y+1][x] != "B" and (x,y+1) not in visited:   #up
                    to_visit.append((x,y+1))
                else:
                    continue

            if y != 0:   
                if self.field[y-1][x] != "B" and (x,y-1) not in visited:   #down
                    to_visit.append((x,y-1))
                else:
                    continue

            if x != self.width-1:               #right
                if self.field[y][x+1] != "B" and (x+1,y) not in visited:
                    to_visit.append((x+1,y))
                else:
                    continue

            if x != 0:                          #left
                if self.field[y][x-1] != "B" and (x-1,y) not in visited:
                    to_visit.append((x-1,y))
                else:
                    continue

    def clearfield(self):
        self.visited = [[True for i in range(self.width)]for j in range(self.height)]

    def winconditions(self):
        remaining = 0
        visited = 0
        for i in range(len(self.visited)):
            for j in range(len(self.visited[i])):
                if self.visited[i][j] == False:
                    remaining += 1
                elif self.visited[i][j] == True and self.field[i][j] != "B":
                    visited += 1
        self.score = (((visited) * (self.bomb_num**2))/self.size)*100
        return remaining <= self.bomb_num

    def play(self):
        while not self.gameover:
            self.win = self.winconditions()
            if self.win:
                break

            self.display()
            x = int(input("X = "))
            y = int(input("Y = "))
            if x < 0 or y < 0:
                self.clearfield()
                self.gameover = True
                input("Debugging...")
                continue
            
            self.search4mines(x,y)
            self.turn += 1
            
            self.flush()

        self.clearfield()
        self.display()
        
        if self.win:
            self.winconditions()
            self.flush()
            self.display()
            print("Congrats, you made it dude.")
        else:
            print("Kaboom! You lost man.")

        input("Game Over. Press ENTER...")




if __name__ == "__main__":
    w = int(input("Width: "))
    h = int(input("Heigth: "))
    b = int(input("Number of Bombs: "))

    while b > w*h-2 or b < 0:
        print("Invalid bombs, try again")
        w = int(input("Width: "))
        h = int(input("Heigth: "))
        b = int(input("Number of Bombs: "))

    gameboard = board(w,h,b)
    gameboard.flush()
    gameboard.play()
