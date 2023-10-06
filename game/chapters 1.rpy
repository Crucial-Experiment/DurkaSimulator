label cp1_a1:

    $ achievement.grant("ChapterOne")
    init:
        $ achievement.register("ChapterOne")
        $ achievement.sync()

    $ achievement.sync()

    scene Redsquare with dissolve

    dictor "Наша история начинается в 2019 году"

    scene Mikki_House with dissolve

    show mikki_happy_image at center with moveinleft

    dictor "В одном доме жил мальчик по имени Микки, до сегодняшнего дня он был самым обычным человеком"

    hide mikki_happy_image with dissolve

    scene black with dissolve

    pause(1.0)

    dictor "4 месяца назад Микки и его друг Ларри окончили 9-й класс. После этого у них был выбор: остаться до 11-го класса или уйти после 9-го класса."

    dictor "Немного подумав они выбрали первый вариант, и решили пойти в один колледж"

    scene college_admissions with dissolve

    pause(0.6)

    larry "Я немного беспокоюсь по этому поводу."

    mikki "Не волнуйся, Ларь, все будет хорошо."

    larry "Ты говоришь так, будто это так просто."

    mikki "Для меня, да, я уже сталкивался с подобными случаями десятки раз."

    larry "Это как сказать... *Ларри начал думать про себя*"

    mikki "Ну что, я жду?"

    larry "*Ларри продолжал молчать*"

    larry "Давай просто забудем об этом?"

    mikki "Хорошо, теперь мы можем войти внутрь?"

    scene black with dissolve

    play sound sound_list["chapter1_sound_open_door"]

    pause(1.5)

    dictor "Неделю назад Микки съехал от своих родителей."

    dictor "В принципе, Микки живет очень хорошо, у него много денег, которые он получил от родителей, и прекрасная квартира."

    pause(1.0)

    scene Mikki_House with dissolve

    show mikki_happy_image at center with dissolve

    mikki "Сегодня суббота, а это значит, что мне не нужно идти в колледж!"

    hide mikki_happy_image

    show mikki_not_happy_image at center

    #Но нам дали кучу домашних заданий, которые я должен выполнить за эти два дня.
    mikki "Но нам задали кучу рефератов, которые я должен сделать за два дня."

    hide mikki_not_happy_image

    show mikki_happy_image at center

    mikki "Хотя я, наверное, спишу некоторые материалы из интернета."

    mikki "Начну через пару часов, а пока пойду поиграю в плойку."

    play sound sound_list["chapter1_sound_knockonthedoor"]

    "*Громкий стук в парадную дверь*"

    hide mikki_happy_image

    show mikki_serious_image at center

    show mikki_serious_image at left with moveinleft

    show zagadochnuy_image at right with moveinright

    mikki "Добрый день, чем я могу вам помочь?"

    zagadochnuy "Нету времени объяснять, нам надо с вами срочно убегать отсюда!"

    zagadochnuy "Мое имя Загадочный, и я агент спецслужб. Мне нужно вытащить тебя из этой квартиры, пока не стало слишком поздно!"

    "*Загадочный достал свой значок*"

    mikki "А что происходит?"

    play sound sound_list["chapter1_sound_shot"]

    pause(0.5)

    stop sound fadeout 1.0

    "Гражданин Микки, выходите во двор, у нас есть ордер на ваш арест!"

    hide mikki_serious_image

    show mikki_shouts_image at left

    mikki "Что все это значит?!?"

    zagadochnuy "Они уже здесь, нам нужно убегать!"

    play sound sound_list["chapter1_sound_shot"]

    pause(0.5)

    stop sound fadeout 1.0

    mikki "Х-хорошо, я пойду с в-вами."

    hide mikki_shouts_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene black with dissolve

    play sound sound_list["chapter1_sound_rungrass"]

    pause(6.0)

    stop sound fadeout 1.0

    scene Forest with dissolve

    show zagadochnuy_image at right with moveinleft

    pause(0.6)

    show mikki_thinks_image at left with moveinleft

    zagadochnuy "Нам нужно бежать, пока захватчики не поймали тебя, Микки."

    mikki "Откуда ты знаешь мое имя?"

    zagadochnuy "Позволь мне рассказать тебе все позже, а сейчас нам лучше продолжать убегать."

    hide mikki_thinks_image

    show mikki_shouts_image at left

    play sound sound_list["chapter1_sound_crunchingsticks"]

    pause (0.6)

    stop sound fadeout 1.0

    mikki "Т-ты это слышал!?"

    zagadochnuy "О чем ты говоришь?"

    mikki "Возможно, выстрел или л-ломание моей квартиры."

    hide mikki_shouts_image

    show mikki_not_happy_image at left

    pause(1.0)

    mikki "Там же много важных вещей: документы, телефон, компьютер... плойка."

    zagadochnuy "Что ты там бормочешь себе под нос?"

    mikki "А не обращай внимания."

    hide mikki_not_happy_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene black with dissolve

    dictor "Тем временем на главной базе захватчиков."

    scene DurkaBase with dissolve

    pause(0.2)

    show durka_image at center with moveinleft

    "*Набирает номер группы Дельта*"

    durka "Алё, группа дельта?"

    "Мы слушаем вас, командир."

    durka "Найдите объект А и приведите его ко мне!"

    "Да, сэр!"

    "*Вызов завершен*"

    hide durka_image at center with easeoutright

    scene black with dissolve

    dictor "Тем временем наши герои добрались до секретной базы неизвестного."

    scene ZagadochnuyBase with dissolve

    show zagadochnuy_image at right with moveinright

    pause(0.6)

    show mikki_thinks_image at left with moveinleft

    zagadochnuy "Пока они не знают, где мы, я расскажу тебе одну историю."

    mikki "Зачем мне твои истории, что происходит, лучше расскажи мне!"

    zagadochnuy "Терпение, мой друг, терпение."

    hide zagadochnuy_image at right with dissolve

    hide mikki_thinks_image at left with dissolve

    scene black with dissolve

    zagadochnuy "Все началось в далеком 2075 году, птицы пели, дети играли на улицах, а я, как всегда, собирался на работу."

    zagadochnuy "Когда я пришел в офис, мне сразу сказали, что произошла телепортация из параллельной вселенной в нашу."

    zagadochnuy "Нам сообщили, что они прибыли из параллельного мира под кодовым названием C-137."

    zagadochnuy "После того, как прозвучал сигнал тревоги, они напали на нашу базу, и пока у нас были силы сражаться, мне сказали отправиться в 2020 год и придумать что-нибудь, что остановит их прибытие в 2075 году."

    zagadochnuy "Но они раскусили наш план и сами отправились в 2020 год, чтобы остановить меня, но, как ты понимаешь, им это не удалось, и тогда они решили пойти ещё дальше и найти меня ещё молодым..."

    mikki "Итак, ты появились в 2019 году?"

    zagadochnuy "Да, я искал их базу, я искал тебя, но в конце концов нашел только одного тебя."

    zagadochnuy "Моих сил недостаточно, чтобы остановить их, и ты поможешь мне в этом."

    scene ZagadochnuyBase with dissolve

    show zagadochnuy_image at right with dissolve

    show mikki_not_happy_image at left with dissolve

    mikki "А у нас есть хотя-бы какие-то шансы победить их?"

    mikki "Разве у нас с тобой есть какие-то шансы победить?"

    show screen info_panel with dissolve

    zagadochnuy "Конечно, есть, потому что у меня есть ты!"

    hide mikki_not_happy_image at left

    show mikki_thinks_image at left

    mikki "Я?"

    zagadochnuy "Конечно, в тебе есть очень древняя сила, скрытая со времен монахов при Сталине!"

    $ mikki_stats = _("Монах")

    hide mikki_thinks_image at left

    show mikki_shouts_image at left

    #Какой, к черту, монах? Что ты курил?
    mikki "Какой монах ты что курил?"

    zagadochnuy "Я ничего не курил, ты действительно монах, ты просто не знаешь, как использовать свои способности."

    hide mikki_shouts_image

    show mikki_thinks_image at left

    zagadochnuy "Ладно, это пока ещё не главное, пойдем со мной, я тебе кое-что покажу."

    hide screen info_panel with dissolve

    hide mikki_thinks_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene mysterious_base_armory_bg with dissolve

    show zagadochnuy_image at right with moveinright

    pause(0.1)

    show mikki_thinks_image at left with moveinleft

    zagadochnuy "Это моя оружейная комната, в нем хранятся различные виды всевозможного оружия, в том числе одно от захватчиков."

    hide mikki_thinks_image at left

    show mikki_shouts_image at left

    mikki "Вау, существует так много различных видов оружия, и с какого года ты все это собирал?"

    zagadochnuy "Я начал эту коллекцию в 2063 году и закончил ее в 2019 году."

    hide mikki_shouts_image at left

    show mikki_thinks_image at left

    mikki "Хорошо, у тебя есть план, как мы начнем вмешиваться в их дела?"

    zagadochnuy "Обижаешь, конечно, у меня он есть, так что слушай."

    hide mikki_thinks_image at left with dissolve

    hide zagadochnuy_image at right with dissolve

    scene Hallway1 with dissolve

    zagadochnuy "Мы натыкаемся на главный офис захватчиков или просто команда дурки."

    mikki "Вау, они уже успели построить офисы?"

    zagadochnuy "Да, короче говоря, ты входишь в главный коридор и привлекаешь внимание санитара."

    mikki "Единственное, чего я не могу понять, это то, что в параллельной вселенной все были санитарами?"

    zagadochnuy "Микки, откуда я могу знать?"

    mikki "Ладно, как мне определить, где находится этот главный коридор?"

    zagadochnuy "У меня есть служебная карточка, которую я укра... одолжил у одного санитара."

    "*Достал карту доступа и переделал её Микки*"

    mikki "Почему она вся в крови?"

    zagadochnuy "А не обращай внимания, я просто ел варенье..."

    mikki "Послушай, но это не похоже на варенье, и по вкусу определенно не похоже на варенье."

    zagadochnuy "Ты когда попробовать успел?"

    zagadochnuy "Ладно, это не имеет значения, позволь мне продолжить рассказывать тебе о плане?"

    mikki "Конечно, но тогда ты скажешь мне, откуда взялась кровь на карточке доступа."

    zagadochnuy "Ты входишь в главный коридор и привлекаешь внимание санитара."

    mikki "Как именно мне привлечь его внимание?"

    zagadochnuy "Я не знаю, обзови его как-нибудь."

    show mikki_shouts_image at left with moveinleft

    mikki "Эй, ты в белом халате!"

    "*Санитар обернулся злобно сморщив лицо*"

    mikki "Ты знаешь, что ты самый первый урод на Руси?"

    show orderly_image at right with moveinright

    orderly "Как ты меня назвал?\nИди сюда, если ты такой храбрый"

    zagadochnuy "Ты подходишь и начинаешь с ним драться, пока я делаю фотографии, чтобы прикрепить её к камере наблюдения."

    mikki "Я-я?"

    zagadochnuy "А кто еще? Возьми себя в руки, Микки."

    hide mikki_shouts_image

    show mikki_serious_image at left

    mikki "Д-давайте драться!"

    orderly "Ты думаешь, что ты сильнее меня?"

    #Но я собираюсь выиграть эту игру!
    orderly "Но я выиграю эту игру!"

    "*Похоже, драка неизбежна*"

    hide screen info_panel with dissolve

    hide mikki_serious_image at left with easeoutleft

    hide orderly_image at right with easeoutright

    scene ZagadochnuyArmoryRoom with dissolve

    show mikki_thinks_image at left with dissolve

    show zagadochnuy_image at right with dissolve

    "*Загадочный произносит заклинания*"

    zagadochnuy "Авада кедавра!"

    show mikki_not_happy_image at left

    mikki "Это было заклинание из Гарри Поттера прямо сейчас?"

    zagadochnuy "Это не имеет значения, просто таинственное прошлое, выходящее из меня."

    zagadochnuy "Я бы сейчас все спел песней, но мы не в диснеевском мультфильме."

    zagadochnuy "А теперь давай посмотрим на твои способности?"

    mikki "Может быть, в этом нет необходимости?"

    zagadochnuy "Конечно нету... Покажи мне, давай."

    mikki "Л-ладно."

    "*Микки пытается колдовать, но ничего не получается*"

    hide mikki_thinks_image

    show mikki_not_happy_image at left

    zagadochnuy "Мда... Я ожидал большего."

    mikki "Что нам тогда делать?"

    zagadochnuy "Дай мне подумать..."

    "*Загадочный думает о том, как усилить способности Микки*"

    zagadochnuy "Мы можем отправиться за камнями бесконечности, чтобы усилить твои способности!"

    hide mikki_not_happy_image

    show mikki_serious_image at left

    mikki "Загадочный... Ты что, с ума сошел?!"

    mikki "Какие еще камни бесконечности?"

    zagadochnuy "Ну, обычные камни."

    mikki "Скажите мне, когда ты в последний раз смотрели фильмы Marvel?"

    zagadochnuy "Ну, примерно неделю назад, а что?"

    mikki "Ясно, ты сошел с ума."

    menu:
        "Что будет делать Микки дальше?"
        "Повернуться и сказать, что я ухожу" if True:

            mikki "Ты какой-то странный. Я ухожу отсюда."

            hide mikki_serious_image at left with easeoutleft

            zagadochnuy "Я говорю правду!"

            "*Микки почти ушел, когда Загадочный крикнул*"

            zagadochnuy "Я знаю, кто ты на самом деле, Микки! Ты всегда встаешь ровно в 6 утра и идешь в колледж, ты никогда не пропускал его, хотя и хотел."

            "*И Микки развернулся и пошел обратно.*"

            show mikki_shouts_image at left with moveinleft

            mikki "Кто ты, черт возьми, такой?"

            zagadochnuy "Я не могу рассказать тебе все прямо сейчас, но скажу тебе кое-что."

            hide mikki_shouts_image

            show mikki_thinks_image at left

            mikki "Я внимательно тебя слушаю."

            zagadochnuy "Ты необычный парень, Микки, как и я, но ты не знаешь всей правды... Ты думаешь, я просто искал тебя? Как ты думаешь, захватчики тоже искали тебя, чтобы остановить меня по какой-то причине?"

            zagadochnuy "Мы взаимно связаны, считай меня своим братом, который потерялся пару лет назад.\nЯ больше ничего не могу сказать, мне очень жаль..."

            zagadochnuy "Прощай, Микки."

            "*Загадочный повернулся и начал куда-то уходить*"

            hide zagadochnuy_image at right with easeoutright

            hide mikki_thinks_image

            show mikki_shouts_image at left

            mikki "Подожди, не уходи!"

            "*Микки звал Загадочного, чтобы тот вернулся, но тот был уже слишком далеко*"

            hide mikki_shouts_image at left with easeoutleft

            scene onemonthlater with dissolve

            pause(1.0)

            scene Mikki_House with dissolve

            show mikki_not_happy_image at center with moveinleft

            mikki "Прошел месяц, и я не могу забыть это Загадочного."

            mikki "Его характер был мне до боли знаком... Он был незабываемым, как будто я уже где-то его видел."

            "*Недавно Микки отправился на то место, где раньше была база загадочного, но её там больше нет...*"

            mikki "Загадочный, если ты слышишь меня, пожалуйста, вернись!"

            play sound sound_list["chapter1_sound_knockonthedoor"]

            "*Громкий стук в парадную дверь*"

            hide mikki_not_happy_image

            show mikki_happy_image at center

            mikki "О-он вернулся!!!"

            show mikki_happy_image at left with easeoutleft

            show larry_image at right with moveinright

            mikki "А это ты..."

            larry "Микки, почему ты не учился в колледже целый месяц?"

            mikki "Извини... Я искал одного знакомого."

            larry "Какого знакомого?"

            mikki "Это не имеет значения, я так и не нашел его."

            larry "Я могу тебе помочь!"

            mikki "И как ты мне поможешь?"

            larry "Пока тебя не было, я успел стать крутым технарем и могу быть твоим навигатором."

            larry "Я сяду за кучу мониторов и буду говорить тебе, что делать и куда идти."

            mikki "Я не уверен... Ты уверен, что сможешь?"

            larry "Конечно, я могу!"

            mikki "Что ж, мне нужно найти Загадочного того, кто пришел из будущего, чтобы спасти меня."

            "*Ларри решил промолчать*"

            mikki "И ты ничего не скажешь?"

            larry "Что я могу сказать: Микки, ты с ума сошел?"

            larry "Я видел, как ты убегала с каким-то черным парнем, он ещё был в маске."

            mikki "А... когда тебе удалось проследить за мной?"

            larry "Я как раз шел к твоему дому и увидел, что там стоят санитары и зовут тебя."

            mikki "А ты помнишь номерные знаки машины! Может быть, они захватили его в плен!!!"

            larry "Я постараюсь вспомнить..."

            "*У Микки все еще было ощущение, что с Загадочным что-то случилось*"

            larry "Я вспомнил, срочно принесите сюда ноутбук!"

            mikki "Я достану его сейчас же!"

            hide mikki_happy_image with easeoutleft

            mikki "Где он?"

            larry "Откуда мне знать, что у тебя в доме."

            mikki "Верно..."

            show mikki_happy_image at left with moveinleft

            mikki "Я нашел его!"

            larry "Дай его сюда."

            "*Микки достал ноутбук и протянул его Ларри*"

            larry "Спасибо, осталось только определить, где они находятся, это пара строк кода, а тем временем установи это на свой телефон."

            mikki "Хорошо, я установлю его сейчас."

            "*Звуки нажатия клавиш на клавиатуре*"

            developer "Данный этап выбора небел доделан, и мы перенаправляем вас к старому диалогу."

            hide mikki_happy_image

            hide larry_image

            scene black

            scene ZagadochnuyBase
        "Поверить загадочному и пойти с ним" if True:


            developer "Данный этап выбора небел доделан, и мы перенаправляем вас к старому диалогу."

            scene ZagadochnuyBase

    pause(1.0)

    hide zagadochnuy_image

    show zagadochnuy_angry_image at right

    zagadochnuy "Хватит придираться к моим словам!!!!"

    hide mikki_not_happy_image at left

    show mikki_shouts_image at left

    mikki "Ладно-ладно, чё орать то?"

    zagadochnuy "Надоел придираться к моим словам."

    pause(2.5)

    hide mikki_shouts_image at left

    show mikki_thinks_image

    mikki "Ну что же."

    mikki "Пошли за этими камнями бесконечности."

    pause(0.6)

    hide zagadochnuy_angry_image at right

    show zagadochnuy_image at right

    zagadochnuy "Да, пошли."

    hide mikki_thinks_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene black with dissolve

    dictor "И они отправились за первым камнем бесконечности."

    dictor "Их путь будет непростым, но они справятся (наверное)."

    scene Forest with dissolve

    show mikki_happy_image at left with moveinleft

    show zagadochnuy_image at right with moveinright

    mikki "Куда мы пойдем сначала?"

    zagadochnuy "В самое страшное место на Руси! В шестерочку!"

    hide mikki_happy_image

    show mikki_thinks_image at left

    mikki "Там что, первый камень бесконечности?"

    zagadochnuy "Нет просто нам нужен чай со слоником.\nШутка."

    zagadochnuy "Камня там нету, но есть тот кто подскажет путь."

    mikki "Ну тогда пошли?"

    hide mikki_thinks_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene Street with dissolve

    show mikki_thinks_image at left with moveinleft

    show zagadochnuy_image at right with moveinright

    zagadochnuy "Так, она должна быть где-то тут."

    mikki "Да вон же она нет?"

    zagadochnuy "Да это она, заходим."

    hide mikki_thinks_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene Pyaterochka_lb2 with dissolve

    show mikki_thinks_image at left with moveinleft

    show zagadochnuy_image at right with moveinright

    mikki "И кого нам надо тут найти?"

    zagadochnuy "Нам нужен менеджер и чай со слоником."

    mikki "Я пойду за чаем а ты найди менеджера."

    zagadochnuy "Хорошо."

    menu:
        "Переключить управление на Загадочного?"
        "Да" if True:



            $ achievement.grant("ChoosingTheUnknown")
            init:
                $ achievement.register("ChoosingTheUnknown")
                $ achievement.sync()

            $ achievement.sync()

            hide mikki_thinks_image at left with easeoutleft

            show zagadochnuy_image at center with moveinright

            zagadochnuy "Извините кассир."

            show zagadochnuy_image at left with moveinleft

            show thecashier_image at right with moveinright

            thecashier "Что вам надо?"

            zagadochnuy "Шоколада! Хахахаха."

            thecashier "Это какой то пранк?"

            zagadochnuy "Нет извините. Мне нужен ваш менеджер."

            thecashier "Хорошо, сейчас позову."

            hide thecashier_image at right with easeoutright

            thecashier "Наташ, там тебя ищут."

            manager "Скажи что я скоро подойду."

            show thecashier_image at right with moveinright

            thecashier "Она скоро подойдет."

            zagadochnuy "Хорошо подожду."

            hide thecashier_image at right with easeoutright

            show justapasserby_image at right with moveinright

            passer_all "Здравствуйте, вы не знаете где тут можно купить чай?"

            zagadochnuy "Мне очень жаль, но я не знаю."

            passer_all "Ладно, спасибо хотя бы за это."

            hide justapasserby_image at right with dissolve

            show ilovembsboy_image at right with dissolve

            zagadochnuy "Это щас что было?"

            passer_all "Вы про что?"

            zagadochnuy "Нет ничего."

            passer_all "Ладно, я ухожу."

            hide ilovembsboy_image at right with easeoutright

            show manager_image at right with moveinright

            manager_name "Здравствуйте, чем я могу вам помочь?"

            zagadochnuy "Мне нужна подсказка до камня бесконечности."

            manager_name "Мокки, сколько раз я просила не приходить в это место с такими просьбами?"

            zagadochnuy_name "Я снова забыл, но это срочно."

            manager_name "Хорошо, тогда слушай."

            manager_name "Далеко-далеко за горами есть одинокая деревня."

            manager_name "В нем найдите одного старика, который покажет вам путь к первому камню бесконечности."

            manager_name "А также, чтобы старик показал вам дорогу, скажите ему - Танос не ворует."

            zagadochnuy_name "Хорошо, спасибо."

            manager_name "Береги себя, Мокки."

            hide manager_image at right with easeoutright

            show zagadochnuy_image at center with moveinleft

            zagadochnuy "Хм, что за старик..."

            zagadochnuy "Ладно, не имеет значения, где Микки?"

            show zagadochnuy_image at right with moveinright

            show mikki_thinks_image at left with moveinleft

            mikki "Ну как, узнал куда идти?"

            zagadochnuy "Да, я узнал."

            mikki "Тогда пошли?"

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright
        "Нет" if True:


            $ achievement.grant("MickeysChoice")
            init:
                $ achievement.register("MickeysChoice")
                $ achievement.sync()

            $ achievement.sync()

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            scene Pyaterochka_lb1 with dissolve

            show mikki_thinks_image at center with moveinleft

            mikki "Так, где этот чай?"

            mikki "А вот же он там на полке."

            show mikki_thinks_image at left with moveinleft

            show security_image at right with moveinright

            security "Молодой человек, пройдемте со мной."

            mikki "Я?"

            security "А кто же ещё?"

            mikki "Зачем мне идти с вами?"

            security "Мне сообщили что вы украли жвачку по рублю."

            mikki "Но я только пришел, как я могу что-то украсть?"

            security "Ничего не знаю пройдемте со мной."

            show ilovembsboy_image at center with moveinright

            passer_all "Погодите он ничего не крал я смотрю на него как только он зашел!"

            security "Мальчик иди отсюда."

            passer_all "Он ничего не крал! Так в сценарии написали."

            mikki "Какой ещё сценарий?"

            passer_all "Ну обычный сценарий к этой игре."

            dictor "Кажется он сломал четвертую стену! Разработчики фиксите баг!"

            developer "(Переписывает сценарий.)"

            hide ilovembsboy_image at center with dissolve

            show justapasserby_image at center with dissolve

            mikki "Что это щас было?"

            security "Что было?"

            mikki "Ладно не важно."

            dictor "В этот момент, Микки думал что же произошло."

            security "Ладно раз у тебя есть свидетель, значит ты этого не делал."

            hide security_image at right with easeoutright

            show justapasserby_image at right with moveinright

            mikki "Спасибо тебе."

            passer_all "Не за что я думаю мы ещё встретимся."

            hide justapasserby_image at right with dissolve

            show mikki_thinks_image at center with moveinleft

            hide mikki_thinks_image

            show mikki_shouts_image at center

            mikki "Не понял, а где он?."

            mikki "Он что, взял и исчез ?"

            hide mikki_shouts_image

            show mikki_not_happy_image at center

            mikki "Мне бы так."

            hide mikki_not_happy_image

            show mikki_thinks_image at center

            mikki "...Неважно."

            mikki "Беру чай и иду к Загадочному."

            mikki "Интересно, он скажет мне свое имя когда-то?"

            hide mikki_thinks_image at left with easeoutleft

            scene Pyaterochka_lb2 with dissolve

            show zagadochnuy_image at right with moveinright

            show mikki_thinks_image at left with moveinleft

            mikki "Ну как, узнал куда идти?"

            zagadochnuy "Да, я узнал."

            mikki "Тогда пошли?"

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

    scene black with dissolve

    dictor "И они отправились в ту деревню."

    scene Street with dissolve

    show zagadochnuy_image at right with moveinright

    show mikki_thinks_image at left with moveinleft

    pause(0.5)

    mikki "Забыл спросить."

    mikki "А где это деревня находится?"

    zagadochnuy "За горами."

    mikki "Интересно, чем будет добираться?"

    zagadochnuy "Хмм...."

    zagadochnuy "Маршруткой."

    hide zagadochnuy_image at right with easeoutright

    hide mikki_thinks_image at left with easeoutleft

    scene Trapping with dissolve

    show zagadochnuy_image at right with moveinright

    show mikki_thinks_image at left with moveinleft

    mikki "Надеюсь что маршрутка скоро приедет."

    zagadochnuy "Я тоже."

    hide zagadochnuy_image at right with easeoutright

    hide mikki_thinks_image at left with easeoutleft

    scene black with dissolve

    "Спустя 3 минуты."

    scene Minibus with dissolve

    zagadochnuy "О, а вот и маршрутка приехала."

    pause(0.5)

    show zagadochnuy at center with moveinleft

    zagadochnuy "Вы едите до гор?"

    driver "Молодой человек, это маршрутка, а не автобус чтобы ехать куда-то далеко."

    zagadochnuy "Ой."

    zagadochnuy "Ну ладно. Тогда подождём автобус"

    hide zagadochnuy_image at center with easeoutright

    scene black with dissolve

    "Спустя 12 минут."

    scene Bus with dissolve

    "(Зевание)"

    show zagadochnuy at center with moveinleft

    zagadochnuy "...Надеюсь это автобус, а не очередная маршрутка."

    pause(0.5)

    zagadochnuy "Это автобус?"

    driver "Да."

    zagadochnuy "..."

    zagadochnuy "Боже, наконец-то."

    zagadochnuy "Кхм-кхм."

    zagadochnuy "Вы едите до гор?"

    driver "Конечно."

    zagadochnuy "Микки, садимся!"

    mikki "Что, автобус приехал, и он едит до гор?"

    zagadochnuy "Да."

    mikki "Ура, наконец-то!"

    hide zagadochnuy_image at right with easeoutright

    scene BusInInside with dissolve

    show zagadochnuy_image at right with moveinright

    show mikki_thinks_image at left with moveinleft

    zagadochnuy "Скажите когда вы доедите до одинокой деревни, просто мы не знаем где это деревня."

    driver "Хорошо, скажу когда доедем до одинокой деревни."

    scene Conversation_Inside_In_Bus1 with dissolve

    pause(6.0)

    mikki "Прости что сегодня придирался к твоим словам."

    mikki "Не думай что я такой."

    pause(0.9)

    mikki "Просто ситуация не особо для меня понятна."

    mikki "Какие-то санитары решили навести тут шороху."

    mikki "Сила монаха с времён Сталина которая у меня есть."

    mikki "Война за планету в 2075 году."

    mikki "Какие-то камни бесконечности."

    mikki "И ты который прибыл из 2077 года."

    pause(2.5)

    zagadochnuy "..."

    zagadochnuy "Я понимаю."

    pause(2.0)

    mikki "Загадочный, давай о чём нибудь поговорим."

    mikki "А то скучно просто сидеть или смотреть в окно."

    scene Conversation_Inside_In_Bus2

    zagadochnuy "О чём поговорим?"

    mikki "Ну..."

    scene Conversation_Inside_In_Bus3

    mikki "Давай про мемы поговорим."

    zagadochnuy "Ну давай."

    scene Conversation_Inside_In_Bus2

    mikki "Хмм..."

    scene Conversation_Inside_In_Bus3

    mikki "Какие мемы у вас популярные в 2077 году."

    zagadochnuy "Хмм..."

    zagadochnuy "Юмор 21 века."

    zagadochnuy "Вроде этот мем появился где-то в 2021 году."

    zagadochnuy "Но каким-то чудом оно вновь стало популярным."

    mikki "О чём этот мем?"

    zagadochnuy "К сожалению я не могу рассказать о чём оно."

    pause(0.2)

    zagadochnuy "Но могу показать видео связанное с этим мемом."

    "(Роется в кармане)"

    mikki "У тебя есть телефон?"

    zagadochnuy "Да."

    pause(0.9)

    zagadochnuy "Так."

    zagadochnuy "Теперь надо найти это видео."

    "(Ищет видео)"

    zagadochnuy "Нашел."

    mikki "Ну показывай."

    scene black with dissolve

    "Спустя 1-у минуту."

    scene Conversation_Inside_In_Bus3 with dissolve

    mikki "..."

    zagadochnuy "Этот мем не имеет никакого смысла."

    zagadochnuy "Просто рандомные картинки, видео и звуки."

    pause(0.8)

    zagadochnuy "А какие мемы у вас сейчас популярные."

    mikki "Не знаю."

    mikki "Особо за популярными мемами не наблюдаю."

    pause(0.2)

    mikki "Но могу рассказать, какие мемы я знаю."

    menu:
        "Выберите мем, который расскажет Микки."
        "Чи да?" if True:



            scene Conversation_Inside_In_Bus2

            mikki "Хмм..."

            scene Conversation_Inside_In_Bus3

            mikki "Мем - Чи да?"

            pause(0.5)

            mikki "Суть мема заключается в том что - \nЧувак с кепкой по имени Эдвард Бил."

            mikki "Подходит к случайным прохожим и говорит."

            mikki "Чи да? Чи или не чи?"

            mikki "Прохожие не понимают что он хочет."

            mikki "А Эдвард Бил всё также продолжает говорить - Чи да? Чи или не чи?"

            pause(0.5)

            mikki "В принципе всё."

            pause(0.3)

            zagadochnuy "А этот Эдвард Бил подходил к пенсионерам."

            mikki "Не знаю."

            scene black with dissolve

            "Мы прерываем историю на маленькую музыкальную паузу."

            scene DeathNodeL with dissolve

            play music music_list["death_note_ls_theme_b_music"]

            $ achievement.grant("LThisIsMe")
            init:
                $ achievement.register("LThisIsMe")
                $ achievement.sync()

            $ achievement.sync()

            pause(180.05)

            stop music fadeout 1.0

            $ achievement.grant("DeathNote")
            init:
                $ achievement.register("DeathNote")
                $ achievement.sync()

            $ achievement.sync()

            scene Conversation_Inside_In_Bus3 with dissolve
        "Камеру вырубай" if True:


            scene Conversation_Inside_In_Bus2

            mikki "Хмм..."

            scene Conversation_Inside_In_Bus3

            mikki "Мем - Камеру вырубай."

            mikki "Суть мема заключается в том что - \n Оператор снимает что-то, потом подходит охранник до оператора и говорит."

            mikki "Тут съёмка видео запрещена."

            mikki "Камеру вырубай."

            mikki "После этого говорит одно и тоже, но с обзыванием на адрес оператора."

            pause(0.2)

            mikki "А оператор как и не в чём не бывало продолжает снимать."

            mikki "А охранник всё также продолжает что-то говорить оператору."

            pause(0.2)

            mikki "Оператору видимо пофиг на охранника."

            pause(0.3)

            mikki "Но всё же оператор выключает камеру."

            pause(0.4)

            mikki "Впринципе всё."

    scene Conversation_Inside_In_Bus4

    "Звук сирены."

    mikki "Сирена?"

    zagadochnuy "Пригнись! Это санитары!"

    mikki "Как ты-"

    zagadochnuy "Без вопросов!"

    mikki "Х-хорошо."

    scene Durka_Car with dissolve

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

    "(Вызов завершён)"

    scene Conversation_Inside_In_Bus4 with dissolve

    zagadochnuy "Н-наёмник."

    zagadochnuy "В одинокой деревне!"

    mikki "..."

    scene Conversation_Inside_In_Bus5

    mikki "Когда мы начали говорить про мемы."

    mikki "На мгновение я забыл про этих санитаров и про всякое там."

    mikki "..."

    "(Сигнал автобуса)"

    driver "Выключите сирену!"

    orderly "Мы не можем выключить сирену."

    orderly "Кнопка сирены сломалось."

    scene Conversation_Inside_In_Bus2

    mikki "Надеюсь нас не встретят санитары."

    mikki "Да и этот наёмник."

    zagadochnuy "Я тоже надеюсь."

    scene black with dissolve

    "Спустя 40 минут."

    scene Conversation_Inside_In_Bus1 with dissolve

    driver "Приехали."

    zagadochnuy "До одинокой деревни?"

    driver "Да."

    zagadochnuy "...Я думал что реально там далеко-далеко."

    scene Forest with dissolve

    show zagadochnuy_image at right with moveinright

    pause(0.6)

    show mikki_happy_image at left with moveinleft

    mikki "Наконец-то."

    mikki "Свежий воздух."

    zagadochnuy "Ага, а то в автобусе было душно."

    hide mikki_happy_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene Lonely_Village with dissolve

    show zagadochnuy_image at right with moveinright

    show mikki_thinks_image at left with moveinleft

    mikki "У нас есть одна проблема."

    zagadochnuy "Какая?"

    mikki "Мы не знаем в каком доме живёт этот старик."

    zagadochnuy "..."

    zagadochnuy "Блин. Насчёт этого я не подумал."

    pause(0.3)

    zagadochnuy "Хм..."

    zagadochnuy "Что будем делать?"

    mikki "Давай будем спрашивать у прохожих."

    zagadochnuy "Ок."

    pause(0.7)

    mikki "Поехали."

    zagadochnuy "Может - Пошли?"

    mikki "Мы это, поправляем слова или спрашиваем у людей где этот дед?"

    zagadochnuy "Ух какие серьёзные."

    hide mikki_thinks_image

    show mikki_serious_image at left

    mikki "..."

    zagadochnuy "Ладно-ладно."

    zagadochnuy "Пошли спрашивать."

    hide mikki_serious_image

    show mikki_thinks_image at left

    hide mikki_thinks_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    scene Forest with dissolve

    show zagadochnuy_image at center with moveinleft

    show mikki_thinks_image at left with moveinleft

    mikki "О, вижу кого-то."

    zagadochnuy "Будем спрашивать?"

    mikki "Да."

    pause(0.5)

    show justapasserby at right with moveinright

    pause(0.6)

    passer_all "Привет."

    hide mikki_thinks_image

    show mikki_shouts_image at left

    mikki "А что ты тут делаешь?"

    passer_all "Дела."

    zagadochnuy "А вы с ним знакомы?"

    passer_all "Да."

    passer_all "В шестёрочке встретились."

    hide mikki_shouts_image

    show mikki_thinks_image at left

    mikki "Вообщем."

    mikki "Перейдём к теме."

    mikki "Ты знаешь где живёт дед который знает где камни бесконечности?"

    passer_all "Прости, я тут только первый раз."

    mikki "Жаль."

    mikki "Ну спасибо хотя бы за это."

    mikki "Пока."

    passer_all "Пока."

    hide justapasserby at right with easeoutright

    mikki "Подожди!"

    show justapasserby at right with moveinright

    passer_all "Что?"

    mikki "А как тебя зовут?"

    vania "Меня зовут Ваня."

    hide mikki_thinks_image

    show mikki_happy_image at left

    mikki "А моё имя Микки."

    zagadochnuy "А моё имя..."

    zagadochnuy "..."

    zagadochnuy "Не буду говорить."

    hide mikki_happy_image

    show mikki_thinks_image at left

    mikki "А почему?"

    zagadochnuy "Потому что потому."

    vania "Ладно. Не буду задерживаться."

    mikki "Пока."

    hide justapasserby at right with easeoutright

    show zagadochnuy_image at right with moveinright

    pause(1.0)

    mikki "Реально."

    mikki "Почему ты не сказал своё имя?"

    zagadochnuy "Мне это сложно объяснить."

    pause(0.8)

    mikki "Ладно. Пошли следующего спрашивать."

    hide mikki_thinks_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    show Lonely_Village with dissolve

    show zagadochnuy_image at center with moveinleft

    show mikki_thinks_image at left with moveinleft

    zagadochnuy "Надеюсь хоть этот знает."

    zagadochnuy "Эй, подойди сюда."

    mikki "Загадочный, а что ты так говоришь?"

    zagadochnuy "Просто хочу уже побыстрее"

    show yura_image at right with moveinright

    passer_all "О, ещё новые."

    passer_all "Давайте познакомимся."

    yura "Я Юра, а вас как?"

    zagadochnuy "Спасибо что с нами гостеприимно знакомишься."

    zagadochnuy "Но можешь сказать где дед который знает где камни бесконечности."

    yura "Хм..."

    yura "Вроде идти вперёд, потом повернуть и дойти до 6-го дома."

    zagadochnuy "Спасибо."

    yura "Не за что."

    hide yura_image at right with easeoutright

    show zagadochnuy_image at right with moveinright

    hide mikki_thinks_image

    show mikki_happy_image at left

    mikki "Пошли."

    hide mikki_happy_image at left with easeoutleft

    hide zagadochnuy_image at right with easeoutright

    show black with dissolve

    "Спустя 30 секунд."

    scene Lonely_Village with dissolve

    show zagadochnuy_image at right with moveinright

    show mikki_thinks_image at left with moveinleft

    "(Стучание в дверь)"

    "Кто там?"

    show zagadochnuy_image at center with moveinright

    show grandfather_image at right with moveinright

    grandfather "Вы кто?"

    mikki "Я Микки, а это загадочный."

    hide grandfather_image

    show grandfather_thinks_image at right

    grandfather "У него такое имя?"

    mikki "Нет. Просто-"

    hide grandfather_thinks_image

    show grandfather_image at right

    zagadochnuy "Неважно."

    zagadochnuy "Короче."

    zagadochnuy "Танос не ворует."

    grandfather "..."

    grandfather "Проходите. Дома расскажу где камни бесконечности."

    hide grandfather_image at right with easeoutright

    hide mikki_thinks_image at right with easeoutright

    hide zagadochnuy_image at right with easeoutright

    scene Grandfather_Home with dissolve

    show grandfather_image at right with moveinright

    show zagadochnuy_image at center with moveinright

    show mikki_thinks_image at left with moveinright

    hide grandfather_image

    show grandfather_thinks_image at right

    grandfather "А как ты узнал эту фразу?"

    zagadochnuy "Узнал у менеджера из шестерочке."

    grandfather "...Ладно."

    hide grandfather_thinks_image

    show grandfather_image at right

    grandfather "Дайка вспомнить."

    pause(2.0)

    grandfather "Вспомнил."

    grandfather "Кхм-кхм."

    pause(0.9)

    hide grandfather_image

    show grandfather_serious_image at right

    grandfather "Первый и второй камень бесконечности находятся в Сочи."

    grandfather "В Пляже Светлячок."

    zagadochnuy "Эм..."

    zagadochnuy "Серьёзно?"

    grandfather "Да. я на полном серьёзно говорю."

    show zagadochnuy_image at right with moveinright

    show grandfather_serious_image at right with moveinright:
        xalign 0.7 yalign 1.0

    show granny_image with moveinleft:
        xalign 0.35 yalign 1.0

    granny "О чём говорите?"

    hide grandfather_serious_image

    show grandfather_image:
        xalign 0.7 yalign 1.0

    grandfather "О камнях бесконечности."

    granny "..."

    granny "Опять ты со своими камнями!"

    granny "Это просто бред который вешаешь лапшу на уши!"

    show grandfather_serious_image:
        xalign 0.7 yalign 1.0

    grandfather "..."

    grandfather "Камни бесконечности и вправду существуют!"

    granny "Ну давай принеси эти камни, тогда и поверю."

    play sound sound_list["chapter1_sound_shot"]

    pause(0.5)

    stop sound

    hide mikki_thinks_image

    show mikki_shouts_image at left

    "Твою дивизию, как я мог промазать!"

    zagadochnuy "Бежим."

    hide zagadochnuy_image at right with easeoutright

    hide mikki_shouts_image at right with easeoutright

    hide granny_image at right with easeoutright

    hide grandfather_serious at left with easeoutleft

    scene Lonely_Village with dissolve

    show mercenary at center with moveinleft

    mercenary "Снова."

    mercenary "Моя неуверенность."

    mercenary "Глава дурки меня за это прибьёт."

    pause(0.8)

    mercenary "Так. А где они?"

    hide mercenary with dissolve

    play sound sound_list["chapter1_sound_padenia_zemly"]

    pause(0.6)

    stop sound

    show mikki_serious_image at center with moveinleft

    mikki "Повезло что рядом лежала арматура."

    mikki "Так. Он живой?"

    pause(1.6)

    mikki "Видимо не живой."

    show mikki_serious_image at left with moveinleft

    show mercenary at right with dissolve

    hide mikki_serious_image

    show mikki_shouts_image at left

    mikki "Ты как чёрт подери ещё жив после такого сильного удара?!"

    mercenary "Я сам не знаю как это так."

    mercenary "Вообщем."

    mercenary "Твой путь к камням бесконечностям закончится тут!"

    hide mikki_shouts_image

    show mikki_serious_image at left

    show screen info_panel with dissolve

