import tkinter as tk
from tkinter import PhotoImage, Label

# 버튼 클릭 시 이미지가 출력될 함수들
def show_dog():
    img = PhotoImage(file="dog.png")
    label.config(image=img)
    label.image = img  # 이미지를 레이블에 연결하여 참조 유지

def show_cat():
    img = PhotoImage(file="cat.png")
    label.config(image=img)
    label.image = img  # 이미지를 레이블에 연결하여 참조 유지

def show_rabbit():
    img = PhotoImage(file="rabbit.png")
    label.config(image=img)
    label.image = img  # 이미지를 레이블에 연결하여 참조 유지

# 기본 윈도우 설정
root = tk.Tk()
root.title("동물 이미지 출력 GUI")

# 출력 레이블 설정
label = Label(root)
label.pack(pady=20)

# 버튼 설정
dog_button = tk.Button(root, text="강아지", command=show_dog)
dog_button.pack(padx=10, pady=5)

cat_button = tk.Button(root, text="고양이", command=show_cat)
cat_button.pack(padx=10, pady=5)

rabbit_button = tk.Button(root, text="토끼", command=show_rabbit)
rabbit_button.pack(padx=10, pady=5)

# GUI 실행
root.mainloop()

