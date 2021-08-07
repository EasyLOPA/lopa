from tkinter import *
import sqlite3



root = Tk()

root.geometry("10000x10000")
canvas = Canvas(root, width=10000, height=10000, bg="white")
canvas.grid(padx=10, pady=10)


# square_canvas.create_line(x1, y1, x2, y2, )

x1_square = 20
y1_square = 40
x2_square = 60
y2_square = 20

x1_line = 60
y1_line = 30
x2_line = 70
y2_line = 30

conn = sqlite3.connect("lopa.db")
cur = conn.cursor()

cur.execute("""SELECT cause_id FROM Cause;
            """)
cause_iter = cur.fetchall()
for i in cause_iter:

    cur.execute("""SELECT cause_barrier_id FROM Cause_Barrier WHERE cause_id = ?;""", (i))
    cause_barrier_iter = cur.fetchall()
    print(cause_barrier_iter)


    for i in cause_barrier_iter:

        canvas.create_line(x1_line, y1_line, x2_line, y2_line, fill="black", width=2)
        x1_line = x2_square
        x2_line = x1_line + 50

        canvas.create_rectangle(x1_square, y1_square, x2_square, y2_square, fill="blue")
        x1_square = x1_line + 40
        x2_square = x1_square + 40
    
    x1_square = x1_square + 20 
    y1_square = y1_square + 20
    x2_square = x2_square + 20
    y2_square = y2_square + 20

    x1_line = x1_line + 20
    y1_line = y1_line + 20
    x2_line = x2_line + 20
    y2_line = y2_line + 20




















# bow_tie = Button(root, text="Create Bow Tie Diagram")
# bow_tie.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()   
