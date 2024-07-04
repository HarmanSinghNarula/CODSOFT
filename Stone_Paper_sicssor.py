import random
game=['Rock','Paper','Scissor'] # i creted a set here and while i choose random it denied so sets dont perform random.choice() as well
print("Welcome to the game of Stone Paper Scissor,You will b competing against the computer!")

score1=0
score2=0
while score1<5 and score2<5:
 p1=str(input("Choose one odf three options from above,"))
 comp=random.choice(game)
 if p1==comp:
  print('Tie, try again')
 elif p1=='Rock' and comp=='Paper':
 
  print('p1 wins')
  score1+=1
 elif p1=='Paper' and comp=='Rock':
  print('comp wins')
  score2+=1
 elif p1=='Rock' and comp=='Scissor':
  print('p1 wins')
  score1+=1
 elif p1=='Scissor' and comp=='Rock':
  print('comp wins')
  score2+=1
 elif p1=='Paper' and comp=='Scissor':
  print('p1 wins')
  score1+=1
 elif p1=='Scissor' and comp=='Paper':
  print('comp wins')
  score2+=1
  
if score1==5:
   print('p1 winssssssssssss')
  
else:
   print('comp winssssssssss')