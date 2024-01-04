screen modifications():

    tag menu
    modal True

    use game_menu(_("Модификации"), scroll="viewport"):

        style_prefix "modifications"

        if mods:
            viewport id "mods":
                draggable True
                mousewheel True
                scrollbars None
                yinitial 0.0

                has grid 1 len(mods)
                for lbl, name in sorted(mods.iteritems()):
                    textbutton name action (SetField(persistent, "jump_to", lbl), Start())
        else:
            if steam_running:
                text _("Похоже, что каталог модификаций пуст. Загрузите модификацию с {a=steam_web_overlay:https://steamcommunity.com/app/1450150/workshop/}Steam Workshop{/a} или с других сайтов.")
            else:
                text _("Похоже, что каталог модификаций пуст. Загрузите модификацию с {a=https://steamcommunity.com/app/1450150/workshop/}Steam Workshop{/a} или с других сайтов.")