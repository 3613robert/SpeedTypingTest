from tkinter import *
from logo import logo
import time
import random

class SpeedTyping:
    def __init__(self):
        self.sentences = {1: 'Nancy was proud that she ran a tight shipwreck.',
                          2: "If you spin around three times, you'll start to feel melancholy.",
                          3: "He enjoys practicing his ballet in the bathroom.",
                          4: "Whenever he saw a red flag warning at the beach he grabbed his surfboard.",
                          5: "The fact that there's a stairway to heaven and a highway to hell explains life well.",
                          6: "The hummingbird's wings blurred while it eagerly sipped the sugar water from the feeder.",
                          7: "Waffles are always better without fire ants and fleas.",
                          8: "His confidence would have bee admirable if it wasn't for his stupidity.",
                          9: "The manager of the fruit stand always sat and only sold vegetables.",
                          10: "The knives were out and she was sharpening hers."
                          }

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg='green')
        self.window.title('Typing speed test')
        self.intro = Label(text=f'HIGHSCORE: {self.get_highscore()} words per second', bg='green', fg='lightgreen')
        self.intro.grid(column=1, row=0)
        self.logo = Label(self.window, text=logo, font=("Courier", 12), bg='green', fg='lightgreen')
        self.logo.grid(column=0, row=1, columnspan=3)
        self.start_button = Button(text='Start', padx=20, pady=20, bg='lightgreen', fg='green', command=self.start_game)
        self.start_button.grid(column=1, row=3)
        self.start_time = None
        self.end_time = None
        self.user_input= ""
        self.chosen_sentence = ""
        self.amount_words = None
        self.user_input_entry = ""

    def get_highscore(self):
        with open('highscore.txt', 'r') as data:
            highscore = data.read()
        return highscore

    def end_game(self):
        self.end_time = time.time()
        self.user_input_entry = self.user_input.get()
        score_window = Toplevel(self.window)
        score_window.config(padx=20, pady=20, bg='green')
        score = Label(score_window, text=self.calculate_results(start_time=self.start_time,
                                                                end_time=self.end_time), bg='green', fg='lightgreen')
        score.pack()

    def on_enter_key(self, event):
        self.end_game()

    def start_game(self):
        self.start_time = time.time()
        new_window = Toplevel(self.window)
        new_window.config(padx=20, pady=20, bg='green')
        new_window.title('Test started')
        rng = random.randint(1,10)
        label = Label(new_window, text="Press ENTER when finished", bg='green', fg='lightgreen')
        label.grid(column=2, row=1)

        self.chosen_sentence = self.sentences[rng]
        sentence = Label(new_window, text=self.chosen_sentence, font=('Courier', 12), bg='green', fg='lightgreen', padx=10, pady=10)
        sentence.grid(column=1, row=2, columnspan=3)
        self.amount_words = len(self.chosen_sentence.split(' '))

        empty_label = Label(new_window, text= "", bg='green')
        empty_label.grid(column=2, row=4)

        self.user_input = Entry(new_window, bg='lightgreen', width=100, borderwidth=3)
        self.user_input.grid(column=1, row=3, columnspan=3)
        self.user_input.focus()

        finished_button = Button(new_window, text='Finished', bg='lightgreen', fg='green', command=self.end_game)
        finished_button.grid(column=2, row=5)
        self.user_input.bind("<Return>", self.on_enter_key)

    def calculate_results(self, start_time, end_time):
        total_time = round(end_time - start_time)
        correct_sentence = [char for char in self.chosen_sentence]
        test_sentence = [char for char in self.user_input_entry]
        count = 0
        try:
            for i in range(len(correct_sentence)):
                if correct_sentence[i] != test_sentence[i]:
                    count += 1
        except IndexError:
            count += 1
        with open('highscore.txt', 'r') as data:
            highscore = data.read()
            if float(highscore) < round(self.amount_words / total_time, 2):
                with open('highscore.txt', 'w') as data_write:
                    data_write.write(str(round(self.amount_words / total_time, 2)))
        return (f'Total time: {total_time} seconds\n'
                f'Amount of words: {self.amount_words}\n'
                f'Words per second: {round(self.amount_words/total_time, 2)}\n'
                f'Mistakes made: {count}')


speed_typing = SpeedTyping()
speed_typing.window.mainloop()
