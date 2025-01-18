label part1_village:

    scene bus_inside_bg with dissolve

    show mysterious_normal at right with moveinright
    show mickey_thinks at left with moveinleft

    mysterious "Скажите когда вы доедите до одинокой деревни, просто мы не знаем где это деревня."

    driver "Хорошо, скажу когда доедем до одинокой деревни."

    hide mysterious_normal
    hide mickey_thinks
    with dissolve

    scene bus_inside_c1_bg with dissolve

    pause(1.5)

    mickey "Прости что сегодня придирался к твоим словам."

    mickey "Не думай что я такой."

    pause(0.9)

    mickey "Просто ситуация не особо для меня понятна."

    mickey "Какие-то санитары решили навести тут шороху."

    mickey "Сила монаха с времён Сталина которая у меня есть."

    mickey "Война за планету в 2075 году."

    mickey "Какие-то камни бесконечности."

    mickey "И ты который прибыл из 2077 года."

    pause(2.1)

    mysterious "..."

    mysterious "Я понимаю."

    pause(1.5)

    mickey "Загадочный, давай о чём нибудь поговорим."

    mickey "А то скучно просто сидеть или смотреть в окно."

    mysterious "О чём поговорим?"

    mickey "Ну..."

    scene bus_inside_c2_bg with dissolve

    mickey "Давай про мемы поговорим."

    mysterious "Ну давай."

    scene bus_inside_c1_bg with dissolve

    mickey "Хмм..."

    scene bus_inside_c2_bg with dissolve

    mickey "Какие мемы у вас популярные в 2077 году."

    mysterious "Хмм..."

    mysterious "Юмор 21 века."

    mysterious "Вроде этот мем появился где-то в 2021 году."

    mysterious "Но каким-то чудом оно вновь стало популярным."

    mickey "О чём этот мем?"

    mysterious "К сожалению я не могу рассказать о чём оно."

    pause(0.2)

    mysterious "Но могу показать видео связанное с этим мемом."

    "Загадочный ищет что-то в своем кармане."

    mickey "У тебя есть телефон?"

    mysterious "Да."

    pause(0.9)

    mysterious "Так... Какой бы ты мем хотел увидеть?"

    $ ricroll_mem = False

    menu:
        "Вы можете выбрать, какой мем вы хотите увидеть."

        "Номер 1":
            mysterious "Теперь надо найти это видео."

            "Ищет видеоролик."

            mysterious "Нашел."

            mickey "Ну показывай."

            scene black with dissolve

            $ renpy.movie_cutscene("video/dancing_dog.webm")

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221118)
            else:
                $ achievement.grant("DancingDog")
                $ achievement.sync()

        "Номер 2":
            mysterious "Теперь надо найти это видео."

            "Ищет видеоролик."

            mysterious "Нашел."

            mickey "Ну показывай."

            scene black with dissolve

            $ renpy.movie_cutscene("video/dancing_bear.webm")

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221119)
            else:
                $ achievement.grant("DancingBears")
                $ achievement.sync()

        "Номер 3":
            mysterious "Теперь надо найти это видео."

            "Ищет видеоролик."

            mysterious "Нашел."

            mickey "Ну показывай."

            scene black with dissolve

            $ renpy.movie_cutscene("video/dancing_pirate.webm")

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221120)
            else:
                $ achievement.grant("DancingPirate")
                $ achievement.sync()

        "Номер 4":
            mysterious "Теперь надо найти это видео."

            "Ищет видеоролик."

            mysterious "Нашел."

            mickey "Ну показывай."

            scene black with dissolve

            $ ricroll_mem = True 

            $ renpy.movie_cutscene("video/Rick_Astley-Never_Gonna_Give_You_Up.webm")

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221121)
            else:
                $ achievement.grant("Ricroll")
                $ achievement.sync()

        "Номер 5" if is_event_sprite(new_year_start_date, new_year_end_date):
            mysterious "Теперь надо найти это видео."

            "Ищет видеоролик."

            mysterious "Нашел."

            mickey "Ну показывай."

            scene black with dissolve

            $ renpy.movie_cutscene("video/new_year_yes_and_no.webm")

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(253084)
            else:
                $ achievement.grant("ThereWillBeNoNewYear")
                $ achievement.sync()

    scene bus_inside_c2_bg with dissolve

    mickey "..."

    if ricroll_mem:
        mickey "Это сейчас был рикролл?"

        mysterious "Что такое рикролл?"

        mickey "..."

        mysterious "Для меня это мем с картинками, видео и звуком."
    else:
        mickey "Этот мем не имеет никакого смысла."

        mickey "Просто рандомные картинки, видео и звуки."

    pause(0.8)

    mysterious "А какие мемы у вас сейчас популярные."

    mickey "Не знаю."

    mickey "Особо за популярными мемами не наблюдаю."

    pause(0.2)

    mickey "Но могу рассказать, какие мемы я знаю."

    menu:
        "Выберите мем, который расскажет Микки."

        "Чи да?":
            mickey "Хмм..."

            scene bus_inside_c1_bg with dissolve

            mickey "Один из таких \"Чи да?\"."

            pause(0.5)

            mickey "Суть мема заключается в том что -\nЧувак с кепкой по имени Эдвард Бил."

            mickey "Подходит к случайным прохожим и говорит."

            mickey "Чи да? Чи или не чи?"

            mickey "Прохожие не понимают что он хочет."

            mickey "А Эдвард Бил всё также продолжает говорить - Чи да? Чи или не чи?"

            pause(0.5)

            mickey "В принципе всё."

            pause(0.3)

            mysterious "А этот Эдвард Бил подходил к пенсионерам."

            mickey "Не знаю."

            if not ricroll_mem:

                scene black with dissolve

                "Мы прерываем историю на маленькую музыкальную паузу."

                scene l_dn_bg with dissolve

                play music music_list["death_note_ls_theme_b_music"]

                if config.steam_appid == 0 and persistent.name and persistent.token:
                    $ GameJoltAPI.addAchieved(221103)
                else:
                    $ achievement.grant("LThisIsMe")
                    $ achievement.sync()

                pause(180.05)

                stop music fadeout 1.0

                scene bus_inside_c1_bg with dissolve

        "Камеру вырубай":
            mickey "Хмм..."

            scene bus_inside_c1_bg with dissolve

            mickey "Один из таких \"Камеру вырубай\"."

            mickey "Суть мема заключается в том что - \n Оператор снимает что-то, потом подходит охранник до оператора и говорит."

            mickey "Тут съёмка видео запрещена."

            mickey "Камеру вырубай."

            mickey "После этого говорит одно и тоже, но с обзыванием на адрес оператора."

            pause(0.2)

            mickey "А оператор как и не в чём не бывало продолжает снимать."

            mickey "А охранник всё также продолжает что-то говорить оператору."

            pause(0.2)

            mickey "Оператору видимо пофиг на охранника."

            pause(0.3)

            mickey "Но всё же оператор выключает камеру."

            pause(0.4)

            mickey "Впринципе всё."

    play sound sound_list["ambulance"] loop

    "Звук сирены."

    mickey "Сирена?"

    mysterious "Пригнись! Это санитары!"

    mickey "Как ты-"

    mysterious "Без вопросов!"

    mickey "Х-хорошо."

    scene durka_car_bg with dissolve

    orderly "Сэр, мы по всему городу его искали."

    orderly "И мы так и не нашли."

    pause(0.7)

    orderly "Пожалуйста сэр, не кричите."

    pause(1.0)

    orderly "..."

    orderly "Вызывайте подкрепление, чтобы стало немного легче найти того с голубой кофтой."

    pause (0.3)

    orderly "Что?"

    pause(0.5)

    orderly "Почему у нас работает сирена?"

    orderly "Ну у нас кнопка сирены сломалось."

    pause(0.5)

    orderly "Но сирена ещё пригодится сэр."

    pause(0.7)

    orderly "Вообщем. Позвоним когда найдём его."

    pause(0.7)

    orderly "Что?"

    orderly "Вы послали наёмника до одинокой деревне."

    orderly "Ну ладно."

    pause(1.5)

    orderly "Хорошо."

    orderly "Всё, досвидание."

    pause(0.3)

    "Вызов завершён."

    scene bus_inside_c1_bg with dissolve

    mysterious "Н-наёмник."

    mysterious "В одинокой деревне!"

    mickey "..."

    mickey "Когда мы начали говорить про мемы."

    mickey "На мгновение я забыл про этих санитаров и про всякое там."

    mickey "..."

    "Сигнал автобуса."

    driver "Выключите сирену!"

    orderly "Мы не можем выключить сирену."

    orderly "Кнопка сирены сломалось."

    mickey "Надеюсь нас не встретят санитары."

    mickey "Да и этот наёмник."

    mysterious "Я тоже надеюсь."

    stop sound fadeout 1.0

    scene black with dissolve

    center_text "Спустя 40 минут"

    scene bus_inside_c2_bg with dissolve

    driver "Приехали."

    mysterious "До одинокой деревни?"

    driver "Да."

    mysterious "...Я думал что реально там далеко-далеко."

    scene black with dissolve
    pause(1.2)
    scene forest_2_bg with dissolve

    show mysterious_normal at right with moveinright
    pause(0.6)
    show mickey_happy at left with moveinleft

    mickey "Наконец-то."

    mickey "Свежий воздух."

    mysterious "Ага, а то в автобусе было душно."

    hide mickey_happy at left with easeoutleft
    hide mysterious_normal at right with easeoutright

    scene lonely_village_bg with dissolve

    show mysterious_normal at right with moveinright
    show mickey_thinks at left with moveinleft

    mickey "У нас есть одна проблема."

    mysterious "Какая?"

    mickey "Мы не знаем в каком доме живёт этот старик."

    mysterious "..."

    mysterious "Блин, насчёт этого я не подумал."

    pause(0.3)

    mysterious "Хм..."

    mysterious "Что будем делать?"

    mickey "Давай будем спрашивать у прохожих."

    mysterious "Ок."

    pause(0.7)

    mickey "Поехали."

    mysterious "Может - Пошли?"

    mickey "Мы это, поправляем слова или спрашиваем у людей где этот дед?"

    mysterious "Ух какие серьёзные."

    hide mickey_thinks
    show mickey_serious at left

    mickey "..."

    mysterious "Ладно-ладно."

    mysterious "Пошли спрашивать."

    hide mickey_serious
    show mickey_thinks at left
    with dissolve

    hide mickey_thinks with easeoutleft
    hide mysterious_normal with easeoutleft

    scene black with dissolve
    pause(1.2)
    scene forest_2_bg with dissolve

    show mysterious_normal at center with moveinleft
    show mickey_thinks at left with moveinleft

    mickey "О, вижу кого-то."

    mysterious "Будем спрашивать?"

    mickey "Да."

    pause(0.5)

    show justapasserby_normal at right with moveinright

    pause(0.6)

    passer_all "Привет."

    hide mickey_thinks
    show mickey_shouts at left

    mickey "А что ты тут делаешь?"

    passer_all "Дела."

    mysterious "А вы с ним знакомы?"

    passer_all "Да."

    passer_all "В шестёрочке встретились."

    hide mickey_shouts
    show mickey_thinks at left
    with dissolve

    mickey "Вообщем."

    mickey "Перейдём к теме."

    mickey "Ты знаешь где живёт дед который знает где камни бесконечности?"

    passer_all "Прости, я тут только первый раз."

    mickey "Жаль."

    mickey "Ну спасибо хотя бы за это."

    mickey "Пока."

    passer_all "Пока."

    hide justapasserby_normal at right with easeoutright

    mickey "Подожди!"

    show justapasserby_normal at right with moveinright

    passer_all "Что?"

    mickey "А как тебя зовут?"

    passer_all "Меня зовут Ваня."

    hide mickey_thinks
    show mickey_happy at left

    mickey "А моё имя Микки."

    mysterious "А моё имя..."

    mysterious "..."

    mysterious "Не буду говорить."

    hide mickey_happy
    show mickey_thinks at left

    mickey "А почему?"

    mysterious "Потому что потому."

    passer_all "Ладно. Не буду задерживаться."

    mickey "Пока."

    hide justapasserby_normal with easeoutright
    show mysterious_normal at right with moveinright

    pause(1.0)

    mickey "Реально."

    mickey "Почему ты не сказал своё имя?"

    mysterious "Мне это сложно объяснить."

    pause(0.8)

    mickey "Ладно. Пошли следующего спрашивать."

    hide mickey_thinks with easeoutright
    hide mysterious_normal with easeoutright

    show lonely_village_bg with dissolve

    show mysterious_normal at center with moveinleft
    show mickey_thinks at left with moveinleft

    mysterious "Надеюсь хоть этот знает."

    mysterious "Эй, подойди сюда."

    mickey "Загадочный, а что ты так говоришь?"

    mysterious "Просто хочу уже побыстрее"

    show yura_normal at right with moveinright

    passer_all "О, еще новенькие, давайте знакомиться."

    passer_all "Я Юра, а вас как?"

    mysterious "Спасибо что с нами гостеприимно знакомишься."

    mysterious "Но можешь сказать где дед который знает где камни бесконечности."

    passer_all "Хм..."

    passer_all "Вроде идти вперёд, потом повернуть и дойти до 6-го дома."

    mysterious "Спасибо."

    passer_all "Не за что."

    hide yura_normal at right with easeoutright
    show mysterious_normal at right with moveinright

    hide mickey_thinks
    show mickey_happy at left
    with dissolve

    mickey "Пошли."

    hide mickey_happy at left with easeoutleft
    hide mysterious_normal at right with easeoutright

    show black with dissolve

    center_text "Спустя какое-то время"

    scene lonely_village_2_bg with dissolve

    show mysterious_normal at right with moveinright
    show mickey_thinks at left with moveinleft

    play sound renpy.random.choice([sound_list["knock_door_1"], sound_list["knock_door_2"]])

    "Стук в парадную дверь."

    grandfather "Кто там?"

    show mysterious_normal at center with moveinright
    show old_man_normal at right with moveinright

    mickey "Я Микки, а это загадочный."

    hide old_man_normal
    show old_man_thinks at right
    with dissolve

    grandfather "У него такое имя?"

    mickey "Нет. Просто-"

    hide old_man_thinks
    show old_man_normal at right
    with dissolve

    mysterious "Неважно."

    mysterious "Короче."

    mysterious "Танос не ворует."

    grandfather "..."

    grandfather "Проходите. Дома расскажу где камни бесконечности."

    hide old_man_normal with easeoutright
    hide mickey_thinks with easeoutright
    hide mysterious_normal with easeoutright

    scene grandfather_home_bg with dissolve

    show old_man_normal at right with moveinright
    show mysterious_normal at center with moveinright
    show mickey_thinks at left with moveinright

    hide old_man_normal
    show old_man_thinks at right
    with dissolve

    grandfather "А как ты узнал эту фразу?"

    mysterious "Узнал у менеджера из шестерочке."

    grandfather "...Ладно."

    hide old_man_thinks
    show old_man_normal at right
    with dissolve

    grandfather "Дайка вспомнить."

    pause(1.4)

    grandfather "Вспомнил."

    grandfather "Кхм-кхм."

    pause(0.9)

    grandfather "Первый и второй камень бесконечности находятся в Сочи, а именно на пляже \"Светлячок\"."

    mysterious "Эм..."

    mysterious "Серьёзно?"

    grandfather "Да, я абсолютно серьезен."

    show old_man_normal at right with moveinright
    show mysterious_normal at right with moveinright:
        xalign 0.7 yalign 1.0
    show grandma_normal with moveinleft:
        xalign 0.35 yalign 1.0

    granny "О чём говорите?"

    grandfather "О камнях бесконечности."

    granny "..."

    granny "Опять ты со своими камнями!"

    granny "Это просто чушь, которую вы вешаете всем на уши!"

    grandfather "..."

    grandfather "Камни бесконечности и вправду существуют!"

    hide old_man_normal
    show old_man_serious at right
    with dissolve

    granny "Ну давай принеси эти камни, тогда и поверю."

    play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

    pause(0.6)

    play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

    pause(0.6)

    play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

    pause(0.6)

    hide mickey_thinks
    show mickey_shouts at left
    with dissolve

    mysterious "Бежим."

    scene black with dissolve

    scene lonely_village_bg with dissolve

    show mercenary_anim with moveinleft

    mercenary "Я опять промахнулся, вождь дурки убьет меня..."

    pause(0.4)

    mercenary "Так, а где они?"

    scene black with dissolve

    play sound sound_list["punch"]

    pause(0.3)

    play sound sound_list["fall"]

    pause(0.7)

    scene lonely_village_bg
    show mickey_serious
    with dissolve

    mickey "Повезло, что рядом валялась арматура."

    mickey "Так, он ещё живой?"

    pause(0.8)

    mickey "Видимо нет."

    show mickey_serious at left with moveinleft
    show mercenary_anim at right with dissolve

    hide mickey_serious
    show mickey_shouts at left
    with dissolve

    mickey "Как, черт возьми, ты еще жив после такого сильного удара?!"

    mercenary "Я сам не знаю, но это хороший повод убить тебя."
    mercenary "Вообщем..."
    mercenary "Твой путь к камням бесконечностям закончится тут!"

    hide mickey_shouts
    show mickey_serious at left
    with dissolve

    $ battle_character = "mercenary"
    $ battle_label = "part2_village"

    show screen info_panel
    show screen info_panel_enemy
    with dissolve
    
    jump game_battle

    return