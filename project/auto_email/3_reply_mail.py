import smtplib
from imap_tools import MailBox
from account import *
from email.message import EmailMessage

application_list = []  # 지원자 리스트
max_val = 3

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1  # 순번
    for msg in mailbox.fetch('(SENTSINCE 25-Dec-2020)'):  # 2020년 12월 25일 이후로 온 메일 조회
        if "파이썬 특강 신청입니다." in msg.subject:
            name, phone = msg.text.strip().split("/")
            # print(index, name, phone)
            application_list.append((msg, index, name, phone))  # 튜플식으로 넣는다.
            index += 1

print("[2. 선정 / 탈락 메일 발송]")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in application_list:
        to_addr = applicant[0].from_  # 수신 메일 주소
        # index = applicant[1]
        # name = applicant[2]
        # phone = applicant[3]
        index, name, phone = applicant[1:]

        title = None
        content = None

        if index <= max_val:
            title = "파이썬 특강 안내 [선정]"
            content = "{}님 축하드립니다. 특강 대상자로 선정되셨습다. (선정순정 {}번)".format(
                name, index)

        else:
            title = "파이썬 특강 안내 [탈락]"
            content = "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {}번)".format(
                name, index - max_val)

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(name, "님에게 메일 발송 완료")


# [선정 안내 메일]
# 제목 : 파이썬 특강 안내 [선정]
# 본문 : xx님 축하드립니다. 특강 대상자로 선정되셨습ㄴ디ㅏ. ( 선정순정 1번)

# [탈락 안내 메일]
# 제목 : 파이썬 특강 안내 [탈락]
# 본문 : xx님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 1번)
