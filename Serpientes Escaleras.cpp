// Serpientes Escaleras.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
class Dice {
private:
    int numberOfOptions;
public:

    Dice(int numberOfOptions = 6) {
        this->numberOfOptions = numberOfOptions;
    }

    int roll(){
        srand((unsigned)time(NULL)); // Set a pseudo random seed
        return (rand() % this->numberOfOptions) + 1;
        }
};

class Player {
private:
    int last_pos, pos, num;
public:
    Player(int num) {

        pos = 0;
        this->num = num;

    }

    std::string draw() {
        std::cout << 
            "\n\nPlayer " << this->num <<
            "\nPlayer 1 previous pos: " << this->getLast() + 1 <<
            "\nPlayer 1 current pos: " << this->getTile() + 1 << "\n\n";
        return (std::to_string(this->num) + ' ' + std::to_string(this->getLast() + 1) + ' ' + std::to_string(this->getTile()));
    }

    int getTile() {
        return pos;
    }

    int getLast() {
        return last_pos;
    }

    void setTile(int n) {
        this->pos = n;
    }

    void setLast(int n) {
        this->last_pos = n;
    }

};

/*
Características del Board
    El Board debe contener 30 casillas (tiles).
    El Board debe contener 3 casillas de tipo serpiente indicadas con la letra S (snakes).
    El Board debe contener 3 casillas de tipo escalera indicadas con la letra L (ladders).
    Las casillas restantes deberán identificarse como casillas normales con la letra N.
    Cada casilla serpiente deberá retroceder al jugador 3 casillas (penalty).
    Cada casilla escalera deberá avanzar 3 casillas adicionales (reward).
    Cada casilla se identifica con un número natural a partir del 1.
*/

class Board {
protected:
    char tiles[30];
    std::string name;
    int snakes[3], ladders[3];
public:

    Board(std::string name) {
        this->name = name;
        srand((unsigned)time(NULL)); // Set a pseudo random seed
        fillBoard();
    }

    std::string draw();
    bool isIn(int target, int array[3]);
    char getTile(int n);
    void fillBoard();
    int logic(int tile);

};

char Board::getTile(int n) {
    return this->tiles[n];
}

std::string Board::draw() {
    std::cout << this->name << "\n\n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            std::cout << this->tiles[i * 6 + j] << ' ';
        }
        std::cout << '\n';
    }
    std::cout << "\n\n";
    return (this->tiles);
}

bool Board::isIn(int target, int array[3]) {
    // Check if a tile has already been designated.
    for (int i = 0; i < 3; i++) {
        if (target == array[i]) {
            return true;
        }
    }
    return false;
}

void Board::fillBoard() {

    // Fill snakes
    int i = 0;
    while (i < 3) {
        int attemp = rand() % 28 + 1;
        if (!isIn(attemp, this->snakes)) {
            this->snakes[i] = attemp;
            i++;
        }
    }

    // Fill ladders
    i = 0;
    while (i < 3) {
        int attemp = rand() % 28 + 1;
        if (!isIn(attemp, this->ladders) && !isIn(attemp, this->snakes)) {
            this->ladders[i] = attemp;
            i++;
        }
    }

    // Fill the board
    for (i = 0; i < 30; i++) {
        if (isIn(i, this->snakes)) {
            this->tiles[i] = 'S';
        }
        else if (isIn(i, this->ladders)) {
            this->tiles[i] = 'L';
        }
        else {
            this->tiles[i] = 'N';
        }
    }

}

// Manages the logic of snakes and ladders
int Board::logic(int tile) {
    if (this->getTile(tile) == 'S'){
        std::cout << "You encountered a Snake!\n\n";
        return -3;
    } else if (this->getTile(tile) == 'L') {
        std::cout << "You encountered a Ladder!\n\n";
        return 3;
    }
    else {
        return 0;
    }
}

/*
Características de los jugadores
    El juego debe soportar 2 jugadores.
    Cada jugador se identifica con un número natural a partir del 1.
    Al inicio del juego todos los jugadores se encuentran en la casilla 1.
    El jugador 1 comienza el primer turno del juego.

Características del juego
    El juego se compone de una sucesión de turnos.
    Cada turno se podrá ejecutar en línea de comandos alguna de las 2 posibles acciones siguientes:
        Introducir la letra “C” (continue) para continuar con el juego con el siguiente turno.
        Introducir la letra “E” (end) para terminar el juego.
        Solamente antes del primer turno se debe imprimir el siguiente menú de instrucciones:
        Press C to continue next turn, or E to end the game:

Si la tecla introducida no es alguna de “C” o “E” se debe imprimir el siguiente mensaje:
    Invalid option, please press C to continue next turn or E to end the game

Ejecución del turno:
    Durante cada turno se debe imprimir en consola la siguiente información correspondiente al turno.
    El número del turno (el primer turno se indica con el número 1).
    El número del jugador con el turno actual.
    El número de casilla correspondiente a la posición actual del jugador.
    El número obtenido al simular un dado convencional de 6 caras.

El tipo de casilla a la que el jugador debería moverse después de tirar el dado:
    N para casillas normales.
    S para casillas serpiente (Snake).
    L para casillas escalera (Ladder).

La casilla final a la que el jugador debe moverse:
    Si la casilla es Normal, entonces indicar la posición final directamente.
    Si la casilla es Escalera, la posición final será la resultante del incremento en casillas. correspondiente indicado por la recompensa.
    Si la casilla es Serpiente, la posición final será la resultante del retroceso en casillas correspondiente, indicado por la penalización.
    Si una casilla especial (Serpiente o Escalera) da como resultado que el jugador en turno caiga en otra casilla especial, esta segunda deberá ser ignorada, es decir, sólo se permite un salto o un retroceso por turno.
*/

