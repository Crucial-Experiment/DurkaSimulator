label part2_home:

    play sound sound_list["open_door_1"]

    pause(3.3)

    if school_choose:
        scene mickey_home2_bg with dissolve
    else:
        scene mickey_home_bg with dissolve
    
    show mickey_thinks with moveinright

    mickey "..."

    hide mickey_thinks
    show mickey_happy
    with dissolve

    mickey "Ничего себе!"

    mickey "С моим домом ничего не случилось."

    mickey "Как будто ничего и не было."

    pause(0.8)

    mickey "Лол."

    mickey "Я сказал слово - ничего, более 4-х раз."

    mickey "А нет, уже пять."

    mickey "Так, вроде только нужен паспорт."

    show mickey_happy at left with moveoutleft
    show orderly_normal at right with moveinright

    orderly "Ты ищешь это?"

    mickey "Эй! Это мой паспорт."

    orderly "Попробуй отнять его у меня."

    hide mickey_happy
    show mickey_serious at left
    with dissolve

    $ battle_character = "orderly"
    $ battle_label = "part2_home_b1"
    $ orderly_health = 200

    show screen info_panel
    show screen info_panel_enemy
    with dissolve

    jump game_battle

label part2_home_b1:

    hide screen info_panel
    hide screen info_panel_enemy
    with dissolve

    scene black with dissolve

    $ mickey_health = 100

    play sound sound_list["fall"]

    pause(0.7)

    if school_choose:
        scene mickey_home2_bg
    else:
        scene mickey_home_bg

    show mickey_serious
    with dissolve

    mickey "Хаха, я победил тебя."

    hide mickey_serious
    with dissolve
    
    call add_inv_item(inv_passport_item_id, show_item=True)

    play sound sound_list["picked_up_an_item"]

    show mickey_happy
    with dissolve

    mickey "Фух... Вроде всё."

    hide mickey_happy with easeoutleft

    jump part1_airoport

    return