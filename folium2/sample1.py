import folium

# 地図の中心となる緯度経度を指定
sapporo_center = [43.0625587, 141.354376]

# 地図を作成
folium_map = folium.Map(location=sapporo_center, zoom_start=12)

# ツールチップを指定
tooltip = "Click me!"

# マーカープロット（時計台）
folium.Marker(
    location=[43.0625587, 141.354376],
    popup="<i>時計台</i>",  # ポップアップを指定
    tooltip=tooltip,  # ツールチップを指定
    icon=folium.Icon(color="red", icon="tower")  # アイコンを指定
).add_to(folium_map)

# 地図をHTMLファイルとして保存
folium_map.save('map-sample1.html')