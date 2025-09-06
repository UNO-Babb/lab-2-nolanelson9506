#FutureTime.py
#Name:Nola Nelson
#Date:9/5/25
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) %24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later
  print("Current time: {currentHour}:{currentMinute}")
  #TODO:
  #Ask user for hours
  addHours = int(input("How many hours from now?: "))
  #Ask user for minutes
  addMinutes = int(input("How many minutes from now?"))
  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + addMinutes
  totalHours = currentHour + addHours + (totalMinutes // 60)
  futureMinutes = totalMinutes % 60
  futureHours = totalHours % 24
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"{futureHours:02}:{futureMinutes:02}")

if __name__ == '__main__':
  main()
