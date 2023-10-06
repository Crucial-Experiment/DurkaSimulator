label part2_village:

    hide screen info_panel
    hide screen info_panel_enemy
    with dissolve

    scene black with dissolve

    $ mickey_health = 100

    play sound sound_list["fall"]

    pause(0.7)

    scene grass_mercenary_bg with dissolve

    mercenary "Я не думал, что именно так умру."

    menu:
        "Добить":
            mickey "Увидимся в другой жизни."

            $ mercenary_dead = True

            scene black with dissolve

            play sound sound_list["punch"]

            $ achievement.grant("FirstBlood")
            $ achievement.sync()

            pause(0.4)

            scene grass_mercenary_bg with dissolve

            mickey "Теперь точно не живой."

            mickey "Что это у него в кармане..."

            show mickey_shaver
            with dissolve

            $ shaver_killer = True
            "Получен 1 бритвенный станок."

            play sound sound_list["picked_up_an_item"]

            hide mickey_shaver
            with dissolve

            mickey "Хм... Его можно использовать как оружие."

            mickey "Так, а где загадочный?"

            mickey "Думаю он где-то поблизости."

            scene forest_2_bg with dissolve

            show mickey_thinks with moveinleft

            mickey "Та где он?"

            mysterious "Микки, ты где!?"

            mickey "Я тут!"

            show mickey_thinks at left with moveinright
            show mysterious_normal at right with moveinright

            mysterious "Где ты был?!"

            mickey "Возле дома деда. Сражался с наёмником."

            mysterious "И что в итоге?"

            mickey "Убил."

            mysterious "Чем?"

            mickey "Арматура...  Я нашел рядом бритву."

            mysterious "Вот как."

            pause(0.2)

            mickey "Уверен что старик правду сказал?"

            mysterious "Я не знаю даже, но поверить ему стоит."

            hide mickey_thinks
            show mickey_serious at left
            with dissolve

            mickey "Серьёзно?"

            mickey "Вот так просто поверить?"

            mickey "А вдруг он перепутал местоположение этих камней?"

            mickey "Или это просто бред, которая рассказала та бабка."

            mysterious "Другого выхода нет!"

            hide mickey_serious
            show mickey_thinks at left
            with dissolve

            mickey "..."
            mickey "Ну ладно, допустим."

            pause(0.4)

            mysterious "Мы узнали где находятся камни бесконечности."

            mysterious "Так что. Нам в деревне делать нечего."

            mysterious "Можем уже возвращаться."

            hide mickey_thinks at left with easeoutleft
            hide mysterious_normal at right with easeoutright

            scene black with dissolve

            play sound sound_list["steps_on_asphalt"]

            pause (12.5)

            stop sound fadeout 1.0

            scene trapping_2_bg with dissolve

            show mickey_thinks at left with moveinleft
            show mysterious_normal at right with moveinright

            pause(1.3)

            mickey "Слушай, а куда бабка с дедом убежали?"

            mysterious "Я сам не знаю."

            mysterious "Они даже ничего не сказали."

            scene black with dissolve

            center_text "Спустя 10 минут"

            scene bus_inside_bg with dissolve
            show mickey_happy at left with moveinleft
            show mysterious_normal at right with moveinright

            driver "О, снова вы."

            driver "Что-то вы быстро."

            pause(1.0)

            mysterious "Нам до Москвы."

            driver "Хорошо."

            scene bus_inside_c1_bg with dissolve

            pause(1.0)

            mysterious "Мне кажется, что я уже был здесь раньше."

            mickey "В автобусе что ли?"

            mysterious "Нет. Мне кажется, что такое со мной уже случалось... Как будто я сам убил наемника."

            pause(1.0)

            scene bus_inside_c2_bg with dissolve

            mickey "Хочешь послушать шутку, которую я только что придумал?"

            mysterious "Ну давай."           

            mickey "Не суди строго, это всего лишь мой первый анекдот."

            mysterious "Хорошо."

            pause(1.1)

            if school_choose:

                mickey "Во время урока учитель спросил - Дети, вы хотите уйти домой пораньше?"

                mickey "Дети без раздумий сразу сказали - Да!"

                mickey "Они собрались"

                mickey "Учитель говорит - Идите тихо как мышки, ведь у других школьников уроки."

                mickey "И после этого дети в прямом смысле пошли как мышки."

                mickey "Учитель говорит - Вы совсем ку-ку, я же в образном смысле."

            else:
                mickey "Во время пары преподаватель спросил - Студенты, вы хотите уйти домой пораньше?"

                mickey "Студенты без раздумий сразу сказали - Да!"

                mickey "Они собрались."

                mickey "Преподаватель говорит - Идите тихо как мышки, ведь у других студентов пары."

                mickey "И после этого студенты в прямом смысле пошли как мышки."

                mickey "Преподаватель говорит - Вы совсем ку-ку, я же в образном смысле."

            mysterious "..."

            mysterious "Ну пойдёт для первого раза."

            scene black with dissolve

            center_text "Спустя 45 минут"

            scene bus_inside_c2_bg with dissolve

            driver "Приехали."

            scene bus_inside_bg
            show mickey_happy at right
            show mysterious_normal at left
            with dissolve
            
            mysterious "Хм... В этот раз мы приехали немного быстрее."

            scene trapping_bg with dissolve

            show mickey_happy at left with moveinleft
            show mysterious_normal at right with moveinright

            pause(0.4)

            mickey "Наконец-то могу достать арматуру."

            mysterious "..."

            hide mickey_happy
            show mickey_thinks at left
            with dissolve

            mickey "Что дальше будем делать?"

            mysterious "Я сначала схожу в банк, а ты иди домой и забери свои документы."

            mysterious "Затем мы встречаемся в аэропорту и покупаем билеты."

            mickey "Ладно, надеюсь, они не разрушили мой дом."

            pause(0.3)

            hide mickey_thinks at left with easeoutleft

            scene black

            center_text "Какое-то время спустя"

            jump part2_home

        "Не добивать":
            $ mercenary_dead = False

            mercenary "Это все, на что ты способен?"

            mercenary "Я даже не пробовал пострелять..."

            mickey "Скажи пожалуйста."

            mickey "Зачем вы сюда прибыли?"

            mercenary "..."

            mercenary "В 2075-м году мы сражались за захват планеты."

            mercenary "Во время битвы Мокки появился из ниоткуда и начал уничтожать нас своей невероятной силой."

            mickey "Кто этот Мокки?"

            mercenary "Они все еще ничего тебе не сказали?"

            mickey "...Нет"

            mercenary "Ты и есть Мокки."

            mickey "ЧЕГО?!"

            mercenary "Я тебя ещё больше удивлю."

            mercenary "Тот, с которым ты ходишь - Мокки."

            mercenary "Или ты из будущего."

            mickey "..."

            mickey "Хмм..."

            mickey "Так вы пришли сюда, чтобы похитить меня из-за силы, которой я обладаю?"

            mercenary "Да..."

            mickey "Я хочу тебя огорчить."

            mercenary "Просто потому, что у тебя нет сил?"

            mickey "Нет."

            mickey "Сила у меня всё таки."

            mickey "Дело в том, что в данный момент мои силы очень слабы."

            mercenary "Чего?!"

            mercenary "Значит, мы прибыли сюда зря?"

            mickey "Скорее нет, потому что через некоторое время мои силы станут сильнее."

            pause(1.0)

            mickey "Ну я пошёл."

            mercenary "Стой!"

            mickey "?"

            mercenary "Я хочу кое-что сказать."

            mercenary "..."

            play music music_list["game_music_003_dialogue"] loop

            mercenary "Я был раньше совершенно обычным человеком."

            mercenary "Не думал о всяких войнах и прочее."

            pause(0.2)

            mercenary "Когда прибыли санитары... Меня похитили."

            mercenary "После этого я проснулся в палате, которая была полностью белая."

            mercenary "Даже смирительная рубашка тоже была белой."

            mercenary "И начал кричать чтобы меня выпустили."

            mercenary "Прошли секунды, минуты, часы."

            mercenary "Никакого результата."

            mercenary "После этого я отчаялся и решил, что останусь здесь до самой смерти."

            mercenary "Спустя 10 часов у меня начались галлюцинации из-за белого цвета."

            mercenary "..."

            mercenary "Через два часа я уснул."

            pause(0.3)

            mercenary "Когда я проснулся, возле меня стояли санитары и сказали."

            mercenary "Уважаемый, следуйте за нами."

            mercenary "Я не задумывая стал, и понял что я без смирительной рубашки."

            pause(0.2)

            mercenary "Я последовал за санитарами, гадая, что со мной будет дальше."

            mercenary "Меня привели к их шефу... Я ожидал от него многого."

            mercenary "..."

            mercenary "Глава дурки сказал -"

            scene black with dissolve
            pause(0.2)

            scene durka_base_bg
            show dir_durka_normal at left
            show kolya_past_angry at right
            with dissolve

            durka "У тебя есть вопросы насчёт того что происходит?"

            mercenary "Определенно!"

            mercenary "Кхм-кхм."

            mercenary "Зачем я вам вообще нужен?!"

            durka "Чтобы увеличивать нашу армию."

            durka "Для того чтобы было легко захватить вашу планету."

            mercenary "..."

            mercenary "Я не буду в этом участвовать."

            durka "Ну значит убьём."

            pause(0.5)

            durka "Слушай, ты конечно ещё молод, и тебе еще рано умирать."

            durka "Подумай хорошенько."

            hide kolya_past_angry
            show kolya_past at right
            with dissolve

            pause(2.0)

            mercenary "Ладно... Пусть будет по вашему."

            durka "Хорошо, надень это."

            hide kolya_past with easeoutright

            pause(1.5)

            play sound sound_list["zipper_on_clothes"]

            pause(1.2)

            show kolya_clear at right with moveinright

            durka "Поздравляю, теперь ты один из нас."

            mercenary "..."

            scene black with dissolve
            pause(0.2)
            scene grass_mercenary_bg with dissolve

            mercenary "Через день мы с санитарами начали похищать первых попавшихся людей."

            pause(1.5)

            mercenary "Через пару месяцев у нас была очень большая армия."

            mercenary "Мы были готовы захватывать планету."

            pause(0.2)

            mercenary "Сначала все было хорошо, но потом появился ты, и все пошло не по плану."

            mercenary "Мы решили отступить."

            mercenary "Через четыре дня мы узнали, кто ты, кем ты был в прошлом и в чем твоя сила."

            mercenary "Мы решили переместиться в 2019 год, чтобы получить твою силу."

            pause(0.2)

            mercenary "Меня официально сделали наемником, который охотится за всеми."

            pause(0.9)

            mercenary "Когда я нашел вас обоих, я не хотел вас убивать, моей задачей было привести вас к шефу."

            mercenary "..."

            mercenary "Когда я приготовился стрельнуть."

            mercenary "В этот момент я не был уверен, что все закончится хорошо."

            mercenary "Моя неуверенность в себе привела к тому, что я промахнулся..."

            pause(1.0)

            mickey "Ты не хотел участвовать в этом?"

            mercenary "Что за глупый вопрос?"

            mercenary "Я так и сказал несколько секунд назад."

            mickey "Ааа... Прости..."

            stop music fadeout 0.8

            scene lonely_village_bg
            show mickey_thinks at left
            with dissolve

            mickey "Дай мне свою руку."

            show kolya_normal at right with dissolve

            pause(0.5)

            mercenary "Могу я присоединиться к вам?"

            mercenary "Я не хочу быть в их команде, мне все это надоело..."

            mickey "Хмм..."

            pause(2.0)

            hide mickey_thinks
            show mickey_happy at left
            with dissolve

            mickey "Можно!"

            mercenary "Тебя не беспокоит, что я только что хотел тебя убить?"

            mickey "Нет."

            mercenary "В принципе, я так и думал."

            mercenary "Надеюсь Мокки оценит это."

            mercenary "Ох, забыл спросить."

            mercenary "Если тебя сейчас зовут не Мокки, то как тебя зовут?"

            mickey "Микки."

            pause(2.0)

            mickey "Как тебя зовут то?"

            mercenary "Коля."

            mysterious "Микки! Ты где!?"

            show kolya_normal at center with moveinright
            show mysterious_normal at right with moveinright

            mysterious "Вот ты где..."

            pause(0.2)

            mysterious "Этот ещё кто?"

            kolya "Я Коля."

            kolya "Я хочу присоединиться к вам против дурки."

            mysterious "Хм..."

            mysterious "Значит, ты уже в курсе происходящего."

            pause(0.6)

            mysterious "У тебя есть какие-то заклинания или что-то в этом роде?"

            kolya "Только огнестрельное оружие."

            mysterious "!"

            mysterious "Это же оружие из базы дурки!"

            mysterious "Как ты его добыл!?"

            kolya "Ну как вам сказать..."

            kolya "..."

            kolya "Я нашел его на полу..."

            mysterious "..."

            mysterious "Вот как... Проверка вещей."

            kolya "...Хорошо."

            play sound sound_list["journal_opening"]

            pause(1.2)

            mysterious "Угу..."

            mysterious "Почему вся твоя одежда в крови?"

            kolya "Помог Микки убить наемника."

            mysterious "Хорошо..."

            mysterious "Ты принят."

            pause(0.8)

            mickey "Идем на осто-"

            play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

            pause(0.6)

            play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

            pause(0.6)

            hide mickey_happy
            show mickey_serious at left
            with dissolve

            kolya "Кажется, они нашли нас..."

            play sound renpy.random.choice([sound_list["shot_1"], sound_list["shot_2"]])

            pause(0.6)

            orderly "Черт, патроны кончились."

            show mickey_serious at center with moveinright:
                xalign 0.35 yalign 1.0


            show kolya_normal at center with moveinright:
                xalign 0.7 yalign 1.0


            show orderly_normal at left with moveinleft:
                xalign -0.2 yalign 1.0
            
            mickey "Я тебя с одного удара вынесу!"

            orderly "Посмотрим."

            orderly "И да Коля, помогай."

            kolya "Прости, но я больше не с вами."

            mysterious "..."

            pause(0.9)

            mysterious "Микки, это твоя первая битва."

            mickey "Я бы сказал вторая."

            pause(0.6)

            mickey "Ты будешь помогать?"

            mysterious "Нет, у тебя же есть в руках арматура."

            mickey "Тебе пофиг на меня?!"

            kolya "Тот же вопрос, почему Мокки, вдруг не хочет помочь?"

            mysterious "!"

            mysterious "Не пали контору."

            mickey "Я уже и так знаю твоё имя."

            mysterious "Ладно, поздравляю."

            mysterious "Кхм-кхм."

            mysterious "Нет, просто хочу посмотреть как ты сражаешься."

            mysterious "Когда что-то пойдет не так, тогда я буду что-то делать."

            orderly "Да вы задолбали! Давайте уже начнём!"

            kolya "Ой, мне приспичило в туалет..."

            orderly "..."

            hide kolya_normal
            hide mysterious_normal
            with easeoutright

            show mickey_serious at right with moveinright
            show orderly_normal at left with moveinleft

            $ battle_character = "orderly"
            $ battle_label = "part2_village_b1"

            show screen info_panel
            show screen info_panel_enemy
            with dissolve

            jump game_battle

    return

