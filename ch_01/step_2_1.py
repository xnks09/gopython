# 01-2 폴더 크기 측정 프로그램
from pathlib import Path

# __file__ : 현재 파일의 절대 경로(C:\Dev\git\study\gopython\ch_01\setp_1.py)
# __name__ : 확장자를 제외한 현재 파일명(stpe_1 또는 __main__)

WORK_DIR = Path(__file__).parent
OUT_DIR = WORK_DIR / "output"

# OUT_DIR 경로에 output 폴더가 이미 존재하는 경우 오류가 발생하는데,
# 이 오류를 무시하기 위해 매개변수 exist_ok에 True를 전달
if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True)


# 파이썬은 하나의 변수에 서로 다른 타입의 데이터를 저장할 수 있음. 이러한 언어적 특성은 코드를 편리하고 빠르게 작성할 수 있도록 도와주지만,
# 반대로 코드가 복잡해질수록 오류 발생 위험 증가. 그래서 변수에 저장되는 데이터 타입을 사전에 지정할 수 있는데 이를 "타입힌트"라고 부름

# 예시
# x: int = 323, y: str="Hello, World"
# (함수의 경우) def get_size(path: Path) -> int:
#               pass