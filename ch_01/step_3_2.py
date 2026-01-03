from pathlib import Path
import matplotlib.pyplot as plt
from step_2_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import load_plot_data

plot_data = load_plot_data()

#plt 모듈의 함수 subplots()를 호출하여 객체 Figure와 Axes를 생성하고 각각 변수 fig. ax에 저장
# axes는 축(x축, y축)
fig, ax = plt.subplots()  

#함수 barh()를 호출하여 바 차트를 그립니다. 첫 번째 입력값으로 세로축에 사용할 폴더 이름을,
#두번째 입력값으로 가로축에 사용할 폴더 크기를 전달
ax.barh(plot_data["stem"], plot_data["size"])

# savefig()를 호출하여 fig에 저장된 차트를 png 파일로 저장
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")
