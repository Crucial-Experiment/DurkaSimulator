init python:
    sound_list_nwdl = {}
    sound_list_nwdl["game_pc_start"] = "dlc/NewWorld/sound/pc/game_pc_start.mp3"
    sound_list_nwdl["game_windows_background"] = "dlc/NewWorld/sound/pc/game_windows_background.mp3"
    sound_list_nwdl["gas_stove"] = "dlc/NewWorld/sound/gas_stove.mp3"
    sound_list_nwdl["microwave_operation"] = "dlc/NewWorld/sound/microwave_operation.mp3"

image bg_mikki_kitchen = "dlc/NewWorld/images/mikki_kitchen.png"

label newWorld_DLC:

    stop music fadeout 1.0

    scene Redsquare with dissolve

    dictor "Данная история,{w=0.2} как и все начинается с 2020 года,{w=0.2} где в Москве сейчас проживает мальчик по имени Микки"

    dictor "Возможно вы спросите,{w=0.2} а почему рассказ начинается с красной площади?{w=0.2} Ответ очень прост,{w=0.2} ведь именно на ней произойдет самое важное событие в истории Микки"

    dictor "Давайте пока не торопить события,{w=0.2} а лучше отправимся к самому началу нашей истории"

    scene Mikki_House with dissolve

    show mikki_happy_image with moveinleft

    dictor "Недавно Микки поступил в колледж,{w=0.2} где вместе со своим другом Ларри покарают гранит науки,{w=0.2} но на самом деле они были оба странного характера ко всему что происходит в колледже"

    dictor "Поговаривали,{w=0.2} что это из-за них случаются все беды внутри помещения,{w=0.2} но все это были обычные сплетни ничего большего"

    dictor "Недавно их отправили на дистанционное обучение из-за технических проблем в колледже,{w=0.2} и от сюда начинается наша история"

    $ achievement.grant("MickeyStory")
    init:
        $ achievement.register("MickeyStory")
        $ achievement.sync()
    $ achievement.sync()

    mikki "Сегодня 15 октября,{w=0.2} и пока у нас не начались пары можно заняться более важными делами"

    menu:
        mikki "Выбор небольшой поиграть в компьютер, посмотреть аниме или поесть{w=0.4}.{w=0.4}.{w=0.4}"

        "Поиграть":
            mikki "Нет нечего важней чем игра в компьютер"

            hide mikki_happy_image with easeoutright

            pause(0.4)

            mikki "Всегда возникал вопрос,{w=0.2} а почему я выключаю его,{w=0.2} если можно так сэкономить время ожидания?"

            play sound "<from 0 to 15>" + sound_list_nwdl['game_pc_start']

            pause(14.9)

            play sound "<from 15 to 75>" + sound_list_nwdl['game_pc_start'] loop

            play audio sound_list_nwdl['game_windows_background']

            mikki "Странно,{w=0.2} в этот раз он запустился быстрее чем обычно,{w=0.2} но это даже лучше"

            mikki "Так пришло время запускать Grand Morning мою самую любимую игру"

            scene black with dissolve

            "Спустя какое-то количество времени"

            scene Mikki_House with dissolve

            mikki "Да блин опять я проиграл,{w=0.2} так хватит с меня игр за компьютером"

            stop sound

            play sound "<from 75>" + sound_list_nwdl['game_pc_start']

            pause(0.4)

            show mikki_happy_image with moveinright

            mikki "Каждый раз проигрываю в этой игре,{w=0.2} но все продолжаю в неё играть"

            mikki "Надо позвать в неё Ларри может с ним мне станет легче?"
        
        "Посмотреть аниме":
            mikki "Посмотрю, наверное,{w=0.2} продолжение одного из понравившихся мне аниме"

            mikki "Вчера я досмотрел первый сезон \"Этот сударь вечно умирает\",{w=0.2} и теперь хочется посмотреть продолжение"

            mikki "Интересно,{w=0.2} сколько по времени занимает рисование одной серии такого аниме?"

        "Покушать":
            mikki "Пойду лучше посмотрю,{w=0.2} что есть в холодильнике"

            hide mikki_happy_image with easeoutleft

            pause(0.4)

            scene bg_mikki_kitchen with dissolve

            show mikki_happy_image with moveinright

            mikki "Так посмотрим{w=0.4}.{w=0.4}.{w=0.4}. Значит у меня есть яйца,{w=0.2} салат,{w=0.2} макароны,{w=0.2} гречка и оливки"
            
            menu:
                mikki "Возьму ка я себе{w=0.4}.{w=0.4}.{w=0.4}."

                "Макароны":
                    mikki "Погрею себе макароны, так я смогу быстрее покушать и  вернутся к своим важным делам"

                    hide mikki_happy_image with easeoutright

                    pause(0.4)

                    play sound sound_list_nwdl["microwave_operation"]

                    pause(21)

                    show mikki_happy_image with moveinright

                    mikki "Так моя еда разогрелась"

                "Гречку":
                    mikki "Погрею себе гречку, так я смогу быстрее покушать и  вернутся к своим важным делам"

                    hide mikki_happy_image with easeoutright

                    pause(0.4)

                    play sound sound_list_nwdl["microwave_operation"]

                    pause(21)

                    show mikki_happy_image with moveinright

                    mikki "Так моя еда разогрелась"

                "Салат":
                    mikki "Возьму себе салат, так я смогу быстрее покушать и вернутся к своим важным делам"

                "Яйца":
                    mikki "Приготовлю себе что ли яичницу из яиц"

                    hide mikki_happy_image with easeoutright

                    pause(0.4)

                    play sound sound_list_nwdl['gas_stove']

                    pause(3.1)

                    mikki "Надо не забыть посолить мою яичницу"

                    pause(5)

                    stop sound

                    mikki "Ну вот моя яичница и готова"

                    $ achievement.grant("MickeyCooks")
                    init:
                        $ achievement.register("MickeyCooks")
                        $ achievement.sync()
                    $ achievement.sync()

            mikki "Пришло время к трапезе,{w=0.2} приятного аппетита самому себе"

            hide mikki_happy_image with dissolve

            scene black with dissolve

            #play sound sound_list_nwdl["microwave_operation"]

            show mikki_happy_image with dissolve

            scene bg_mikki_kitchen with dissolve

            mikki "После сытного обеда,{w=0.2} по закону Архимеда,{w=0.2} полагается заняться важными делами"

            hide mikki_happy_image with easeoutright

            pause(0.4)

            scene Mikki_House with dissolve

            pause(0.4)

            show mikki_happy_image with moveinleft

    return