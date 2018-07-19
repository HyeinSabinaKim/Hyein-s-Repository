
print "Please select the level of difficulty of the game."
print "Possible choices are easy, medium, and hard. Type in the level."


paragraph_intro = "The current paragraph reads as such:"
level_wrong = "I am sorry, but the written word is not an option. Type again."
easy_paragraph = "Programming language is a formal language that specifies a set of instructions that can be used to produce various kinds of output. In Intro to Programming course, we first learned html, which enable the user to make webpage. We are now learning python, which is famous for its code readability and the fact that it allows beginners to learn programming easily."
medium_paragraph = "Python is a programming language which was first implemented in 1989. There are several statements in python. If statement executes a block of code conditionally. Also there are loop statements; for-loop statement iterates over elements in the list, and executes the block of code for each element. Additionally, while-loop statement executes a block of code as long as its condition is true.Python is a programming language which was first implemented in 1989. There are several statements in python. If statement executes a block of code conditionally. Also there is for-loop statement, which iterates over elements in the list, and executes the block of code for each element. Lastly, there is also while-loop statement, which executes a block of code as long as its condition is true."
hard_paragraph = "In Intro to Programming Nanodegree course, we learned several functions in Python. First of all, in terms of functions related with strings, there was find statement, which led the user to find the location of a substring in a string. Next, we also learned while-loop statement. It enabled us to repeat a particular process over and over again until the defined condition is no longer met. Last, but not least, we could also use the len statement to measure the length of a string.With regards to lists, append statement adds new elements to the existing list. Also, for-loop statement iterates over the members of elements in the string. The difference between while-loop and for-loop is that for-loop is used when a condition needs to be checked each iteration in contrast to while-loop, which is used to repeat the block of code forever while the condition is met. Finally, index statement is used when the user wants to find the location of an element in the list."

easy_answer = ["programming", "language", "html", "python"]
medium_answer = ["programming", "if", "for", "while"]
hard_answer = ["find", "while", "len", "append", "for", "index"]        

paragraph = [easy_paragraph, medium_paragraph, hard_paragraph]
answer = [easy_answer, medium_answer, hard_answer]
quiz_level = ["easy", "medium", "hard"]

# question(number) function makes the blank with the question number in it.
# input : question number
# output : "__question number__"
def question(number):
    return "__" + str(number) + "__"

# question_remark(number) function makes the question line with the next question's number in it.
# input : question number
# output : "What should be substituted in for __next question's number__ ?"
def question_remark(number):
    return "What should be substituted in for" + question(number+1) + "?"

# wrong_paragraph(trys_left) functions gives the line that says the user wrote the wrong answer.
# input : number of trys left
# output : "This is not a correct answer. Try again; you have 'number of trys left' trys left!"
def wrong_paragraph(trys_left):
        return "[-] This is not a correct answer. Try again; you have " + str(trys_left) + " trys left!\n\n" 
right_paragraph = "[+] Correct!\n\n"


# This process tells the users to write the proper game level. 
# The game level should be among 'easy', 'medium', and 'hard'.
# By the list 'quiz_level', 'easy' level would turn into 'level_number' as 1, 'medium' as 2, 'hard' as 3. 
def level_intro():
    user_input = raw_input()
    while user_input not in quiz_level:
        print level_wrong
        user_input = raw_input()
    if user_input in quiz_level:
        level = user_input
        global level_number
        level_number = quiz_level.index(level)
        print paragraph_intro
        
# This function exists in order to limit the trials to 5 times.        
def right_wrong():
    trials = 5
    while trials > 0:
        print "Input : "
        submit = raw_input()
        trials = trials-1
        global replaced
        replaced = ""
        # Lowering the answer was needed to make searching answers easier.
        global answer_element
        if submit.lower() == answer_element:
            # This shows that the user wrote the right answer.
            print right_paragraph
            paragraph_split()
            break
            print "\n\n\n[+] Congratulations!! -by Hyein"
        else:
            print wrong_paragraph(trials)
    if trials == 0:
       quit()   


# This function shows user the paragraph with the blanks inside.  
# Making the original paragraph in lower cases was needed for finding the word at once in order to change it as a blank.
def paragraph_blank():
    lower_paragraph = paragraph[level_number].lower()
# This process is to find the answers and change them into blanks. 
# Adding 1 to the number was needed because the index function starts with 0, whereas the question number starts with 1.
    global answer_element
    for answer_element in answer[level_number]:
        lower_paragraph = lower_paragraph.replace(answer_element, question(answer[level_number].index(answer_element) + 1))
    print lower_paragraph + "\n"
    for answer_element in answer[level_number]:
        # This print statement shows the question after the paragraph with blanks.
        print question_remark(answer[level_number].index(answer_element)) + "\n"
        # n shows the trials left for users
        right_wrong()
        


# This function shows the paragraph of which the blank is filled with the right answer. 
# First, we split the paragraph. Second, we exclude the previous answer from the answer list.
# Third, if the answer starts with the answer element in the answer list(that is, the user input includes upper case,
# make the word as lower case. Else, we can use the user input just as it is.
def paragraph_split():
    for word in paragraph[level_number].split():
        for answer_element2 in answer[level_number][((answer[level_number].index(answer_element))+1):]:
            if word.lower().startswith(answer_element2) == True:
                word = word.lower()
            else:
                word = word
                # This process makes the 'replaced' longer as the word is added.
        global replaced
        replaced = replaced + word + " "
        # This process makes blanks for the remaining questions.
        for answer_element2 in answer[level_number][((answer[level_number].index(answer_element))+1):]:
            replaced = replaced.replace(answer_element2, question(answer[level_number].index(answer_element2) + 1))
    print replaced    



                


level_intro()
paragraph_blank()
               




