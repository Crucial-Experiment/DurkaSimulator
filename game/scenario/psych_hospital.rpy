label psych_hospital_part1:

    hide screen info_panel
    hide screen info_panel_enemy
    with dissolve

    $ mickey_health = 100

    scene black with dissolve

    play sound sound_list["fall"]

    pause(0.7)
    scene airport_inside_1_bg
    show mickey_happy at left
    with dissolve

    mickey "Ха-ха, меня не победить!"

    orderly "Это мы ещё посмотрим."

    play sound sound_list["fall"]

    scene black with dissolve
    center_text "Спустя 1 час"
    pause(1.2)
    scene durka_base_2_bg
    show dir_durka_normal at right
    show mickey_shouts_straitjacket at left
    with dissolve

    call remove_inv_item(inv_key_card_item_id)
    call remove_inv_item(inv_shaver_item_id)

    $ renpy.notify("У вас забрали некоторые предметы из инвентаря")

    durka "Добро пожаловать в нашу обитель."
    durka "Я уже думал, за тобой придется отправлять целый отряд."

    mickey "Что вам от меня нужно!?"

    return