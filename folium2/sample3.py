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

kuyakusyo_list.append([43.090693, 141.340882])  # 北区の場所
kuyakusyo_list.append([43.076242, 141.363662])  # 東区の場所
kuyakusyo_list.append([42.989995, 141.353496])  # 南区の場所
kuyakusyo_list.append([43.074347, 141.300898])  # 西区の場所

# 多角形の描画
folium.Polygon(
    locations=[kuyakusyo_list[0], kuyakusyo_list[1], kuyakusyo_list[2], kuyakusyo_list[3]],  # 多角形の頂点
    color="blue",  # 線の色
    weight=2,  # 線の太さ
    fill=True,  # 塗りつぶす
    fill_opacity=0.2  # 透明度（1=不透明）
).add_to(folium_map)

# 地図をHTMLファイルとして保存
folium_map.save('map-sample3.html')
