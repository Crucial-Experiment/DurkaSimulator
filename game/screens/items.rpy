screen inventory_items():

    python:
        import requests, shutil, os

        for name, item in items.items():
            images_directory = config.gamedir + "/images/items/steam_inv/"
            filename = item['name'] + ".png"

            filepath = os.path.join(images_directory, filename)

            response = requests.get(item['icon_url'], stream=True)
            response.raise_for_status()   

            with open(filepath, "wb") as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)

            del response

    tag menu

    use game_menu(_("Инвентарь"), scroll="viewport"):
        for name, item in items.items():
            hbox:
                frame:
                    hbox:
                        xsize 890
                        yalign 0.5

                        add "images/items/steam_inv/" + item['name'] + ".png" size(84, 84)

                        vbox:
                            text item['name_ru']:
                                color item['color']
                            text item['description_ru']

            null height (2 * gui.pref_spacing)