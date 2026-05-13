# -----------------------------------------------------------------
# Program: wordle_solver.py
# Author: Arnav Kothekar
# Created: 2025-05-29
# Description:
#   Interactive Wordle solver that takes your previous guesses and
#   feedback to suggest the next best word from the allowed list.
# -----------------------------------------------------------------

# Credits to M Somervile (dracos) for Wordle valid words list:
# https://gist.github.com/dracos


# =========================
# Standard Library Imports
# =========================

# (No external imports needed)


# =========
# Constants
# =========

# (No constants defined)


# =========================
# Helper Functions
# =========================


# Input: filename string | Processing: read and filter 5-letter words | Output: list of valid words
def load_words(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [w.strip().lower() for w in f if len(w.strip()) == 5]


# Input: guess and answer strings | Processing: compare letters for feedback | Output: feedback list
def comparison(guess: str, answer: str) -> list[str]:
    global feedback
    feedback = ["-", "-", "-", "-", "-"]
    remaining = []
    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = "G"
        else:
            remaining.append(answer[i])
    for i in range(5):
        if feedback[i] == "-" and guess[i] in remaining:
            feedback[i] = "Y"
    print(feedback)
    return feedback


# Input: guess, feedback, greens, yellows, grays | Processing: update constraints based on feedback | Output: updated constraints
def update_constraints(
    guess: str,
    feedback: list[str],
    greens: list[str | None],
    yellows: dict[str, set[int]],
    grays: set[str]
) -> None:
    for i in range(5):
        letter = guess[i]
        if feedback[i] == "G":
            greens[i] = letter
        elif feedback[i] == "Y":
            yellows.setdefault(letter, set()).add(i)
        elif feedback[i] == "-":
            if letter not in greens and letter not in yellows:
                grays.add(letter)


# Input: word, greens | Processing: check if word matches green positions | Output: boolean
def matches_greens(w: str, greens: list[str | None]) -> bool:
    for i in range(5):
        if greens[i] is not None and w[i] != greens[i]:
            return False
    return True


# Input: word, yellows | Processing: check yellow constraints | Output: boolean
def matches_yellows(w: str, yellows: dict[str, set[int]]) -> bool:
    for letter, banned in yellows.items():
        if letter not in w:
            return False
        if any(w[pos] == letter for pos in banned):
            return False
    return True


# Input: word, grays | Processing: check gray constraints | Output: boolean
def matches_grays(w: str, grays: set[str]) -> bool:
    return not any(letter in w for letter in grays)


# Input: words, constraints | Processing: filter candidates | Output: filtered list
def filter_candidates(
    words: list[str],
    greens: list[str | None],
    yellows: dict[str, set[int]],
    grays: set[str]
) -> list[str]:
    return [
        w for w in words
        if matches_greens(w, greens) and
           matches_yellows(w, yellows) and
           matches_grays(w, grays)
    ]


# =========================
# Main Program
# =========================


# Initialization
greens = [None, None, None, None, None]
yellows = {}
grays = set()
word_list = load_words("wordle_valid_words.txt")
attempt = 0
guess = "audio"


# Input: user input | Processing: validate 5-letter word | Output: valid answer
while True:
    answer = input("Enter the 5 letter answer: ")
    answer = answer.lower()
    if answer not in word_list or len(answer) != 5:
        print("Answer is not a valid Wordle word.")
        continue
    break


# Main Loop
while True:
    attempt += 1
    print(f"\nGuess #{attempt}:")
    print(list(guess))
    feedback = comparison(guess, answer)

    if feedback == ["G"] * 5:
        print(f"\nFound it in {attempt} guesses!")
        break

    update_constraints(guess, feedback, greens, yellows, grays)
    cands = filter_candidates(word_list, greens, yellows, grays)
    print(f"{len(cands)} possible words remain...")

    guess = cands[0]


# Formatted by pycleaner agent May 12, 2026 12:00:00
# Formatted by pycleaner agent May 12, 2026 12:01:00