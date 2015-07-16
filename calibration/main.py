#!/usr/bin/env python

import math, os, subprocess, sys, time, traceback
import effects as ef, engine
adjust=lambda x: int(math.floor(x))
c=engine.context()
startdate=time.time()*1000
beat=0
cycle=subcycle=1
test=0
# test=1

def loop(step):

  ef.meatballs(c,step)
  if beat%2: c.text(4,10,".","UNTZ")
  else: c.text(15,30,".","UNTZ")

def updatebeat():
  global beat
  beat=adjust((time.time()*1000-startdate)/326)
  # Remove this for release :D
  print beat,"/",cycle,"/",subcycle
  return beat

def main():
  global cycle
  subprocess.Popen(["bash", "audio.sh"])
  while 1:
    c.clear()
    beat=updatebeat()
    loop(cycle)
    #cycle+=1
    cycle=adjust((time.time()*1000-startdate)/25)
    c.draw()
    time.sleep(1/15)#30

if __name__=="__main__":
  try: main()
  except: 
    os.system('clear')
    traceback.print_exc()
