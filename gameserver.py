import socket

class RockPaperScissorsGame:
    def __init__(self):
        self.player1_choice = None
        self.player2_choice = None

    def make_choice(self, player, choice):
        if player == "player1":
            self.player1_choice = choice
        elif player == "player2":
            self.player2_choice = choice

        if self.player1_choice and self.player2_choice:
            if self.player1_choice == self.player2_choice:
                return "Tie!"
            elif (self.player1_choice == "rock" and self.player2_choice == "scissors") or \
                 (self.player1_choice == "paper" and self.player2_choice == "rock") or \
                 (self.player1_choice == "scissors" and self.player2_choice == "paper"):
                return "Player 1 wins!"
            else:
                return "Player 2 wins!"

        return None

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(2)

print("Server is listening on port 8000")

game = RockPaperScissorsGame()

while True:
    conn1, addr1 = server_socket.accept()
    print("Connected by", addr1)

    conn2, addr2 = server_socket.accept()
    print("Connected by", addr2)

    while True:
        data1 = conn1.recv(1024).decode()
        if not data1:
            break
        response = game.make_choice("player1", data1)
        if response:
            conn1.send(response.encode())
            conn2.send(response.encode())

        data2 = conn2.recv(1024).decode()
        if not data2:
            break
        response = game.make_choice("player2", data2)
        if response:
            conn1.send(response.encode())
            conn2.send(response.encode())

    conn1.close()
    conn2.close()