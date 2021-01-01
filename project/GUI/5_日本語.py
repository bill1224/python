import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *  # __all__에서 지정해주지 않으면 서브모듈은 사용불가
from tkinter import filedialog  # filedialog는 서브 모듈이기 때문에 따로 불어와야함
from PIL import Image

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정

# 서로다른 크기 서로다른 위젯이 혼합되어있는 프로젝트이기 때문에 gird가 아닌 pack으로 구현

# 파일 추가


def add_file():
    # askopenfilenames 유저가 복수의 파일을 열도록 해주는 것
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                        filetypes=(
                                            ("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                        initialdir=r"D:\python")  # 최초에 c드라이브를 띄어줌
    # 경로 앞에 r을 붙혀주면 \를 escape로 받아들이지 않고 그냥 그대로 받아들임

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 선택 삭제


def del_file():
    list_file.curselection()

    # 오름차순인 상태에서 삭제하게되면 index가 바뀌게 때문에 다른 목록이 삭제되기 때문에 reversed를 사용
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장경로 (폴더)


def browse_dest_path():
    floder_selected = filedialog.askdirectory()
    if floder_selected == '':  # 취소했을 경우
        return
    # print(floder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, floder_selected)

# 이미지 통합


def merge_image():
    # 가로 넓이
    img_width = cmb_width.get()
    if img_width == "원본유지":
        img_width = -1  # -1일 때는 원본 기준으로

    else:
        img_width = int(img_width)

    # 간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 60
    elif img_space == "넓게":
        img_space = 90
    else:  # 없음
        img_space = 0

    # 포멧
    img_format = cmb_format.get().lower()  # png, jpg 값을 받아와서 소문자로 변경

    # print(list_file.get(0, END))  # 모든 파일 목록을 가지고 오기
    images = [Image.open(x) for x in list_file.get(0, END)]

    # 이미지 사이즈를 리스트에 넣어서 하나씩 처리
    # [(widths1, height1), (widths2, height2), (widths3, height3)]
    image_sizes = []
    if img_width > -1:
        # width 값 변경
        image_sizes = [(int(img_width), int(
            img_width*x.size[1] / x.size[0])) for x in images]
    else:
        # 원본 사이즈 사용
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    # 계산식
    # 100*60 이미지가 있음 -> width 를 80으로 줄이면 height 는 ?
    # 원본 width : 원본 height = 변경 width : 변경 height

    # 코드에 대입하면
    # 변경 height = (변경 width * 원본 height )/ 원본 width

    #[(widths, height), (widths, height), (widths, height)]
    widths, height = zip(*(image_sizes))

    # 최대 넓이 , 전체 높이 구함
    max_width, total_height = max(widths), sum(height)

    # 전체 스케지북 준비
    if img_space > 0:  # 이미지 간격 옵션 적용
        total_height += (img_space * (len(images) - 1))

    result_img = Image.new(
        "RGB", (max_width, total_height), (255, 255, 255))  # 배경 흰색
    y_offset = 0  # y 위치 (간격)

    for idx, img in enumerate(images):
        # width 가 원본유지가 아닐 때에는 이미지 크기 조정
        if img_width > -1:
            img = img.resize(image_sizes[idx])

        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_space)  # height 값 + 사용자가 지정한 간격

        progress = (idx + 1) / len(images) * 100  # 실제 진행 percent 정보 계산
        p_var.set(progress)
        progress_bar.update()

    # 포멧 옵션 처리
    # 저장 될 경로는 , 입력받은 경로에 "파일명" 이 된 경로
    file_name = "jong_photo."+img_format
    dest_path = os.path.join(txt_dest_path.get(), file_name)
    result_img.save(dest_path)
    msgbox.showinfo("知らせ", "作業が完了しました。")


# 시작
def start():
    # 각 옵션들 값을 확인
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("파일포멧 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("ウォーニング", "イメージファイルを追加してください")
        return  # 더이상 동작하면 안되니까 빠져나가기 위함

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("ウォーニング", "保存経路を選択してください。")
        return  # 더이상 동작하면 안되니까 빠져나가기 위함

    # 이미지 통합 작업
    try:
        merge_image()
    # 원인 불명에 대한 에러에 대해서도 전부 처리해주기 위해서 통합적인
    # Execption으로 예외처리
    except Exception as err:
        msgbox.showerror("error", err)


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)  # 간격 띄우기

btn_add_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="ファイル追加", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="選択削除", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
# 스크롤과 listbox를 맵핑한다.
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="保存経路")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,
                   padx=5, pady=5, ipady=4)  # ipady 높이 변경

btn_dest_path = Button(path_frame, text="経路検索",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="オプション")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="横幅", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["原本維持", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="無い", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["無い", "狭く", "ミドル", "広く"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)


# 3. 파일 포멧 옵션
# 파일 포멧 레이블
lbl_foramt = Label(frame_option, text="フォメット", width=8)
lbl_foramt.pack(side="left", padx=5, pady=5)

# 파일 포멧 콤보
opt_format = ["PNG", "JPG", "BMG"]
cmb_format = ttk.Combobox(frame_option, state="readonly",
                          values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진행 상황 프로그레스바
frame_progress = LabelFrame(root, text="進行状況")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

# variable=p_var 실제 값과 프로그레스 상황이 일치하도록
p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="クローズ",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5,
                   text="スタート", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 ( 창크기 변경 불가)
root.mainloop()  # 창이 닫히지 않게 해주는 것
