from mosaico import widget, colors
import random

# Global variables to store the rectangles and background
dice_bg = None
previous_number = None  # Global variable to store the previous number

# Global variables to store dice face elements
dot1 = None
dot2 = None
dot3 = None
dot4 = None
dot5 = None
dot6 = None

# Number of shuffles before stopping
shuffle_count = 10
current_shuffle = 0

def draw_dice_bg():
    global dice_bg  
    dice_bg = widget.createRectangle()
    dice_bg.setSize(40, 40)
    dice_bg.moveTo(12, 12)    
    dice_bg.setColor(colors.red)     

def draw_dice_face_1():
    """Draws the dice face with one dot."""
    global dot1
    dot1 = widget.createRectangle()
    dot1.setSize(10, 10)
    dot1.setColor(colors.black)
    dot1.moveTo(27, 27)

def draw_dice_face_2():
    """Draws the dice face with two dots."""
    global dot1, dot2
    dot1 = widget.createRectangle()
    dot1.setSize(10, 10)
    dot1.setColor(colors.black)
    dot1.moveTo(15, 15)

    dot2 = widget.createRectangle()
    dot2.setSize(10, 10)
    dot2.setColor(colors.black)
    dot2.moveTo(39, 39)

def draw_dice_face_3():
    """Draws the dice face with three dots."""
    draw_dice_face_1()
    global dot2
    dot2 = widget.createRectangle()
    dot2.setSize(10, 10)
    dot2.setColor(colors.black)
    dot2.moveTo(39, 39)

def draw_dice_face_4():
    """Draws the dice face with four dots."""
    global dot1, dot2, dot3, dot4
    dot1 = widget.createRectangle()
    dot1.setSize(10, 10)
    dot1.setColor(colors.black)
    dot1.moveTo(15, 15)

    dot2 = widget.createRectangle()
    dot2.setSize(10, 10)
    dot2.setColor(colors.black)
    dot2.moveTo(39, 15)

    dot3 = widget.createRectangle()
    dot3.setSize(10, 10)
    dot3.setColor(colors.black)
    dot3.moveTo(15, 39)

    dot4 = widget.createRectangle()
    dot4.setSize(10, 10)
    dot4.setColor(colors.black)
    dot4.moveTo(39, 39)

def draw_dice_face_5():
    """Draws the dice face with five dots."""
    draw_dice_face_4()
    global dot5
    dot5 = widget.createRectangle()
    dot5.setSize(10, 10)
    dot5.setColor(colors.black)
    dot5.moveTo(27, 27)

def draw_dice_face_6():
    """Draws the dice face with six dots."""
    global dot1, dot2, dot3, dot4, dot5, dot6
    dot1 = widget.createRectangle()
    dot1.setSize(10, 10)
    dot1.setColor(colors.black)
    dot1.moveTo(15, 15)

    dot2 = widget.createRectangle()
    dot2.setSize(10, 10)
    dot2.setColor(colors.black)
    dot2.moveTo(39, 15)

    dot3 = widget.createRectangle()
    dot3.setSize(10, 10)
    dot3.setColor(colors.black)
    dot3.moveTo(15, 27)

    dot4 = widget.createRectangle()
    dot4.setSize(10, 10)
    dot4.setColor(colors.black)
    dot4.moveTo(39, 27)

    dot5 = widget.createRectangle()
    dot5.setSize(10, 10)
    dot5.setColor(colors.black)
    dot5.moveTo(15, 39)

    dot6 = widget.createRectangle()
    dot6.setSize(10, 10)
    dot6.setColor(colors.black)
    dot6.moveTo(39, 39)

def get_new_number():
    global previous_number
    while True:
        new_number = random.randint(1, 6)
        if new_number != previous_number:
            previous_number = new_number
            return new_number

def draw_dice_face(number):
    """Draws the dice face based on the given number."""
    global dot1, dot2, dot3, dot4, dot5, dot6
    widget.clear()
    draw_dice_bg()  
    
    # Clear previous face elements
    dot1 = dot2 = dot3 = dot4 = dot5 = dot6 = None

    if number == 1:
        draw_dice_face_1()
    elif number == 2:
        draw_dice_face_2()
    elif number == 3:
        draw_dice_face_3()
    elif number == 4:
        draw_dice_face_4()
    elif number == 5:
        draw_dice_face_5()
    elif number == 6:
        draw_dice_face_6()

def loop():  
    global current_shuffle
    if current_shuffle < shuffle_count:
        number = get_new_number()
        draw_dice_face(number)
        current_shuffle += 1
    else:
        # Stop after shuffle_count is reached
        widget.clear()
        draw_dice_bg()
        final_number = previous_number if previous_number is not None else 1
        draw_dice_face(final_number)

