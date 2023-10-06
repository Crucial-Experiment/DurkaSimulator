init:
    image CrucialExperiment = "gui/logos/crucialexperiment.png"

    if _preferences.language == "russian":
        image RenPy = "gui/logos/renpy_ru.png"
        image Later_001 = "gui/logos/later_ru.png"
        image attention = "gui/logos/attention_ru.png"
        image onemonthlater = "gui/logos/onemonthlater_ru.png"
        image gameover = "gui/logos/gameover_ru.png"
    else:
        image RenPy = "gui/logos/renpy_en.png"
        image Later_001 = "gui/logos/later_en.png"
        image attention = "gui/logos/attention_en.png"
        image onemonthlater = "gui/logos/onemonthlater_en.png"
        image gameover = "gui/logos/gameover_en.png"

    image DeathNodeL = "images/l_dn.png"
    image capthepl = "images/capthepl.png"

    define mikki = Character(_('Mickey'), color="#c8ffc8")
    define zagadochnuy = Character(_('Mysterious'), color="#c8ffc8")
    define zagadochnuy_name = Character(_('Mokki'), color="#c8ffc8")
    define durka = Character(_('Chief Durku'), color="#c8ffc8")
    define orderly = Character(_('Orderly'), color="#c8ffc8")
    define larry = Character(_('Larry'), color="#c8ffc8")
    define dictor = Character(_('Announcer'), color="#c8ffc8")
    define policeman = Character(_('Policeman #1'), color="#c8ffc8")
    define policeman2 = Character(_('Policeman #2'), color="#c8ffc8")
    define thecashier = Character(_('Cashier'), color="#c8ffc8")
    define manager = Character(_('Manager'), color="#c8ffc8")
    define manager_name = Character(_('Manager Natasha'), color="#c8ffc8")
    define passer_all = Character(_('Passerby'), color="#c8ffc8")
    define schoolboy = Character(_('Schoolboy'), color="#c8ffc8")
    define security = Character(_('Guard'), color="#c8ffc8")
    define developer = Character(_('Developer'), color="#c8ffc8")
    define driver = Character(_('Driver'), color="#c8ffc8")
    define vania = Character(_('Vanya'), color="#c8ffc8")
    define yura = Character(_('Yura'), color="#c8ffc8")
    define mercenary = Character(_('Mercenary'), color="#c8ffc8")
    define grandfather = Character(_('Grandpa'), color="#c8ffc8")
    define granny = Character(_('Grandma'), color="#c8ffc8")
    define rigagent = Character(_('Registration agent'), color="#c8ffc8")
    define kolia = Character(_('Kolya'), color="#c8ffc8")
    define zah_orderly = Character(_('Invader'), color="#c8ffc8")
    define stalin = Character(_('Stalin'), color="#c8ffc8")

    image mikki_happy_image = 'images/characters/mickey/mickey_happy.png'
    image mikki_not_happy_image = 'images/characters/mickey/mickey_not_happy.png'
    image mikki_shouts_image = 'images/characters/mickey/mickey_shouts.png'
    image mikki_thinks_image = 'images/characters/mickey/mickey_thinks.png'
    image mikki_serious_image = 'images/characters/mickey/mickey_serious.png'

    image zagadochnuy_image = 'images/characters/mysterious.png'
    image zagadochnuy_angry_image = 'images/characters/mysterious_angry.png'

    image durka_image = 'images/characters/durka.png'
    image orderly_image = 'images/characters/orderly.png'
    image orderly_image_katscene = 'images/characters/orderly.png'
    image orderly_deltagroup_image = 'images/characters/orderly-deltagroup.png'

    image mercenary = 'images/characters/kolia/mercenary.png'
    image kolia = 'images/characters/kolia/kolia.png'
    image kolia_past = 'images/characters/kolia/kolia_past.png'
    image kolia_angry_past = 'images/characters/kolia/kolia_angry_past.png'

    image rig_agent = 'images/characters/rig_agent/rig_agent.png'
    image rig_agent_happy = 'images/characters/rig_agent/rig_agent_happy.png'

    image larry_image = 'images/characters/larry.png'

    image policeman_image = 'images/characters/policeman.png'
    image policeman2_image = 'images/characters/policeman2.png'
    image security_image = 'images/characters/security.png'

    image manager_image = 'images/characters/manager.png'
    image thecashier_image = 'images/characters/thecashier.png'

    image justapasserby_image = 'images/characters/justapasserby.png'
    image schoolboy_image = 'images/characters/schoolboy.png'
    image escapedfromdurka_image = 'images/characters/escapedfromdurka.png'
    image ilovembsboy_image = 'images/characters/ilovembsboy.png'
    image yura_image = 'images/characters/yura.png'
    image granny_image = 'images/characters/granny.png'

    image grandfather_image = 'images/characters/grandfather/grandfather.png'
    image grandfather_thinks_image = 'images/characters/grandfather/grandfather_thinks.png'
    image grandfather_serious_image = 'images/characters/grandfather/grandfather_serious.png'

    image stalin_image = 'images/characters/stalin.png'

    image l_dn_image = 'images/characters/L_DeathNode.png'
    image lightyagami_dn_image = 'images/characters/LightYagami_DeathNode.png'

    image Mikki_House = "images/backgrounds/Mikki_House.png"
    image Redsquare = "images/backgrounds/Redsquare.jpg"
    image Forest = "images/backgrounds/Forest.png"
    image Prenistory_Forest = "images/backgrounds/Prenistory_Forest.png"
    image Ward1 = "images/backgrounds/Ward1.jpg"
    image DurkaBase = "images/backgrounds/DurkaBase.png"
    image Hallway1 = "images/backgrounds/Hallway1.jpg"
    image ZagadochnuyBase = "images/backgrounds/ZagadochnuyBase.png"
    image DurkaBaseControlRoom = "images/backgrounds/DurkaBaseControlRoom.png"
    image OldHome = "images/backgrounds/OldHome.jpg"
    image DurkaBathRoom = "images/backgrounds/DurkaBathRoom.png"
    image ZagadochnuyArmoryRoom = "images/backgrounds/ZagadochnuyArmoryRoom.png"
    image Street = "images/backgrounds/Street.png"
    image Beach = "images/backgrounds/Beach.png"
    image AirplaneInside = "images/backgrounds/AirplaneInside.png"
    image Pyaterochka_lb1 = "images/backgrounds/Pyaterochka_lb1.jpg"
    image Pyaterochka_lb2 = "images/backgrounds/Pyaterochka_lb2.jpg"
    image Trapping = "images/backgrounds/Trapping.jpg"
    image Minibus = "images/backgrounds/Minibus.jpg"
    image Bus = "images/backgrounds/Bus.png"
    image BusInInside = "images/backgrounds/BusInInside.jpg"
    image Durka_Car = "images/backgrounds/Durka_Car.png"
    image Lonely_Village = "images/backgrounds/Lonely_Village.png"
    image Grandfather_Home = "images/backgrounds/Grandfather_Home.png"
    image Airport = "images/backgrounds/Airport.png"
    image InsideInAirport = "images/backgrounds/InsideInAirport.png"
    image Airplane = "images/backgrounds/Airplane.png"
    image Bank = "images/backgrounds/Bank.jpg"
    image Forest2 = "images/backgrounds/Forest2.png"

    image College_Admissions = "images/illustrations/College_Admissions.png"
    image Conversation_Inside_In_Bus1 = "images/illustrations/Conversation_Inside_In_Bus1.jpg"
    image Conversation_Inside_In_Bus2 = "images/illustrations/Conversation_Inside_In_Bus2.jpg"
    image Conversation_Inside_In_Bus3 = "images/illustrations/Conversation_Inside_In_Bus3.jpg"
    image Conversation_Inside_In_Bus4 = "images/illustrations/Conversation_Inside_In_Bus4.jpg"
    image Conversation_Inside_In_Bus5 = "images/illustrations/Conversation_Inside_In_Bus5.jpg"
    image Defeated_Mercenary = "images/illustrations/Defeated_Mercenary.png"

