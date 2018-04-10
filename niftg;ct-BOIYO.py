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
        print("The correct answer is:",Q5answer, ".")
        score = score
    print("Current Score:", score, "out of 5.")
    print("")
    
    if score <2:
        print("Sorry,{}.".format(name), "You have failed the quiz with a score of", score,"out of 5")
        print("Now you will move on to Round 2 of the quiz.")
    if score >= 3 and  score < 5:
        print("Great Job, {}!".format(name),"You passed this round with a score of {}!".format(score))
    if score = 5:
        print("Amazing, {}!".format(name), "You're a regular football fiend! You passed this round with a score of", score, "out of 5!")
  
    
    retake = input("Would you like to take the quiz again? Y/N?:")
    if retake == "Y" or retake == 'y':
        continue
    elif retake != "Y" or retake != 'y':
        break
'''


    # Round 2:

    #Question 1
    print("Question 1: How many minutes in one quarter of a football game? \n")
    print("A. 90 minutes")
    print("B. 12 minutes")
    print("C. 15 minutes")
    print("")

    # Question 2
    print("Question 2: How does a football game commence? \n")
    print("A. With a Coin Toss")
    print("B. With a Kickoff")
    print("C. With the away team snapping ball at their 20 yard line")
    print("")

    # Question 3
    print("Question 3: What football franchise currently hold the most SuperBowl championship wins? \n")          
    print("A. Dallas Cowboys")
    print("B. New England Patriots")
    print("C. Pittsburgh Steelers")
    print("")

    # Question 4
    print("Question 4: What is the term used to refer to an infraction committed by a team? \n")
    print("A. Foul")
    print("B. Red Card")
    print("C. Penalty/flag")
    print("")

    # Question 5
    print("Question 5: What is the name of the coach of the New England Patriots? \n")
    print("A. Bill Belichick")
    print("B. John Madden")
    print("C. Tom Brady")
    print("")

    # Round 3:
    
    # Question 1
    print("Question 1: What is the maximum amount of players allowed on the field at a time for both offense and defense? \n")
    print("A. 5")
    print("B. 11")
    print("C. 15")
    print("")

    # Question 2
    print("Question 2: Where is the football Hall of Fame located? \n")
    print("A. Canton, Ohio")
    print("B. Cooperstown, New York")
    print("C. Springfield, Massachusetts")
    print("")

    # Question 3
    print("Question 3: How many offensive linemen are on the field during an offensive playcall? \n")
    print("A. 10)
    print("B. 5)
    print("C. 9)
    print("")

    # Question 4
    print("Question 4: Which one of these 3 numbers can a wide receiver in the NFL wear? \n")
    print("A. 11")
    print("B. 1")
    print("C. 90")
    print("")

    # Question 5
    print("Question 5: When was the last time the Cleveland Browns won an NFL game? \n")
    print("Week 17: 2017")
    print("Week 16: 2016")
    print("3 whole football seasons ago")
    print("")
'''
