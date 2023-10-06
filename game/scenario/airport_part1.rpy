label part1_airoport:

    scene airport_bg with dissolve

    show mickey_happy at center with moveinleft

    mickey "Вот и аэропорт."

    if mercenary_dead:
        mickey "Но я не вижу Загадочного."
        mickey "Я думаю, он скоро придет."
    else:
        mickey "Но я не вижу Загадочного с Колей."
        mickey "Я думаю, они скоро появятся."

    pause(0.7)

    hide mickey_happy
    show mickey_thinks
    with dissolve

    show mickey_thinks at left with moveinright
    show mysterious_normal at right with moveinright
    if not mercenary_dead:
        show kolya_normal at center with moveinright

    mickey "Всё ок?"

    if not mercenary_dead:
        kolya "С санитарами пришлось повозиться."

        mysterious "Кстати, сколько ты тут стоишь."

        mickey "Примерно 6-7 минут."

        pause(0.5)

        mysterious "Ладно, пойдемте внутрь."
    else:
        mysterious "Да... Идём внутрь."

    hide mickey_thinks
    show mickey_happy at left
    with dissolve

    hide mysterious_normal with easeoutright
    hide mickey_happy with easeoutleft
    if not mercenary_dead:
        hide kolya_normal with easeoutleft

    scene airport_inside_2_bg with dissolve

    show mysterious_normal at right with moveinleft
    show mickey_thinks at left with moveinleft
    if not mercenary_dead:
        show kolya_normal at center with moveinleft

    mickey "Так, а где агент по регистрации?"

    mysterious "Да вот же он."

    if not mercenary_dead:
        show kolya_normal at right with moveinright:
            xalign 0.7 yalign 1.0
        show mickey_thinks with moveinleft:
            xalign 0.35 yalign 1.0
    else:
        show mickey_thinks at center with moveinright
    show rig_agent_normal at left with moveinleft

    rigagent "Здравствуйте."

    mysterious "Здравствуйте, мы собираемся лететь в Сочи."

    rigagent "Давайте документы, деньги, и паспорт."

    play sound sound_list["journal_opening"]

    pause(2.5)

    rigagent "Угу."

    hide rig_agent_normal at left
    show rig_agent_happy at left
    with dissolve

    rigagent "Всё отлично."

    rigagent "Вам на 106 рейс."

    hide rig_agent_happy at left with easeoutleft
    show mickey_thinks at left with moveinleft

    if not mercenary_dead:
        show kolya_normal at center with easeinright

    pause(0.5)

    hide mickey_thinks
    show mickey_happy at left
    with dissolve

    if not mercenary_dead:
        kolya "Может сходим пока в кафе?"

        mysterious "Нет."

        mysterious "Скоро самолет улетит без нас."

        mysterious "Мы ведь этого не хотим?"

        pause(0.2)

        kolya "Эх..."

        kolya "А так хотелось."

        kolya "Ну ладно."

        kolya "Когда мы прилетим, я пойду в кафе."

        kolya "Правда мы будем летать длительное время."

        pause(0.7)

    mickey "Ну вперёд."

    hide mickey_happy with easeoutleft
    hide mysterious_normal with easeoutright
    if not mercenary_dead:
        hide kolya_normal with easeoutright

    scene airplane_bg with dissolve

    show mickey_happy at left with moveinleft
    show mysterious_normal at right with moveinright
    if not mercenary_dead:
        show kolya_normal at center with moveinright

    mickey "Я никогда не летал на самолете."

    mickey "Я не знаю какие у меня будут впечатление!"

    mysterious "Ты так говоришь как будто это что-то сверхъестественное."

    if not mercenary_dead:
        kolya "Мокки, не будь таким душниловой."

        kolya "В конце концов, по словам Микки, он никогда не летал на самолете."

    hide mickey_happy with easeoutleft
    hide mysterious_normal with easeoutright
    if not mercenary_dead:
        hide kolya_normal with easeoutright

    pause(2.0)

    show orderly_normal with moveinright

    "Набирает номер."

    durka "Да."

    orderly "Сэр, мы нашли их в аэропорту."

    orderly "И они отправляются в 106 рейс."

    durka "А насчёт наёмника?"

    if mercenary_dead:
        orderly "Он погиб."
    else:
        orderly "Он стал предателем."

    durka "Вот как."

    if mercenary_dead:
        durka "Жаль что технологии из будущего не достигли до такой развитии. Чтобы можно возрождать мёртвого."
    else:
        durka "Поймайте его, допросите, а затем убейте."

    pause(0.9)

    durka "Кстати, куда отправляется 106 рейс?"

    orderly "Хм... В Сочи."

    durka "Хорошо."

    durka "Я пошлю войска в Сочи."

    durka "Хотя погодите, вы должны схватить Микки прямо сейчас и посадить его на поезд!"

    pause(0.4)

    orderly "Хорошо, досвидания сэр!"

    durka "Досвидание."

    "Вызов завершен."

    hide orderly_normal
    scene black
    with dissolve

    jump part1_airplane

    return