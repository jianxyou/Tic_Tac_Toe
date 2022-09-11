# Tic_Tac_Toe




This is a graphic game that is played alone on a square grid: the teaser game. The teaser game is explained here and can be played on the web.
Before explaining how the game works, we have to understand how the tiles are displayed.

On the hardware side, displaying images (and also text) on a computer screen is done by controlling the contents of a rectangular grid of square pixels. The grid has a width and height that depends on the screen resolution (for example 1600 columns by 1200 rows). Each pixel has an X-Y coordinate that indicates its position in the grid. By convention, the top leftmost pixel has the coordinate (0,0) and the bottom rightmost pixel has the coordinate (width-1,height-1).

Each pixel is a cell that has a color specified by its red, green, and blue components, which are integers between 0 and a maximum value that depends on the screen configuration (eg 15, 255, or 65535). The three components are combined to determine the final color of the pixel. We will use the value 15 as the maximum value. The higher a component is (up to a maximum of 15), the more this color will be present in the final color of the pixel. We can therefore use a record with three fields to represent a color. We will use the field names r, g and b (for red, green and blue). Here is how we could define some colors:

    black = struct(r= 0, g= 0, b= 0)
    blank = struct(r=15, g=15, b=15)
    green = struct(r= 0, g=15, b= 0)
    yellow = struct(r=15, g=15, b= 0)
Under the orders of the screen driver of the operating system, the graphics processor of the computer (the GPU), stores in each pixel the components r, g and b necessary to display the desired image. To make a screen display, a program must send appropriate requests to the operating system, whose screen driver will translate these requests into commands for the GPU.
