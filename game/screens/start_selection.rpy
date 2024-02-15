screen start_selection():

    tag menu

    use game_menu(""):

        vbox:
            style_prefix "navigation"
            spacing gui.navigation_spacing

            textbutton _("Продолжить") action Continue()

            textbutton _("Новая игра") action Start()

            textbutton _("Эпизоды") action ShowMenu("gm_episode")

            if sp_episodes:
                textbutton _("Спец. Эпизоды") action ShowMenu("sp_episode")
            else:
                textbutton _("Спец. Эпизоды")

screen gm_episode():
    tag menu
    modal True

    use game_menu(""):

        viewport id "gm_episodes":
            style_prefix "navigation"
            spacing gui.navigation_spacing

            draggable True
            mousewheel True
            scrollbars None
            yinitial 0.0

            xalign 0.5
            yalign 0.5

            xsize 180
            ysize 180

            has grid 1 len(gm_episodes)
            for lbl, name in sorted(gm_episodes.iteritems()):
                if lbl != "start":
                    textbutton name:
                        action ( SetField(persistent, "jump_to", lbl), Start() )
                else:
                    textbutton name:
                        action Start()

screen sp_episode():
    tag menu
    modal True

    use game_menu(""):

        viewport id "sp_episodes":
            style_prefix "navigation"
            spacing gui.navigation_spacing

            draggable True
            mousewheel True
            scrollbars None
            yinitial 0.0

            xalign 0.5
            yalign 0.5

            xsize 180
            ysize 180

            has grid 1 len(sp_episodes)
            for lbl, name in sorted(sp_episodes.iteritems()):
                if lbl != "start":
                    textbutton name:
                        action ( SetField(persistent, "jump_to", lbl), Start() )
                else:
                    textbutton name:
                        action Start()