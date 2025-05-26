import flet as ft
import json
import time
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import threading

def main(page: ft.Page):
    channel_text = ft.Text("Channels", no_wrap=False, max_lines=None, selectable=True)
    numbers_text = ft.Text("", no_wrap=False, max_lines=None, selectable=True)
    bools_text = ft.Text("", no_wrap=False, max_lines=None, selectable=True)

    # チェックボックスリスト
    channel_checks = []
    selected_channels = set(["1"])  # 初期選択

    def on_checkbox_change(e):
        selected_channels.clear()
        for i, cb in enumerate(channel_checks, 1):
            if cb.value:
                selected_channels.add(str(i))

    # チェックボックス生成
    for i in range(1, 33):
        cb = ft.Checkbox(label=f"Ch {i}", value=(i == 1), on_change=on_checkbox_change)
        channel_checks.append(cb)

    # グラフ用データ
    x_data = []
    y_data_dict = {str(i): [] for i in range(1, 33)}
    t = 0  # mainスコープ

    # 初期グラフ
    fig, ax = plt.subplots()
    lines = {}
    for i in range(1, 33):
        (line,) = ax.plot([], [], label=f"Ch {i}")
        lines[str(i)] = line
    ax.set_title("Numbers")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()
    chart = MatplotlibChart(fig, expand=True)

    # リセットボタンの処理
    def reset_graph(e):
        nonlocal t
        x_data.clear()
        for y_list in y_data_dict.values():
            y_list.clear()
        for line in lines.values():
            line.set_data([], [])
        t = 0  # ここでtもリセット
        chart.update()

    reset_button = ft.ElevatedButton("リセット", on_click=reset_graph)

    def update_json_view():
        nonlocal t
        while True:
            with open("test.json", "r") as file:
                data = json.load(file)
            numbers_values = [str(a) for a in data["Numbers"].values()]
            bools_values = [str(a) for a in data["Bools"].values()]
            channel_values = [str(a) for a in range(1,33)]
            channel_text.value = "Channels:\n" + "\n".join(channel_values)
            numbers_text.value = "Numbers:\n" + "\n".join(numbers_values)
            bools_text.value = "Bools:\n" + "\n".join(bools_values)

            x_data.append(t)
            if len(x_data) > 100:
                x_data.pop(0)
            # 各チャンネルのデータ更新
            for ch in range(1, 33):
                ch_key = str(ch)
                y_data_dict[ch_key].append(data["Numbers"][ch_key])
                if len(y_data_dict[ch_key]) > 100:
                    y_data_dict[ch_key].pop(0)
            # グラフ更新
            for ch_key, line in lines.items():
                if ch_key in selected_channels:
                    line.set_data(x_data, y_data_dict[ch_key])
                else:
                    line.set_data([], [])
            ax.relim()
            ax.autoscale_view()
            chart.update()
            t += 1

            page.update()
            time.sleep(0.01)  # 更新頻度を0.01秒ごとに

    # ページの設定
    page.add(
        ft.Row(
            [
                ft.Column(channel_checks + [reset_button], scroll="always", expand=0),
                ft.Row([channel_text, numbers_text, bools_text], expand=1),
                chart
            ],
            expand=True
        )
    )
    threading.Thread(target=update_json_view, daemon=True).start()

ft.app(target=main)