label battle_mercenary:

    if mikki_health < 0:
        jump mikki_dead
    elif True:

        menu:
            "Выберите атаку."
            "Арматура" if True:

                "Вы использовали арматуру."

                $ random3 = renpy.random.randint(1, 3)

                if random3 == 1:
                    "Урон нанес 25"

                    $ mercenary_healht -= 25

                if random3 == 2:
                    "Урон нанес 50"

                    $ mercenary_healht -= 50

                if random3 == 3:
                    "Урон нанес 100"

                    $ mercenary_healht -= 100



                if mercenary_healht < 0:
                    jump mercenary_dead
                elif True:

                    "Жизней у наёмника: [mercenary_healht]"

                    if random3 == 1:

                        "Наёмник нанес вам 20 урона"

                        $ mikki_health -= 20

                    if random3 == 2:

                        "Наёмник нанес вам 27 урона"

                        $ mikki_health -= 27

                    if random3 == 3:

                        "Наёмник нанес вам 37 урона"

                        $ mikki_health -= 37

                    jump battle_mercenary
            "Пропустить ход" if True:

                $ random3 = renpy.random.randint(1, 3)

                if random3 == 1:

                    "Наёмник нанес вам 20 урона"

                    $ mikki_health -= 20

                if random3 == 2:

                    "Наёмник нанес вам 27 урона"

                    $ mikki_health -= 27

                if random3 == 3:

                    "Наёмник нанес вам 37 урона"

                    $ mikki_health -= 37

                jump battle_mercenary

    return

