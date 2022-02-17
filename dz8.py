#Игра Paper, Rock, Lizard, Spock, Scissors
#Игра должна записывать данные статистики в текстовый файл (пронумерованный список: дата и время, кто выиграл, что выбросили).


import sys
import random
from venv import create
from webbrowser import open_new
score_u=0
score_c=0
games=0
wins=0
loses=0
while True:
  games=games+1
  u_ch=5
  c_ch=random.randint(0,4)
  while(u_ch!=0 and u_ch!=1 and u_ch!=2 and u_ch!=3 and u_ch!=4):
    u_ch=int(input("Enter paper, rock, lizard, spock, scissors (0, 1, 2, 3, 4):"))
  print(c_ch)
  if u_ch==c_ch:
    print("Draw")
    continue
  
  if u_ch>c_ch:
    if (u_ch-c_ch)%2:
      score_u=score_u+1
    else:
      score_c=score_c+1
  else:
    if (u_ch-c_ch)%2:
      score_u=score_u+1
    else:
      score_c=score_c+1
  
  if score_u>=2:
    wins=wins+1
    print("You win!")
    choose=0
    while(choose!='y' and choose!='n'):
      choose=input("Do you want play more(y/n)? ")
    if choose=='y':
      score_c=0
      score_u=0
      continue
    elif choose=='n':
      break
    else:
      print("Error")
      break
    
  if score_c>=2:
    loses=loses+1
    print("You lose!")
    choose=0
    while(choose!='y' and choose!='n'):
      choose=input("Do you want play more(y/n)? ")
    if choose=='y':
      score_c=0
      score_u=0
      continue
    elif choose=='n':
      break
    else:
      print("Error")
      break
  print("score_u: "+ str(score_u))
  print("score_c: "+ str(score_c))  
print("score_u: "+ str(score_u))
print("score_c: "+ str(score_c))  
print("games:"+str(games))
print("wins/loses:" + str(wins)+ "/"+str(loses))




sys.stdout=open("new 1.txt","w")
print("score_u: "+ str(score_u))
print("score_c: "+ str(score_c))  
print("games:"+str(games))
print("wins/loses:" + str(wins)+ "/"+str(loses))
sys.stdout.close()