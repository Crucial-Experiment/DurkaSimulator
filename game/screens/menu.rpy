screen main_menu_bg():
    $ state = "mm"
    
    add TrackCursor("gui/main menu/main_menu.png", 20)
    add TrackCursor("gui/main menu/main_menu_C.png", 13)
    add TrackCursor("gui/main menu/main_menu_A.png", 10)

    if is_event_sprite(new_year_start_date, new_year_end_date):
        add TrackCursor("gui/main menu/main_menu_B_yn.png", 7)
    else:
        add TrackCursor("gui/main menu/main_menu_B.png", 7)

screen main_menu():
    tag menu

    use main_menu_bg

    frame:
        style "main_menu_frame"

    use navigation

screen navigation():

    if renpy.get_screen("main_menu"):

        frame:
            background Frame( Transform("gui/frame.png", alpha=0.7) , gui.frame_borders, tile=gui.frame_tile)
            
            xalign 0.5
            yalign 0.5

            padding(180, 280)

            vbox:
                style_prefix "navigation"

                xalign 0.5
                yalign 0.5

                spacing gui.navigation_spacing

                if main_menu:
                    textbutton _("Начать") action ShowMenu("start_selection")
                else:
                    textbutton _("История") action ShowMenu("history")

                    textbutton _("Сохранить") action ShowMenu("save")

                textbutton _("Загрузить") action ShowMenu("load")

                if main_menu and not renpy.variant("mobile"):
                    textbutton _("DLC") action ShowMenu("dlc_menu")

                #textbutton _("Инвентарь") action ShowMenu("inventory_items")

                textbutton _("Настройки") action ShowMenu("preferences")

                if _in_replay:

                    textbutton _("Завершить повтор") action EndReplay(confirm=True)

                if not main_menu:
                    textbutton _("Главное меню") action MainMenu()

                #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                #    textbutton _("Помощь") action ShowMenu("help")

                if renpy.variant("pc"):

                    textbutton _("Выход") action Quit(confirm=not main_menu)

        hbox:
            xalign 0.5
            #xpos gui.navigation_xpos
            yalign 0.98
            spacing 8

            imagemap:
                idle "gui/media/discord_icon.png"
                if config.steam_appid == 0 and persistent.name and persistent.token:
                    hotspot (0, 0, 100, 100) action [GameJoltAPI.addAchieved(221112), OpenURL('https://discord.gg/RNzGSkGhqz')]
                else:
                    hotspot (0, 0, 100, 100) action [achievement.grant("WelcomeToCommunity"), achievement.sync(), OpenURL('https://discord.gg/RNzGSkGhqz')]

            imagemap:
                idle "gui/media/vk_icon.png"
                hotspot (0, 0, 100, 100) action OpenURL('https://vk.com/crucialexperim')

            imagemap:
                idle "gui/media/telegram_icon.png"
                hotspot (0, 0, 100, 100) action OpenURL('https://t.me/CrucialExperiment')

            imagemap:
                idle "gui/media/youtube_icon.png"
                hotspot (0, 0, 100, 100) action OpenURL('https://www.youtube.com/c/CrucialExperiment')

        if main_menu:
            add "gui/logo.png":
                xalign 0.5
                yalign 0.2

    else:

        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:
                textbutton _("Начать") action Start()
            else:
                textbutton _("История") action ShowMenu("history")

                textbutton _("Сохранить") action ShowMenu("save")

            textbutton _("Загрузить") action ShowMenu("load")

            if main_menu and not renpy.variant("mobile"):
                textbutton _("Модификации") action ShowMenu("modifications")

            textbutton _("Настройки") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("Завершить повтор") action EndReplay(confirm=True)

            if not main_menu:
                textbutton _("Главное меню") action MainMenu()

            #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            #    textbutton _("Помощь") action ShowMenu("help")

            if renpy.variant("pc"):

                textbutton _("Выход") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5

style main_menu_frame is empty
style main_menu_vbox is vbox

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

screen gamejolt_start_screen():
    frame:
        padding (12, 10)
        xalign 0.5
        yalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5

            vbox:
                text "Добро пожаловать, давайте настроим для вас Game Jolt API,\nчтобы получить все возможности игры?"
            
            null height 15

            hbox:
                textbutton "Отказаться" action MainMenu(confirm=False)
                null width 15
                textbutton "Согласиться" action Return()