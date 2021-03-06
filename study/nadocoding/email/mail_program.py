# Quiz) 당신은 (주) 나도출판의 편집자입니다. 최근에 파이썬에 관한 책을 기획 중인데,
# 양질의 컨텐츠를 제공하는 유튜버들을 발견하여 제안서를 보내고자 합니다.
# 동일한 내용의 메일에 유튜버 이름 정보만 변경하여 파일로 저장하는 프로그램을 만드세요.

# [조건]
# 1. 유튜버 이름은 리스트로 제공 (최서 2명 이상)
# 예) name = ["유튜버1", "유튜버2", "유튜버3", "유튜버4"]

# 2. 파일명은 "유튜버 이름.txt" 로 저장
# 예) 나도코딩.txt, 너도코딩.txt

# [메일 본문]
# 안녀하세요 ? xxx님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# xxx님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용을 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니디.

# -나코드림


names = ["나도코딩", "김사원세끼", "마스크맨"]


for i in range(len(names)):
    contents = (f"안녀하세요 ? {names[i]}님.\n\n"
                "(주)나도출판 편집자 나코입니다.\n"
                "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
                f"{names[i]}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
                "자세한 내용을 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n"
                "좋은 하루 보내세요 ^^\n"
                "감사합니디.\n\n"
                "-나코드림")
    with open("{}.txt".format(names[i]), "w", encoding="utf8") as f:
        f.write(contents)
