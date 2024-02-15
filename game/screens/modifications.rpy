screen modifications():
    tag menu
    modal True

    use game_menu(_("Модификации")):

        if mods:
            viewport id "mods":
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

                has grid 1 len(mods)
                for lbl, name in sorted(mods.iteritems()):
                    textbutton name:
                        action (SetField(persistent, "jump_to", lbl), Start())
        else:
            vbox:
                style_prefix "navigation"
                spacing gui.navigation_spacing

                if steam_running:
                    text _("Похоже, что каталог\nмодификаций пуст.\nЗагрузите\nмодификацию с\n{a=steam_web_overlay:https://steamcommunity.com/app/1450150/workshop/}Steam Workshop{/a}\nили с других сайтов."):
                        xalign 0.5
                        yalign 0.5
                else:
                    text _("Похоже, что каталог\nмодификаций пуст.\nЗагрузите модификацию с\n{a=https://steamcommunity.com/app/1450150/workshop/}Steam Workshop{/a}\nили с других сайтов."):
                        xalign 0.5
                        yalign 0.5