init python:
    music_list = {}
    sound_list = {}

    sound_list["chapter1_and_2_sound_aaablaa"] = "sound/audio/chapter1_and_2_sound_aaablaa.mp3"
    sound_list["chapter1_sound_padenia"] = "sound/audio/chapter1_sound_padenia.mp3"
    sound_list["chapter1_sound_padenia_zemly"] = "sound/audio/chapter1_sound_padenia_zemly.mp3"
    sound_list["chapter1_sound_rungrass"] = "sound/audio/chapter1_sound_rungrass.mp3"
    sound_list["chapter1_sound_shot"] = "sound/audio/chapter1_sound_shot.mp3"
    sound_list["chapter1_sound_sirena"] = "sound/audio/chapter1_sound_sirena.mp3"
    sound_list["chapter2_sound_dusheroom"] = "sound/audio/chapter2_sound_dusheroom.mp3"
    sound_list["chapter1_sound_open_door"] = "sound/audio/chapter1_sound_open_door.mp3"
    sound_list["chapter1_sound_knockonthedoor"] = "sound/audio/chapter1_sound_knockonthedoor.mp3"
    sound_list["chapter1_sound_crunchingsticks"] = "sound/audio/chapter1_sound_crunchingsticks.mp3"

    music_list["death_note_alert_music"] = "sound/music/death_note_alert_music.mp3"
    music_list["death_note_ls_theme_b_music"] = "sound/music/death_note_ls_theme_b_music.mp3"
    music_list["game_music_003_dialogue"] = "sound/music/game_music_003_dialogue.ogg"
    music_list["game_music_006"] = "sound/music/game_music_006.mp3"
    music_list["main_menu_music"] = "sound/music/main_menu_music.mp3"
    music_list["main_menu_music_2"] = "sound/music/main_menu_music_2.mp3"