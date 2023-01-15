name = input("Enter your name: ")

print ("Welcome " + name + "!!" + " " + "Please do put specific answers" + "\n" + "Example: ~M v N 1 Impl" + "\n")

questions = [
    {
        "question": " 1. M -> N \n 2. M -> O / M -> (N ^ O)",
        "answer": "~M v N 1 Impl"
    },
    {
        "question": " 1. M -> N \n 2. M -> O / M -> (N ^ O) \n 3. ~M v N      1 Impl",
        "answer": "~M v O 2 Impl"
    },
    {
        "question": " 1. M -> N \n 2. M -> O / M -> (N ^ O) \n 3. ~M v N        1 Impl \n 4. ~M v O      2 Impl ",
        "answer": "(~M v N) ^ (~M v O) 3,4 Conj"
    },
    {
        "question": " 1. M -> N \n 2. M -> O / M -> (N ^ O) \n 3. ~M v N        1 Impl \n 4. ~M v O      2 Impl \n 5. (~M v N) ^ (~M v O)       3,4 Conj",
        "answer": "~M v (N ^ O) 5 Dist"
    },
    {
        "question": " 1. M -> N \n 2. M -> O / M -> (N ^ O) \n 3. ~M v N        1 Impl \n 4. ~M v O      2 Impl \n 5. (~M v N) ^ (~M v O)       3,4 Conj \n 6. ~M v (N ^ O)        5 Dist",
        "answer": "M -> (N ^ O) 6 Impl"
    }
]

score = 0
mistakes = 0

for question in questions:
    user_answer = input(question["question"] + "\n" + "Answer: ")
    if user_answer.lower() == question["answer"].lower():
        score += 1
        print("======================")
        print("\n" + "Correct!" + "\n" + "Current Score: " + str(score) + "\n")
        print("======================")
    else:
        print("Incorrect. The correct answer is " + question["answer"])

print(name + "" + "You scored " + str(score) + " !!! " + "\n" + "Enter stage 2" )

questions2 = [
    {
        "question": " 1.~A      / A -> B",
        "answer": "~A v B 2 Add"
    },
    {
        "question": " 1.~A      / A -> B \n 2. ~A v B      2 Add",
        "answer": "A -> B 2 Impl"
    }
]

for question in questions2:
    user_answer = input(question["question"] + "\n" + "Answer: ")
    if user_answer.lower() == question["answer"].lower():
        score += 1
        print("======================")
        print("\n" + "Correct!" + "\n" + "Current Score: " + str(score) + "\n")
        print("======================")
    else:
        print("Incorrect. The correct answer is " + question["answer"])

print(name + "You scored " + str(score) + " !!! " )