label mercenary_dead:

    hide screen info_panel with dissolve

    $ mikki_health = 100

    hide mercenary with dissolve

    play sound sound_list["chapter1_sound_padenia_zemly"]

    pause(1.0)

    stop sound

    pause(0.2)

    menu:
        "Выбирете действие."
        "Не добивать" if True:



            hide mikki_serious_image with dissolve

            scene Defeated_Mercenary with dissolve

            mercenary "Это всё."

            mercenary "На то что я способен?"

            mercenary "Я даже не пробовал пострелять."

            mikki "Скажи пожалуйста."

            mikki "Зачем вы сюда прибыли?"

            mercenary "..."

            mercenary "В 2075-м году мы сражались за захват планеты."

            mercenary "Во время сражения появился Мокки из ниоткуда."

            mercenary "И начал прям в одиночку выносить нас с своей невероятной силой."

            mikki "А кто этот Мокки?"

            mercenary "Это ты."

            mikki "..."

            mikki "ЧЕГО?!"

            mercenary "Я тебя ещё больше удивлю."

            mercenary "Тот c которым ты ходишь."

            mercenary "Это и есть Мокки."

            mercenary "Ну или ты из будущего."

            mikki "..."

            mikki "Хмм..."

            mikki "То есть вы сюда прибыли чтобы меня похитить, из-за той силы которая у меня есть?"

            mercenary "Да."

            mikki "Я хочу тебя огорчить."

            mercenary "То что тебя нет силы?"

            mikki "Нет."

            mikki "Сила у меня всё таки."

            mikki "Но дело в том что на данный момент у меня сила ну прям очень слабая."

            mercenary "Чего?!"

            mercenary "То есть мы сюда прибыли зря?"

            mikki "Скорее не совсем, ведь через какой-то время у меня сила будет сильней."

            pause(1.0)

            mikki "Ну я пошёл."

            mercenary "Стой!"

            mikki "?"

            mercenary "Я хочу кое-что сказать."

            mercenary "..."

            play music music_list["game_music_003_dialogue"]

            mercenary "Я был раньше совершенно обычным человеком."

            mercenary "Не думал о всяких войнах и прочее."

            pause(0.2)

            mercenary "Когда прибыли санитары."

            mercenary "Меня похитили."

            mercenary "После этого я проснулся в палате, которая была полностью белая."

            mercenary "Даже смирительная рубашка тоже была белой."

            mercenary "И начал кричать чтобы меня выпустили."

            mercenary "Прошли секунды, минуты, часы."

            mercenary "Никакого результата."

            mercenary "После этого я отчаялся."

            mercenary "И подумал что я тут останусь до конца до своей смерти."

            mercenary "Спустя 10 часов у меня начались галлюцинации из-за белого цвета."

            mercenary "..."

            mercenary "Спустя 2 часа я заснул."

            pause(0.3)

            mercenary "Когда я проснулся, возле меня стояли санитары."

            mercenary "И сказали."

            mercenary "Уважаемый, пройдёмтесь за нами."

            mercenary "Я не задумывая стал, и понял что я без смирительной рубашки."

            pause(0.2)

            mercenary "Ну и я пошёл за санитарами думая - что произойдёт со мной дальше?"

            mercenary "Меня привели к главе дурки."

            mercenary "Я ожидал много чего от него."

            mercenary "..."

            mercenary "Глава дурки сказал -"

            scene DurkaBase with dissolve

            show durka_image at left with dissolve

            show kolia_angry_past at right with dissolve

            durka "У тебя есть вопросы насчёт того что происходит?"

            "Определенно!"

            "Кхм-кхм."

            "Зачем я вообще вам нужен!"

            durka "Чтобы увеличивать нашу армию."

            durka "Для того чтобы было легко захватить вашу планету."

            "..."

            "Я не буду в этом участвовать."

            durka "Ну значит убьём."

            pause(1.0)

            durka "Слушай, ты конечно ещё молод, и тебе еще рано умирать."

            durka "Подумай хорошенько."

            hide kolia_angry_past

            show kolia_past at right

            pause(2.0)

            "Ладно."

            "Так и уж быть."

            durka "Вот и славно)"

            hide durka_image with dissolve

            hide kolia_past with dissolve

            scene Defeated_Mercenary with dissolve

            mercenary "Через день мы с санитарами начали похищать первых попавшийся человеков."

            pause(1.5)

            mercenary "Через пару месяцев у нас была очень большая армия."

            mercenary "Мы были готовы захватывать планету."

            pause(0.2)

            mercenary "По началу было довольно хорошо."

            mercenary "Но потом появился ты."

            mercenary "И всё пошло на перекосяк."

            mercenary "Мы решили отступить."

            mercenary "Спустя 4 дня мы узнали кто ты из себя представляешь, кем ты являлся в прошлом и какая у тебя сила."

            mercenary "Мы решили переместиться в 2019 год чтобы получить твою силу."

            pause(0.2)

            mercenary "Глава дурки меня сделала наёмником."

            mercenary "Потому что я был очень опытным."

            pause(0.9)

            mercenary "Когда я вас нашел."

            mercenary "Я не хотел забирать вашу жизнь."

            mercenary "Но мне надо было."

            mercenary "..."

            mercenary "Когда я приготовился стрельнуть."

            mercenary "В этот момент я был не уверен что это чем-то хорошо кончится."

            mercenary "Из-за своей неуверенности я промазал."

            pause(1.0)

            mikki "Ты не хотел участвовать в этом?"

            mercenary "Что за глупый вопрос?"

            mercenary "Несколько секунд назад об этом говорил."

            mikki "А."

            stop music fadeout 0.8

            scene Lonely_Village with dissolve

            show mikki_thinks_image at left with dissolve

            mikki "Подай руку."

            show kolia at right with dissolve

            pause(0.5)

            mercenary "Можно к вам присоединиться?"

            mercenary "Я не хочу быть в команде дурке!"

            mikki "Хмм..."

            pause(2.0)

            hide mikki_thinks_image

            show mikki_happy_image at left

            mikki "Можно!"

            mercenary "В принципе так и думал."

            mercenary "Надеюсь Мокки оценит это."

            mercenary "Ох, забыл спросить."

            mercenary "Если сейчас твоё имя не Мокки, а тогда как тебя зовут?"

            mikki "Микки."

            pause(2.0)

            mikki "А тебя то как зовут?"

            kolia "Коля."

            zagadochnuy_name "Микки! Ты где!?"

            show kolia at center with moveinleft

            show zagadochnuy at right with moveinright

            zagadochnuy_name "А вот ты где."

            pause(0.2)

            zagadochnuy_name "А этот кто?"

            kolia "Я Коля."

            kolia "Я хочу к вам присоединиться против дурки."

            zagadochnuy_name "Хм..."

            zagadochnuy_name "Ты уже в курсе тогда насчёт происходящего."

            pause(0.6)

            zagadochnuy_name "У тебя есть какие-то заклинания или типа того?"

            kolia "Только огнестрельное оружие."

            zagadochnuy_name "!"

            zagadochnuy_name "Это же оружие из базы дурки!"

            zagadochnuy_name "Как ты его добыл!?"

            kolia "Ну как вам сказать..."

            kolia "..."

            kolia "Я был членом команды дурки."

            zagadochnuy_name "..."

            zagadochnuy_name "Вот как."

            pause(0.9)

            zagadochnuy_name "Проверка вещей."

            kolia "...Хорошо."

            "(Показывает предметы.)"

            zagadochnuy_name "Уху."

            zagadochnuy_name "Хорошо."

            zagadochnuy_name "Ты принят."

            pause(0.8)

            mikki "Идем на осто-"

            play sound sound_list["chapter1_sound_shot"]

            pause(0.5)

            stop sound

            "(Промах.)"

            hide mikki_happy_image

            show mikki_serious_image at left

            kolia "О нет! Походу снайпер!"

            play sound sound_list["chapter1_sound_shot"]

            pause(0.5)

            stop sound

            "(Промах.)"

            orderly "Блин, патроны закончились."

            show mikki_serious_image at center with moveinright:
                xalign 0.35 yalign 1.0


            show kolia at center with moveinright:
                xalign 0.7 yalign 1.0


            show orderly-deltagroup at left with moveinleft:
                xalign -0.2 yalign 1.0

            mikki "Я тебя с одного удара вынесу!"

            show screen info_panel with dissolve

            orderly "Посмотрим."

            orderly "И да Коля, помогай."

            kolia "Прости, но я больше не с вами."

            pause(0.9)

            zagadochnuy_name "Микки, это твоя первая битва."

            mikki "Я бы сказал вторая."

            pause(0.6)

            mikki "Ты будешь помогать?"

            zagadochnuy "Нет, у тебя же есть в руках арматура."

            mikki "Тебе пофиг на меня?!"

            kolia "Такой же вопрос, почему Мокки, ты вдруг не будешь помогать?"

            zagadochnuy_name "!"

            zagadochnuy_name "Не пали контору."

            mikki "Я уже и так знаю твоё имя)"

            zagadochnuy_name "Ладно, поздравляю."

            zagadochnuy_name "Кхм-кхм"

            zagadochnuy_name "Нет, просто хочу посмотреть как ты сражаешься."

            zagadochnuy_name "А вот когда что-то пойдёт не так, тогда что-то сделаю."

            orderly "Да вы задолбали! Давайте уже начнём!"

            kolia "Ой, мне приспичило в туалет."

            hide kolia at left with easeoutleft

            hide zagadochnuy at left with easeoutright

            show mikki_serious_image at right with moveinright

            show orderly-deltagroup at left with moveinleft

            show screen info_panel with dissolve

            jump battle_orderly

            return

            label battle_orderly:

            if mikki_health < 0:
                jump mikki_dead
            elif True:

                menu:
                    "Выберите атаку."
                    "Арматура" if True:

                        "Вы использовали арматуру."

                        $ random3 = renpy.random.randint(1, 3)

                        if random3 == 1:
                            "Урон нанес 25"

                            $ orderly_health -= 25

                        if random3 == 2:
                            "Урон нанес 50"

                            $ orderly_health -= 50

                        if random3 == 3:
                            "Урон нанес 100"

                            $ orderly_health -= 100

                            $ achievement.grant("IToldYou")
                            init:
                                $ achievement.register("IToldYou")
                                $ achievement.sync()

                            $ achievement.sync()

                        if orderly_health < 0:
                            jump orderly_dead
                        elif True:

                            "Жизней у санитара: [orderly_health]"

                            if random3 == 1:

                                "Санитар нанес вам 20 урона"

                                $ mikki_health -= 20

                            if random3 == 2:

                                "Санитар нанес вам 27 урона"

                                $ mikki_health -= 27

                            if random3 == 3:

                                "Санитар нанес вам 37 урона"

                                $ mikki_health -= 37

                            jump battle_orderly
                    "Пропустить ход" if True:

                        $ random3 = renpy.random.randint(1, 3)

                        if random3 == 1:

                            "Санитар нанес вам 20 урона"

                            $ mikki_health -= 20

                        if random3 == 2:

                            "Санитар нанес вам 27 урона"

                            $ mikki_health -= 27

                        if random3 == 3:

                            "Санитар нанес вам 37 урона"

                            $ mikki_health -= 37

                        jump battle_orderly

            return

            label orderly_dead:

            hide screen info_panel with dissolve

            hide orderly-deltagroup with dissolve

            play sound sound_list["chapter1_sound_padenia_zemly"]

            pause(1.0)

            stop sound

            hide mikki_serious_image

            show mikki_happy_image at right

            mikki "Это было довольно легко."

            show mikki_happy_image at left with moveinright

            show zagadochnuy_image at right with moveinright

            zagadochnuy_name "Конечно, он же безоружный."

            pause(0.9)

            show kolia at center with moveinright

            kolia "Так, я вернулся."

            pause(0.3)

            kolia "Оу, ты уже его победил?"

            mikki "Конечно."

            pause(0.9)

            mikki "Пошли."

            hide mikki_happy_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            hide kolia at left with easeoutleft

            scene Forest with dissolve

            show mikki_happy_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinright

            mikki "О, а вот и автобус подъезжает."

            hide mikki_happy_image

            show mikki_thinks_image at left

            mikki "На котором мы приехали сюда."

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            hide kolia at left with easeoutleft

            scene BusInInside with dissolve

            show mikki_happy_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinright

            driver "О, снова вы."

            driver "Что-то вы быстро."

            pause(1.0)

            zagadochnuy_name "До Москвы."

            driver "Хорошо."

            kolia "Я сяду в конце."

            kolia "Буду наблюдать."

            pause(0.2)

            kolia "Если увижу санитаров, скажу вам об этом."

            hide mikki_happy_image with dissolve

            hide zagadochnuy_image with dissolve

            hide kolia with dissolve

            scene Conversation_Inside_In_Bus1 with dissolve

            pause(6.0)

            zagadochnuy_name "Я тут был ранее."

            mikki "В автобусе что ли?"

            zagadochnuy_name "Нет."

            zagadochnuy_name "Я имею ввиду то что я тут был ранее, чтобы усилить свою силу благодаря камням бесконечностям."

            pause(4.0)

            scene Conversation_Inside_In_Bus2

            mikki "А куда убежали дедушка и бабушка."

            zagadochnuy_name "Я сам не знаю куда они убежали."

            mikki "А они что-то сказали?"

            zagadochnuy_name "Ничего не сказали."

            scene Conversation_Inside_In_Bus1

            pause(4.0)

            scene Conversation_Inside_In_Bus3

            mikki "Хочешь анекдот расскажу?"

            zagadochnuy_name "Ну го."

            mikki "Не суди строго."

            mikki "Это только мой первый анекдот."

            zagadochnuy "Хорошо."

            pause(1.1)

            mikki "Во время урока учитель спросил -"

            mikki "Дети, вы хотите уйти домой пораньше."

            mikki "Дети без раздумий сразу сказали - да."

            mikki "Дети собрались."

            mikki "Учитель говорит -"

            mikki "Идите тихо как мышки, ведь у других школьников урок."

            mikki "И после этого дети в прямом смысле пошли как мышки."

            mikki "Учитель говорит -"

            mikki "Вы совсем ку-ку, я же в образном смысле."

            zagadochnuy_name "..."

            zagadochnuy_name "Ну пойдёт для первого раза."

            scene black with dissolve

            "Спустя 45 минут."

            scene Conversation_Inside_In_Bus1 with dissolve

            driver "Приехали."

            scene Trapping with dissolve

            show mikki_happy_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinleft

            pause(0.4)

            mikki "Наконец-то могу достать арматуру."

            "(Достал арматуру)"

            hide mikki_happy_image

            show mikki_thinks_image at left

            mikki "Что дальше будем делать?"

            zagadochnuy_name "С начала мы пойдём в банк, чтобы получить документы для того чтобы полететь в Сочи."

            zagadochnuy_name "Потом мы идём за паспортами."

            zagadochnuy_name "После этого идём в аэропорт."

            zagadochnuy_name "Там встретимся."

            kolia "У меня и так собой паспорт."

            pause(0.3)

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            hide kolia at left with easeoutleft

            scene Bank with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinright

            zagadochnuy_name "Это будет долго..."

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            hide kolia at left with easeoutleft

            scene black with dissolve

            "Спустя 25 минут."

            scene Bank with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinright

            mikki "Фух, наконец-то."

            zagadochnuy_name "Теперь идём за паспортами."

            pause(0.3)

            mikki "Коля, а с кем ты пойдёшь?"

            kolia "..."

            kolia "С Мокки."

            menu:
                "Выберите персонажа."
                "Микки" if True:



                    hide zagadochnuy_image at right with easeoutright

                    hide kolia at right with easeoutright

                    show mikki_thinks_image at center with moveinleft

                    pause(0.2)

                    mikki "Надеюсь что с моим домом ничего не случилось."

                    hide mikki_thinks_image at center with easeoutleft

                    scene Forest with dissolve

                    show mikki_thinks_image at center with moveinleft

                    mikki "..."

                    hide mikki_thinks_image

                    show mikki_happy_image at center

                    mikki "Ничего себе!"

                    mikki "С моим домом ничего не случилось."

                    mikki "Как будто ничего и не было."

                    pause(0.8)

                    mikki "Лол."

                    mikki "Я сказал слово - ничего \nБолее 4-х раза."

                    mikki "А нет."

                    mikki "Уже пять."

                    hide mikki_happy_image at center with easeoutleft

                    scene mikki_house with dissolve

                    show mikki_happy_image at center with moveinleft

                    hide mikki_happy_image

                    show mikki_thinks_image at center

                    mikki "Так, вроде только нужен паспорт."

                    hide mikki_thinks_image with dissolve

                    scene black with dissolve

                    "Спустя 10 минут."

                    scene mikki_house with dissolve

                    show mikki_happy_image at center with dissolve

                    mikki "Фух.."

                    mikki "Вроде всё."

                    mikki "Идём."

                    hide mikki_happy_image at center with easeoutleft

                    scene Airport with dissolve

                    show mikki_happy_image at center with moveinleft

                    mikki "Вот и аэропорт."

                    mikki "Что-то их тут нет."

                    mikki "Думаю они скоро придут."

                    hide mikki_happy_image with dissolve

                    scene black with dissolve

                    "Спустя 6 минут."

                    scene Airport with dissolve

                    show mikki_thinks_image at center with dissolve

                    mikki "Что-то они задерживаются."

                    pause(0.7)

                    show mikki_thinks_image at left with moveinright

                    show zagadochnuy_image at right with moveinright

                    show kolia at center with moveinright

                    mikki "Почему вы так долго?"

                    kolia "С санитарами пришлось повозиться."

                    zagadochnuy_name "Кстати, сколько ты тут стоишь."

                    mikki "Примерно 6-7 минут."

                    pause(0.5)

                    zagadochnuy_name "Идём внутрь."

                    hide mikki_thinks_image

                    show mikki_happy_image at left

                    hide zagadochnuy_image at right with easeoutright

                    hide mikki_happy_image at left with easeoutright

                    hide kolia at left with easeoutright
                "Мокки и Коля" if True:


                    hide zagadochnuy_image at right with easeoutright

                    hide kolia at right with easeoutright

                    hide mikki_thinks_image with dissolve

                    scene Forest with dissolve

                    show zagadochnuy_image at right with moveinright

                    show kolia at left with moveinleft

                    zagadochnuy_name "А почему ты решил со мной пойти?"

                    kolia "Не знаю."

                    pause(4.9)

                    kolia "А куда мы идём?"

                    zagadochnuy_name "К моем базе."

                    pause(2.0)

                    zagadochnuy_name "Мы пришли."

                    hide zagadochnuy_image at right with easeoutright

                    hide kolia at right with easeoutright

                    scene ZagadochnuyBase with dissolve

                    show zagadochnuy_image at right with moveinright

                    show kolia at left with moveinleft

                    kolia "А как ты построил базу?"

                    zagadochnuy_name "С помощью своей силы."

                    zagadochnuy_name "Примерно за полтора часа."

                    pause(0.7)

                    zagadochnuy_name "Стой тут."

                    zagadochnuy_name "Я сейчас."

                    hide zagadochnuy_image at right with easeoutright

                    pause(6.0)

                    zagadochnuy_name "Всё."

                    show zagadochnuy_image at right with moveinright

                    kolia "У тебя есть патроны к этому оружию?"

                    zagadochnuy_name "Зачем тебе оружие? Ведь тебя не пустят в аэропорт с оружием."

                    kolia "А ой."

                    kolia "Не подумай что я тебя это."

                    pause(0.3)

                    zagadochnuy_name "Пошли уже."

                    hide zagadochnuy_image at right with easeoutright

                    hide kolia at left with easeoutleft

                    scene Forest with dissolve

                    show zagadochnuy_image at right with moveinright

                    show kolia at left with moveinleft

                    pause(0.3)

                    play sound sound_list["chapter1_sound_shot"]

                    pause(0.5)

                    stop sound

                    "(Промах)"

                    zagadochnuy_name "Ну вот опять..."

                    kolia "Эй Мокки."

                    zagadochnuy_name "Что?"

                    kolia "Короче слушай."

                    zagadochnuy_name "Ну давай."

                    play sound sound_list["chapter1_sound_shot"]

                    pause(0.5)

                    stop sound

                    "(Промах)"

                    kolia "Я крикну что ты пойман."

                    kolia "А когда он подойдет, ты с помощью своей силы ударишь его."

                    zagadochnuy_name "...Хорошо."

                    zagadochnuy_name "Но если он тупой, не догадается в меня стрельнуть."

                    pause(0.7)

                    kolia "Он пойман!"

                    show orderly at center with moveinright

                    orderly "Коля, я по твоему не знаю что ты делаешь?"

                    "(Удар)"

                    hide orderly with dissolve

                    play sound sound_list["chapter1_sound_padenia_zemly"]

                    pause(0.7)

                    stop sound

                    zagadochnuy_name "Лол."

                    pause(0.7)

                    kolia "Пош-"

                    play sound sound_list["chapter1_sound_shot"]

                    pause(0.5)

                    stop sound

                    zagadochnuy_name "АЙ!"

                    kolia "Мокки, спрячься!"

                    hide zagadochnuy_image at right with easeoutright

                    pause(0.7)

                    show orderly-deltagroup at right with moveinright

                    orderly "Предатель! Чего ты добиваешься?!"

                    "(Удар)"

                    hide orderly-deltagroup with dissolve

                    play sound sound_list["chapter1_sound_padenia_zemly"]

                    pause(0.7)

                    stop sound

                    pause(1.5)

                    show zagadochnuy_image at right with moveinright

                    kolia "Ты в порядке?"

                    zagadochnuy_name "Да."

                    zagadochnuy_name "Ранение довольно сильное."

                    kolia "А куда пуля попала?"

                    zagadochnuy_name "В правое плечо."

                    pause(0.8)

                    kolia "Давай уже пойдём в аэропорт."

                    kolia "Микки нас там заждался."

                    kolia "А с пулей разберемся в Сочи."

                    hide zagadochnuy_image at right with easeoutright

                    hide kolia at left with easeoutleft

                    scene Airport with dissolve

                    show mikki_thinks_image at left with moveinleft

                    show zagadochnuy_image at right with moveinright

                    show kolia at center with moveinright

                    mikki "Почему вы так долго?"

                    kolia "С санитарами пришлось повозиться."

                    zagadochnuy_name "Кстати, сколько ты тут стоишь."

                    mikki "Примерно 6-7 минут."

                    pause(0.5)

                    zagadochnuy_name "Идём внутрь."

                    hide mikki_thinks_image

                    show mikki_happy_image at left

                    hide zagadochnuy_image at right with easeoutright

                    hide mikki_happy_image at left with easeoutleft

                    hide kolia at center with easeoutright

            scene InsideInAirport with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinright

            kolia "Так, а где агент по регистрации?"

            zagadochnuy_name "Да вот же он."

            show mikki_thinks_image at right with moveinright:
                xalign 0.7 yalign 1.0

            show kolia with moveinleft:
                xalign 0.35 yalign 1.0

            show rig_agent at left with moveinleft

            rigagent "Здравствуйте."

            zagadochnuy_name "Мы собираемся полететь в Сочи."

            rigagent "Давайте документы, деньги, и паспорт."

            "(Дают)"

            pause(4.5)

            rigagent "Угу."

            hide rig_agent at left

            show rig_agent_happy at left

            rigagent "Всё отлично."

            rigagent "Вам на 106 рейс."

            hide rig_agent_happy at left with easeoutleft

            show kolia at center with moveinright

            show mikki_thinks_image at left with moveinleft

            hide mikki_thinks_image

            show mikki_thinks at left

            pause(2.0)

            hide mikki_thinks_image

            show mikki_happy_image at left

            kolia "Может сходим пока в кафе?"

            zagadochnuy_name "Нет."

            zagadochnuy_name "Скоро самолет улетает."

            zagadochnuy_name "Мы ведь этого не хотим?"

            pause(0.2)

            kolia "Эх..."

            kolia "А так хотелось."

            kolia "Ну ладно."

            kolia "Когда мы прилетим. Я схожу в кафе."

            kolia "Правда мы будем летать длительное время."

            pause(0.7)

            mikki "Ну вперёд."

            hide mikki_thinks

            hide mikki_happy_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            hide kolia at right with easeoutright

            scene Airplane with dissolve

            show mikki_happy_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            show kolia at center with moveinright

            mikki "Я никогда не летал на самолете."

            mikki "Я не знаю какие у меня будут впечатление!"

            zagadochnuy_name "Ты так говоришь как будто это что-то сверхъестественное."

            kolia "Мокки, не будь таким душниловой."

            kolia "Ведь по словам Микки он никогда не летал на самолете."

            hide mikki_happy_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            hide kolia at left with easeoutleft

            pause(4.0)

            show orderly_image at center with moveinright

            "(Набирает номер)"

            durka "Да."

            orderly "Сэр, мы нашли их в аэропорту."

            orderly "И они отправляются в 106 рейс."

            durka "А насчёт наёмника?"

            orderly "Он стал предателем."

            durka "Вот как."

            pause(0.9)

            durka "За такое ему точно не жить."

            durka "Кстати, куда отправляется 106 рейс?"

            orderly "В Сочи."

            durka "Хорошо."

            durka "Я пошлю войска в Сочи."

            durka "Хотя погодите мне передали чтобы вы прямо сейчас хватали Микки и посадили его в поезд!"

            pause(0.4)

            orderly "Хорошо до свидания сэр!"

            durka "Досвидание."

            "(Вызов завершен)"

            hide orderly_image with dissolve

            scene black with dissolve

            dictor "Наша история прерывается из-за недоработки игры, но вы успели узнать про некоторых героев и их тестовые характеры.\nКонец тестовой первой главы."

            pause(2.0)

            developer "Сейчас мы разрабатываем совсем другую историю игры и поэтому данная версия, недоработанная и в ней есть куча ошибок как в коде, так и в грамотеек."

            return
        "Добить" if True:


            mikki "Увидимся в другой жизни."

            "(Добивание)"

            pause(0.2)

            mikki "Теперь точно не живой."

            pause(0.4)

            hide mikki_serious_image

            show mikki_thinks_image at left

            show mikki_thinks_image at center with moveinleft

            mikki "А где загадочный?"

            mikki "Думаю он где-то поблизости."

            hide mikki_thinks_image at left with easeoutleft

            scene Forest2 with dissolve

            show mikki_thinks_image at center with moveinleft

            mikki "Та где он?"

            zagadochnuy "Микки, ты где!?"

            mikki "Я тут!"

            show mikki_thinks_image at left with moveinright

            show zagadochnuy_image at right with moveinright

            zagadochnuy "Где ты был?!"

            mikki "Возле дома деда. Сражался с наёмником."

            zagadochnuy "И что в итоге?"

            mikki "Убил."

            zagadochnuy "Чем?"

            "(Показывает арматуру)"

            zagadochnuy "Вот как."

            pause(0.2)

            mikki "Уверен что старик правду сказал?"

            zagadochnuy "Я не знаю даже."

            zagadochnuy "Но поверить ему стоит."

            hide mikki_thinks_image

            show mikki_serious_image at left

            mikki "Серьёзно?"

            mikki "Вот так просто поверить?"

            mikki "А вдруг он перепутал местоположение этих камней?"

            mikki "Или это просто бред, которая рассказала та бабка."

            zagadochnuy "Другого выхода нет!"

            hide mikki_serious_image

            show mikki_thinks_image at left

            mikki "..."

            mikki "Ну ладно. Допустим."

            pause(0.4)

            zagadochnuy "Мы узнали где находятся камни бесконечности."

            zagadochnuy "Так что. Нам в деревне делать нечего."

            zagadochnuy "Можем уже возвращаться."

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            scene Forest with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            pause(2.0)

            mikki "А куда убежали дедушка и бабушка."

            zagadochnuy "Я сам не знаю."

            zagadochnuy "Они даже ничего не сказали."

            hide mikki_thinks_image at left with dissolve

            hide zagadochnuy_image at right with dissolve

            scene black with dissolve

            "Спустя 8 минут."

            scene Forest with dissolve

            show mikki_thinks_image at left with dissolve

            show zagadochnuy_image at right with dissolve

            hide mikki_thinks_image

            show mikki_happy_image at left

            mikki "О, а вот и автобус подъезжает."

            hide mikki_happy_image

            show mikki_thinks_image at left

            mikki "На котором мы приехали сюда."

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            scene BusInInside with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            driver "О, снова вы."

            driver "Что-то вы быстро."

            pause(1.0)

            zagadochnuy "До Москвы."

            driver "Хорошо."

            hide mikki_thinks_image with dissolve

            hide zagadochnuy_image with dissolve

            scene Conversation_Inside_In_Bus1 with dissolve

            pause(6.0)

            zagadochnuy "Я тут был ранее."

            mikki "В автобусе что ли?"

            zagadochnuy "Нет."

            zagadochnuy "Я имею ввиду то что я тут был ранее, чтобы усилить свою силу благодаря камням бесконечностям."

            pause(4.0)

            scene Conversation_Inside_In_Bus3

            mikki "Хочешь анекдот расскажу?"

            zagadochnuy "Ну го."

            mikki "Не суди строго."

            mikki "Это только мой первый анекдот."

            zagadochnuy "Хорошо."

            pause(1.1)

            mikki "Во время урока учитель спросил -"

            mikki "Дети, вы хотите уйти домой пораньше."

            mikki "Дети без раздумий сразу сказали - да."

            mikki "Дети собрались."

            mikki "Учитель говорит -"

            mikki "Идите тихо как мышки, ведь у других школьников урок."

            mikki "И после этого дети в прямом смысле пошли как мышки."

            mikki "Учитель говорит -"

            mikki "Вы совсем ку-ку, я же в образном смысле."

            zagadochnuy "..."

            zagadochnuy "Ну пойдёт для первого раза."

            scene black with dissolve

            "Спустя 45 минут."

            scene Conversation_Inside_In_Bus1 with dissolve

            driver "Приехали."

            scene Trapping with dissolve

            show mikki_happy_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            pause(0.4)

            mikki "Наконец-то могу достать арматуру."

            "(Достал арматуру)"

            hide mikki_happy_image

            show mikki_thinks_image at left

            mikki "Что дальше будем делать?"

            zagadochnuy "С начала мы пойдём в банк, чтобы получить документы для того чтобы полететь в Сочи."

            zagadochnuy "Потом мы идём за паспортами."

            zagadochnuy "После этого идём в аэропорт."

            zagadochnuy "Там встретимся."

            pause(0.3)

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            scene Bank with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            zagadochnuy "Это будет долго..."

            hide mikki_thinks_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            scene black with dissolve

            "Спустя 25 минут."

            scene Bank with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            mikki "Фух, наконец-то."

            zagadochnuy "Теперь идём за паспортами."

            pause(0.3)

            menu:
                "Выберите персонажа."
                "Микки" if True:



                    hide zagadochnuy_image at right with easeoutright

                    show mikki_thinks_image at center with moveinleft

                    pause(0.2)

                    mikki "Надеюсь что с моим домом ничего не случилось."

                    hide mikki_thinks_image at center with easeoutleft

                    scene Forest with dissolve

                    show mikki_thinks_image at center with moveinleft

                    mikki "..."

                    hide mikki_thinks_image

                    show mikki_happy_image at center

                    mikki "Ничего себе!"

                    mikki "С моим домом ничего не случилось."

                    mikki "Как будто ничего и не было."

                    pause(0.8)

                    mikki "Лол."

                    mikki "Я сказал слово - ничего \nБолее 4-х раза."

                    mikki "А нет."

                    mikki "Уже пять."

                    hide mikki_happy_image at center with easeoutleft

                    scene mikki_house with dissolve

                    show mikki_happy_image at center with moveinleft

                    hide mikki_happy_image

                    show mikki_thinks_image at center

                    mikki "Так, вроде только нужен паспорт."

                    hide mikki_thinks_image with dissolve

                    scene black with dissolve

                    "Спустя 10 минут."

                    scene mikki_house with dissolve

                    show mikki_happy_image at center with dissolve

                    mikki "Фух.."

                    mikki "Вроде всё."

                    mikki "Идём."

                    hide mikki_happy_image at center with easeoutleft

                    scene Airport with dissolve

                    show mikki_happy_image at center with moveinleft

                    mikki "Вот и аэропорт."

                    mikki "Что-то его тут нет."

                    mikki "Думаю он скоро придет."

                    pause(0.7)

                    hide mikki_happy_image

                    show mikki_thinks_image at center

                    show mikki_thinks_image at left with moveinright

                    show zagadochnuy_image at right with moveinright

                    mikki "Всё ок?"

                    zagadochnuy "Да."

                    pause(0.5)

                    zagadochnuy "Идём внутрь."

                    hide mikki_thinks_image

                    show mikki_happy_image at left

                    hide zagadochnuy_image at right with easeoutright

                    hide mikki_happy_image at left with easeoutleft
                "Загадочный" if True:


                    hide zagadochnuy_image at right with easeoutright

                    hide mikki_thinks_image with dissolve

                    scene Forest with dissolve

                    show zagadochnuy_image at center with moveinright

                    pause(4.0)

                    zagadochnuy "А вот и моя база."

                    hide zagadochnuy_image at right with easeoutright

                    scene ZagadochnuyBase with dissolve

                    show zagadochnuy_image at center with moveinright

                    pause(0.2)

                    zagadochnuy "Хм..."

                    zagadochnuy "Где же мой паспорт?"

                    hide zagadochnuy_image with dissolve

                    scene black with dissolve

                    "Спустя 12 минут."

                    scene ZagadochnuyBase with dissolve

                    show zagadochnuy_image at center with dissolve

                    zagadochnuy "Хух."

                    zagadochnuy "Это было не просто."

                    hide zagadochnuy_image at right with easeoutright

                    scene black with dissolve

                    pause(1.1)

                    scene Airport with dissolve

                    show mikki_thinks_image at left with dissolve

                    show zagadochnuy_image at right with moveinright

                    mikki "Всё ок?"

                    zagadochnuy "Да."

                    pause(0.5)

                    zagadochnuy "Идём внутрь."

                    hide mikki_thinks_image

                    show mikki_happy_image at left

                    hide zagadochnuy_image at right with easeoutright

                    hide mikki_happy_image at left with easeoutleft

            scene InsideInAirport with dissolve

            show mikki_thinks_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            mikki "Так, а где агент по регистрации?"

            zagadochnuy "Да вот же он."

            show mikki_thinks_image at center with moveinright

            show rig_agent at left with moveinleft

            rigagent "Здравствуйте."

            zagadochnuy "Мы собираемся полететь в Сочи."

            rigagent "Давайте документы, деньги, и паспорт."

            "(Дают)"

            pause(2.5)

            rigagent "Угу."

            hide rig_agent at left

            show rig_agent_happy at left

            rigagent "Всё отлично."

            rigagent "Вам на 106 рейс."

            hide rig_agent_happy at left with easeoutleft

            show mikki_thinks_image at left with moveinleft

            pause(2.0)

            hide mikki_thinks_image

            show mikki_happy_image at left

            mikki "Ну вперёд."

            hide mikki_happy_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            scene Airplane with dissolve

            show mikki_happy_image at left with moveinleft

            show zagadochnuy_image at right with moveinright

            mikki "Я никогда не летал на самолете."

            mikki "Я не знаю какие у меня будут впечатление!"

            zagadochnuy "Ты так говоришь как будто это что-то сверхъестественное."

            hide mikki_happy_image at left with easeoutleft

            hide zagadochnuy_image at right with easeoutright

            pause(4.0)

            show orderly_image at center with moveinright

            "(Набирает номер)"

            durka "Да."

            orderly "Сэр, мы нашли их в аэропорту."

            orderly "И они отправляются в 106 рейс."

            durka "А насчёт наёмника?"

            orderly "Он погиб."

            durka "Вот как."

            durka "Жаль что технологии из будущего не достигли до такой развитии. Чтобы можно возрождать мёртвого."

            pause(0.9)

            durka "Кстати, куда отправляется 106 рейс?"

            orderly "В Сочи."

            durka "Хорошо."

            durka "Я пошлю войска в Сочи."

            durka "Хотя погодите мне передали чтобы вы прямо сейчас хватали Микки и посадили его в поезд!"

            pause(0.4)

            orderly "Хорошо до свидания сэр!"

            durka "Досвидание."

            "(Вызов завершен)"

            hide orderly_image with dissolve

            scene black with dissolve

            dictor "Наша история прерывается из-за недоработки игры, но вы успели узнать про некоторых героев и их тестовые характеры.\nКонец тестовой первой главы."

            pause(2.0)

            developer "Сейчас мы разрабатываем совсем другую историю игры и поэтому данная версия, недоработанная и в ней есть куча ошибок как в коде, так и в грамотеек."

            return
