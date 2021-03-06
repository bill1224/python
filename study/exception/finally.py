class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        # raise를 만나게 되면 해당 오류 ValueError except 부분으로 넘어가서
        # 다음 코딩은 실행이 안된다. (예외처리가 된다.)
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("에러 발생. 한 자리 숫자만 입력하세요.")
    print(err)

#finally는  예외처리에서 맨 마지막 구문에 위치를하고 
#정상적으로 작동할 떄나 예외처리가 될 경우나 상관없이 항상 동작함 
finally:
    print("계산기를 이용해 주셔서 감사합니다.")


