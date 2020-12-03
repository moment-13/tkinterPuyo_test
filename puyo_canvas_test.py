import tkinter as tk

# 定数 １マスのサイズとキャンバスを構成するマスの数
BLOCK_SIZE = 70

CANVAS_WIDTH = 6
CANVAS_HEIGHT = 12


# メインの画面と次のぷよが表示される画面を作成
root = tk.Tk()
root.title('ぷよぷよ')
root.geometry("1000x800")

canvas_main = tk.Canvas(root, width = BLOCK_SIZE * CANVAS_WIDTH, 
                         height = BLOCK_SIZE * CANVAS_HEIGHT, bg = 'lightblue')

next_window = tk.LabelFrame(root, text = 'NEXT', width = 100, height = 150, bg = 'lightgreen')



canvas_main.place(x=0, y=0)
next_window.place(x=500, y=40)



root.mainloop()