import time
import threading

def calc_square(numbers):
   print("Calculate square numbers: ")
   for n in numbers:
      time.sleep(0.2)   #artificial time-delay
      print('square: ', str(n*n))
	  
def calc_cube(numbers):
   print("Calculate cude numbers: ")
   for n in numbers:
      time.sleep(0.2)
      print('cube: ', str(n*n*n))
	  
	  
arr = [2,3,8,9]
t = time.time()

t1 = threading.Thread(target = calc_square,args=(arr,))
t2 = threading.Thread(target = calc_cube,args=(arr,))
# creating two threads here t1 & t2

t1.start()
t2.start()
# starting threads here parallelly by usign start function.

t1.join()
# this join() will wait until the cal_square() function is finised.
t2.join()
# this join() will wait unit the cal_cube() function is finised.

print("Successed!")