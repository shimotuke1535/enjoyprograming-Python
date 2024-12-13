import json
import csv
from datetime import datetime

# JSONファイルを読み込む
with open('watch-history.json', 'r', encoding='utf-8') as file:
    json_load = json.load(file)

# 10月の"YouTube Music"エントリをフィルタリング
october_entries = [
    entry for entry in json_load
    if entry.get("header") == "YouTube"
]

# CSVファイルを書き込む
with open('All_youtube_history.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
    fieldnames = ["Title", "URL", "Time", "Channel"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # ヘッダーを書き込む
    writer.writeheader()

    # 各エントリを書き込む
    for entry in october_entries:
        title = entry.get("title", "No Title")
        
        # " を視聴しました" を削除
        title = title.replace(" を視聴しました", "")
        title = title.replace("゙", "")  # 濁点を削除する
        
        writer.writerow({
            "Title": title,
            "URL": entry.get("titleUrl", "No URL"),
            "Time": entry.get("time", "No Time"),
            "Channel": entry.get("subtitles", [{"name": "No Channel"}])[0].get("name", "No Channel")
        })
        print({
            "Title": title,
            "URL": entry.get("titleUrl", "No URL"),
            "Time": entry.get("time", "No Time"),
            "Channel": entry.get("subtitles", [{"name": "No Channel"}])[0].get("name", "No Channel")
        })


print("completed!!!")