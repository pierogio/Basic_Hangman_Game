import random

class GetRandomWord:
    def __init__(self):
        self.words = ["pepe", "casa", "padre", "marido", "mujer", "hombre"]
      
    def get_word(self):
        return random.choice(self.words)
class Hangman:
    def __init__(self , word, max_attempts):
        self.word = word
        self.guessed = []
        self.max_attempts = max_attempts

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed:
            print("You guessed the letter!")
            self.guessed.append(letter)
        elif letter in self.guessed:
            print("You already guessed that letter")
            self.max_attempts -= 1  
        else:
            print("You guessed wrong!")
            self.max_attempts -= 1   
           
    def get_status(self, letter):
        print("Guess the word:")
        for letter in self.word:
            if letter in self.guessed:
                print(letter, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        return set(self.word) == set(self.guessed)


class Game:
    def __init__(self):
        self.word = GetRandomWord().get_word()
        max_attempts = len(self.word)
        self.hanged = Hangman(self.word, max_attempts)

    def start (self):
        while not self.hanged.check_if_player_won() and self.hanged.max_attempts > 0:
            letter = input("Write a letter: ")
            self.hanged.get_status(letter)
            self.hanged.guess(letter)
            print(f"Attempts left: {self.hanged.max_attempts}")
            if self.hanged.check_if_player_won():
                print(f"You won! The word was: {self.word}")
            elif self.hanged.max_attempts == 0:
                print(f"You lost! The word was: {self.word}")


if __name__ == "__main__":
    game = Game()
    game.start()