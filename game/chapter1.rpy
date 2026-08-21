label chapter1:

    scene gate

    "夜色像一块湿布，捂住了校园。再待下去，总觉得下一盏路灯后面就会冒出第二个 Bedra。"

    show zhuoyuan:
        xpos 960
        ypos 650

    zhuoyuan "走吧，我们不能待在学校里，邓迪克的人随时会找到你。"

    turtle "那去哪？总不能一直在外边晃。"

    zhuoyuan "放心，组织有安全屋，就在学校附近的公寓。"

    zhuoyuan "从现在起，你必须二十四小时处在监护下，直到危机解除。"

    turtle "监护……？意思是我不能一个人？"

    zhuoyuan "没错，你已经被魔力标记了，单独行动等于送死。"

    turtle "那……谁监护我？"

    zhuoyuan "当然是我啦！"
    
    hide zhuoyuan

    show gaoruihang_sprite:
        xpos 960
        ypos 800

    "校门口路灯下，一个身姿笔直的女生靠在栏杆旁，长发束起，表情冷淡。"

    gaoruihang "邓大然。"

    turtle "啊，我、我……"

    gaoruihang "debuff 清除完成，效率勉强合格。"

    hide gaoruihang_sprite

    show zhuoyuan:
        xpos 960
        ypos 650

    zhuoyuan "喂，我可是单挑干部哎！"

    hide zhuoyuan

    show gaoruihang_sprite:
        xpos 960
        ypos 800

    gaoruihang "任务失败，暴露平民，按规扣分。"

    "她就是特别行动组的人——睾锐夯，负责处理学院所有魔法相关事件。"

    gaoruihang "执行预案：转移至校外安全屋，二十四小时轮班监护。"

    turtle "安全屋？"

    gaoruihang "单人公寓，两间卧室，我和何茁圆轮守，你住主卧。"

    gaoruihang "其实就是何茁圆家。"

    hide gaoruihang_sprite

    show zhuoyuan:
        xpos 960
        ypos 650    

    zhuoyuan "欸嘿嘿，我申请守夜班！我可以——"

    hide zhuoyuan

    show gaoruihang_sprite:
        xpos 960
        ypos 800

    gaoruihang "按战力排班，你值白班，我值夜班。"

    hide gaoruihang_sprite

    show zhuoyuan:
        xpos 960
        ypos 650

    zhuoyuan "……知道了。"

    hide zhuoyuan

    scene flat_night

    "校外小公寓里家具不多，但两道锁、一台路由器、一张书桌，反倒比宿舍更让人踏实些。"

    turtle "这里真的安全吗？"

    show gaoruihang_sprite:
        xpos 960
        ypos 800

    gaoruihang "屏蔽魔法信号，普通监控拍不到内部，邓迪克找不到。"

    hide gaoruihang_sprite

    show zhuoyuan:
        xpos 960
        ypos 650

    zhuoyuan "终于能歇会儿了！刚才差点被 Bedra 打死。"

    "何茁圆往沙发上一瘫，开始宽衣解带——脱下的丝袜随后飞到了我脸上。"

    turtle "呃啊啊啊……"

    zhuoyuan "呀！你叫什么啦！"

    hide zhuoyuan
    
    show gaoruihang_sprite:
        xpos 960
        ypos 800

    gaoruihang "干什么？你以为这里是你家客厅啊？"

    hide gaoruihang_sprite

    show zhuoyuan_damn:
        xpos 960
        ypos 650

    zhuoyuan "但是这里确实是我家啊……"

    hide zhuoyuan_damn

    show gaoruihang_sprite:
        xpos 960
        ypos 800

    gaoruihang "现在开始这里是组织的安全屋！你要遵守纪律！"

    hide gaoruihang_sprite

    show zhuoyuan_damn:
        xpos 960
        ypos 650

    zhuoyuan "好吧……"

    hide zhuoyuan_damn

    "小灯亮着，窗外是城市夜景。远处邓迪克国际学院的大楼在夜幕里泛着一层诡异的绿光。"

    "我从没想过，自己的大二生活会从‘迷茫宅’变成‘被魔法追杀的关键人物’。"

    turtle "‘黑暗势力’具体是什么？真的能毁灭世界吗？"

    show gaoruihang_sprite:
        xpos 960
        ypos 800

    gaoruihang "从技术指标上来说，他们还不具备毁灭世界的条件。目前阶段，只能毁掉几座城市的网络和能源系统。"

    turtle "这种程度就‘只’了吗？！"

    gaoruihang "邓迪克想利用学生的编程能力，把魔法阵变成网络病毒，一旦扩散，全国系统瘫痪。"

    gaoruihang "你今天能把魔法阵从何茁圆身上扯下来，不是偶然。"

    "那一刻，客厅里突然安静下来。我第一次意识到，自己好像不是纯粹的路人甲。"

    "楼下悄悄掠过一个人影。"

    hide gaoruihang_sprite

    myth "邓大然……居然被睾锐夯抓去‘保护’了啊。"

    myth "真好奇，他到底有什么特别的地方。"

    "门缝下，一道微不可察的细小光线流过，像有人在做实验一样。"

    myth "（窃笑）明天上课，见个面吧。"

    show dim_overlay at dim_in zorder 100
    pause 1.5

    jump chapter2
