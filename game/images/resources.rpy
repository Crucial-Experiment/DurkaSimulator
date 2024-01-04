init python:
    import datetime

    new_year_start_date = [2023, 12, 21]
    new_year_end_date = [2024, 1, 4]

    def is_event_sprite(start, end):
        start_date = datetime.date( start[0], start[1], start[2] )
        end_date = datetime.date( end[0], end[1], end[2] )

        today = datetime.date.today()
        return start_date <= today <= end_date

init 1:

    #Позиции для диалогового меню
    define center_text = Character(None, what_size=42, all_at_once=False, what_xalign=0.5, what_text_align=0.5, window_xalign=0.5, window_yalign=0.5)

    #Создания персонажей
    define mickey = Character('Микки', color="#87CEEB")
    define veronika = Character('Вероника', color="#c8ffc8")
    define mysterious = Character('Загадочный', color="#c8ffc8")
    define larry = Character('Ларри', color="#c8ffc8")
    define announcer = Character('Диктор', color="#c8ffc8")
    define someone = Character('Кто-то', color="#c8ffc8")
    define durka = Character('Вождь Дурки', color="#c8ffc8")
    define orderly = Character('Санитар', color="#c8ffc8")
    define security = Character('Охранник', color="#c8ffc8")
    define passer_all = Character('Прохожий', color="#c8ffc8")
    define cashier = Character('Кассир', color="#c8ffc8")
    define manager = Character('Менеджер', color="#c8ffc8")
    define driver = Character('Водитель', color="#c8ffc8")
    define grandfather = Character('Старик', color="#c8ffc8")
    define granny = Character('Бабка', color="#c8ffc8")
    define mercenary = Character('Наемник', color="#c8ffc8")
    define rigagent = Character('Агент по регестрации', color="#c8ffc8")
    define kolya = Character('Коля', color="#c8ffc8")
    define stewardess = Character('Стюардесса', color="#c8ffc8")

    # Загрузка изображений

    #Персонажи

    #Микки
    if is_event_sprite(new_year_start_date, new_year_end_date): # mickey_happy
        image mickey_happy:
            "images/sprites/mickey/mickey_happy_yn.png"
            zoom 1.1
    else:
        image mickey_happy:
            "images/sprites/mickey/mickey_happy.png"
            zoom 1.1

    if is_event_sprite(new_year_start_date, new_year_end_date): # mickey_not_happy
        image mickey_not_happy:
            "images/sprites/mickey/mickey_not_happy_yn.png"
            zoom 1.1
    else:
        image mickey_not_happy:
            "images/sprites/mickey/mickey_not_happy.png"
            zoom 1.1

    if is_event_sprite(new_year_start_date, new_year_end_date): # mickey_serious
        image mickey_serious:
            "images/sprites/mickey/mickey_serious_yn.png"
            zoom 1.1
    else:
        image mickey_serious:
            "images/sprites/mickey/mickey_serious.png"
            zoom 1.1

    if is_event_sprite(new_year_start_date, new_year_end_date): # mickey_shouts
        image mickey_shouts:
            "images/sprites/mickey/mickey_shouts_yn.png"
            zoom 1.1
    else:
        image mickey_shouts:
            "images/sprites/mickey/mickey_shouts.png"
            zoom 1.1

    if is_event_sprite(new_year_start_date, new_year_end_date): # mickey_thinks
        image mickey_thinks:
            "images/sprites/mickey/mickey_thinks_yn.png"
            zoom 1.1
    else:
        image mickey_thinks:
            "images/sprites/mickey/mickey_thinks.png"
            zoom 1.1

    image mickey_back:
        "images/sprites/mickey/mickey_back.png"
        zoom 1.1

    #Загадочный
    if is_event_sprite(new_year_start_date, new_year_end_date): # mysterious_normal
        image mysterious_normal:
            "images/sprites/mysterious_yn.png"
            zoom 1.1
    else:
        image mysterious_normal:
            "images/sprites/mysterious.png"
            zoom 1.1

    if is_event_sprite(new_year_start_date, new_year_end_date): # mysterious_angry
        image mysterious_angry:
            "images/sprites/mysterious_angry_yn.png"
            zoom 1.1
    else:
        image mysterious_angry:
            "images/sprites/mysterious_angry.png"
            zoom 1.1

    #Старик
    image old_man_normal:
        "images/sprites/old_man.png"
        zoom 1.1
    image old_man_thinks:
        "images/sprites/old_man_thinks.png"
        zoom 1.1
    image old_man_serious:
        "images/sprites/old_man_serious.png"
        zoom 1.1

    #Наемник
    image mercenary_anim:
        zoom 1.1
        "images/sprites/kolya/mercenary_a1.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a2.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a3.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a4.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a5.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a6.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a7.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a8.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a7.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a6.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a5.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a4.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a3.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a2.png"
        pause 0.17
        "images/sprites/kolya/mercenary_a1.png"
        repeat
    image kolya_normal:
        "images/sprites/kolya/kolya.png"
        zoom 1.1
    image kolya_clear:
        "images/sprites/kolya/kolya_clear.png"
        zoom 1.1
    image kolya_past:
        "images/sprites/kolya/kolya_past.png"
        zoom 1.1
    image kolya_past_angry:
        "images/sprites/kolya/kolya_past_angry.png"
        zoom 1.1
    image kolya_dead:
        "images/sprites/kolya/kolya_dead.png"
        zoom 1.1

    #Агент по регестрации
    image rig_agent_normal:
        "images/sprites/rig_agent.png"
        zoom 1.1
    image rig_agent_happy:
        "images/sprites/rig_agent_happy.png"
        zoom 1.1

    #Остальные
    image larry_normal:
        "images/sprites/larry.png"
        zoom 1.1
    image larry_back:
        "images/sprites/larry_back.png"
        zoom 1.1
    if is_event_sprite(new_year_start_date, new_year_end_date): # orderly_normal
        image orderly_normal:
            "images/sprites/orderly_yn.png"
            zoom 1.1
    else:
        image orderly_normal:
            "images/sprites/orderly.png"
            zoom 1.1
    if is_event_sprite(new_year_start_date, new_year_end_date): # dir_durka_normal
        image dir_durka_normal:
            "images/sprites/orderly_v2_yn.png"
            zoom 1.1
    else:
        image dir_durka_normal:
            "images/sprites/orderly_v2.png"
            zoom 1.1
    image security_normal:
        "images/sprites/security.png"
        zoom 1.1
    image justapasserby_normal:
        "images/sprites/justapasserby.png"
        zoom 1.1
    image cashier_normal:
        "images/sprites/cashier.png"
        zoom 1.1
    image manager_normal:
        "images/sprites/manager.png"
        zoom 1.1
    image yura_normal:
        "images/sprites/yura.png"
        zoom 1.1
    image grandma_normal:
        "images/sprites/grandma.png"
        zoom 1.1
    image priest_normal:
        "images/sprites/priest.png"
        zoom 1.1
    image stewardess_normal:
        "images/sprites/stewardess.png"
        zoom 1.1

    #Предметы
    image mysterious_credentials:
        "images/items/credentials.png"
        xalign 0.5
        yalign 0.5
    image mickey_notebook:
        "images/items/notebook.png"
        xalign 0.5
        yalign 0.5
        zoom 0.6
    image durka_key_card:
        "images/items/key_card.png"
        xalign 0.5
        yalign 0.5
        zoom 0.6
    image shop_tea:
        "images/items/tea.png"
        xalign 0.5
        yalign 0.5
        zoom 0.7
    image mickey_shaver:
        "images/items/shaver.png"
        xalign 0.5
        yalign 0.5
        zoom 0.7
    image mickey_passport:
        "images/items/passport.png"
        xalign 0.5
        yalign 0.5
        zoom 0.7

    #Фоны
    image redsquare_bg = "images/backgrounds/redsquare.jpg"
    image mickey_home_bg = "images/backgrounds/mickey_home.png"
    image mickey_home2_bg = "images/backgrounds/mickey_home2.png"
    image college_admissions_bg = "images/backgrounds/college_admissions.png"
    image school_bg = "images/backgrounds/school.png"
    image forest_bg = "images/backgrounds/forest.png"
    image durka_base_bg = "images/backgrounds/durka_base.png"
    image durka_base_2_bg = "images/backgrounds/durka_base_2.png"
    image mysterious_base_bg = "images/backgrounds/zagadochnuy_base.png"
    image mysterious_base_armory_bg = "images/backgrounds/zagadochnuy_armory_room.png"
    image street_bg = "images/backgrounds/street.png"
    image pyaterochka_lb1_bg = "images/backgrounds/pyaterochka_lb1.jpg"
    image pyaterochka_lb2_bg = "images/backgrounds/pyaterochka_lb2.jpg"
    image trapping_bg = "images/backgrounds/trapping.jpg"
    image minibus_bg = "images/backgrounds/minibus.jpg"
    image bus_bg = "images/backgrounds/bus.png"
    image bus_inside_bg = "images/backgrounds/bus_inside.jpg"
    image bus_inside_c1_bg = "images/backgrounds/bus_inside_c1.png"
    image bus_inside_c2_bg = "images/backgrounds/bus_inside_c2.png"
    image l_dn_bg = "images/l_dn.png"
    image durka_car_bg = "images/backgrounds/durka_car.png"
    image forest_2_bg = "images/backgrounds/forest_2.png"
    image lonely_village_bg = "images/backgrounds/lonely_village.png"
    image lonely_village_2_bg = "images/backgrounds/lonely_village_2.png"
    image grandfather_home_bg = "images/backgrounds/grandfather_home.png"
    image grass_mercenary_bg = "images/backgrounds/grass_mercenary.png"
    image trapping_2_bg = "images/backgrounds/trapping_2.png"
    image capthepl_bg = "images/capthepl.png"
    image airport_bg = "images/backgrounds/airport.png"
    image airport_inside_1_bg = "images/backgrounds/airport_inside_1.png"
    image airport_inside_2_bg = "images/backgrounds/airport_inside_2.png"
    image airplane_bg = "images/backgrounds/airplane.png"
    image airplane_inside_bg = "images/backgrounds/airplane_inside.png"
    image airplane_inside_c1_bg = "images/backgrounds/airplane_inside_c1.png"
    image airplane_inside_c2_bg = "images/backgrounds/airplane_inside_c2.png"
    image airplane_inside_c3_bg = "images/backgrounds/airplane_inside_c3.png"
    image airplane_inside_c4_bg = "images/backgrounds/airplane_inside_c4.png"
    
    # Персонажи в самолете
    image airplane_inside_m1:
        "images/backgrounds/airplane_inside_m1.png"
        xalign 0.202
    image airplane_inside_m2:
        "images/backgrounds/airplane_inside_m2.png"
        xalign 0.202
    image airplane_inside_k1:
        "images/backgrounds/airplane_inside_k1.png"
        xalign 0.735
    image airplane_inside_k2:
        xalign 0.735
        "images/backgrounds/airplane_inside_k2.png"
    image airplane_inside_k2_anim:
        xalign 0.735
        "images/backgrounds/airplane_inside_k2_a1.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a2.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a3.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a4.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2.png"
    image airplane_inside_k2_anim2:
        xalign 0.735
        "images/backgrounds/airplane_inside_k2.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a4.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a3.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a2.png"
        pause 0.12
        "images/backgrounds/airplane_inside_k2_a1.png"

    # Логотипы
    image CrucialExperiment = "gui/logos/crucialexperiment.png"
    
    if _preferences.language != None:
        image RenPy = "gui/logos/renpy_en.png"
        image Later_001 = "gui/logos/later_en.png"
        image attention = "gui/logos/attention_en.png"
        image onemonthlater = "gui/logos/onemonthlater_en.png"
        image gameover = "gui/logos/gameover_en.png"
    else:
        image RenPy = "gui/logos/renpy_ru.png"
        image Later_001 = "gui/logos/later_ru.png"
        image attention = "gui/logos/attention_ru.png"
        image onemonthlater = "gui/logos/onemonthlater_ru.png"
        image gameover = "gui/logos/gameover_ru.png"

    # Загрузка музыки и звуков
    $ music_list = {}
    $ sound_list = {}

    $ music_list["death_note_ls_theme_b_music"] = "sound/music/death_note_ls_theme_b_music.mp3"
    $ music_list["death_note_alert_music"] = "sound/music/death_note_alert_music.mp3"
    $ music_list["game_music_003_dialogue"] = "sound/music/game_music_003_dialogue.ogg"

    $ sound_list["open_door_1"] = "sound/audio/open_door_1.mp3"
    $ sound_list["open_door_2"] = "sound/audio/open_door_2.mp3"
    $ sound_list["open_door_3"] = "sound/audio/open_door_3.mp3"
    $ sound_list["knock_door_1"] = "sound/audio/knock_door_1.mp3"
    $ sound_list["knock_door_2"] = "sound/audio/knock_door_2.mp3"
    $ sound_list["journal_closing"] = "sound/audio/journal_closing.mp3"
    $ sound_list["journal_opening"] = "sound/audio/journal_opening.mp3"
    $ sound_list["screams"] = "sound/audio/screams.mp3"
    $ sound_list["removing_the_pen_guard"] = "sound/audio/removing_the_pen_guard.mp3"
    $ sound_list["shot_1"] = "sound/audio/shot_1.mp3"
    $ sound_list["shot_2"] = "sound/audio/shot_2.mp3"
    $ sound_list["door_knockout"] = "sound/audio/door_knockout.mp3"
    $ sound_list["kicking_the_door"] = "sound/audio/kicking_the_door.mp3"
    $ sound_list["steps"] = "sound/audio/steps.mp3"
    $ sound_list["twig_crunch"] = "sound/audio/twig_crunch.mp3"
    $ sound_list["item_received_1"] = "sound/audio/item_received_1.mp3"
    $ sound_list["opening_metal_door"] = "sound/audio/opening_metal_door.mp3"
    $ sound_list["picked_up_an_item"] = "sound/audio/picked_up_an_item.mp3"
    $ sound_list["shackles"] = "sound/audio/shackles.mp3"
    $ sound_list["steps_on_asphalt"] = "sound/audio/steps_on_asphalt.mp3"
    $ sound_list["ambulance"] = "sound/audio/ambulance.mp3"
    $ sound_list["fall"] = "sound/audio/fall.mp3"
    $ sound_list["punch"] = "sound/audio/punch.ogg"
    $ sound_list["zipper_on_clothes"] = "sound/audio/zipper_on_clothes.mp3"
    $ sound_list["paper_rustle"] = "sound/audio/paper_rustle.mp3"
    $ sound_list["laugh"] = "sound/audio/laugh.mp3"
    $ sound_list["dadsaasd"] = "sound/audio/dadsaasd.mp3"
    $ sound_list["airplane_takeoff"] = "sound/audio/airplane_takeoff.mp3"
    $ sound_list["inside_airplane"] = "sound/audio/inside_airplane.mp3"
    $ sound_list["slap"] = "sound/audio/slap.mp3"