screen dlc_menu():
    tag menu
    modal True

    use game_menu(_("DLC")):

        if new_image_dlc:
            textbutton _("Новый Образ"):
                action Start()
        else:
            if steam_running:
                text _("{a=steam_web_overlay:https://steamcommunity.com/app/1450150/workshop/}Новый Образ{/a}"):
                    xalign 0.5
                    yalign 0.5
            else:
                text _("{a=https://steamcommunity.com/app/1450150/workshop/}Новый Образ{/a}"):
                    xalign 0.5
                    yalign 0.5