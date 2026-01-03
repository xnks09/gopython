import pandas as pd

from step_3_2 import OUT_3_2  # 이전에 작성한 모듈을 불러옵니다.

# 상위 4개를 따로 구성하고 나머지는 기타로 합쳐서 간소화
N = 4
df_raw = pd.read_excel(OUT_3_2)
# iloc 명령어를 사용해 데이터프레임을 슬라이싱
# iloc[:N] : 0부터 N-1행까지
# iloc[N:] : N부터 마지막행까지 슬라이싱
df_head, df_tail = df_raw.iloc[:N], df_raw.iloc[N:]
df_tail

# drop으로 '분류'열을 제거하고 함수 sum()으로 열별 합계를 구함.
# 그리고 이를 함수 to_frame()으로 데이터프레임으로 변환 후, 함수 transpose()를
# 사용하여 행과 열을 바꿈
df_sum = df_tail.drop(columns=["분류"]).sum().to_frame().transpose()
df_sum
# '기타'문자열을 분류 열에 추가
df_sum["분류"] = "기타"
df_sum

# df_head와 df_sum을 연결하고, ignore_index 매개변수에 True를 전달하여
# 데이터프레임의 인덱스를 0부터 N-1까지 다시 생성
df_final = pd.concat([df_head, df_sum], ignore_index=True)
df_final

from pathlib import Path

import matplotlib.pyplot as plt

from step_1 import OUT_DIR

values = df_final["누적금액"]

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.pie(
    values,
    textprops=dict(color="black", size=20),  # 폰트 설정
    startangle=90,  # 차트 각도 설정
    autopct="%.1f%%",  # 비율 출력 형식 지정
)
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
