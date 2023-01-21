import tkinter as tk

# list of questions and answers
questions = [
    {"question": " 1. M -> N \n 2. M -> O / M -> (N ^ O)", "answer": "~M v N 1 Impl"},
    {"question": "1. M -> N \n 2. M -> O / M -> (N ^ O) \n 3. ~M v N                     1 Impl", "answer": "~M v O 2 Impl"},
    {"question": "1. M -> N \n 2. M -> O / M -> (N ^ O) \n 3. ~M v N                     1 Impl \n 4. ~M v O                     2 Impl ", "answer": "(~M v N) ^ (~M v O) 3,4 Conj"}
]

# index of the current question
current_question = 0

def check_answer():
    global current_question
    user_answer = input_field.get()
    if user_answer.lower() == questions[current_question]["answer"].lower():
        current_question += 1
        if current_question == len(questions):
            label.config(text="You've answered all the questions!")
            button.config(state="disabled")
        else:
            label.config(text=questions[current_question]["question"])
            input_field.delete(0, 'end')
    else:
        label.config(text="Incorrect, try again")

app = tk.Tk()
app.title("Quiz")

label = tk.Label(app, text=questions[current_question]["question"])
label.pack()

input_field = tk.Entry(app)
input_field.pack()

button = tk.Button(app, text="Submit", command=check_answer)
button.pack()

app.mainloop()
