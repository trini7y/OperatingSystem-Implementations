import random
import time
import threading


class Philosopher(threading.Thread):
  running = True
  def __init__(self,  forkOnLeft, forkOnRight, nameOfPhilosopher):
    threading.Thread.__init__(self)
    self.name = nameOfPhilosopher
    self.forkOnRight = forkOnRight
    self.forkOnLeft = forkOnLeft
 
#Process is running
  def run(self):
    while self.running:
      time.sleep(random.uniform(3, 13))
      print ("%sis hungry" % self.name)
      self.dine()
  #Get Chopsticks 
  def dine(self):
    fork1, fork2 = self.forkOnLeft, self.forkOnRight
    while self.running:
      fork1.acquire(True)
      #the process will be blocked until acquires the lock
      locked = fork2.acquire(False)
      #the process will not be blocked if no lock is acquired
      if locked:
        break
        # if both forks acquired, quit
      fork1.release()
      fork1, fork2 = fork2, fork1
    else:
      return
    self.dining()
    fork2.release()
    fork1.release()
    # Philosophers have started dinning
  def dining(self):
    print ("%s starts eating " % self.name)
    time.sleep(random.uniform(1, 10))
    print ("%s finished eating and goes back to thinking" % self.name)

def DiningPhilosophers():
  forks = [threading.Lock() for i in range(5)]
  philosopherNames = ["Alade", "Mulika", "Daniel", "Boniface", "Gilbert"]
  philosophers = [Philosopher(forks[i%5], forks[(i+1)%5], philosopherNames[i]) for i in range(5)]
  random.seed(507129)
  Philosopher.running = True
  for philosopher in philosophers:
    philosopher.start()
  time.sleep(100)
  Philosopher.running = False
  print ("Now we are done")

if __name__ == "__main__":
  DiningPhilosophers()
