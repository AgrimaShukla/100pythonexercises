# Progressive Time Printer with Threshold
import time
i = 0
while True:
    if i <= 3:
        print("Hello")
        i = i + 1
        time.sleep(i)
    else:
         print("End of loop")
         break