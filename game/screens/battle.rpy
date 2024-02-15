screen info_panel:
    frame:
        padding (12,10)
        xalign 0.015
        yalign 0.09

        vbox:
            xsize 240
            text _("Информация"):
                font gui.interface_text_font
                xalign 0.5
            text _("Имя: Микки"):
                font gui.interface_text_font
                xalign 0.5
            text _("Статус: [mickey_stats]"):
                font gui.interface_text_font
                xalign 0.5
            text _("Здоровье: [mickey_health]%"):
                font gui.interface_text_font
                xalign 0.5

screen info_panel_enemy:
    frame:
        padding (12,10)
        xalign 0.990
        yalign 0.09

        vbox:
            xsize 240
            text _("Информация"):
                font gui.interface_text_font
                xalign 0.5

            if battle_character == "mercenary":
                text _("Имя: Наемник"):
                    font gui.interface_text_font
                    xalign 0.5
            elif battle_character == "orderly":
                text _("Имя: Санитар"):
                    font gui.interface_text_font
                    xalign 0.5

            text _("Статус: Работник"):
                font gui.interface_text_font
                xalign 0.5

            if battle_character == "mercenary":
                text _("Здоровье: [mercenary_health]%"):
                    font gui.interface_text_font
                    xalign 0.5
            elif battle_character == "orderly":
                text _("Здоровье: [orderly_health]%"):
                    font gui.interface_text_font
                    xalign 0.5