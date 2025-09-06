#Magic8Ball.py
#Name:Nola Nelson
#Date:9/5/25
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ("Yes", "No", "Definitely", "For sure", "Most likely", "Outlook not so good",
"Try again", "Don't count on it")
  #Answer question randomly with one of the options from your earlier list.
r = random.choice(answers)
print(r)
input("What is your question?: ")
if __name__ == '__main__':
  main()
