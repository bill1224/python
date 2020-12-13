import os
import keyboard
import time
from PIL import ImageGrab
from tkinter import *
from tkinter import filedialog


def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

# 저장경로 (폴더)


def test():
    # if txt_dest_path != '':
    #     save_path = txt_dest_path.get()+"/"
    #     print(str(txt_dest_path))
    # else:
    #     save_path = ""
    # curr_time = time.strftime("_%Y%m%d_%H%M%S")
    # save_path += "image{}.png".format(curr_time)
    # print(save_path)
    file_name = "jong_photo.png"
    print(os.path.join(txt_dest_path, file_name))


def browse_dest_path():
    floder_selected = filedialog.askdirectory()
    if floder_selected == '':  # 취소했을 경우
        return
    # print(floder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, floder_selected)


def run():
    keyboard.add_hotkey("F9", screenshot)
    keyboard.wait("esc")


def printf():
    print(txt_run.get())


def printf2():
    print(txt_stop.get())


root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
# root.geometry("640x480")  # 가로 x 세로의 크기 지정

# 스크린샷 키 설정 프레임
key_frame = LabelFrame(root, text="스크린샷 단축키 설정")
key_frame.pack(fill="x", padx=5, pady=5)

txt_run = Entry(key_frame)
txt_run.pack(side="left", fill="x", expand=True,
             padx=5, pady=5, ipady=4)
txt_run.insert(END, "F9")

btn_key = Button(key_frame, width=8,
                 text="키변경", command=printf)
btn_key.pack(side="right", padx=5, pady=5)


# 종료 키 설정 프레임
stop_frame = LabelFrame(root, text="종료 단축키 설정")
stop_frame.pack(fill="x", padx=5, pady=5)

txt_stop = Entry(stop_frame)
txt_stop.pack(side="left", fill="x", expand=True,
              padx=5, pady=5, ipady=4)
txt_stop.insert(END, "esc")

btn_key = Button(stop_frame, width=8, text="키변경", command=printf2)
btn_key.pack(side="right", padx=5, pady=5)

# 파일경로
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,
                   padx=5, pady=5, ipady=4)  # ipady 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


# 실행/종료
run_frame = Frame(root)
run_frame.pack(fill="x")

btn_close = Button(run_frame, width=8, text="닫기", command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_run = Button(run_frame, width=8, text="실행", command=test)
btn_run.pack(side="right", padx=5, pady=5)

root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 ( 창크기 변경 불가)
root.mainloop()  # 창이 닫히지 않게 해주는 것
