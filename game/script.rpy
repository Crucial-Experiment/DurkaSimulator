init python early:
    mods = {}
    endings = 2
    
label start:

    $ mickey_stats = "Неизвестно"
    $ mickey_health = 100

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
            $ achievement.grant("ILoveDeath")
            $ achievement.sync()

    pause(0.5)

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