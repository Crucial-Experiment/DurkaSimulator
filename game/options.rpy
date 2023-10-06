init -1 python hide:
    import os, steamapi

    ## Основные настройки окна игры
    config.name = "Durka Simulator"
    config.version = "1.0.4"
    gui.show_name = False
    build.name = "Durka Simulator"
    #config.window_icon = "gui/window_icon.png"

    ## Настройки разработчиков
    config.developer = True
    config.skip_indicator = True
    config.has_autosave = True
    config.gl_resize = True
    config.console = False
    config.save_directory = "Durka Simulator"
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.steam_appid = "1450150" #Steam: 1450150; VKPlay: 2018064

    ## Остальные настройки
    config.default_text_cps = 15
    config.main_menu_music = renpy.random.choice( ("sound/music/main_menu_music.mp3", "sound/music/main_menu_music_2.mp3") )
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.window = "auto"
    config.autosave_slots = 6

    # Курсор
    config.mouse = { }
    config.mouse["default"] = [("gui/mouse/cur_normal-idle.png",  0, 0)]
    config.mouse["hand"] = [("gui/mouse/cur_normal-pressed.png",  2, 2)]

    # Описания игры
    gui.about = _p("""
        Durka Simulator is a visual novel created as a demonstration of some game mechanics and prototype story, it is not related to the actual Crucial Experiment games!\n
        Copyright:\n
        The song "Trouble with the Bash" was created by youtuberess {a=https://www.youtube.com/@AmyLeeman}Amy Leeman{/a}.\n
        Some music from the anime {a=https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%82%D1%80%D0%B0%D0%B4%D1%8C_%D1%81%D0%BC%D0%B5%D1%80%D1%82%D0%B8}Death Note{/a}.\n
        Our Social Media:\n
        {a=https://www.youtube.com/channel/UCoYggKKmEqa1c0vMbO63lWA}YouTube{/a} | {a=https://vk.com/crucialexperim}VK{/a} | {a=https://discord.com/invite/RNzGSkGhqz}Discord{/a} | {a=https://t.me/CrucialExperiment}Telegram{/a}
    """)

    ## Настройка переходов
    config.enter_transition = Dissolve(.25)
    config.exit_transition = Dissolve(.25)
    config.intra_transition = Dissolve(.25)
    config.main_game_transition = Dissolve(.25)
    config.game_main_transition = Dissolve(.25)
    config.end_splash_transition = Dissolve(.25)
    config.end_game_transition = fade
    config.after_load_transition = dissolve
    config.window_show_transition = Dissolve(.25)
    config.window_hide_transition = Dissolve(.25)

    # Google Play License Key
    # define build.google_play_key = "..."

init python:
    build.directory_name = "Durka-Simulator"
    build.executable_name = "DurkaSimulator"
    build.include_update = False

    # DLC
    build.archive("new_image", "dlc")
    build.classify("game/images/characters/**", "new_image")
    build.package("DLC", "zip", "dlc", dlc=True)

    build.archive("game", "all")
    build.archive("libs", "all")
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.bat', None)
    build.classify('**.txt', None)
    build.classify('**.bak', None)
    build.classify('**.rpy#', None)
    build.classify('**.log', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/images/characters-beckup/**', None)
    build.classify('game/python-packages/**.**', 'libs')
    build.classify('game/steamlib/**.**', 'libs')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.pdn', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.rpym', 'archive')
    build.classify('game/**.rpymc', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.txt', 'archive')
    build.classify('game/**.rpyb', 'archive')