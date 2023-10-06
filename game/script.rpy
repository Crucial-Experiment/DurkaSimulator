init -2 python:
    mikki_health = 100
    mikki_stats = _("Неизвестен")
    orderly_health = 99
    mercenary_healht = 149

python early:
    mods = {}
    dls = {}
    achs = {}

    chapter1_ending = 0

label start:

    stop music fadeout 1.0

    #$ _steamlib.set_rich_presence("steam_display", "#StatusTestGame")
    #$ _steamlib.set_rich_presence("text", "Play The Game")

    python:
        if persistent.jump_to:
            j = persistent.jump_to
            persistent.jump_to = False
            renpy.jump(j)

    scene black

    play music music_list["game_music_005"]

    #pause(1.0)

    #scene Chapter1 with fade

    #pause(1.5)

    jump cp1_a1

    return

label mikki_dead:

    hide screen info_panel with dissolve

    scene black with dissolve

    "Товарищ, вы не справились со своей миссией. Объект Микки был убит, а это значит, что санитары получат власть в данном мире. Вам придется вернуться назад во времени чтобы избежать данной ситуации."

    pause(0.5)

    $ achievement.grant("MickeyDead")
    init:
        $ achievement.register("MickeyDead")
        $ achievement.sync()

    $ achievement.sync()

    scene capthepl with dissolve

    pause(3.5)

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

    if not persistent.lang_menu and not steam_running:
        call screen choose_language_panel