import tkinter as tk

# 定数 １マスのサイズとキャンバスを構成するマスの数
BLOCK_SIZE = 70

CANVAS_WIDTH = 6
CANVAS_HEIGHT = 12




# ぷよ管理
puyopuyo = []
puyo_manage = []


for h in range(CANVAS_HEIGHT):
        puyopuyo.append([0, 0, 0, 0, 0, 0])
        puyo_manage.append([0, 0, 0, 0, 0, 0])

def draw_puyo():
    for y in range(CANVAS_HEIGHT):
        for x in range(CANVAS_WIDTH):
            if puyopuyo[y][x] > 0:
                canvas_main.create_image(x * BLOCK_SIZE + 35, y * BLOCK_SIZE + 35, image=img_puyo[puyopuyo[y][x]], tag="PUYO")



# メインの画面と次のぷよが表示される画面を作成
root = tk.Tk()
root.title('ぷよぷよ')
root.geometry("1000x840")

canvas_main = tk.Canvas(root, width = BLOCK_SIZE * CANVAS_WIDTH, 
                         height = BLOCK_SIZE * CANVAS_HEIGHT + 35, bg = 'lightblue')

next_window = tk.LabelFrame(root, text = 'NEXT', width = 100, height = 150, bg = 'lightgreen')
canvas_main.place(x=0, y=0)
next_window.place(x=500, y=40)




img_puyo = [
    None,
    tk.PhotoImage(file="puyo1.png"),
    tk.PhotoImage(file="puyo2.png"),
    tk.PhotoImage(file="puyo3.png"),
    tk.PhotoImage(file="puyo4.png"),
    tk.PhotoImage(file="puyo5.png"),
]




draw_puyo()

root.mainloop()