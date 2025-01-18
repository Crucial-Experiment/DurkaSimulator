screen dlc_menu():
    tag menu
    modal True

    use game_menu(_("DLC")):

        if new_image_dlc:
            textbutton _("Новый Образ"):
                action Start()
        else:
            if steam_running:
                text _("{a=steam_web_overlay:https://store.steampowered.com/app/1540040/Novyj_Obraz__Durka_Simulator/}Новый Образ{/a}"):
                    xalign 0.5
                    yalign 0.5
            else:
                text _("{a=https://store.steampowered.com/app/1540040/Novyj_Obraz__Durka_Simulator/}Новый Образ{/a}"):
                    xalign 0.5
                    yalign 0.5