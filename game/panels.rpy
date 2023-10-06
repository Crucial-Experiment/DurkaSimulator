screen info_panel:
    frame:
        padding (12,10)
        xalign 0.95
        yalign 0.05
        xsize 250

        has vbox:
            xsize 250
            text _("Information")
            text _("Name: Mickey")
            text _("Status: [mikki_stats]")
            text _("Health: [mikki_health]%")

screen choose_language_panel:

    frame:
        padding (40,35)
        xalign 0.5
        yalign 0.5

        vbox:
            label "Select a language" xalign 0.5

            for cd, name in sorted(languages_panel.iteritems()):
                if cd != "english":
                    textbutton name action [Language(cd), Hide("choose_language_panel"), SetField(persistent, "lang_menu", True), Return('OK')] xalign 0.5
                else:
                    textbutton name action [Language(None), Hide("choose_language_panel"), SetField(persistent, "lang_menu", True), Return('OK')] xalign 0.5
