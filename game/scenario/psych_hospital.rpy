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

    call remove_inv_item(inv_key_card_item_id) from _call_remove_inv_item
    call remove_inv_item(inv_shaver_item_id) from _call_remove_inv_item_1

    $ renpy.notify("У вас забрали некоторые предметы из инвентаря")

    durka "Добро пожаловать в нашу обитель."
    durka "Я уже думал, за тобой придется отправлять целый отряд."

    mickey "Что вам от меня нужно!?"

    durka "Что нам от тебя нужно? Хм... А в правду, что же?"
    with hpunch
    play sound sound_list["punch"]
    durka "Не делай вид, что не знаешь."

    mickey "Я правда не понимаю."

    durka "Хватит придуряться! Ребята, киньте его уже в камеру."

    scene black with dissolve
    play sound sound_list["fall"]
    pause(1.2)
    scene durka_base_3_bg
    show mickey_serious_straitjacket at center
    with dissolve

    orderly "Подними эту бирку!"
    orderly "Я сказал, подними эту бирку!"
    with hpunch
    play sound sound_list["punch"]

    mickey "Хорошо..."

    call add_inv_item(inv_iron_tag_item_id, show_item=True) from _call_add_inv_item_6

    orderly "Хе-хе"

    play sound sound_list["closing_metal_door"]
    pause 3

    mickey "Вот же уроды."
    mickey "..."

    hide mickey_serious_straitjacket
    show mickey_shouts_straitjacket at center

    mickey "Кто здесь?!"

    show escapedfromdurka_normal at left with moveinleft
    "???" "Эээ... не... не ори."
    "???" "Я... я здесь."

    mickey "Ты кто такой?!"

    "???" "Я... эээ... я... {w=0.4} Подожди... как это... эээ..."

    hide mickey_shouts_straitjacket
    show mickey_thinks_straitjacket at center

    mickey "Ты чего молчишь?"

    "???" "Да... забыл... Эээ... бывает."

    mickey "Ну ты даёшь... Даже имени не помнишь."
    mickey "И что, тебя так и зовут – Эээ?"

    "Эээ" "Можешь так звать... Мне всё равно."

    mickey "Окей, Эээ, а чего ты тут вообще делаешь?"

    "Эээ" "Я здесь... давно. Два или три года..."

    mickey "Три года? Может ты знаешь как выбраться отсюда?"

    "Эээ" "Выбраться?.. Ха... ха... ну... эээ... как сказать... пытался."

    mickey "Пытался?"

    "Эээ" "Три раза... эээ... не получилось."
    "Эээ" "Первый раз... дверь, как говорится... не ту выбрал."
    "Эээ" "Второй... охранник... этот... как танк."
    "Эээ" "Третий... вентиляция."

    mickey "Вентиляция? Серьёзно?"

    "Эээ" "Да, только эээ... я застрял."

    mickey "Ну ты, конечно, мастер побегов."

    play sound sound_list["turning_off_light"]
    scene black with dissolve

    mickey "Эй! Что происходит?!"
    mickey "Эй! Кто-нибудь!"

    mysterious "Тихо. Это только начало."

    "Эээ" "Это... эээ... он..."

    durka "Найдите его! Немедленно!"

    mickey "Что ты тут делаешь?!"

    center_text "Конец 1 эпизода\nОжидайте следующих обновлений"

    return