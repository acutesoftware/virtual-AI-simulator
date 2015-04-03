# user_commands.py  written by Duncan Murray 3/4/2015


def mouse_click(x,y):
    print ("clicked at", x, y)

def key_pressed(char, y, x):
    #print ("key pressed: __" + char + "__")
    #print ("repr version = " , repr(char))
    if char == 'w':
        print('move North')
        y -= 1
    elif char == 's':
        print('move South')
        y += 1
    elif char == 'a':
        print('move West')
        x -= 1
    elif char == 'd':
        print('move East')
        x += 1
        
        