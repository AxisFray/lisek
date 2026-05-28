import turtle as t
t.speed(0)
colors = {
".": "#FFFFFF",
"N": "#000000",
"Y": "#FFF506",
"M":"#546677",
"P":"#754334",
"K":"#ff8500"
}

bitmap=[
    ".....................NN...........................",
    "...................NNKN...........................",
    "..................NN.KN...........................",
    ".................NK.KKKN..........................",
    "................NKN...KN..........................",
    "..NN...........NKN...K.NN.........................",
    ".NKKNNN........NKN...KKNNNNNNN....................",
    ".NKKNKKNN...NNNKKKNKKKKNKKKKKKNN..................",
    ".NK..NNKKNNNKKKKKKKNKKNKNKKKKKKKN.................",
    ".NKK..NKKKKKKKKKKKKKKKNKNKKKKKKKKNN...............",
    "..NK...NKKKKKKKKKKKKKKKNKKKKKKKKKKKN..............",
    "..N...NKKKKKKKKKKKKKKKKNNKKKKKKKKKKKN.............",
    "..NKKKKKKKKKKKKKKKKKKKKK.NKKKKKKKKKKN.............",
    "..NKKKKKKKKKKKKKKKKKKKK..NKKKKKKKKKKKN............",
    "...NKKKKKKKKKKKKKKKKKN...NKKKKKNNKKKKN............",
    "...NNKKKKKKKKKKKKKKKN....NKKKNNKKKKKKN............",
    "...NKNKKKKKKKKKKKKKKN....NKKNKKKKKKKKN............",
    "....NKNKKKKKKKKKKKKKN....NNNKKKKKKKKKKN...........",
    "....NKNKKKKKKKKKKKKK....NKKKKKKKKKKKKKN...........",
    ".....NN.KKKKKKKKKKKK...NKKKKKKKKKKKKKKN...........",
    "......N..KNNNKKKKKKK..NK.KKKKKKKKKKKKN............",
    "......N......NN....N.NN.K.KKKKKKKKKKKN............",
    ".......N............N.N.K.K....KKKKKKN............",
    "........NNNNNNNNNNNNKKN.......KKKKKKN.............",
    "............NK...NKKKKN.......K..KKN..............",
    "............NKK.NKKKKNN..........KN...............",
    "............NKKKNKKKN.N..........N................",
    ".............NNNKKKN..N........NN.................",
    "................NNN...N.....NNN...................",
    ".......................N..NN......................",
    ".......................NNN........................",
    "..................................................",
    "..................................................",
]
PIXEL_SIZE = 8
max_width = max(len(row) for row in bitmap)
bitmap = [row.ljust(max_width, ".") for row in bitmap]
screen = t.Screen()
screen.bgcolor("white")
screen.tracer(0)
WIDTH = len(bitmap[0])
HEIGHT = len(bitmap)

start_x = -WIDTH * PIXEL_SIZE // 2
start_y = HEIGHT * PIXEL_SIZE // 2

t.hideturtle()
t.penup()
for y in range(HEIGHT):
    for x in range(WIDTH):
        char = bitmap[y][x]
        color = colors.get(char, "#FFFFFF")
        t.goto(start_x + x  *PIXEL_SIZE, start_y - y * PIXEL_SIZE)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(PIXEL_SIZE)
            t.right(90)
        t.end_fill()
        t.penup()
screen.update()
t.done()

