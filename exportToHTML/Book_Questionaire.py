######################################################################
# Author(s): Ariana Meatchem
# Username(s): Meatchema
#
# Assignment: Book Recommendation Quiz
#
# Purpose: Create a program that gives specific book recommendations
######################################################################

import random
import json
def ask_questions():
    print("\nWelcome to Ace's Book Recommendation Quiz!\nAnswer the following questions to receive a Book suggestion.\n")
    questions = {
        "Genre": "What genre of book do you prefer? (action, rom-com, fantasy, dark academia, manga) ",
        "Amount": "Do you prefer Standalones or Series?"
    }
    responses = {}
    for key, questions_text in questions.items():
        responses[key] = input(questions_text).strip().lower()

    return responses

def recommend_book(responses):
    """Recommend a game based on the user's responses."""
    Genre = responses.get("Genre")
    Amount = responses.get("Amount")

    if Genre == "dark academia" and Amount == "Standalones":
        return "Babel"
    elif Genre == "fantasy" and Amount == "Standalones":
        return "The Song of Achilles"
    else:
        return "The Train from Platform 2"

def main():

    name = input("Hello, whats your name?:")
    print(f"Hello, {name}!")
    responses = ask_questions()
    recommendation = recommend_book(responses)
    print(f"\n🎮 Based on your answers, we recommend: {recommendation} 🎮\n")




if __name__ == "__main__":
    main()