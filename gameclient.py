import tkinter as tk
import socket

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.server_address = ('localhost', 8000)

        self.create_widgets()

    def create_widgets(self):
        self.message_label = tk.Label(self.master, text="Choose rock, paper, or scissors:")
        self.message_label.pack()

        self.choice_frame = tk.Frame(self.master)
        self.choice_frame.pack()

        self.rock_button = tk.Button(self.choice_frame, text="Rock", command=lambda: self.send_choice("rock"))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.choice_frame, text="Paper", command=lambda: self.send_choice("paper"))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", command=lambda: self.send_choice("scissors"))
        self.scissors_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def send_choice(self,choice):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall(choice.encode())
            data = sock.recv(1024).decode()

        self.result_label.configure(text=data)

    def reset_game(self):
        self.result_label.configure(text="")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry('300x200')
game = RockPaperScissors(root)
root.mainloop()