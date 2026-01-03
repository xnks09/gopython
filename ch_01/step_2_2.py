from pathlib import Path

from step_2_1 import WORK_DIR  # 이전에 작성한 모듈을 불러옵니다.

#glob : 입력값으로 전달된 글로브 패턴과 일치하는 파일명을 리스트로 반환

def get_total_filesize(base_dir: Path, pattern: str = "*") -> int:
    total_bytes = 0
    for fullpath in base_dir.glob(pattern): 
        if fullpath.is_file():
            total_bytes += fullpath.stat().st_size
    return total_bytes


if __name__ == "__main__":
    base_dir = WORK_DIR
    filesize = get_total_filesize(base_dir, pattern="*")
    print(f"{base_dir.as_posix()=}, {filesize=} bytes")
