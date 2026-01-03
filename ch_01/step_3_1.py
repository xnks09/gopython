import json
from pathlib import Path
from step_2_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_4 import load_filesize_per_dir

OUT_3_1 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_plot_data():
    size_per_path = load_filesize_per_dir()
    #딕셔너리에 키로 지정된 경로를 폴더 이름으로 변경하고, 변수 size_per_stem에 저장. 이때 폴더 크기가 0보다 큰 데이터만 추출
    size_per_stem = {Path(path).stem: size for path, size in size_per_path.items() if size > 0}

    #두 개의 키 stem과 size를 갖는 새로운 딕셔너리 plot_data를 생성
    plot_data = dict(
        stem=list(size_per_stem.keys()),
        size=list(size_per_stem.values()),
    )
    with open(OUT_3_1, "w", encoding="utf-8") as fp:
        json.dump(plot_data, fp, ensure_ascii=False, indent=2)

def load_plot_data() -> dict[str, list]:
    if OUT_3_1.is_file():
        with open(OUT_3_1, encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__ == "__main__":
    dump_plot_data()
