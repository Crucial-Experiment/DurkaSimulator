init python:
    import os

    def get_filename_from_url(url):
        filename = os.path.basename(url)
        name, extension = os.path.splitext(filename)
        return name

    def update_inventory_icon(server_icon):
        file_name = get_filename_from_url(server_icon)
        new_name = server_inventory_img.get(file_name, file_name)
        return new_name

    '''
    def update_steam_inventory():

        for server_item in server_data:

            if config.language != None:
                inventory[ server_item["name_en"] ] = {
                    "name": server_item["name_en"],
                    "description": server_item["description_en"],
                    "icon": update_inventory_icon( server_item["icon_url"] ),
                    "show_steam_btn": True,
                    **({"use": True} if "jacket" or "applies" in server_item.get("tags") else {}),

                    **({"use_type": "clothes"} if "jacket" in server_item.get("tags") else {}),
                    **({"use_type": "applies"} if "applies" in server_item.get("tags") else {}),

                    **({"clothes_variable": "mickey_prisoner_jacket"} if server_item.get("id") == "11" else {}),
                    **({"applies_type": "boom"} if server_item.get("id") == "13" else {}),
                }
            else:
                inventory[ server_item["name_en"] ] = {
                    "name": server_item["name_ru"],
                    "description": server_item["description_ru"],
                    "icon": update_inventory_icon( server_item["icon_url"] ),
                    "show_steam_btn": True,
                    **({"use": True} if "jacket" or "applies" in server_item.get("tags") else {}),

                    **({"use_type": "clothes"} if "jacket" in server_item.get("tags") else {}),
                    **({"use_type": "applies"} if "applies" in server_item.get("tags") else {}),

                    **({"clothes_variable": "mickey_prisoner_jacket"} if server_item.get("id") == "11" else {}),
                    **({"applies_type": "boom"} if server_item.get("id") == "13" else {}),
                }
    '''

label add_inv_item(item_id, show_item = True):

    if item_id["name"] in inventory:
        $ del inventory[item_id["name"]]

    $ inventory[ item_id["name"] ] = {
        "name": item_id["name"],
        "description": item_id["description"],
        "icon": item_id["icon"],
        "show_steam_btn": False,
        **({"use": item_id["use"]} if item_id.get("use") is not None else {}),
        **({"use_description": item_id["use_description"]} if item_id.get("use_description") is not None else {}),
        **({"use_type": item_id["use_type"]} if item_id.get("use_type") is not None else {})
    }

    if show_item:

        if item_id.get("sound") is not None:
            play sound sound_list[ item_id["sound"] ]       

        $ renpy.show(item_id["sprite"])
        $ renpy.with_statement(dissolve)

        $ renpy.say("", item_id['message'])

        if item_id.get("sound") is not None:
            stop sound fadeout 1.0

        $ renpy.hide(item_id["sprite"])
        $ renpy.with_statement(dissolve)

    return

label remove_inv_item(item_id):
    if item_id["name"] in inventory:
        $ del inventory[item_id["name"]]

label update_sprite_clothes(var_name = None):
    $ mickey_prisoner_jacket = False

    if var_name is not None:
        $ setattr(store, var_name, True)
    $ renpy.restart_interaction()

image inv_notebook = im.Scale("images/items/notebook.png", 64, 64)
image inv_shaver = im.Scale("images/items/shaver.png", 64, 64)
image inv_passport = im.Scale("images/items/passport.png", 64, 64)
image inv_key_card = im.Scale("images/items/key_card.png", 64, 64)
image inv_bible = im.Scale("images/items/bible.png", 64, 64)
image inv_tea = im.Scale("images/items/tea.png", 64, 64)

image inv_child_moon = im.Scale("images/items/steam_inv/Child of the Moon.png", 64, 64)
image inv_kitchen_knife = im.Scale("images/items/steam_inv/Kitchen Knife.png", 64, 64)
image inv_household_soap = im.Scale("images/items/steam_inv/Household soap.png", 64, 64)
image inv_prisoner_hat = im.Scale("images/items/steam_inv/Prisoner's Hat.png", 64, 64)
image inv_prisoner_jacket = im.Scale("images/items/steam_inv/Prisoner's Jacket.png", 64, 64)
image inv_remote_control_nuclear_weapons = im.Scale("images/items/steam_inv/Remote control for nuclear weapons.png", 64, 64)
image inv_vodka = im.Scale("images/items/steam_inv/Vodka.png", 64, 64)
image inv_warden_hat = im.Scale("images/items/steam_inv/Warden's Hat.png", 64, 64)
image inv_rose = im.Scale("images/items/steam_inv/rose_small.png", 64, 64)

init python early:

    inv_passport_item_id = {
        "name": _("Паспорт"),
        "description": _("Документ с вашим фото, которое менее похоже на вас, чем стикер в мессенджере. Печать – техника, не пойман - не вор!"),
        "icon": "inv_passport",

        "message": _("Паспорт получен."),
        "sprite": "mickey_passport",
        "sound": "item_received_1"
    }

    inv_key_card_item_id = {
        "name": _("Служебная карточка"),
        "description": _("Это служебная карточка, которую Микки получил от Загадочного во время рассказа истории."),
        "icon": "inv_key_card",

        "message": _("Достал карту доступа и переделал её Микки."),
        "sprite": "durka_key_card",
        "sound": "picked_up_an_item"
    }

    inv_notebook_item_id = {
        "name": _("Тетрадка с домашним заданием"),
        "description": _("Открываешь её, и вместо волшебства – домашнее задание. Все, никаких желаний."),
        "icon": "inv_notebook",

        "message": _("Получена 1 тетрадка с домашним заданием."),
        "sprite": "mickey_notebook",
        "sound": "item_received_1"
    }

    inv_shaver_item_id = {
        "name": _("Бритва"),
        "description": _("Может использоваться как оружие, но лучше использовать его по прямому назначению!"),
        "icon": "inv_shaver",

        "message": _("Получен 1 бритвенный станок."),
        "sprite": "mickey_shaver",
        "sound": "picked_up_an_item"
    }

    inv_tea_item_id = {
        "name": _("Упаковка с чаем"),
        "description": _("Индийский чай со слоником. В нем целебной силы есть секрет."),
        "icon": "inv_tea",

        "use": True,
        "use_type": "health",
        "use_description": "Восстанавливает 5-10 единиц здоровья",

        "message": _("Получена 1 упаковка с чаем."),
        "sprite": "shop_tea",
        "sound": "picked_up_an_item"
    }

    inv_bible_item_id = {
        "name": _("Библия"),
        "description": _("Эта книга была написана самим Богом и не может попасть в руки неверующих. Вы получили уникальный экземпляр этой книги! Продолжайте верить в Бога, и все будет хорошо."),
        "icon": "inv_bible",

        "message": _("Получена 1 книга с библией."),
        "sprite": "mickey_bible",
        "sound": "picked_up_an_item"
    }