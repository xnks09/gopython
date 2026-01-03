# seaborn 패키지를 사용하는 경우
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_4_2 import load_data


# pct : 개별항목의 비율, total : 전체 합계
def custom_autopct(pct, total):
    real_val = int(pct / 100 * total)
    return f"{real_val:,}원\n({pct:.1f}%)"


df_raw = load_data()
labels, values = df_raw["분류"], df_raw["누적금액"]

sns.set_theme(context="poster", font="Malgun Gothic")  # 맥OS 사용자는 font에 "Apple SD Gothic Neo" 입력
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.pie(
    values,
    textprops=dict(color="white", size=20),
    startangle=90,
    autopct=lambda pct: custom_autopct(pct, sum(values)),
)
# legend를 통해 차트의 범례를 출력
# 매개변수 bbox_to_anchor에 (1. 0.5)를 전달하여 차트의 X축 오른쪽, Y축 중간 지점을 범례 출력의 기준점으로 설정하고,
# loc 'center left'를 전달하여 범례의 왼쪽 중간을 기준점에 맞춤
ax.legend(labels, bbox_to_anchor=(1, 0.5), loc="center left")
# set_title을 통해 차트의 소제목 설정
# labels, values의 첫 번째 값을 불러와 가장 많이 사용한 분류와 누적 금액을 출력
ax.set_title(f"1분기에는 {labels[0]}에 {values[0]:,}원을 사용했습니다.")
# suptitle을 통해 차트 제목 설정
fig.suptitle("1분기 카드 사용 내역")
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