label part2_village_b1:

    hide screen info_panel
    hide screen info_panel_enemy
    with dissolve

    scene black with dissolve

    $ mickey_health = 100

    play sound sound_list["fall"]

    pause(0.7)

    $ achievement.grant("FirstBlood")
    $ achievement.sync()

    scene lonely_village_bg
    hide mickey_serious 
    with dissolve

    hide mickey_serious 
    show mickey_happy at right
    with dissolve

    mickey "Это было довольно легко."

    show mickey_happy at left with moveinright
    show mysterious_normal at right with moveinright

    mysterious "Конечно, он же безоружный."

    pause(0.9)

    show kolya_normal at center with moveinright

    kolya "Так, я вернулся."

    pause(0.3)

    kolya "Оу, ты уже его победил?"

    mickey "Конечно."

    mysterious "Коля, нечего сказать не хочешь?"

    kolya "...Ну да, я работал на дурку."

    mysterious "Что ж, я буду наблюдать за тобой."

    pause(0.9)

    mickey "Теперь мы можем идти?"

    mysterious "Да."

    hide mickey_happy with easeoutleft
    hide mysterious_normal with easeoutright
    hide kolya_normal with easeoutleft

    scene trapping_2_bg with dissolve

    show mickey_happy at left with moveinleft
    show mysterious_normal at right with moveinright
    show kolya_normal with moveinright

    mickey "О, а вот и автобус подъезжает."

    hide mickey_happy
    show mickey_thinks at left
    with dissolve

    mickey "На котором мы приехали сюда."

    scene bus_inside_bg with dissolve
    show mickey_happy at left with moveinleft
    show mysterious_normal at right with moveinright
    show kolya_normal at center with moveinright

    driver "О, снова вы."

    driver "Что-то вы быстро."

    pause(1.0)

    mysterious "Нам до Москвы."

    driver "Хорошо."

    pause(0.4)

    kolya "Я буду сидеть в конце и наблюдать."

    kolya "Если увижу санитаров, скажу вам об этом."

    scene bus_inside_c2_bg with dissolve

    pause(1.0)

    mickey "Хочешь послушать шутку, которую я только что придумал?"

    mysterious "Ну давай."           

    mickey "Не суди строго, это всего лишь мой первый анекдот."

    mysterious "Хорошо."

    pause(1.1)

    if school_choose:

        mickey "Во время урока учитель спросил - Дети, вы хотите уйти домой пораньше?"

        mickey "Дети без раздумий сразу сказали - Да!"

        mickey "Они собрались"

        mickey "Учитель говорит - Идите тихо как мышки, ведь у других школьников уроки."

        mickey "И после этого дети в прямом смысле пошли как мышки."

        mickey "Учитель говорит - Вы совсем ку-ку, я же в образном смысле."

    else:
        mickey "Во время пары преподаватель спросил - Студенты, вы хотите уйти домой пораньше?"

        mickey "Студенты без раздумий сразу сказали - Да!"

        mickey "Они собрались."

        mickey "Преподаватель говорит - Идите тихо как мышки, ведь у других студентов пары."

        mickey "И после этого студенты в прямом смысле пошли как мышки."

        mickey "Преподаватель говорит - Вы совсем ку-ку, я же в образном смысле."

    mysterious "..."

    mysterious "Ну пойдёт для первого раза."

    scene black with dissolve

    center_text "Спустя 45 минут"

    scene bus_inside_c2_bg with dissolve

    driver "Приехали."

    scene bus_inside_bg
    show mickey_happy at right
    show mysterious_normal at left
    show kolya_normal
    with dissolve
            
    mysterious "Хм... В этот раз мы приехали немного быстрее."

    scene trapping_bg with dissolve

    show mickey_happy at left with moveinleft
    show mysterious_normal at right with moveinright
    show kolya_normal at center with moveinright

    pause(0.4)

    mickey "Наконец-то могу достать арматуру."

    mysterious "..."

    hide mickey_happy
    show mickey_thinks at left

    mickey "Что дальше будем делать?"
    
    mysterious "Сначала мы с Колей сходим в банк, а ты иди домой и забери свои документы."

    mysterious "Затем мы встречаемся в аэропорту и покупаем билеты."

    mickey "Ладно, надеюсь, они не разрушили мой дом."

    pause(0.3)

    hide mickey_thinks at left with easeoutleft

    scene black

    center_text "Какое-то время спустя"

    jump part2_home

    return