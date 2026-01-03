import pandas as pd

from step_2_2 import OUT_2_2  # 이전에 작성한 모듈을 불러옵니다.

# 거래일시, 가맹점명, 분류, 사용금액의 데이터
df_raw = pd.read_excel(OUT_2_2)
# 분류별로 사용금액으로 집계
df_pivot_1 = pd.pivot_table(df_raw, index="분류", values="사용금액", aggfunc="sum") # 새로운 DataFrame으로
df_pivot_1 # Jupyter 또는 Python 환경에서 마지막 줄의 변수는 자동으로 화면에 출력

# 2024-01-01 19:40에서 slice(0, 7)을 통해 2024-01-01 추출 후 새로운 거래연월 컬럼 생성하여 추출 값 입력
df_raw["거래연월"] = df_raw["거래일시"].str.slice(0, 7)
df_raw

#분류, 거래연월별로 사용금액 집계
df_pivot_2 = pd.pivot_table(df_raw, index="분류", columns="거래연월", values="사용금액", aggfunc="sum")
# axis를 생략하거나 axis=0을 전달하면 열별 합계를 계산함
df_pivot_2["누적금액"] = df_pivot_2.sum(axis=1)
df_pivot_2

df_sort = df_pivot_2.sort_values("누적금액", ascending=False)
df_sort

# rest_index는 데이터프레임의 인덱스를 일반 열로 전환하고, 0부터 시작하는 정수를 인덱스로 재설정
df_reindex = df_sort.reset_index()
df_reindex

from pathlib import Path

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

df_reindex.to_excel(OUT_DIR / f"{Path(__file__).stem}.xlsx", index=False, sheet_name="분류별누적금액")
