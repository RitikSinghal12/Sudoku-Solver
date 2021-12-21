from tkinter import *
from Sudoku_Solver import solver

root = Tk()
root.title("Sudoku Solver")
root.geometry("324x450")

label = Label(root,text="Fill the numbers and click SOLVE button").grid(row=0,column=1,columnspan=10)

errlabel = Label(root,text="",fg="red")
errlabel.grid(row=15,column=1,columnspan=10,pady=5)

solvedlabel = Label(root,text="",fg="green")
solvedlabel.grid(row=15,column=1,columnspan=10,pady=5)

# Dictionary
cells = {}

def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P)<2
    return out

reg = root.register(ValidateNumber)

def draw3x3Grid(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5,bg=bgcolor,justify="center",validate="key",validatecommand=(reg,"%P") )
            e.grid(row=row+i+1,column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1,column+j+1)] = e

def draw9x9Grid():
    color = "cyan"

    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if(color == "cyan"):
                color = "yellow"
            else:
                color = "cyan"    

def clearValues():
    errlabel.configure(text="")
    solvedlabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

def getValues():
    # empty list to store every input value
    sudoku = []
    errlabel.configure(text="")
    solvedlabel.configure(text="")
    for row in range(2,11):
        # empty list to store every value in a row
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if(val == ""):
                rows.append(0)
            else:
                rows.append(int(val))

        sudoku.append(rows)
    updateValues(sudoku)

btn1 = Button(root, command=getValues, text="Solve", width=10)
btn1.grid(row=20, column=1, columnspan=5, pady=20)

btn1 = Button(root, command=clearValues, text="Clear", width=10)
btn1.grid(row=20, column=5, columnspan=5, pady=20)

def updateValues(s):
    sol = solver(s)
    if sol != "NO":
        for row in range(2,11):
            for col in range(1,10):
                cells[(row,col)].delete(0,"end")
                cells[(row,col)].insert(0,sol[row-2][col-1])
        solvedlabel.configure(text="Sudoku Solved!")
    else:
        errlabel.configure(text="No Solution Possible for this Sudoku")

draw9x9Grid()

root.mainloop()
