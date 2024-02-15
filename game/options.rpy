init -1 python hide:
    config.name = _("Durka Simulator")
    config.version = "0.4.2"
    build.name = "Durka Simulator"
    gui.show_name = False

    ## Дополнительные настройки окна
    config.default_fullscreen = False
    # config.window_icon = "images/misc/icon.png"
    # config.windows_icon = "images/misc/icon.png"

    config.steam_appid = 1450150 # SteamID: 1450150, VK Play: 2018064, GameJolt: 0
    config.developer = True
    config.skip_indicator = True
    config.has_autosave = True
    config.gl_resize = True
    config.console = True
    config.log = True
    config.save_directory = "Durka Simulator"

    config.default_text_cps = 17
    config.main_menu_music = renpy.random.choice(["sound/music/main_menu_music.mp3", "sound/music/main_menu_music_2.mp3"])
    config.has_sound = True; config.has_music = True; config.has_voice = False
    config.window = "auto"
    config.autosave_slots = 6
    config.default_music_volume = 0.5

    gui.about = _p("""   """)

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

# Достижения
define GameJoltAPI = None
define GameJoltAPICheck = None 

init:
    if config.steam_appid == 0 and persistent.name and persistent.token:
        $ GameJoltAPI = GameJoltTrophy(persistent.name, persistent.token, 752408, "6a59d4828b16e13ca47ee16cf35a98bd")
        $ GameJoltAPICheck = GameJoltAPI.openSession()

    $ achievement.register("ChapterOne") # Эпизод 1
    $ achievement.register("ILoveSchool") # Я люблю школу
    $ achievement.register("IHateSchool") # Я ненавижу школу
    $ achievement.register("WeHaveYouNow") # Теперь ты наш
    $ achievement.register("SearchingForRocks") # В поисках камней
    $ achievement.register("ChoosingTheUnknown") # Выбор Загадочного
    $ achievement.register("MickeysChoice") # Выбор Микки
    $ achievement.register("DancingDog") # Танцующий пес
    $ achievement.register("DancingBears") # Танцующие медведи
    $ achievement.register("DancingPirate") # Танцующий пират
    $ achievement.register("Ricroll") # Рикролл
    $ achievement.register("LThisIsMe") # L это я
    $ achievement.register("DeathNote") # Тетрадь смерти
    $ achievement.register("SweeneyTodd") # Суини Тодд
    $ achievement.register("FirstBlood") # Первая кровь
    $ achievement.register("BiblicalMurder") # Библейское убийство
    $ achievement.register("LovePineapple") # Люблю Ананасы
    $ achievement.register("MiraclesAch") # Чудеса
    $ achievement.register("MickeyDead") # Микки умер
    $ achievement.register("MeatGrinder") # Мясорубка в доме Микки, при получение паспорта
    $ achievement.register("WelcomeToPlane") # Добро пожаловать в самолет
    $ achievement.register("WelcomeToCommunity") # Добро пожаловать в сообщество (Discord)
    $ achievement.register("StrayBullet") # Шальная пуля
    $ achievement.register("INotHuman") # Я не человек
    $ achievement.register("Creators") # Создатели
    $ achievement.register("ILoveDeath") # Я люблю смерть

    $ achievement.sync()

init python:
    build.directory_name = "New_Durka_Simulator"
    build.executable_name = "DurkaSimulator"
    build.include_update = False

    #build.archive("old_content_pack", "dlc")
    #build.classify("game/mods/**.rpy", None)
    #build.classify("game/mods/durka simulator content/**", "old_content_pack")
    #build.package("DLC", "zip", "dlc", dlc=True)
    
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.bat', None)
    build.classify('**.txt', None)
    build.classify('**.md', None)
    build.classify('**.bak', None)
    build.classify('**.rpy#', None)
    build.classify('**.log', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpyc', 'archive')
    build.classify('**.py', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.pdn', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.rpym', 'archive')
    build.classify('game/**.rpymc', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.rpyb', 'archive')