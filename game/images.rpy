image zhuoyuan:
    "images/zhuoyuan.png"
    xanchor 0.5
    yanchor 0.5

image zhuoyuan_fighting:
    "images/zhuoyuan_fighting.png"
    xanchor 0.5
    yanchor 0.5

image zhuoyuan_defeated:
    "images/zhuoyuan_defeated.png"
    zoom 0.7
    xanchor 0.5
    yanchor 0.5

image zhuoyuan_nervous:
    "images/zhuoyuan_nervous.png"
    zoom 0.75
    xanchor 0.5
    yanchor 0.5

image zhuoyuan_damn:
    "images/zhuoyuan_damn.png"
    zoom 0.75
    xanchor 0.5
    yanchor 0.5

image hao1:
    "images/hao1.png"
    xanchor 0.5
    yanchor 0.5

image gaoruihang_sprite:
    "images/gaoruihang.png"
    xanchor 0.5
    yanchor 0.5

image yiyigao_sprite:
    "images/yiyigao.jpg"
    xanchor 0.5
    yanchor 0.5

image qiutian:
    "images/qiutian.png"
    zoom 0.6
    xanchor 0.5
    yanchor 0.5

image bedra:
    "images/Bedra.png"
    zoom 0.75
    xanchor 0.5
    yanchor 0.5

image bedra_nervous:
    "images/Bedra_nervous.png"
    zoom 0.75
    xanchor 0.5
    yanchor 0.5

image caren:
    "images/Caren.png"
    xanchor 0.5
    yanchor 0.5

# 所有章节背景统一保持原始比例并铺满 1920×1080。
# 比例不一致的图片会从画面边缘裁切，不会被拉伸变形。
image canteen = Transform("images/canteen.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image classroom = Transform("images/classroom.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image dorm = Transform("images/dorm.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image flat_day = Transform("images/flat_day.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image flat_night = Transform("images/flat_night.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image gate = Transform("images/gate.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image lab_building = Transform("images/lab_building.jpg", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image lab = Transform("images/lab.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image lab_alarm = Transform("images/lab_alarm.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image office = Transform("images/office.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image restaurant = Transform("images/restaurant.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image toilet = Transform("images/toilet.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image toilet1 = Transform("images/toilet1.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image toilet2 = Transform("images/toilet2.png", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)
image ttk1 = Transform("images/ttk1.jpg", xysize=(1920, 1080), fit="cover", xalign=0.5, yalign=0.5)

image dim_overlay = Solid("#000000")

transform dim_in:
    alpha 0.0
    linear 1.0 alpha 1
