"""
멘토세션7 - 예외처리

예외(Exceptions)
- 정상적인 동작은 아니지만, 적절히 해결이 가능한 상황
- ex) 서버 접속이 해제됨, 로그인 비밀번호가 틀림 등

오류(Errors)
- 비정상 동작으로, 더 이상 프로그램 동작을 신뢰할 수 없는 경우
- ex) 인덱스 벗어남, 자료형 미일치, 변수명 불일치 등

if문을 이용한 예외 처리
- 함수를 작성할 때 주로 사용
- 주로 잘못된 입력을 처리
- 처리 방법
    - 자체적으로 입력을 수정
    - Falsy(False처럼 받아들여지는 값들을 Falsy라고 한다) 반환값으로 예외 전달
    - raise를 이용하여 예외 발생
"""
import time
import random

MAX_ID_LENGTH = 12
MIN_PW_LENGTH = 4
def login(userId, userPw):
    if len(userId) > MAX_ID_LENGTH:
        # raise는 다시 시도해봤자 어차피 안 되는, 예외보다 에러에 가까운 애들
        raise ValueError('UserId longer than {}! ({})'.format(MAX_ID_LENGTH, len(userId)))

    if len(userPw) < MIN_PW_LENGTH:
        raise ValueError('UserPw shorter than {}! ({})'.format(MIN_PW_LENGTH, len(userPw)))

    if len(userId) == 0:
        userId = 'admin_debug'

    # Do login process
    if random.randint(0, 2):
        return False

    return True

"""
try ~ catch 문을 이용한 예외 처리
- 함수를 호출할 때 주로 사용
- 예외가 발생할 수 있는 곳에 사용
- 처리 방법
    - 예외 상황을 대처하기 위한 로직 작성
"""
def main():
    while login('test', 'testpw') is False:
        print('login failed! retrying in 1sec...')
        time.sleep(1)
    print('Login successful!')

    try:
        res = login('verylognidforthisprogram', 'password')
    except ValueError as e:
        print(e.args[0])

if __name__ == '__main__':
    main()