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

# 札幌市の各区役所の位置情報を管理するリスト
kuyakusyo_list = list()

kuyakusyo_list.append([43.090693,141.340882])  # 北区の場所
kuyakusyo_list.append([43.076242,141.363662])  # 東区の場所
kuyakusyo_list.append([42.989995,141.353496])  # 南区の場所
kuyakusyo_list.append([43.074347,141.300898])  # 西区の場所

# 折れ線の描画
folium.PolyLine(locations=kuyakusyo_list,).add_to(folium_map)

# 地図をHTMLファイルとして保存
folium_map.save('map-sample2.html')