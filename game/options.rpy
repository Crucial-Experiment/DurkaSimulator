init -1 python hide:
    import os, steamapi

    ## Основные настройки окна игры
    config.name = "Durka Simulator"
    config.version = "1.0.3"
    gui.show_name = False
    build.name = "DurkaSimulator"
    config.screen_width = 1280
    config.screen_height = 720
    config.default_fullscreen = False
    config.window_icon = "gui/window_icon.png"

    ## Настройки разработчиков
    config.developer = True
    config.skip_indicator = True
    config.has_autosave = True
    persistent.vkplay = False
    config.gl_resize = True
    config.console = False
    config.save_directory = "Durka Simulator"
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.steam_appid = "1450150" # VKPlay: 2018064 #Steam: 1450150

    ## Остальные настройки
    config.default_text_cps = 15
    if persistent.vkplay == False:
        if _steamlib.steam_init() and _steamlib.vac_banned():
            config.main_menu_music = renpy.random.choice( ("sound/music/main_menu_music.mp3", "sound/music/im_a_cheater.mp3", "sound/music/main_menu_music_2.mp3", "sound/music/death_note_opening2_music.mp3") )
        else:
            config.main_menu_music = renpy.random.choice( ("sound/music/main_menu_music.mp3", "sound/music/main_menu_music_2.mp3", "sound/music/death_note_opening2_music.mp3") )
    else:
        config.main_menu_music = renpy.random.choice( ("sound/music/main_menu_music.mp3", "sound/music/main_menu_music_2.mp3", "sound/music/death_note_opening2_music.mp3") )
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
        Durka Simulator – это визуальна новелла, созданная как демонстрация некоторых игровых механик и прототипа сюжета. Возможно что к выходу новых версий или релиза игры сюжет будет полностью переделан.\n
        Авторские права:\n
        Песня "Беда с Башкой" была создана ютубершой {a=https://www.youtube.com/@AmyLeeman}Amy Leeman{/a}.\n
        Песня "Я - Читер!" была взята с ютуб канала {a=https://www.youtube.com/@Montyfaith}Monty{/a}.\n
        Песня "Кукла колдуна" была создана группой {a=https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C_%D0%B8_%D0%A8%D1%83%D1%82}Король и Шут{/a}.\n
        Некотороя музыка из аниме {a=https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%82%D1%80%D0%B0%D0%B4%D1%8C_%D1%81%D0%BC%D0%B5%D1%80%D1%82%D0%B8}Death Note{/a}.\n
        Наши социальные сети:\n
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

init python:
    build.directory_name = "DurkaSimulator"
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
    build.classify('game/images/characters-beckap/**', None)
    #build.classify('game/**.py', 'libs')
    #build.classify('game/**.pyc', 'libs')
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
