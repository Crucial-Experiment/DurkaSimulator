screen inventory_button():

    frame:
        padding (30, 5)

        textbutton _("Инвентарь"):
            action ( ToggleScreen("inventory"), ToggleScreen("inventory_item_info") )

screen inventory():

    frame:
        yalign 0.12
        padding(30, 30)

        viewport id "inventory":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 0.0

            xsize 220
            ysize 220

            vpgrid:
                cols 3
                spacing 10

                mousewheel True
                scrollbars None
                draggable True

                for item_name, item_data in sorted(inventory.items()):
                    if item_data is not None:
                        imagebutton:
                            idle item_data["icon"]
                            hovered Show("inventory_item_info", transition=None, item_data = item_data)
                            action NullAction()

screen inventory_item_info(item_data = None):

        frame:

            yalign 0.12
            xpos 290
            padding(30, 30)

            viewport id "inventory":
                draggable True
                mousewheel True
                scrollbars None
                yinitial 0.0

                xsize 220
                ysize 220

                vbox:

                    if item_data is not None:

                        if item_data["name"] is not None:
                            label item_data["name"]
                        else:
                            label "Тестовый предмет"

                        null height 10
                        
                        if item_data["description"] is not None:
                            text item_data["description"]
                        else:
                            text "Описание тестового предмета"

                        if item_data.get("use") is not None and item_data["use"] == True:

                            null height 10

                            if item_data.get("use_description") is not None:
                                text item_data["use_description"]

                            null height 10

                            if item_data.get("use_type") is not None:

                                if item_data.get("use_type") is "health":
                                    textbutton _("Использовать") sensitive (mickey_health < 100) action If(mickey_health != 100, [
                                        SetVariable("mickey_health", min(mickey_health + renpy.random.randint(5, 11), 100)),
                                        Call("remove_item_from_inventory", item_data["name"])
                                    ])

                                elif item_data.get("use_type") is "clothes":

                                    if eval(item_data["clothes_variable"]):
                                        textbutton _("Снять") action Call("update_sprite_clothes", None)
                                    else:
                                        textbutton _("Экипировать") action Call("update_sprite_clothes", item_data["clothes_variable"])

                                elif item_data.get("use_type") is "applies":

                                    if item_data.get("applies_type") is not None and item_data.get("applies_type") is "boom":

                                        textbutton _("Использовать") action [ Play("sound", "sound/audio/nuclear_bomb.mp3"), Jump("game_over") ]