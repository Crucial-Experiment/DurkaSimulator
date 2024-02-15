init:
    $ battle_character = None

    $ shaver_killer = False
    $ holy_killer = False
    $ kira_killer  = False

    $ rebar_xp = [25, 50, 100]
    $ homework_xp = [1, 3, 5, 7]
    $ shaver_xp = [50, 25, 75, 100]
    $ bible_xp = [50, 100, 75, 125]

    $ mercenary_health = 150
    $ mercenary_xp = [20, 25, 30, 10, 15, 5]

    $ orderly_health = 200
    $ orderly_xp = [20, 25, 30, 15, 40]

label game_battle:

    $ it_rebar = False
    $ it_homework = False
    $ it_shaver = False
    $ it_pass = False
    $ it_bible = False
    $ it_death_node = False

    if battle_character == "mercenary":
        if mercenary_health <= 0:
            $ renpy.jump(battle_label)
    
    elif battle_character == "orderly":
        if orderly_health <= 0:
            $ renpy.jump(battle_label)

    if mickey_health <= 0:
        jump game_over
    else:
        menu:
            "Выберите атаку, которую вы хотите использовать."

            "Арматура":
                $ it_rebar = True

            "Тетрадь с домашкой":
                $ it_homework = True

            "Тетрадь смерти" if kira_killer:
                $ it_death_node = True

            "Бритва" if shaver_killer:
                if config.steam_appid == 0 and persistent.name and persistent.token:
                    $ GameJoltAPI.addAchieved(221108)
                else:
                    $ achievement.grant("SweeneyTodd")
                    $ achievement.sync()

                $ it_shaver = True

            "Библия" if holy_killer:
                if config.steam_appid == 0 and persistent.name and persistent.token:
                    $ GameJoltAPI.addAchieved(221110)
                else:
                    $ achievement.grant("BiblicalMurder")
                    $ achievement.sync()

                $ it_bible = True                

            "Пропустить ход":
                $ it_pass = True  

    # Арматура
    if it_rebar:
        "Вы используете арматуру."

        $ random = renpy.random.choice(rebar_xp)

        if battle_character == "mercenary":
            $ mercenary_health -= random
            $ mercenary_health = max(0, mercenary_health)

        elif battle_character == "orderly":
            $ orderly_health -= random
            $ orderly_health = max(0, orderly_health)

        "Вы наносите [random] единиц урона."

    # Домашка
    elif it_homework:
        "Вы используете домашку."

        $ random = renpy.random.choice(homework_xp)

        if battle_character == "mercenary":
            $ mercenary_health -= random
            $ mercenary_health = max(0, mercenary_health)

        elif battle_character == "orderly":
            $ orderly_health -= random
            $ orderly_health = max(0, orderly_health)
            
        "Вы наносите [random] единиц урона."

    # Бритва
    elif it_shaver:
        "Вы используете бритву."

        $ random = renpy.random.choice(shaver_xp)

        if battle_character == "mercenary":
            $ mercenary_health -= random
            $ mercenary_health = max(0, mercenary_health)

        elif battle_character == "orderly":
            $ orderly_health -= random
            $ orderly_health = max(0, orderly_health)
            
        "Вы наносите [random] единиц урона."

    # Библия
    elif it_bible:
        "Вы используете библию."

        $ random = renpy.random.choice(bible_xp)

        if battle_character == "mercenary":
            $ mercenary_health -= random
            $ mercenary_health = max(0, mercenary_health)

        elif battle_character == "orderly":
            $ orderly_health -= random
            $ orderly_health = max(0, orderly_health)
            
        "Вы наносите [random] единиц урона."

    elif it_pass:
        "Вы пропускаете ход."
        "Вы наносите 0 единиц урона."

    # Если персонаж наемник
    if battle_character == "mercenary":
        $ random = renpy.random.choice(mercenary_xp)
        $ mickey_health -= random
        $ mickey_health = max(0, mickey_health)

        "Наёмник нанес вам [random] единиц урона."

    # Если персонаж санитар
    elif battle_character == "orderly":
        $ random = renpy.random.choice(orderly_xp)
        $ mickey_health -= random
        $ mickey_health = max(0, mickey_health)
        
        "Санитар нанес вам [random] единиц урона."

    jump game_battle

    return
