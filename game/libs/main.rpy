init python:
    import math

    def profanity_tag(tag, argument, contents):
        rv = [ ]
        tx = [ ]

        for kind, text in contents:
            if persistent.profanity:
                if kind == renpy.TEXT_TEXT:
                    for i in range(len(text)):
                        tx.append("*")
                    text = ''.join(map(str, tx))

            rv.append((kind, text))

        return rv

    config.custom_text_tags["prof"] = profanity_tag

    def newest_slot_tuple():
        newest = renpy.newest_slot()

        if newest is not None:
            page, name = newest.split("-")
            return (page, name)

    class Continue(Action):

        def __call__(self):

            if not self.get_sensitive():
                return

            newest_page, newest_name = newest_slot_tuple()

            FileLoad(newest_name, confirm=False, page=newest_page, newest=True)()

        def get_sensitive(self):

            if not main_menu:
                return False

            if _in_replay:
                return False

            newest = newest_slot_tuple()

            if newest is None:
                return False

            newest_page, newest_name = newest

            if newest_page == '_reload':
                return False

            return FileLoadable(newest_name, page=newest_page)

    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [ self.anchors.get(i, i) for i in start ]
            self.dist = dist
            self.child = child

        def __call__(self, t, sizes):
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move, time, child,add_sizes=True, **properties)

    Shake = renpy.curry(_Shake)

    def moving_camera(trans, st, at):
        if persistent.parallax:
            x, y = renpy.display.draw.get_mouse_pos()
            trans.xoffset = (x - config.screen_width / 2) * .05
            trans.yoffset = (y - config.screen_height / 2) * .05
        else:
            trans.xoffset = 0
            trans.yoffset = 0
        return 0