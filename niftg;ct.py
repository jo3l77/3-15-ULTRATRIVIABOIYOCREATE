# Football Quiz; Create Task
print("This is a quiz that tests your knowledge on football(American).")
name = input("Enter your name: ")
print("Hi there, {}!".format(name))

while True:
    print("")
    print("In this quiz, there are 3 levels you need to beat in order to pass. I will ask you 5 questions each round and give you three choices.")
    print("______________")
    print("Select the correct answer out of choices A, B, or C for each question. The questions will get continuously more difficult as you beat each level.")
    print("______________")
    print("To advance to the next level, you need to score at least a 3 out of 5 in the level that you're on.")
    print("______________")
    print("You are allowed 2 hints per round. After every hint that you use, you will lose a point in your final score. So be careful!")
    print("Are you ready? Good luck, {}!".format(name))
    print("______________")

    # set the score of the quiz to 0

    score = 0
    score = int(score)

    # Question 1
    print("Question 1: How many points does a player score when they get a touchdown? \n")
    print("A. 6")
    print("B. 7")
    print("C. 3")
    print("")

    Q1answer = "A" # the right answer to question 1
    Q1response = input("Your answer:")
    if Q1response == "A" or Q1response == 'a':
        print("Correct!", Q1answer)
        score = score + 1
    elif Q1response != "A" or Q1response != 'a':
        print("Sorry, that is incorrect.")
        print("The correct answer is:",Q1answer, ".")
        score = score
    print("")    
    print("Current Score:", score, "out of 5.")
    print("")
    print("Next Question.")
    print("")

    # Question 2
    print("Question 2: How many teams exist in the NFL? \n")
    print("A. 25")
    print("B. 30")
    print("C. 32")
    print("")

    Q2answer = "C" #the right answer to question 2
    Q2response = input("Your answer:")
    if Q2response == "C" or Q2response == 'c':
        print("Correct!", Q2answer)
        score = score + 1
    elif Q2response != "C" or Q2response != 'c':
        print("Sorry, that is incorrect.")
        print("The correct answer is:",Q2answer, ".")
        score = score
    print("")
    print("Current Score:", score, "out of 5.")
    print("")
    print("Next Question.")
    print("")

    # Question 3
    print("Question 3: How many weeks are there in an NFL season(excluding playoffs)? \n")
    print("A. 10")
    print("B. 17")
    print("C. 16")
    print("")

    Q3answer = "B" #the right answer to question 3
    Q3response = input("Your answer:")

    if Q3response == "B" or Q3response == 'b':
        print("Correct!", Q2answer)
        score = score + 1
    elif Q3response != "B" or Q3response != 'b':
        print("Sorry, that is incorrect.")
        print("The correct answer is:",Q3answer, ".")
        score = score
    print("")
    print("Current Score:", score, "out of 5.")
    print("")
    print("Next Question.")
    print("")

    # Question 4
    print("Question 4: When a pass is thrown by a quarterback but is caught by the other team, what has happened? \n")
    print("A. A touchdown")
    print("B. An incomplete pass")
    print("C. An interception")
    print("")

    Q4answer = "C" #the right answer to question 4
    Q4response = input("Your answer:")

    if Q4response == "C" or Q4response == 'c':
        print("Correct!", Q4answer)
        score = score + 1
    elif Q4response != "C" or Q4response != 'c':
        print("Sorry, that is incorrect.")
        print("The correct answer is:",Q4answer, ".")
        score = score
    print("Current Score:", score, "out of 5.")
    print("")
    print("Next Question.")
    print("")

    # Question 5
    print("Question 5: Which two teams participated in the Super Bowl this year? \n")
    print("A. Philadelphia Eagles and New England Patriots")
    print("B. New York Giants and New England Patriots")
    print("C. Green Bay Packers and Pittsburgh Steelers")
    print("")

    Q5answer = "A" #the right answer to question 5
    Q5response = input("Your answer:")

    if Q5response == "A" or Q5response == 'a':
        print("Correct!", Q5answer)
        score = score + 1
    elif Q5response != "A" or Q5response != 'a':
        print("Sorry, that is incorrect.")
        print("The correct answer is:",Q5answer,".")
        score = score
    print("Current Score:", score, "out of 5.")
    print("")
    
    if score >= 3 and  score < 5:
        print("Great Job, {}!".format(name),"You passed this round with a score of {}!".format(score))
        print("")
        print("Now you will move on to Round 2.")
    if score == 5:
        print("Amazing, {}!".format(name), "You're a regular football fiend! You passed this round with a score of", score, "out of 5!")
        print("")
        print("Now you will move on to Round 2 of the quiz.")

    elif score <2:
        print("Sorry, {}.".format(name), "You have failed the quiz with a score of", score,"out of 5")
    
    retake = input("Would you like to take the quiz again? Y/N?:")
    if retake == "Y" or retake == 'y':
        continue
    elif retake != "Y" or retake != 'y':
        break
