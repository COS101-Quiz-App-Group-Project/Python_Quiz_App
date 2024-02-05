import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


# Function the display the current question and its answer choices
def show_question():
    # Get the current question from quiz_data
    question = quiz_data[current_question]

    # Update the question from quiz_data
    qs_label.config(text=question["question"])

    # Get answer choices for the current question
    choices = question["choices"]
    # Update the text of each choice button with the answer choices
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    # Reset feedback label and disable the "Next" button
    feedback_label.config(text="")
    next_btn.config(state="disabled")
def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")


