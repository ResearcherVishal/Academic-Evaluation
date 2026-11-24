
print("\t---------------------------------------------------------")
print("\tWELCOME TO ADITYA COLLEGE OF ENGINEERING (ACEM), MADANAPALLE")
print("\tAcademic Evaluation:...\n\t\tTheory – 25%,\n\t\t Examinations – 30%,\n\t\t Projects – 35%,\n\t\t Innovative Ideas – 10%.")
print("\t---------------------------------------------------------")
Theory=int(input("\t\t\tTheroy\t: "))
Exam=int(input("\t\t\tExam\t: "))
Project=int(input("\t\t\tProject\t: "))
Idea=int(input("\t\t\tIdea\t: "))
print("\t---------------------------------------------------------")
total_percentage=Theory+Exam+Project+Idea
if total_percentage>100:
    print("\t\tPlease cross check the your provide percentages ")
    print("\t---------------------------------------------------------")
elif total_percentage>=70:
    print("\t\t your eligiable for writen Test for Interview ")
    print("\t---------------------------------------------------------")
    print(" \t\t\twelcome to Python MCQ Test\n")
    print("\t 1 . Who developed Python Programming Language?")
    print("\t\t 1. Wick van Rossum\t2. Rasmus Lerdorf\n\t\t 3.Guido van Rossum\t4.  Niene Stom")
    ans_1=int(input("\tAnswer : ")) #3
    print("\n\t 2 . Which type of Programming does Python support?")
    print("\t\t 1. object-oriented programming\t2. structured programming\n\t\t 3.functional programming\t4.  all of the mentioned")
    ans_2=int(input("\tAnswer : ")) #4
    print("\n\t 3 . Is Python case sensitive when dealing with identifiers?")
    print("\t\t 1.  no\t\t\t2. yes\n\t\t 3.machine dependent\t4.  none of the mentioned")
    ans_3=int(input("\tAnswer : ")) #2
    print("\n\t 4 . Which of the following is the correct extension of the Python file?")
    print("\t\t 1. .python\t\t2. .pl\n\t\t 3. .py\t\t\t4. .p")
    ans_4=int(input("\tAnswer : ")) #3
    print("\n\t 5 . Is Python code compiled or interpreted?")
    print("\t\t 1. Python code is both compiled and interpreted\n\t\t 2. Python code is neither compiled nor interpreted\n\t\t 3. Python code is only compiled\n\t\t 4. Python code is only interpreted")
    ans_5=int(input("\tAnswer : "))#1
    print("\n\t 6 . All keywords in Python are in _________")
    print("\t\t 1. Capitalized\t\t 2. lower case\n\t\t 3. UPPER CASE\t\t 4. None of the mentioned")
    ans_6=int(input("\tAnswer : "))#4
    print("\n\t 7 . What will be the value of the following Python expression?\n\t\t\t\tprint(4 + 3 % 5)")
    print("\t\t 1.  7\t\t 2. 2\t\t 3. 4\t\t 4. 1")
    ans_7=int(input("\tAnswer : "))#1
    print("\n\t 8 .Which of the following is used to define ablock of code in Python language?")
    print("\t\t 1. Indentation\t\t 2. Key\n\t\t 3. Brackets\t\t 4. All of the mentioned")
    ans_8=int(input("\tAnswer : "))#1
    print("\n\t 9 . Which keyword is used for function in Python language?")
    print("\t\t 1. Function\t\t 2. def\t\t 3. Fun\t\t 4. Define")
    ans_9=int(input("\tAnswer : "))#2
    print("\n\t 10 . Which of the following is the truncation division operator in Python?")
    print("\t\t 1. |\t\t 2. //\t\t 3. /\t\t 4. %")
    ans_10=int(input("\tAnswer : "))#2
    print("\n\t----------------------------------------------------------------------------------")
    print("\t\t\t\t Result")
    print("\t------------------------------------------------------------------------------------")
    total_marks=0
    if ans_1==3:
        total_marks+=1
    if ans_2==4:
        total_marks+=1
    if ans_3==2:
        total_marks+=1
    if ans_4==3:
        total_marks+=1
    if ans_5==1:
        total_marks+=1
    if ans_6==4:
        total_marks+=1
    if ans_7==1:
        total_marks+=1
    if ans_8==1:
        total_marks+=1
    if ans_9==2:
        total_marks+=1
    if ans_10==2:
        total_marks+=1
    if total_marks>=6:
        print("\t\t Congratulations on your outstanding achievement!")
        print("\t-----------------------------------------------------------------------------------")
    else:
        print("\t\t\t Butter Luck next Time!")
        print("\t-----------------------------------------------------------------------------------")
        
    

else:
    print("\t\tYour are not eligiable for Writen Test ... ")
    print("\t---------------------------------------------------------")
    print("\t\t\t THANK YOU  ")
    
    
    