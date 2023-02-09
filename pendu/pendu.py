import random
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hangman")

font = pygame.font.Font(None, 32)

with open("mots.txt", "r") as file:
    words = file.readlines()
    words = [word.strip() for word in words]

word = random.choice(words)
display_word = "-" * len(word)
incorrect_guesses = 0
max_incorrect_guesses = 7

images = []
for i in range(6):
    image = pygame.image.load("pendu{}.jpg".format(i))
    images.append(image)

menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "1":
                menu = False
            elif event.unicode == "2":
                new_word = input("Enter a new word: ")
                with open("mots.txt", "a") as file:
                    file.write(new_word + "\n")
                print("Word added to the file.")

    screen.fill((255, 255, 255))
    text = font.render("1. Play", True, (0, 0, 0))
    screen.blit(text, (250, 200))
    text = font.render("2. Add word", True, (0, 0, 0))
    screen.blit(text, (250, 250))

    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            letter = event.unicode.lower()
            if letter in word:
                new_display_word = ""
                for i in range(len(word)):
                    if word[i] == letter:
                        new_display_word += letter
                    else:
                        new_display_word += display_word[i]
                display_word = new_display_word
            else:
                incorrect_guesses += 1

    screen.fill((255, 255, 255))
    if incorrect_guesses > 0 and incorrect_guesses <= len(images):
        screen.blit(images[incorrect_guesses - 1], (400, 100))
    text = font.render(display_word, True, (0, 0, 0))
    screen.blit(text, (250, 200))

    if "-" not in display_word:
        text = font.render("You win!", True, (0, 0, 0))
        screen.blit(text, (250, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False
    elif incorrect_guesses == max_incorrect_guesses:
        text = font.render("You lose!", True, (0, 0, 0))
        screen.blit(text, (250, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()

pygame.quit()
