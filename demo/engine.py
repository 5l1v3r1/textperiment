#!/usr/bin/env python

import font
import math, os

adjust=lambda x: int(math.floor(x))
sign=lambda x: cmp(x,0) #Python doesn't have this and that's dumb

class context:

  def __init__(self):
    """
    Initializes a work area
    """

    x,y=80,40
    self.grid=[[" " for i in range(x)] for i in range(y)]
    self.xsize=x
    self.ysize=y

  def draw(self):

    self.rectangle(0,0,79,39,"#")
    print "\x1B[1;1H"
    for i in self.grid: print "".join(i)

  def putpixel(self,x,y,char):

    try:
      self.grid[adjust(y)][adjust(x)]=char
    except:
      self.grid[y][x]=char

  def line(self,x0,y0,x1,y1,char):
    
    deltax=x1-x0
    deltay=y1-y0
    if deltax==0:
      for i in range(abs(deltay)): self.putpixel(x0, y0+i*sign(deltay), char) 
    elif abs(deltax)>abs(deltay):
      if x0>x1: x0,y0,x1,y1=x1,y1,x0,y0
      for i in range(abs(deltax)): 
          self.putpixel(x0+i, y0+deltay*i/deltax, char)
    else:
      if y0>y1: x0,y0,x1,y1=x1,y1,x0,y0
      for i in range(abs(deltay)): 
          self.putpixel(x0+deltax*i/deltay, y0+i, char)

  def rectangle(self,x,y,xsize,ysize,char):

    self.line(x,y,x+xsize,y,char)
    self.line(x,y,x,y+ysize,char)
    self.line(x+xsize,y,x+xsize,y+ysize,char)
    self.line(x,y+ysize,x+xsize+1,y+ysize,char)

  def circle(self,x0,y0,rad,char):

    x=rad
    y=0
    radiusError=1-x
   
    while x>=y:
      self.putpixel( x+x0, y+y0,char)
      self.putpixel( y+x0, x+y0,char)
      self.putpixel(-x+x0, y+y0,char)
      self.putpixel(-y+x0, x+y0,char)
      self.putpixel(-x+x0,-y+y0,char)
      self.putpixel(-y+x0,-x+y0,char)
      self.putpixel( x+x0,-y+y0,char)
      self.putpixel( y+x0,-x+y0,char)
      y+=1
      if radiusError<0:
        radiusError+=(2*y+1)
      else:
        x-=1
        radiusError+=(2*(y-x)+1)

  def text(self,x,y,char,string):

    for i in range(7): #Height of the font
      line="".join([eval("font."+letter+"[i]") for letter in string.lower().replace(" ","_").replace("4","D").replace("6","F")])
      for j in range(79-x): #total space left
        try: 
          if line[j]=="#" and x+j>0: self.putpixel(x+j,y+i,char)
        except: pass

  def clear(self):

    self.grid=[[" " for i in range(self.xsize)] for i in range(self.ysize)]

if __name__=="__main__":
  pass