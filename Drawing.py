#Bisrat Asefaw

#section 03

# CSC 110

# 04/25/2018

# program that draws a boy and girl with a car 

# given that any reference poin is provided
#i use x and y for all three of my scene elements
#reference points.



import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function definition section

# all parameters have units of pixels


# draws one girl. the parameters x and y specify
# the location of the points at the center of the girls dress
#the last parameter is the size of the girl
#from bottom to top of her scene.
# calling this function whenever necessary to draw a gril.


def draw_a_girl(x,y,size,color):
    unit=size//7
    #draw head of girl circle
    point_y2=y+4*unit
    canvas.circle([x,point_y2],unit,fill='yellow')
    #draw polygon of body of girl triangle
    point_x1=x+2*unit
    point_x2=x-2*unit
    point_y1=y+3*unit
    canvas.polygon([[point_x2,y],[point_x1,y],[x,point_y1]],fill=color)
    #draw legs
    point_x3=x-unit
    point_y3=y-2*unit
    point_x4=x+unit
    point_y4=y-2*unit
    canvas.line([[point_x3,y],[point_x3,point_y3]],fill='black')
    canvas.line([[point_x4,y],[point_x4,point_y4]],fill='black')

    
# function that used to draw a boy by calling many times to
#draw a boy. parameters are x and y since they are local variable they
#belongs to the function definition they are assigned.


def draw_a_boy(x,y,size):
    unit=size/9
    #draw head of the boy circle
    point_y1=y+6*unit
    canvas.circle([x,point_y1],unit,fill='yellow')
    #draw body of the boy
    point_y2=y+5*unit
    canvas.line([[x,y],[x,point_y2]],fill='black',width=0.5*unit)
    
    #draw both legs
    point_x1=x+unit
    point_x3=x-unit
    point_y3=y-2*unit
    point_y4=y-2*unit
    canvas.line([[x,y],[point_x3,point_y4]],fill='black')
    canvas.line([[x,y],[point_x1,point_y3]],fill='black')
    #draw hands
    canvas.line([[x-2*unit,y+3*unit],[x+2*unit,y+3*unit]],fill='black',width=0.25*unit)

# this last function definition is used to draw a car

# by giving random riference point used to excute a car

def draw_a_car(x,y,size,colour):
    unit=size/5
    #draw lower larger rectangle
    point_x1=x+4*unit
    point_x2=x-4*unit
    point_y1=y+2*unit
    canvas.rectangle([[point_x1,point_y1],[point_x2,y]],fill=colour)
    # draw both wheels
    point_y2=y-0.5*unit
    point_x3=x-2.5*unit
    point_x4=x+1.5*unit
    canvas.circle([point_x3,point_y2],0.5*unit,fill='black')
    canvas.circle([point_x4,point_y2],0.5*unit,fill='black')
    # draw the upper small rectangle
    point_x5=x+unit
    point_x6=x-2*unit
    point_y3=y+2*unit
    point_y4=y+4*unit
    canvas.rectangle([[point_x5,point_y3],[point_x6,point_y4]],fill=colour)
    

# function call section

# main function used to call the function  definition that created above
# by giving two reference point used to excute the scene
def main():
    # draw things on the canvas
    draw_a_girl(60,-80,140,'red')
    draw_a_girl(200,160,100,'blue')
    draw_a_car(-200,160,80,'red')
    draw_a_boy(0,-40,160)
    draw_a_car(180,60,100,'magenta')
    draw_a_boy(-200,50,140)
    draw_a_car(-150,-150,150,'black')
    draw_a_girl(-150,50,120,'cyan')
    draw_a_boy(100,140,110)
    draw_a_boy(100,-200,120)
    draw_a_girl(200,-200,140,'pink')
    draw_a_car(450,-200,70,'blue')
    draw_a_car(350,0,100,'green')
    draw_a_boy(350,130,100)
    draw_a_girl(400,150,80,'red')


# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui3.Gui()
win.title('Playing around with Gui')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

#run the main function
main()

# show the window
win.mainloop()

