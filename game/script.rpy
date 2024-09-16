init python early:
    gm_episodes = {} # Эпизоды
    sp_episodes = {} # Спец эпизоды
    endings = 2 # Количество концовок

    gm_episodes["start"] = _("Эпизод 1")  

    # sp_episodes["part1_love"] = _("Нет названия")

# scene black with dissolve
# center_text "Конец демо-версии эпизода\nОжидайте следующих обновлений"

label start:

    $ inventory = {}

    $ mickey_stats = "Неизвестно"
    $ mickey_health = 100

    show screen inventory_button

    stop music fadeout 1.0

    python:
        if persistent.jump_to:
            j = persistent.jump_to
            persistent.jump_to = False
            discord.update(details = _("Пользовательская история"))
            renpy.jump(j)
      
    jump part1_home

    return

label game_over:

    hide screen info_panel 
    hide screen info_panel_enemy
    with dissolve

    scene black with dissolve

    "Вот и все, конец игры... Если, конечно, у вас нет сохранений."

    if not persistent.i_love_death:
        $ persistent.i_love_death = 1
    else:
        $ persistent.i_love_death = persistent.i_love_death + 1

        if persistent.i_love_death >= 15:

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221124)
            else:
                $ achievement.grant("ILoveDeath")
                $ achievement.sync()

    pause(0.5)

    if config.steam_appid == 0 and persistent.name and persistent.token:
        $ GameJoltAPI.addAchieved(221105)
    else:
        $ achievement.grant("MickeyDead")
        $ achievement.sync()

    scene capthepl_bg with dissolve

    pause(3.5)

    scene black with dissolve

    $ persistent.bad_ending_mickey_dead = True

    center_text "Сложно жить, когда ты мертв.\nКонцовка 2 / [endings]"

    return

label splashscreen:

    play music music_list["death_note_alert_music"]

    scene black

    scene CrucialExperiment with fade

    pause(1.5)

    scene RenPy with fade

    pause(1.5)

    scene attention with fade

    pause(3.9)

    scene black with fade

    if config.steam_appid == 0 and not persistent.name and not persistent.token:

        call screen gamejolt_start_screen

        $ persistent.name = renpy.input("Введите ваше имя пользователя GameJolt")

        $ persistent.token = renpy.input("Введите ваш секретный токен")

        $ GameJoltAPI = GameJoltTrophy(persistent.name, persistent.token, 752408, "6a59d4828b16e13ca47ee16cf35a98bd")
        $ GameJoltAPICheck = GameJoltAPI.openSession()