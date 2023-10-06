#image inv_item_img = RemoteImage("https://i.ibb.co/CpyxQ7F/test-had.png")

screen inventory():
    tag menu

    modal True

    use game_menu(_("Инвентарь"), scroll="viewport"):
        style_prefix "inventory"

        $ items = _steamlib.get_inventory()

        for item in items:

            #$ inv_item_img = RemoteImage(item['icon_url'])

            #add inv_item_img size (50, 50) yalign 0.5

            vbox:
                if _preferences.language == None:
                    text item['name_russian'] color item['name_color']
                    text item['description_russian']
                else:
                    text item['name'] color item['name_color']
                    text item['description']
                #textbutton "Надеть" action Function(equip_item, item['itemdefid'], "mickey", "images/characters/zagadochnuy/zagadochnuy.png")
                text ""