define config.quit_callbacks += [discord.close] 

define config.after_load_callbacks += [discord.on_load] 

define config.interact_callbacks += [discord.rollback_check] 

define config.start_callbacks += [discord.reset]

define config.label_callback = discord.set_start 

init -950 python in discord:

    def print_important(s):
        global log_important
        if log_important is True:
            print("\n" + s)
    def print_properties(s):
        global log_properties
        if log_properties is True:
            print("\n" + s)
    def print_rollback(s):
        global log_restore
        if log_restore is True:
            print("\n" + s)

    def format_properties(d):
        s = ""
        for key in d:
            s += "\n{}: ".format(key).ljust(14) + " {}".format(d[key])
        return s

    import pypresence

    try:
        print_important("Attempting to connect to Discord Rich Presence...")
        presence_object = pypresence.Presence(application_id)
        presence_object.connect()
        print_important("Successfully connected.")

    except pypresence.DiscordNotFound:
        print_important("Discord Desktop App not found. Rich Presence will be disabled.")
        presence_object = None

    except pypresence.DiscordError:
        print_important("Error occured during connection. Rich Presence will be disabled.")
        presence_object = None

    from store import NoRollback

    import time

    start_time = time.time()

    from copy import deepcopy

    def presence_disabled(func):
        global presence_object
        if presence_object is None:
            return return_none
        else:
            return func

    def return_none(*_args, **_kwargs): pass

    def record_into_rollback():
        global no_rollback, rollback_properties
        rollback_properties = deepcopy(no_rollback.properties)

    def clean_properties(d):
        d = deepcopy(d)
        global start_time
        if "start" in d:
            if d["start"] == "start_time":
                d["start"] = start_time
        return d

    @presence_disabled
    def set(log = True, **props):

        if "start" in props: #
            if props["start"] == "new_time":
                props["start"] = time.time()

        else:
            props["start"] = "start_time"

        global no_rollback
        no_rollback.properties = deepcopy(props)

        global presence_object
        presence_object.update(**clean_properties(no_rollback.properties))

        record_into_rollback()

        if log:
            print_properties("Discord Presence Set:{}".format(format_properties(rollback_properties)))

    @presence_disabled
    def update(log = True, **props):
        if "start" in props:
            if props["start"] == "new_time":
                props["start"] = time.time()

        global no_rollback
        for p in props:
            no_rollback.properties[p] = props[p]

        global presence_object
        presence_object.update(**clean_properties(no_rollback.properties))

        record_into_rollback()

        if log:
            print_properties("Discord Presence Updated:{}".format(format_properties(rollback_properties)))

    @presence_disabled
    def reset():
        global original_properties
        set(**original_properties)

    @presence_disabled
    def on_load():
        print_rollback("Discord Presence has been loaded from a save file:{}".format(format_properties(rollback_properties)))

        global rollback_properties
        set(log = False, **rollback_properties)

    @presence_disabled
    def rollback_check():
        global no_rollback, rollback_properties

        if no_rollback.properties != rollback_properties:
            print_rollback("Discord Presence does not match during this interaction. It is restored from the rollbackable variable:{}".format(format_properties(rollback_properties)))

            set(log = False, **rollback_properties)

    @presence_disabled
    def set_start(label_name, interaction):
        global start_state, start_label
    
        if isinstance(start_label, list):
            if label_name in start_label:
                set(**start_state)

        elif label_name == start_label:
            set(**start_state)

    @presence_disabled
    def clear():
        global no_rollback
        no_rollback.properties = {}
        
        record_into_rollback()

        global presence_object
        presence_object.clear()

    @presence_disabled
    def close():
        print_important("Closing DRP connection.")

        global presence_object
        presence_object.close()

        print_important("Successfully closed.")

    class RenPyDiscord(NoRollback):
        def __init__(self):
            self.properties = {} 

    global original_properties, main_menu_state    
    original_properties = deepcopy(main_menu_state)

    if not "start" in original_properties:
        original_properties["start"] = "start_time"

    from store import Action

    @presence_disabled
    @renpy.pure
    class Set(Action):

        def __init__(self, **properties):
            self.properties = properties

        def __call__(self):
            set(**self. properties)

            renpy.restart_interaction()

        def get_sensitive(self):
            global presence_object
            return presence_object is not None

        def get_selected(self):
            global rollback_properties

            if "start" in rollback_properties:

                if not "start" in self.properties:

                    a = deepcopy(self.properties)
                    a["start"] = "start_time"

                return a == rollback_properties

            return self.properties == rollback_properties

    @presence_disabled
    @renpy.pure
    class Update(Action):

        def __init__(self, **properties):
            self.properties = properties

        def __call__(self):
            update(**self. properties)

            renpy.restart_interaction()

        def get_sensitive(self):
            global presence_object
            return presence_object is not None

        def get_selected(self):
            global rollback_properties

            if "start" in rollback_properties:

                if not "start" in self.properties:

                    a = deepcopy(self.properties)
                    a["start"] = "start_time"

                return a == rollback_properties

            return self.properties == rollback_properties

define discord.no_rollback = discord.RenPyDiscord()

default discord.rollback_properties = {}