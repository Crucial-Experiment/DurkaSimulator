init -9 python:
    import steamapi

    is_night_version = True

    if not renpy.variant("mobile") and steamapi.Init():
        steam_running = True
        lang = steamapi.SteamApps().GetCurrentGameLanguage().decode("utf-8")
        print("Steam Game Language: " + lang)
        try:
            if lang != "russian":
                renpy.change_language(lang)
            else:
                renpy.change_language(None)
        except:
            print("Unable to update the game language")

        if is_night_version:
            _steamlib.add_item([2])

    else:
        steam_running = False

    languages = {}
    languages["english"] = _("Английский")
    languages["russian"] = _("Русский")

    languages_def = {}
    languages_def["english"] = _("English")
    languages_def["russian"] = _("Russian")

    if renpy.android:
        import jnius
        mActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity").mActivity
    else:
        mActivity = None

    def unlock_achievement(achievement_id):
        if mActivity:
            try:
                Games.Achievements.unlock(mActivity.getApiClient(), achievement_id)
            except Exception as e:
                print("Failed to unlock achievement:", str(e))

screen choose_language_panel:

    frame:
        padding (40,35)
        xalign 0.5
        yalign 0.5

        vbox:
            label "Select a language" xalign 0.5

            for cd, name in sorted(languages_def.iteritems()):
                if cd != "russian":
                    textbutton name action [Language(cd), Hide("choose_language_panel"), SetField(persistent, "lang_menu", True), Return('OK')] xalign 0.5
                else:
                    textbutton name action [Language(None), Hide("choose_language_panel"), SetField(persistent, "lang_menu", True), Return('OK')] xalign 0.5

screen preferences():
    tag menu

    use game_menu( _("Настройки") ):

        vbox:
            style_prefix "navigation"
            spacing gui.navigation_spacing

            textbutton _("Основные") action ShowMenu("all_preferences")

            if renpy.variant("pc") or renpy.variant("web"):
                textbutton _("Видео") action ShowMenu("video_preferences")

            textbutton _("Звук") action ShowMenu("sound_preferences")

screen all_preferences():
    tag menu
    modal True

    use game_menu( _("Настройки") ):

        vbox:
            ypos 50

            viewport:
                style_prefix "navigation"
                spacing gui.navigation_spacing

                draggable True
                mousewheel True
                scrollbars None
                yinitial 0.0

                xalign 0.5
                yalign 0.5

                xsize 180
                ysize 300

                vbox:

                    vbox:
                        style_prefix "radio"

                        label _("Пропуск")

                        textbutton _("Всего текста") action Preference("skip", "toggle")

                        textbutton _("После выборов") action Preference("after choices", "toggle")
                            
                        textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

                    null height (2 * gui.pref_spacing)

                    vbox:
                        style_prefix "radio"
                        label _("Язык")

                        if steam_running == True:
                            text _("Язык можно изменить в лаунчере, где была запущена игра")
                        else:
                            for cd, name in sorted(languages.iteritems()):
                                if cd != "russian":
                                    textbutton name action Language(cd)
                                else:
                                    textbutton name action Language(None)

                    null height (2 * gui.pref_spacing)

                    vbox:
                        label _("Скорость текста")
                        bar value Preference("text speed")

                        # label _("Скорость авточтения")
                        # bar value Preference("auto-forward time")

screen video_preferences():
    tag menu
    modal True

    use game_menu( _("Настройки") ):

        vbox:
            ypos 50

            viewport:
                style_prefix "navigation"
                spacing gui.navigation_spacing

                draggable True
                mousewheel True
                scrollbars None
                yinitial 0.0

                xalign 0.5
                yalign 0.5

                xsize 180
                ysize 300

                vbox:

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

screen sound_preferences():
    tag menu
    modal True

    use game_menu( _("Настройки") ):

        vbox:
            ypos 50

            viewport:
                style_prefix "navigation"
                spacing gui.navigation_spacing

                draggable True
                mousewheel True
                scrollbars None
                yinitial 0.0

                xalign 0.5
                yalign 0.5

                xsize 180
                ysize 300

                vbox:

                    vbox:

                        if config.has_music:
                            label _("Громкость музыки")

                            hbox:
                                bar value Preference("music volume")

                            null height (2 * gui.pref_spacing)

                        if config.has_sound:

                            label _("Громкость звуков")

                            hbox:
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Тест") action Play("sound", config.sample_sound)

                            null height (2 * gui.pref_spacing)

                        if config.has_voice:
                            label _("Громкость голоса")

                            hbox:
                                bar value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Тест") action Play("voice", config.sample_voice)

                            null height (2 * gui.pref_spacing)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Без звука"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox