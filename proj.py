from win10toast import ToastNotifier
import time
import threading
from datetime import datetime

def schedule_notification(scheduled_time, message):
  # create a ToastNotifier object
  notifier = ToastNotifier()
  # get the current time in seconds
  current_time = time.time()

  # convert the scheduled time to seconds
  scheduled_time = time.strptime(scheduled_time, "%Y-%m-%d %H:%M:%S")
  scheduled_time_in_seconds = time.mktime(scheduled_time)
  # calculate the delay (in seconds)
  delay = scheduled_time_in_seconds - current_time

  # if the scheduled time has already passed, add a day (86400 seconds) to the delay
  if delay < 0:
    # delay += 86400
    print("You can not schedule notifications of the passed time. ")
    return 0

  # schedule the notification
  timer = threading.Timer(delay, notifier.show_toast, ["Title", message])
  # timer.daemon = True
  timer.start()

n = int(input("Enter number of notifications do you want to generate? "))
for i in range(n):
  msg = input("Enter message which do you want to show in message? ")
  dateTime = ""
  hasNotDoneValidation = True
  while hasNotDoneValidation:
    try:
      dateTime = input("Enter the date and time at which you want to generate notification? ")
      format = "%Y-%m-%d %H:%M:%S"
      obj = datetime.strptime(dateTime,format)
      hasNotDoneValidation = False
    except ValueError:
      print("Invalid date")
  schedule_notification(dateTime, msg)