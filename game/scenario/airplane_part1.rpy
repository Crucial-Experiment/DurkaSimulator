label part1_airplane:

    scene black with dissolve
    pause(0.2)
    scene airplane_inside_bg with dissolve
    
    $ achievement.grant("WelcomeToPlane")
    $ achievement.sync()

    show mickey_happy at left with moveinleft
    show mysterious_normal at right with moveinright
    if not mercenary_dead:
        show kolya_normal at center with moveinright

    if not mercenary_dead:
        mickey "Коля, на каких места мы сидим?"

        kolya "Я пока не смотрел, ща..."

        play sound sound_list["paper_rustle"]

        "Коля перебирает билеты."

        stop sound fadeout 0.5

        kolya "Тридцать пятое, тридцать шестое и тридцать седьмое."

        mickey "Тогда давайте займем свои места."
    else:
        mickey "Загадочный, на каких места мы сидим?"

        mysterious "Тридцать пятое и тридцать шестое."

        mickey "Может быть, тогда займем свои места?"

    scene black with dissolve
    pause(0.2)
    if not mercenary_dead:
        scene airplane_inside_c4_bg
    else:
        scene airplane_inside_c1_bg
    show mysterious_normal
    with dissolve

    mysterious "Пойду пройдусь, может, что-нибудь найду."

    hide mysterious_normal with easeoutright

    if not mercenary_dead:
        show airplane_inside_m1 with dissolve

        mickey "Как ты себя чувствуешь?"

        show airplane_inside_k1 with dissolve

        kolya "Как ты думаешь? После многочисленных ударов арматурой, как я себя буду чувствовать?"

        mickey "Великолепно."

        play sound sound_list["laugh"]

        pause(4.8)

        hide airplane_inside_m1
        show airplane_inside_m2
        with dissolve

        mickey "Что это сейчас было?"

        kolya "Ты про что?"

        mickey "Только не говори, что ты этого не слышал."

        kolya "Ты, должно быть, шутишь, Микки."

        kolya "Ладно, я пойду вздремну."

        hide airplane_inside_m1
        show airplane_inside_k2_anim
        with dissolve

        mickey "Ладно..."
    else:
        mickey "Мда... Чем бы занятся..."

        mickey "Посмотрю несколько мемов, может, найду что-нибудь для Загадочного."

        scene black with dissolve

        center_text "Какое-то время спустя"

        scene airplane_inside_c1_bg with dissolve

    show mysterious_normal with moveinright

    mysterious "В общем, ничего интересного я не увидел."

    if not mercenary_dead:
        scene airplane_inside_c3_bg
        show airplane_inside_k2
        with dissolve
    else:
        scene airplane_inside_c2_bg
        with dissolve

    mysterious "Микки, ты ведь никогда не был на самолете, хочешь пройтись?"

    mickey "Нет, спасибо."

    play sound sound_list["dadsaasd"]

    pause(0.9)

    stewardess "Дамы и господа, добро пожаловать на борт рейса CH-4."

    stewardess "В настоящее время мы находимся в четвертой очереди на взлет и должны подняться в воздух примерно через 10 минут."

    stewardess "Мы просим вас пристегнуть ремни безопасности и закрепить весь багаж..."

    stewardess "Благодарим вас за выбор авиакомпании Крэйзи Эйрлайнс. Приятного полета!"

    play sound sound_list["dadsaasd"]

    pause(0.9)

    if not mercenary_dead:
        mickey "Эй, Мокки, почему ты сразу не сказал мне, кто ты такой?"

        mysterious "Я не хотел пугать тебя раньше времени."

        mickey "..."

        mickey "В итоге ты все равно меня напугал."

        mysterious "Это не входило в мои планы..."

        mickey "Мокки, тебе удалось с Вероникой это?"
        
    else:
        mickey "Загадочный, ты не знаешь, мне в будущем удалось с Вероникой это?"

    mysterious "Вероника?"

    mickey "Ну да."

    mysterious "Хм... Нет... Не получилось."

    mickey "Ну, екарная бочка..."

    mysterious "Возможно, ты сможешь это сделать благодаря мне."

    mickey "Ты о чем?"

    mysterious "Слушай, я пока не хочу поднимать эту тему."

    mysterious "Может быть, поговорим об этом позже?"

    mickey "Хорошо..."

    pause(0.5)

    mickey "..."

    mickey "Пум-пурум."

    mickey "Пум-пуруууум."

    mickey "Мда..."

    mickey "Микки а... Ой, то есть Мокки."

    mickey "Никак не привыкну."

    mysterious "Да?"

    mickey "Анекдот хочешь?"

    mysterious "Ну, давай."

    mickey "Известная авиакомпания набирает пилотов."

    mickey "На это место претендуют немец, американец и россиянин."

    mickey "Директор компании спрашивает немца."

    mickey "Как давно вы летаете?"

    mickey "Три года."

    mickey "Сколько бы вы хотели получать?"

    mickey "Три тысячи. Тысяча для меня, тысяча для жены, тысяча для страховки."

    mickey "Затем директор спрашивает американца."

    mickey "Давно летаете?"

    mickey "Шесть лет."

    mickey "Сколько бы вы хотели получать?"

    mickey "Шесть тысяч. Две для меня, две для жены, две для страховки."

    mickey "Настала очередь русского."

    mickey "Как давно вы летаете?"

    mickey "Не дай Бог, я даже летать не умею и высоты боюсь."

    mickey "Я хочу зарабатывать девять тысяч."

    mickey "В смысле?! - Спросил директор."

    mickey "Ну, пять для меня, четыре для вас."

    mickey "Стоп, а кто полетит?"

    mickey "Как кто — немец, он же за три согласен!"

    mysterious "..."

    mysterious "Ну, такое."

    mickey "..."

    mickey "Какой жанр анекдотов тебе нравится в целом?"

    mysterious "Комедийный, моральный."

    mickey "А что?"

    mickey "Просто это уже второй анекдот, который я тебе рассказываю, а ты даже не улыбнулся."

    mysterious "Я должен смеяться над каждой вещью?"

    mickey "Нет, нет!"

    mysterious "...Честно говоря, я не очень понял, что ты имеете в виду."

    mickey "Что тут непонятного."

    show stewardess_normal with moveinright

    stewardess "Чай? Кофе? Воду? Покушать желаете?"

    mickey "Нет, спасибо."

    if not mercenary_dead:

        hide airplane_inside_k2
        show airplane_inside_k2_anim2
        with dissolve
        hide airplane_inside_k2_anim2 with dissolve

        kolya "Мы уже прилетели?"

        mysterious "Нет ещё..."

        kolya "Тогда зачем вы меня разбудили?"

        stewardess "Вы будете что-то пить?"

        kolya "Боже, я не ожидал, что вы тут."

        stewardess "Прошу прощения."

        stewardess "Будете что-то брать?"

        kolya "Нет, спасибо."

        stewardess "Хорошо."

        hide stewardess_normal with easeoutleft

        kolya "Мокки, ради этого надо было меня будить?"

        kolya "Мне кажется, ты меня тайно ненавидишь."
    else:
        stewardess "Хорошо."

        hide stewardess_normal with easeoutleft

    scene black with dissolve

    play sound sound_list["airplane_takeoff"]

    pause(15.0)

    stop sound fadeout 1.0

    play sound sound_list["inside_airplane"] loop fadein 1.0

    if not mercenary_dead:
        scene airplane_inside_c3_bg with dissolve
    else:
        scene airplane_inside_c2_bg with dissolve

    mickey "Ура, мы взлетаем."

    mysterious "Поздравляю с первым полетом."

    scene black with dissolve

    center_text "Спустя 3 часа"

    stop sound fadeout 1.0

    if not mercenary_dead:
        scene airplane_inside_c3_bg with dissolve
    else:
        scene airplane_inside_c2_bg with dissolve

    play sound sound_list["dadsaasd"]

    pause(0.9)

    stewardess "Дамы и господа, мы прибыли в Сочи."

    stewardess "Будьте осторожны на выходе..."

    play sound sound_list["dadsaasd"]

    pause(0.9)

    play sound sound_list["shot_1"] volume 0.4

    pause(0.6)

    "???" "ТАК, ТИХО ВСЕМ!"

    "???" "Я спрашиваю ещё раз."

    "???" "Вы видели мудака в синем свитере!!??"

    show airplane_inside_m2 with dissolve

    "Пассажиры" "МЫ БЕЗ ПОНЯТИЯ О КОМ ВЫ."

    play sound sound_list["shot_1"] volume 0.4

    pause(0.6)

    "???" "ДА ГДЕ ЭТОТ МИККИ МАУС???!!!"

    if not mercenary_dead:

        scene airplane_inside_c2_bg
        show airplane_inside_m2
        show kolya_normal
        with dissolve

        kolya "Мокки, ты защищай Микки, а я разберусь с ними."

        "???" "Прощай, предатель."

        play sound sound_list["shot_1"] volume 0.8

        pause(0.6)

        hide kolya_normal
        show kolya_dead
        with dissolve

        $ achievement.grant("StrayBullet")
        $ achievement.sync()

        pause(1.2)

        hide kolya_dead with dissolve
        play sound sound_list["fall"]

        mysterious "Они убили его..."

        mickey "Аа-бб-вые."

        mysterious "Микки... Микки!!!"

        mysterious "Очнись же ты."

        scene black with dissolve

        play sound sound_list["slap"]

        pause(0.8)

        scene airplane_inside_bg
        show mysterious_normal at left
        show mickey_shouts at right
        with dissolve

        mickey "Они убили его..."

        mysterious "Микки, хватит стоять столбом, найди аптечку!"

    else:
        scene airplane_inside_bg
        show mysterious_normal at left
        show mickey_shouts at right
        with dissolve

        mysterious "Микки, хватит стоять столбом!"

    "???" "АГА! Я ИХ ВИЖУ!!"

    mysterious "О, черт, убегаем."

    if not mercenary_dead:
        mickey "Но... Но как же Коля?"
    else:
        mickey "Но... Но..."  

    play sound sound_list["shot_1"] volume 0.8

    pause(0.6)

    if not mercenary_dead:
        mickey "Ладно, понял. Извини, Коля..."
    else:
        mickey "Ладно, понял."

    play sound sound_list["shot_1"] volume 0.8

    pause(0.6)

    hide mysterious_normal with easeoutleft
    hide mickey_shouts with easeoutleft

    scene black with dissolve
    pause(1.2)
    scene airport_inside_1_bg with dissolve

    show mysterious_normal at left
    show mickey_not_happy at right
    with moveinleft

    mickey "Как же мне надоели эти санитары, когда же это закончится...."

    if not mercenary_dead:
        mickey "Мокки, почему мы бросили Колю?"

        mysterious "Мы его почти не знали, я уверен, что санитары уже забрали его и что-то с ним делают."

        mickey "Ты видел, как ему было больно."

        mysterious "Я видел, но это не значит, что он не наигрывал."

        mickey "..."

        mickey "ОН ИСТЕКАЛ КРОВЬЮ!"

        mysterious "Такое случается, и я думаю, что мы бежали от террористов."

        "???" "Далеко собрались?"

        mickey "Пришло время уходить отсюда..."

    scene black with dissolve

    center_text "Конец демо-версии эпизода\nОжидайте следующий обновлений"

    return