class MyGame: public Board, public Dice{
private:
    bool gameOver, turn;
    int MAX_TURN , turn_counter = 0;
    Player player1 = Player(1);
    Player player2 = Player(2);
public:
    MyGame(std::string name, int MAX_TURN ):Board(name){
        this->gameOver = 0;
        this->turn = 0;
        this->MAX_TURN  = MAX_TURN ;
    }

    //Clear the terminal
    void flush() {
        system("CLS");
    }

    void start();
    std::string draw(int DiceRoll);
    void describe();


};

void MyGame::describe() {
    int tile;
    std::cout << this->name <<
        "\n\nCurrent turn: Player " << this->turn + 1 <<
        "\nPlayer 1 poss: " << this->player1.getTile() + 1 <<
        "\nPlayer 2 poss: " << this->player2.getTile() + 1 << "\n\n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            tile = 29 - (i * 6 + j);
            if (this->player1.getTile() == tile && this->player2.getTile() == tile) {
                std::cout << "3" << ' ';
            }
            else if (this->player1.getTile() == tile) {
                std::cout << "1" << ' ';
            }
            else if (this->player1.getTile() == tile) {
                std::cout << "2" << ' ';
            }
            else {
                std::cout << this->tiles[tile] << ' ';
            }

        }
        std::cout << '\n';
    }
    std::cout << "\n\n";
}

std::string MyGame::draw(int DiceRoll) {
    int tile;
    std::cout << this->name << 
        "\n\nTurn " << this->turn_counter + 1 << '/' << this->MAX_TURN <<
        "\nCurrent turn: Player " << this->turn+1 <<
        "\nPlayer " << !this->turn +1 <<" rolled: " << DiceRoll <<
        "\nPlayer 1 previous pos: " << this->player1.getLast() + 1 <<
        "\nPlayer 1 current pos: " << this->player1.getTile() + 1 <<
        "\nPlayer 2 previous pos: " << this->player2.getLast() + 1 <<
        "\nPlayer 2 current pos: " << this->player2.getTile() + 1 << "\n\n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            tile = 29 - (i * 6 + j);
            if (this->player1.getTile() == tile && this->player2.getTile() == tile) {
                std::cout << "3" << ' ';
            } 
            else if (this->player1.getTile() == tile) {
                std::cout << "1" << ' ';
            }
            else if (this->player2.getTile() == tile) {
                std::cout << "2" << ' ';
            } 
            else {
                std::cout << this->tiles[tile] << ' ';
            }
            
        }
        std::cout << '\n';
    }
    std::cout << "\n\n";

    return this->name + std::to_string(this->turn + 1) +
        std::to_string(this->player1.getLast() + 1) +
        std::to_string(this->player1.getTile() + 1) +
        std::to_string(this->player2.getLast() + 1) +
        std::to_string(this->player2.getTile() + 1);
}

void MyGame::start() {
    int DiceRoll, actualMovement;
    char cmd; 

    std::cout << "Press C to continue next turn, or E to end the game.\n";
    this->describe();

    while (!this->gameOver && this->player1.getTile() < 29 && this->player2.getTile() < 29 && this->turn_counter < this->MAX_TURN ) {
        
        std::cin >> cmd;
        std::cin.clear();
        std::cin.ignore(10000, '\n');
        cmd = toupper(cmd);
        this->flush();

        switch (cmd)
        {
        case 'C':
             
            DiceRoll = this->roll();

            player1.setLast(this->player1.getTile());
            player2.setLast(this->player2.getTile());

            if (!this->turn) {
                actualMovement = DiceRoll + this->logic(this->player1.getTile() + DiceRoll);
                player1.setTile(this->player1.getTile() + actualMovement);
            }
            else {
                actualMovement = DiceRoll + this->logic(this->player2.getTile() + DiceRoll);
                player2.setTile(this->player2.getTile() + actualMovement);
            }

            this->turn = !this->turn;
            this->draw(DiceRoll);
            this->turn_counter++;
            break;
        case 'E':
            this->gameOver = !this->gameOver;
            break;

        default:
            std::cout << "Invalid option, please press C to continue next turn or E to end the game.\n";
            this->describe();
            break;
        }
 
    }

    this->flush(); std::cout << "-- GAME OVER --\n\n";

    if (this->turn_counter >= this->MAX_TURN) {
        std::cout << "The maximum number of turns has been reached...\n\n";
    }
    else if (cmd == 'C') {
        this->turn_counter--;
        if (this->player1.getTile() > 29) {
            this->player1.setTile(29);
            }
        if (this->player2.getTile() > 29) {
            this->player2.setTile(29);
        }
        this->draw(DiceRoll);
        if (this->player1.getTile() == 29) {
            std::cout << "Player 1 is the winner";
        } else{
            std::cout << "Player 2 is the winner";
        }
        std::cout << "\n\n";
    }
    else {
        std::cout << "Thanks for playing!!!\n\n";
    }
        
    std::cin >> cmd;
}


int main()
{

    MyGame snakesNLadders = MyGame("SNAKES AND LADDERS",20);
    snakesNLadders.start();

    return 0;

}