
#Quiz game

questions = ("Koliko elementov je v periodnem sistemu?: ",
             "Katera žival izleže najvelje jajce?: ",
             "Najbolj obilen plin v zemeljski atmosferi?: ",
             "Koliko je kosti v človeškem telesu?: ",
             "Kateri planet v sistemu, je najtoplejši?: ")


options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Kit", "B. Krokodil", "C. Slon", "D. Noj" ),
           ("A. Dušik", "B. Kisik", "C. co2", "D. Vodik"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Merkur", "B. Venera", "C. Zemlja", "D. Mars"))



answers = ("C", "D" ,"A" , "A" , "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------")
    print (question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (a, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num].upper():
        score += 1
        print("Pravilno!")
    else:
        print("nepravilno!")
        print(f"{answers[question_num]} je pravilni odgovor")

    question_num += 1
    print()

percent = (score / len(questions)) * 100

print("----------------------------------------")
print("---------------REZULTAT-----------------")
print("----------------------------------------")
print(f"Pravilnih je bilo {score}/5 odgovorov!")
print(f"Kar znaša {percent}% pravilnih odgovorov.")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
