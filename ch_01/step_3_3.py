# 차트를 보기좋게 바꾸는 방법
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np #수치연산

from step_2_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import load_plot_data

plot_data = load_plot_data()

# 함수 log()를 사용하여 주어진 숫자 데이터를 로그로 변환하고, 변수 log_size에 저장
# 폴더 크기와 같이 특정 데이터의 크기가 지나치게 큰 경우 로그를 적용해 단위를 조정하면 이해하기 쉽게
# 시각화가 가능함
log_size = np.log(plot_data["size"])

# 함수 subplots()를 사용하여 객체 Figure와 Axes를 생성하고 각각 gix, ax변수에 저장
# 이때 매개변수 figsize에 차트 크기를 (가로, 세로)형식으로 dpi에 해상도를 전달하여 전체 해상도를 설정(단위는 인치와 인치당 픽셀)
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.barh(plot_data["stem"], log_size)

# grid()를 사용하여 차트에 그리드를 출력, 이때 axis 매개변수의 값으로 'both', 'x', 'y' 등을 전달하여 출력할
# 그리드의 형태를 설정할 수 있음
ax.grid(True, axis="x")  # 축 그리드

# tick_params()를 사용하여 축 눈금을 설정. 매개변수 labelbottom과 length에 각각 False와 0을 전달하여 X축 눈금을 지우고
# labelsize에 30을 전달하여 Y축 눈금의 폰트 크기를 설정
ax.tick_params(labelbottom=False, length=0, labelsize=30)  # 축 눈금

fig.set_layout_engine("tight")  # 차트 여백(tight : 여백 최소화)
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")
