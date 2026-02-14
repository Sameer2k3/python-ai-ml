#create a program capable to diaplay questions to the user like the kbc
questions=["which language is used to create facebook","cpp","pyhton","js","rust"],


levels=["1000",2000,3000,5000,10000,20000,40000,80000,160000,320000]

for i in  range(0,len(questions)):
    question=questions[i]
    print(f"question for rs.{levels[i]} is:::: {question[i]}:")
    print(f"a.{question[1]}           b.{question[2]}")
    print(f"c.{question[3]}           d.{question[4]}")
    reply=int(input("enter the correct option"))
    if(reply==3):
        print(f"correct answer you have won {levels[i]}")
    else:
        print("wrong answer")
        break
      
  