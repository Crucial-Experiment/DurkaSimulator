label part1_home:

    scene redsquare_bg

    if config.steam_appid == 0 and persistent.name and persistent.token:
        $ GameJoltAPI.addAchieved(221021)
    else:
        $ achievement.grant("ChapterOne")
        $ achievement.sync()

    announcer "Эта история начинается в 2019 году."

    scene mickey_home_bg

    show mickey_happy at center with moveinleft

    announcer "В одном доме жил мальчик по имени Микки, до сегодняшнего дня он был самым обычным человеком."

    scene redsquare_bg with dissolve

    pause(1.0)

    announcer "4 месяца назад Микки и его друг Ларри окончили 9-й класс, после чего у них был выбор."
    
    menu:
        "Остаться до 11-го класса":

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221114)
            else:
                $ achievement.grant("ILoveSchool")
                $ achievement.sync()

            $ school_choose = True

            announcer "Немного подумав они выбрали остатся до 11-го класса."

            scene school_bg
            show mickey_back at left
            show larry_back at right
            with dissolve

            larry "Мне кажется, это плохая идея..."

            mickey "Не волнуйся, Ларь, все будет хорошо."

            larry "Как тут не волноваться? Мы опять в школу идем."

            mickey "Это конечно все же не очень, но у нас просто нету выхода."

            larry "Микки, выход всегда был."

            mickey "Давай просто забудем об этом?"

            larry "Хорошо, теперь давай войдем внутрь?"

        "Уйти после 9-го класса":

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221115)
            else:
                $ achievement.grant("IHateSchool")
                $ achievement.sync()

            $ school_choose = False

            announcer "Немного подумав они выбрали уйти после 9-го класса, и пойти в один колледж."

            scene college_admissions_bg
            show mickey_back at left
            show larry_back at right
            with dissolve

            larry "Я немного беспокоюсь по этому поводу."

            mickey "Не волнуйся, Ларь, все будет хорошо."

            larry "Ты говоришь так, будто это так просто."

            mickey "Для меня, да, я уже сталкивался с подобными случаями десятки раз."

            larry "Это как сказать..."

            "Ларри начал думать про себя"

            mickey "Ну что, я жду?"

            "Ларри продолжал молчать"

            larry "Давай просто забудем об этом?"

            mickey "Хорошо, теперь мы можем войти внутрь?"

    scene black with dissolve

    play sound sound_list["open_door_1"]

    pause(5.2)

    if school_choose:
        scene mickey_home2_bg 
    else:
        scene mickey_home_bg
    show mickey_happy
    with dissolve

    if school_choose:
        announcer "Неделю назад родители Микки уехали по своим делам, оставив его одного."
        announcer "В принципе, Микки живет очень хорошо, у него много денег, которые он получает от родителей."
    
        pause(0.4)

        mickey "Сегодня суббота, а это значит, что мне не нужно идти в школу!"
    
        hide mickey_happy
        show mickey_not_happy
        with dissolve

        mickey "Но нам дали кучу домашних заданий, которые я должен выполнить за эти два дня."
    else:
        announcer "Неделю назад Микки съехал от своих родителей."
        announcer "В принципе, Микки живет очень хорошо, у него много денег, которые он получает от родителей, и прекрасная квартира."

        pause(0.4)

        mickey "Сегодня суббота, а это значит, что мне не нужно идти в колледж!"

        hide mickey_happy
        show mickey_not_happy
        with dissolve

        mickey "Но нам задали кучу рефератов, которые я должен сделать за два дня."

    hide mickey_not_happy
    
    call add_inv_item(inv_notebook_item_id, show_item=True)
    
    show mickey_happy with dissolve

    mickey "Хотя я, наверное, спишу некоторые материалы из интернета."

    mickey "Начну что ли через часик или другой, а пока поиграю в плойку."

    play sound renpy.random.choice([sound_list["knock_door_1"], sound_list["knock_door_2"]])

    pause(2.1)

    hide mickey_happy
    show mickey_serious
    with dissolve

    show mickey_serious at left with moveinleft
    show mysterious_normal at right with moveinright

    mickey "Добрый день, чем я могу вам помочь?"

    mysterious "Нету времени объяснять, нам надо с вами срочно убегать отсюда!"
    mysterious "Мое имя Загадочный, и я агент спецслужб. Мне нужно вытащить тебя из этой квартиры, пока не стало слишком поздно!"

    play sound sound_list["journal_opening"]

    hide mysterious_normal
    hide mickey_serious
    show mysterious_credentials
    with dissolve

    "Загадочный достал свой значок."

    play sound sound_list["journal_closing"]

    hide mysterious_credentials
    show mickey_serious at left
    show mysterious_normal at right
    with dissolve

    mickey "Вы можете сначала сказать мне, что происходит?"

    mysterious "Боюсь, у нас мало времени на болтовню..."

    play sound sound_list["removing_the_pen_guard"]

    pause(0.8)

    play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

    pause(0.6)

    play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

    pause(0.6)

    play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

    pause(0.6)

    someone "Гражданин Микки, выходите во двор, у нас есть ордер на ваш арест!"

    play sound sound_list["door_knockout"]

    pause(4.0)

    hide mickey_serious
    show mickey_shouts at left
    with dissolve

    mickey "Что все это значит?!?"

    mysterious "Они уже здесь, нам нужно убегать!"

    mickey "Х-хорошо, я пойду с в-вами."

    scene black with dissolve

    play sound sound_list["steps"]

    pause(10.0)

    stop sound fadeout 1.0

    scene forest_bg
    show mickey_thinks at left
    show mysterious_normal at right
    with dissolve

    mysterious "Нам нужно бежать, пока они не поймали тебя, Микки."

    mickey "Откуда ты знаешь мое имя?"

    mysterious "Я же из СЗС, мы знаем все, а сейчас давай продолжать убегать?"

    play sound sound_list["twig_crunch"]

    pause (0.6)

    hide mickey_thinks
    show mickey_shouts at left
    with dissolve

    mickey "Т-ты это слышал!?"

    mysterious "Ты о чем?"

    mickey "Возможно, выстрел или л-ломание моей квартиры."

    hide mickey_shouts
    show mickey_not_happy at left
    with dissolve

    mickey "Там же много важных вещей: документы, телефон, деньги, компьютер... плойка."

    mysterious "Зачем тебе дома плойка для волос?"

    mickey "...{w=0.3}PlayStation"

    mysterious "Аааа..."

    scene black with dissolve

    announcer "Тем временем на базе нападавших."

    scene durka_base_bg with dissolve

    pause(0.2)

    show dir_durka_normal at center with moveinleft

    "Набирает номер группы Дельта."

    durka "Алё, группа дельта?"

    "Мы слушаем вас, вождь."

    durka "Найдите объект А и приведите его ко мне!"

    "Да, сэр!"

    "Вызов завершен."

    scene black with dissolve

    announcer "Тем временем наши герои добрались до секретной базы загадочного."

    play sound sound_list["opening_metal_door"]

    pause(7.4)

    scene mysterious_base_bg with dissolve

    show mysterious_normal at right with moveinright

    pause(0.4)

    show mickey_thinks at left with moveinleft

    mysterious "Добро пожаловать в мое логово."

    mickey "Почему бы тебе не рассказать мне, что происходит?"

    mysterious "Терпение, мой друг, терпение."

    scene black with dissolve

    mysterious "Все началось в далеком 2075 году, птицы пели, дети играли на улицах, а я, как всегда, собирался на работу."

    mysterious "Когда я пришел в офис, мне сразу сказали, что произошла телепортация из параллельной вселенной в нашу."

    mysterious "Нам сообщили, что они прибыли из параллельного мира под кодовым названием C-137."

    mysterious "После того, как прозвучал сигнал тревоги, они напали на нашу базу, и пока у нас были силы сражаться, мне сказали отправиться в 2020 год и придумать что-нибудь, что остановит их прибытие в 2075 году."

    mysterious "Но они раскусили наш план и сами отправились в 2020 год, чтобы остановить меня, но, как ты понимаешь, им это не удалось, и тогда они решили пойти ещё дальше и найти меня ещё молодым..."

    mickey "Итак, ты появились в 2019 году?"

    mysterious "Да, я искал их базу, я искал тебя, но в конце концов нашел только одного тебя."

    mysterious "Моих сил недостаточно, чтобы остановить их, и ты поможешь мне в этом."

    scene mysterious_base_bg
    show mysterious_normal at right
    show mickey_not_happy at left
    with dissolve

    mickey "А у нас есть хотя-бы какие-то шансы победить их?"
    mickey "Разве у нас с тобой есть какие-то шансы победить?"

    show screen info_panel with dissolve

    mysterious "Конечно, есть, потому что у меня есть ты!"

    hide mickey_not_happy
    show mickey_thinks at left
    with dissolve

    mickey "Я?"

    mysterious "Конечно, в тебе есть очень древняя сила, скрытая со времен монахов при Сталине!"

    $ mickey_stats = _("Монах")

    hide mickey_thinks
    show mickey_shouts at left
    with dissolve

    mickey "Какой монах, ты что курил?"

    mysterious "Я ничего не курил, ты действительно монах, ты просто не знаешь, как использовать свои способности."

    hide mickey_shouts
    show mickey_thinks at left
    with dissolve

    mysterious "Ладно, это пока ещё не главное, пойдем со мной, я тебе кое-что покажу."

    hide screen info_panel with dissolve

    hide mickey_thinks 
    hide mysterious_normal
    with easeoutleft

    scene mysterious_base_armory_bg with dissolve

    show mysterious_normal at right with moveinleft

    pause(0.2)

    show mickey_thinks at left with moveinleft

    mysterious "Это моя оружейная комната, в нем хранятся различные виды всевозможного оружия, в том числе одно от захватчиков."

    hide mickey_thinks
    show mickey_shouts at left
    with dissolve

    mickey "Вау, существует так много различных видов оружия, и с какого года ты все это собирал?"

    mysterious "Я начал эту коллекцию в 2063 году и закончил ее в 2019 году."

    hide mickey_shouts
    show mickey_thinks at left
    with dissolve

    mickey "Хорошо, у тебя есть план, как мы начнем вмешиваться в их дела?"

    mysterious "Обижаешь, конечно, у меня он есть, так что слушай."

    scene black with dissolve

    pause(0.4)

    scene durka_base_2_bg with dissolve

    mysterious "Мы натыкаемся на главный офис захватчиков или просто команды дурки."

    mickey "Вау, они уже успели построить офисы?"

    mysterious "Да, короче говоря, ты входишь в главный коридор и привлекаешь внимание санитара."

    mickey "Единственное, чего я не могу понять, это то, что в параллельной вселенной все были санитарами?"

    mysterious "Микки, откуда я могу знать?"

    mickey "Ладно, как мне определить, где находится этот главный коридор?"

    mysterious "У меня есть служебная карточка, которую я укра... одолжил у одного санитара."

    show durka_key_card with dissolve

    call add_inv_item(inv_key_card_item_id, show_item=True)

    mickey "Почему она вся в крови?"

    mysterious "Не обращай внимания, я просто ел варенье..."

    mickey "Послушай, но это не похоже на варенье, и по вкусу определенно не похоже на варенье."

    mysterious "Ты когда попробовать успел?"

    mysterious "Ладно, это не имеет значения, позволь мне продолжить рассказывать тебе о плане?"

    mickey "Конечно, но тогда ты скажешь мне, откуда взялась кровь на карточке доступа."

    mysterious "Ты входишь в главный коридор и привлекаешь внимание санитара."

    mickey "Как именно мне привлечь его внимание?"

    mysterious "Я не знаю, обзови его как-нибудь."

    show mickey_shouts at left with moveinleft

    mickey "Эй, ты в белом халате!"

    "Санитар обернулся злобно сморщив лицо."

    show orderly_normal at right with moveinright 

    mickey "Ты знаешь, что ты самый первый урод на Руси?"

    orderly "Как ты меня назвал?\nИди сюда, если ты такой храбрый"

    mysterious "Ты подходишь и начинаешь с ним драться, пока я делаю фотографии, чтобы прикрепить её к камере наблюдения."

    mickey "Я-я?"

    mysterious "А кто еще? Возьми себя в руки, Микки."

    hide mickey_shouts
    show mickey_serious at left
    with dissolve

    mickey "Д-давайте драться!"

    orderly "Ты думаешь, что ты сильнее меня?"
    orderly "Но я выиграю эту игру!"

    "Похоже, драка неизбежна."

    show screen info_panel with dissolve

    pause(0.7)

    scene black with dissolve

    hide screen info_panel with dissolve

    pause(0.4)

    scene mysterious_base_armory_bg
    show mickey_thinks at left
    show mysterious_normal at right
    with dissolve

    mysterious "Хм... Нет, ты слишком слаб, чтобы сражаться с ним, нужно что-то придумать..."

    "Загадочный произносит заклинания"

    mysterious "Авада кедавра!"

    hide mickey_thinks
    show mickey_not_happy at left
    with dissolve

    mickey "Это было заклинание из Гарри Поттера прямо сейчас?"

    mysterious "Это не имеет значения, просто таинственное прошлое, выходящее из меня."

    mysterious "Я бы сейчас все спел песней, но мы не в диснеевском мультфильме."

    mysterious "А теперь давай посмотрим на твои способности?"

    mickey "Может быть, в этом нет необходимости?"

    mysterious "Конечно нету... Покажи мне, давай."

    mickey "Л-ладно."

    "Микки пытается колдовать, но ничего не получается."

    mysterious "Мда... Я ожидал большего."

    mickey "Что нам тогда делать?"

    mysterious "Дай мне подумать..."

    "Загадочный думает о том, как усилить способности Микки."

    mysterious "Мы можем отправиться за камнями бесконечности, чтобы усилить твои способности!"

    hide mickey_not_happy
    show mickey_serious at left
    with dissolve

    mickey "Загадочный... Ты что, с ума сошел?!"

    mickey "Какие еще камни бесконечности?"

    mysterious "Ну, обычные камни."

    mickey "Скажите мне, когда ты в последний раз смотрели фильмы Marvel?"

    mysterious "Ну, примерно неделю назад, а что?"

    mickey "Ясно, ты сошел с ума."

    menu:
        "Что будет делать Микки дальше?"

        "Повернуться и сказать, что я ухожу":
            mickey "Ты какой-то странный. Я ухожу отсюда."

            hide mickey_serious at left with easeoutleft

            mysterious "Я говорю правду!"

            "Микки почти ушел, когда Загадочный крикнул."

            mysterious "Я знаю, кто ты на самом деле, Микки! Ты всегда встаешь ровно в 6 утра и идешь в колледж, ты никогда не пропускал его, хотя и хотел."

            "И Микки развернулся и пошел обратно."

            show mickey_shouts at left with moveinleft

            mickey "Кто ты, черт возьми, такой?"

            mysterious "Я не могу рассказать тебе все прямо сейчас, но скажу тебе кое-что."

            hide mickey_shouts
            show mickey_thinks at left
            with dissolve

            mickey "Я внимательно тебя слушаю."

            mysterious "Ты необычный парень, Микки, как и я, но ты не знаешь всей правды... Ты думаешь, я просто искал тебя? Как ты думаешь, захватчики тоже искали тебя, чтобы остановить меня по какой-то причине?"

            mysterious "Мы взаимно связаны, считай меня своим братом, который потерялся пару лет назад.\nЯ больше ничего не могу сказать, мне очень жаль..."

            mysterious "Прощай, Микки."

            "Загадочный повернулся и начал куда-то уходить."

            hide mysterious_normal at right with easeoutright

            hide mickey_thinks
            show mickey_shouts at left
            with dissolve

            mickey "Подожди, не уходи!"

            "Микки звал Загадочного, чтобы тот вернулся, но тот был уже слишком далеко."

            scene black with dissolve

            center_text "Один месяц спустя"

            pause(1.0)

            if school_choose:
                scene mickey_home2_bg 
            else:
                scene mickey_home_bg
            show mickey_not_happy
            with dissolve

            mickey "Прошел месяц, и я не могу забыть это Загадочного."

            mickey "Его характер был мне до боли знаком... Он был незабываемым, как будто я уже где-то его видел."

            "Недавно Микки отправился на то место, где раньше была база загадочного, но её там больше нет..."

            mickey "Загадочный, если ты слышишь меня, пожалуйста, вернись!"

            play sound renpy.random.choice([sound_list["knock_door_1"], sound_list["knock_door_2"]])

            "Громкий стук в парадную дверь."

            hide mickey_not_happy
            show mickey_happy at center
            with dissolve

            mickey "О-он вернулся!!!"

            play sound sound_list["open_door_1"]

            pause(5.2)

            show mickey_happy at left with easeoutleft
            show orderly_normal at right with moveinright

            mickey "Ч-что?!?"

            hide mickey_happy
            show mickey_shouts at left
            with dissolve

            orderly "Хехе, теперь ты наш."

            announcer "Увы, Микки не умеет драться, поэтому его забрали..."

            scene black with dissolve

            play sound sound_list["shackles"]

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221116)
            else:
                $ achievement.grant("WeHaveYouNow")
                $ achievement.sync()

            $ persistent.bad_ending_mys_missing = True

            center_text "Без загадочного он - ничто.\nКонцовка 1 / [endings]"

            stop sound fadeout 1.0

        "Поверить загадочному и пойти с ним":
            hide mysterious_normal
            show mysterious_angry at right
            with dissolve

            mysterious "Хватит придираться к моим словам!!!!"

            hide mickey_serious at left
            show mickey_shouts at left
            with dissolve

            mickey "Ладно-ладно, чё орать то?"

            mysterious "Надоел придираться к моим словам."

            hide mickey_shouts
            show mickey_thinks at left
            with dissolve

            mickey "Ну что же."

            mickey "Пошли за этими камнями бесконечности."

            pause(0.4)

            hide mysterious_angry at right
            show mysterious_normal at right
            with dissolve

            mysterious "Да, пошли."

            hide mickey_thinks at left with easeoutleft
            hide mysterious_normal at right with easeoutright
            scene black with dissolve

            announcer "И они отправились за первым камнем бесконечности."
            announcer "Их путь будет непростым, но они справятся (наверное)."

            if config.steam_appid == 0 and persistent.name and persistent.token:
                $ GameJoltAPI.addAchieved(221117)
            else:
                $ achievement.grant("SearchingForRocks")
                $ achievement.sync()

            scene forest_bg with dissolve
            show mickey_happy at left with moveinright
            show mysterious_normal at right with moveinright

            mickey "Куда мы пойдем сначала?"

            mysterious "В самое страшное место на Руси! В шестерочку!"

            hide mickey_happy
            show mickey_thinks at left
            with dissolve

            mickey "Там что, первый камень бесконечности?"

            mysterious "Нет просто нам нужен чай со слоником.\nШутка."

            mysterious "Камня там нету, но есть тот кто подскажет путь."

            mysterious "Ну тогда пошли?"

            hide mickey_thinks with easeoutleft
            hide mysterious_normal with easeoutleft

            scene black with dissolve
            pause(1.4)
            scene street_bg with dissolve

            show mickey_thinks at left with moveinleft
            show mysterious_normal at right with moveinright

            mysterious "Так, она должна быть где-то тут."

            mickey "Да вон же она нет?"

            mysterious "Да это она, заходим."

            hide mickey_thinks at left with easeoutleft
            hide mysterious_normal at right with easeoutright

            scene pyaterochka_lb2_bg with dissolve

            show mickey_thinks at left with moveinleft

            show mysterious_normal at right with moveinright

            mickey "И кого нам надо тут найти?"

            mysterious "Нам нужен менеджер и чай со слоником."

            mickey "Я пойду за чаем а ты найди менеджера."

            mysterious "Хорошо."

            menu:
                "Выберите, для кого показать историю?"

                "Микки":

                    if config.steam_appid == 0 and persistent.name and persistent.token:
                        $ GameJoltAPI.addAchieved(221102)
                    else:
                        $ achievement.grant("MickeysChoice")
                        $ achievement.sync()

                    hide mickey_thinks at left with easeoutleft

                    scene pyaterochka_lb1_bg with dissolve

                    show mickey_thinks at center with moveinleft

                    mickey "Так, где этот чай?"

                    mickey "А вот же он там на полке."

                    show mickey_thinks at left with moveinleft

                    show security_normal at right with moveinright

                    security "Молодой человек, пройдемте со мной."

                    mickey "Я?"

                    security "А кто же ещё?"

                    mickey "Зачем мне идти с вами?"

                    security "Мне сообщили что вы украли жвачку по рублю."

                    mickey "Но я только пришел, как я могу что-то украсть?"

                    security "Ничего не знаю пройдемте со мной."

                    show justapasserby_normal at center with moveinright

                    passer_all "Подождите, он ничего не украл, я посмотрела на него, как только он вошел!"

                    security "Мальчик иди отсюда."

                    passer_all "Он ничего не крал! Так в сценарии написали."

                    mickey "Какой ещё сценарий?"

                    passer_all "Ну обычный сценарий к этой игре..."

                    "В этот момент Микки подумал, что это снова какой-то чудак."

                    security "Ладно раз у тебя есть свидетель, значит ты этого не делал."

                    hide security_normal at right with easeoutright
                    show justapasserby_normal at right with moveinright

                    mickey "Спасибо тебе."

                    passer_all "Не за что я думаю мы ещё встретимся."

                    hide justapasserby_normal with dissolve
                    show mickey_thinks at center with moveinleft

                    hide mickey_thinks
                    show mickey_shouts at center
                    with dissolve

                    mickey "Не понял, а где он?"
                    mickey "Он что, взял и исчез?"

                    hide mickey_shouts
                    show mickey_not_happy at center
                    with dissolve

                    mickey "Мне бы так."

                    hide mickey_not_happy
                    show mickey_thinks at center
                    with dissolve

                    mickey "...Неважно."

                    mickey "Беру чай и иду к Загадочному."

                    hide mickey_thinks
                    with dissolve
                    
                    call add_inv_item(inv_tea_item_id, show_item=True)

                    show mickey_thinks
                    with dissolve

                    mickey "Интересно, он скажет мне свое имя когда-то?"

                    hide mickey_thinks with easeoutleft

                    scene pyaterochka_lb2_bg
                    show mysterious_normal at right
                    with dissolve

                    show mickey_thinks at left with moveinleft

                    mickey "Ну как, узнал куда идти?"

                    mysterious "Да, я узнал."

                    mickey "Тогда пошли?"

                "Загадочный":

                    if config.steam_appid == 0 and persistent.name and persistent.token:
                        $ GameJoltAPI.addAchieved(221101)
                    else:
                        $ achievement.grant("ChoosingTheUnknown")
                        $ achievement.sync()

                    hide mickey_thinks at left with easeoutleft

                    show mysterious_normal at center with moveinright

                    mysterious "Извините кассир."

                    show mysterious_normal at left with moveinleft
                    show cashier_normal at right with moveinright

                    cashier "Что вам надо?"

                    mysterious "Шоколада! Хахахаха."

                    cashier "Это какой то пранк?"

                    mysterious "Нет извините. Мне нужен ваш менеджер."

                    cashier "Хорошо, сейчас позову."

                    hide cashier_normal with easeoutright

                    cashier "Наташ, там тебя ищут."

                    manager "Скажи что я скоро подойду."

                    show cashier_normal at right with moveinright

                    cashier "Она скоро подойдет."

                    mysterious "Хорошо, я подожду."

                    hide cashier_normal with easeoutright

                    show justapasserby_normal at right with moveinright

                    passer_all "Здравствуйте, вы не знаете где тут можно купить чай?"

                    mysterious "Мне очень жаль, но я не знаю."

                    passer_all "Ладно, спасибо хотя бы за это."

                    hide justapasserby_normal with easeoutright

                    show manager_normal at right with moveinright

                    manager "Здравствуйте, чем я могу вам помочь?"

                    mysterious "Мне нужна подсказка до камня бесконечности."

                    manager "Мокки, сколько раз я просила не приходить в это место с такими просьбами?"

                    mysterious "Я снова забыл, но это срочно."

                    manager "Хорошо, тогда слушай."

                    manager "Далеко-далеко за горами есть одинокая деревня."

                    manager "В нем найдите одного старика, который покажет вам путь к первому камню бесконечности."

                    manager "А также, чтобы старик показал вам дорогу, скажите ему - Танос не ворует."

                    mysterious "Хорошо, спасибо."

                    manager "Береги себя, Мокки."

                    hide manager_normal with easeoutright

                    show mysterious_normal at center with moveinleft

                    mysterious "Хм, что за старик..."

                    mysterious "Ладно, не имеет значения, где Микки?"

                    show mysterious_normal at right with moveinright

                    show mickey_thinks at left with moveinleft

                    mickey "Ну как, узнал куда идти?"

                    mysterious "Да, я узнал."

                    mickey "Тогда пошли?"

            scene black with dissolve

            announcer "И они отправились в ту деревню."

            scene street_bg with dissolve
            show mysterious_normal at right with moveinright
            show mickey_thinks at left with moveinleft

            pause(0.5)

            mickey "Забыл спросить."

            mickey "А где это деревня находится?"

            mysterious "За горами."

            mickey "Интересно, чем будет добираться?"

            mysterious "Хмм...."

            mysterious "Маршруткой."

            scene black with dissolve

            play sound sound_list["steps_on_asphalt"]

            pause(4.2)

            stop sound fadeout 1.0

            scene trapping_bg
            show mysterious_normal at right
            show mickey_thinks at left
            with dissolve

            mickey "Надеюсь что маршрутка скоро приедет."

            mysterious "Я тоже."

            scene black with dissolve

            center_text "Спустя какое-то время"

            scene minibus_bg with dissolve

            mysterious "О, а вот и маршрутка приехала."

            pause(0.5)

            show mysterious_normal with moveinleft

            mysterious "Здравствуйте, вы едите до гор?"

            driver "Молодой человек, это маршрутка, а не автобус чтобы ехать куда-то далеко."

            mysterious "Ой..."

            mysterious "Ну ладно. Тогда подождём автобус."

            scene black with dissolve

            center_text "Спустя ещё какое-то время"

            scene bus_bg with dissolve

            "Зевание от скуки."

            show mysterious_normal with moveinleft

            mysterious "...Надеюсь это автобус, а не очередная маршрутка."

            pause(0.5)

            mysterious "Это автобус?"

            driver "Да."

            mysterious "..."

            mysterious "Боже, наконец-то."

            mysterious "Кхм-кхм."

            mysterious "Вы едите до гор?"

            driver "Конечно."

            mysterious "Микки, садимся!"

            mickey "Что, автобус приехал, и он едит до гор?"

            mysterious "Да."

            mickey "Ура, наконец-то!"

            hide mysterious_normal with easeoutright

            jump part1_village

    return