import json
from pathlib import Path

from step_2_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.json"


def dump_dirnames(base_dir: Path) -> None:
    dirs = []  #하위 목록 저장 리스트 초기화
    for path in base_dir.iterdir():  #주어진 폴더의 모든 파일과 하위 폴더 목록을 반환
        if path.is_dir():
            dirs.append(path.as_posix())
    dirs_sorted = sorted(dirs)  # dirs 리스트를 오름차순으로 정렬

    with open(OUT_2_3, "w", encoding="utf-8") as fp:     # OUT_2_3 경로에 쓰기모드로 파일을 열고 이를 변수 fp에 저장
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)  #json 패키지 함수 dump()를 사용하여 dirs_sorted에 저장된
                                                                  # 폴더 목록을 JSON 형식의 문자열로 파일에 저장.
                                                                  # ensure_ascii=False라면 한글, 일본어, 이모지 등이 그대로 저장. 아니면 유니코드로 저장됨

def load_dirnames() -> list[str]:
    if OUT_2_3.is_file():
        with open(OUT_2_3, encoding="utf-8") as fp:
            return json.load(fp)
    return []    #파일이 없으면 빈 리스트를 반환


if __name__ == "__main__":
    dump_dirnames(Path.home())  #함수 home()을 사용해 홈 디렉터리의 경로를 입력값으로 전달
