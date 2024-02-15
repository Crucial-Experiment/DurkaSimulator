screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        use main_menu_bg
    else:
        add gui.game_menu_background

    if main_menu and not renpy.get_screen("save") and not renpy.get_screen("load"):

        frame:
            #style "main_menu_frame"

            background Frame( Transform("gui/frame.png", alpha=0.7) , gui.frame_borders, tile=gui.frame_tile)
            
            xalign 0.5
            yalign 0.5

            padding(180, 380)

            if scroll == "viewport":

                vbox:
                    style_prefix "navigation"
                    spacing gui.navigation_spacing

                    xalign 0.5
                    yalign 0.5

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

            elif scroll == "vpgrid":

                vbox:
                    style_prefix "navigation"
                    spacing gui.navigation_spacing

                    xalign 0.5
                    yalign 0.5

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

            else:

                vbox:
                    style_prefix "navigation"
                    spacing gui.navigation_spacing

                    xalign 0.5
                    yalign 0.5

                    transclude

    else:

        frame:
            style "game_menu_outer_frame"

            hbox:
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            transclude

                    else:

                        transclude

        use navigation

    if main_menu and not renpy.get_screen("save") and not renpy.get_screen("load"):
        add "gui/logo.png":
            xalign 0.5
            yalign 0.2

        textbutton _("Вернуться"):
            xalign 0.5
            yalign 0.98
            action Return()
    else:
        textbutton _("Вернуться"):
            style "return_button"
            action Return()

    if not main_menu and renpy.get_screen("save") or renpy.get_screen("load"):
        label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -60