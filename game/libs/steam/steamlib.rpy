#Created by: Xrisofor
#GitHub link: https://github.com/Xrisofor

init python:
    config.hyperlink_handlers['steam_web_overlay'] = _steamlib.activate_overlay_to_web_page
    config.hyperlink_handlers['steam_store_overlay'] = _steamlib.activate_overlay_to_store
    config.hyperlink_handlers['steam_inv_dialog'] = _steamlib.activate_game_overlay_invite_dialog

    if not renpy.variant("mobile"):
        _steamlib.steam_init()

init -1499 python in _steamlib:

    import steamapi, requests, json, ctypes

    def steam_init():
        return steamapi.Init()

    # SteamUser

    def get_steam_id():
        """
        Gets the AppID of the current process.
        """
        return steamapi.SteamUser().GetSteamID()

    # SteamUtils

    def get_app_id():
        """
        Gets the AppID of the current process.
        """
        return steamapi.SteamUtils().GetAppID()

    def is_overlay_enabled():
        """
        Checks whether the Steam overlay is open and whether the user has access to it.
        """
        return steamapi.SteamUtils().IsOverlayEnabled()

    def is_steam_china_launcher():
        """
        Returns whether the current launcher is the Steam China version. You can make the client
        work as a Steam China launcher by adding dev -steamchina to the command line when Steam starts.
        """
        return steamapi.SteamUtils().IsSteamChinaLauncher()

    def is_steam_in_big_picture_mode():
        """
        Checks whether Steam and the Steam overlay are running in Big Picture mode.
        """
        return steamapi.SteamUtils().IsSteamInBigPictureMode()

    def is_steam_running_on_steam_deck():
        """
        Checks whether Steam is running on the Steam Deck.
        """
        return steamapi.SteamUtils().IsSteamRunningOnSteamDeck()

    def is_steam_running_in_vr():
        """
        Checks whether Steam is running in VR mode.
        """
        return steamapi.SteamUtils().IsSteamRunningInVR()

    def get_steam_ui_language():
        """
        Returns the language in which the Steam client is running.
        """
        return steamapi.SteamUtils().GetSteamUILanguage().decode("utf-8")

    def set_game_launcher_mode(bLauncherMode):
        """
        If the game launcher does not support the controller, you can call this function so that
        the Steam input system allows you to control the launcher using the keyboard/mouse.
        """
        steamapi.SteamUtils().SetGameLauncherMode(bLauncherMode)

    # SteamFriends

    def get_persona_name():
        """
        Gets the current user's persona (display) name.
        This is the same name that is displayed the user's community profile page.
        """
        return steamapi.SteamFriends().GetPersonaName().decode("utf-8")

    def get_persona_state():
        """
        Retrieves the status of the current user.
        """
        return steamapi.SteamFriends().GetPersonaState()

    def activate_overlay_to_web_page(url):
        """
        Opens the specified link in the overlay's web browser.
        """
        steamapi.SteamFriends().ActivateGameOverlayToWebPage(url.encode('utf-8'), steamapi.k_EActivateGameOverlayToWebPageMode_Default)

    def activate_overlay_to_store(appid, flag=None):
        """
        Opens the page of the specified application in the Steam store in the overlay.
        Optional parameter that uses _renpysteam to output the desired result,
        you can use one of the three flag types: achievement.steam.STORE_NONE, .STORE_ADD_TO_CART,
        or .STORE_ADD_TO_CART_AND_SHOW.
        """
        if flag is None:
            flag = achievement.steam.STORE_NONE

        steamapi.SteamFriends().ActivateGameOverlayToStore(appid, flag)

    def activate_game_overlay_invite_dialog(lobbyid):
        """
        Opens the invitation window in the overlay. The invitations sent in this
        window will relate to the specified lobby.
        """
        steamapi.SteamFriends().ActivateGameOverlayInviteDialog(lobbyid)

    def close_clan_chat_window_in_steam(clanchatid):
        """
        Closes the specified group chat in the Steam interface.
        """
        steamapi.SteamFriends().CloseClanChatWindowInSteam(clanchatid)

    def get_clan_chat_member_count(clanid):
        """
        Gets the number of users in the Steam group chat.
        """
        return steamapi.SteamFriends().GetClanChatMemberCount(clanid)

    def get_clan_count():
        """
        Gets the number of groups that the current user is a member of.
        """
        return steamapi.SteamFriends().GetClanCount()

    def get_clan_name(clanid):
        """
        Gets the displayed name of the specified Steam group, if it is known to the local client.
        """
        return steamapi.SteamFriends().GetClanName(clanid)

    def get_clan_officer_count(clanid):
        """
        Gets the number of officers (administrators and moderators) in the specified Steam group.
        """
        return steamapi.SteamFriends().GetClanOfficerCount(clanid)

    def get_clan_owner(clanid):
        """
        Gets the owner of the Steam group.
        """
        return steamapi.SteamFriends().GetClanOwner(clanid)

    def get_clan_tag(clanid):
        """
        Gets a unique label (abbreviation) the specified Steam group, if it is known to the local client.
        """
        return steamapi.SteamFriends().GetClanTag(clanid).decode('utf-8')

    def get_coplay_friend(coplayfriend):
        """
        Gets the SteamID of those who have recently played with this user, according to the specified index.
        """
        return steamapi.SteamFriends().GetCoplayFriend(coplayfriend)

    def get_coplay_friend_count():
        """
        Gets the number of players that the current user has recently played with, across all games.
        """
        return steamapi.SteamFriends().GetCoplayFriendCount()

    def get_follower_count(user):
        """
        Gets the number of users subscribed to the specified user.
        """
        return steamapi.SteamFriends().GetFollowerCount(user)

    def get_friend_coplay_game(user):
        """
        Gets the AppID of the game that the user played with someone from
        the "recently played together" list.
        """
        return steamapi.SteamFriends().GetFriendCoplayGame(user)

    def get_friend_coplay_time(user):
        """
        Gets the time when the user played with someone from the "recently played together" list.
        """
        return steamapi.SteamFriends().GetFriendCoplayTime(user)

    def get_friend_count(friendflags):
        """
        Gets the number of users meeting the specified criteria that the
        client knows about (friends, blocked, users on the same server, etc.).
        EFriendFlags: https://partner.steamgames.com/doc/api/ISteamFriends#EFriendFlags
        """
        return steamapi.SteamFriends().GetFriendCount(friendflags)

    def get_friend_persona_name(user):
        """
        Retrieves the profile name of the specified user.
        It is known to the current user only if another user is in his friends list,
        on the same game server, in a chat or lobby, or in a small Steam group with a local user.
        """
        return steamapi.SteamFriends().GetFriendPersonaName(user).decode('utf-8')

    def get_friends_group_count():
        """
        Gets the number of friend groups (tags) created by the user.
        """
        return steamapi.SteamFriends().GetFriendsGroupCount()

    def get_friend_steam_level(user):
        """
        Gets the Steam level of the specified user.
        """
        return steamapi.SteamFriends().GetFriendSteamLevel(user)

    def invite_user_to_game(user, pchConnectString):
        """
        Invites a friend or clan member to the current game using a special invitation string.
        If the target user accepts the invitation, then pchConnectString is added to
        the command line when the game starts.
        If the game is already running, then he will receive a GameRichPresenceJoinRequested_t
        callback with the prompt string (https://partner.steamgames.com/doc/api/ISteamFriends#GameRichPresenceJoinRequested_t)
        """
        return steamapi.SteamFriends().InviteUserToGame(user, pchConnectString)

    def set_rich_presence(pchKey, pchValue):
        """
        Sets the key-value pair of the extended status of the current user, which is
        automatically sent to all friends playing the same game.
        Each user can have up to 20 keys, as defined in k_cchmaxrichpresenckeys.
        Additional important information: https://partner.steamgames.com/doc/api/ISteamFriends#SetRichPresence
        """
        try:
            return steamapi.SteamFriends().SetRichPresence(pchKey.encode('utf-8'), pchValue.encode('utf-8'))
        except:
            print("Unable to update Rich Presence, please try again later")

    def clear_rich_presence():
        """
        Deletes the key-value pairs of the extended status of the current user.
        """
        try:
            steamapi.SteamFriends().ClearRichPresence()
        except:
            print("Unable to clear Rich Presence, please try again later")

    def friend_rich_presence(id, pchKey):
        """
        Gets the value of the extended status of the specified friend.
        """
        try:
            return steamapi.SteamFriends().GetFriendRichPresence(id, pchKey.encode('utf-8'))
        except:
            print("Unable to get a friend's Rich Presence, please try again later")

    def request_friend_rich_presence(id):
        """
        Requests the extended status data of the specified user.
        It is used to get information about the extended status of a user who
        is not a friend of the current user, for example, someone in the current
        lobby or on the game server.
        """
        try:
            return steamapi.SteamFriends().RequestFriendRichPresence(id)
        except:
            print("Unable to request data from Rich Presence, please try again later")

    # SteamApps

    def vac_banned():
        """
        Checks whether there is a VAC lock on the user's account.
        """
        return steamapi.SteamApps().BIsVACBanned()

    def get_current_game_language():
        """
        Retrieves the current language selected by the user.
        If the user has not set the language of the product separately,
        the language of the Steam interface will be received.
        """
        return steamapi.SteamApps().GetCurrentGameLanguage().decode("utf-8")

    def app_installed(appid):
        """
        Checks whether a specific application is installed.
        """
        return steamapi.SteamApps().BIsAppInstalled(appid)

    def is_cybercafe():
        """
        Checks whether the current application is intended for an Internet cafe.
        """
        return steamapi.SteamApps().BIsCybercafe()

    def dlc_installed(appid):
        """
        Checks whether the user owns a specific additional content, and whether it is installed.
        """
        return steamapi.SteamApps().BIsDlcInstalled(appid)

    def is_low_violence():
        """
        Checks whether the license that the user owns provides repositories with content with a low level of violence.
        """
        return steamapi.SteamApps().BIsLowViolence()

    def is_subscribed():
        """
        Checks whether the active user is subscribed to the current AppID.
        """
        return steamapi.SteamApps().BIsSubscribed()

    def is_subscribed_app(appid):
        """
        Checks whether the active user is subscribed to the specified AppID.
        """
        return steamapi.SteamApps().BIsSubscribedApp(appid)

    def is_subscribed_from_family_sharing():
        """
        Checks whether an active user is using a Family Library Sharing license owned by another user to access the current AppID.
        """
        return steamapi.SteamApps().BIsSubscribedFromFamilySharing()

    def is_subscribed_from_free_weekend():
        """
        Checks whether an active user is subscribed to the current AppID as part of the "Free Weekend" promotion.
        """
        return steamapi.SteamApps().BIsSubscribedFromFreeWeekend()

    def get_app_build_id():
        """
        Gets the build ID of this application. The value can change at any time if game changes occur on the server.
        """
        return steamapi.SteamApps().GetAppBuildId()

    def get_app_owner():
        """
        Gets the SteamID of the original owner of the current application. If the owner and the current user are different, the application is borrowed.
        """
        return steamapi.SteamApps().GetAppOwner()

    def get_available_game_languages():
        """
        Gets a comma-separated list of languages supported by the current application.
        """
        return steamapi.SteamApps().GetAvailableGameLanguages().decode("utf-8")

    def get_dlc_count():
        """
        Returns the number of additional content elements for the current application.
        """
        return steamapi.SteamApps().GetDLCCount()

    def install_dlc(appid):
        """
        Allows you to set an optional element of additional content.
        """
        steamapi.SteamApps().InstallDLC(appid)

    def mark_content_corrupt(missfileonly = False):
        """
        Allows you to forcibly check the content of the game at the next launch.
        If you find that the game is outdated (for example, if the client determines that
        the version does not match the version on the server), you can call MarkContentCorrupt to
        force verification, show a message to the user and exit the game.
        """
        steamapi.SteamApps().MarkContentCorrupt(missfileonly)

    def uninstall_dlc(appid):
        """
        Allows you to delete an optional element of additional content.
        """
        steamapi.SteamApps().UninstallDLC(appid)

    def dlc_progress(appid):
        """
        Receives data on the progress of downloading optional additional content.
        """
        from ctypes import c_ulonglong, byref

        done = c_ulonglong(0)
        total = c_ulonglong(0)

        if steamapi.SteamApps().GetDlcDownloadProgress(appid, byref(done), byref(total)):
            return done.value, total.value
        else:
            return None

    def get_launch_command_line():
        """
        Gets the command line if the game is launched via a link to Steam,
        for example: steam://run/<appid>//<command line>/. This method is preferable to
        running from the command line through the operating system, which may threaten
        the security of the account. To ensure that this method works when logging in using
        extended statuses without placing it on the OS command line, you need to enable the
        option to use the launch command line from the Installation > General page of your
        application.
        """
        from ctypes import byref, c_bool

        rv = c_bool(False)
        pint = 0

        if not steamapi.SteamApps().GetLaunchCommandLine(byref(rv).decode("utf-8"), pint):
            return None

        return rv.value

    # SteamUserStats

    def find_leaderboard(pchLeaderboardName):
        """
        Gets a list of leaders by name.
        """
        return steamapi.SteamUserStats().FindLeaderboard(pchLeaderboardName.encode('utf-8'))

    def get_leaderboard_entry_count(leaderboard):
        """
        Returns the full number of positions in the leaderboard.
        """
        return steamapi.SteamUserStats().GetLeaderboardEntryCount(leaderboard)

    def get_leaderboard_name(leaderboard):
        """
        Returns the name of the leaderboard.
        """
        return steamapi.SteamUserStats().GetLeaderboardName(leaderboard).decode('utf-8')

    def get_number_of_current_players():
        """
        Asynchronously retrieves the total number of users currently playing this game, both online and offline.
        """
        return steamapi.SteamUserStats().GetNumberOfCurrentPlayers()

    def get_achievement(pchName):
        """
        Gets the achievement unlock status.
        """
        from ctypes import byref, c_bool

        rv = c_bool(False)

        if not steamapi.SteamUserStats().GetAchievement(pchName.encode("utf-8"), byref(rv)):
            return None

        return rv.value

    def get_achievement_icon(pchName):
        """
        Gets the achievement icon.
        """
        return steamapi.SteamUserStats().GetAchievementIcon(pchName.encode("utf-8"))

    def get_achievement_display_attribute(pchName, pchKey = "name"):
        """
        Gets the general attributes of the achievement. Currently provides the following data: name, description and "stealth".
        
        This call gets the value from the dictionary/key-value pair map, so you have to send one of the following keys.
            "name" — to get the localized name of the achievement in UTF-8.
            "desc" — to get the localized description of the achievement in UTF-8.
            "hidden" — whether the achievement is hidden. Returns "0" if not hidden, and "1" if hidden.
        """
        return steamapi.SteamUserStats().GetAchievementDisplayAttribute(pchName.encode("utf-8"), pchKey.encode("utf-8"))

    def get_achievement_achieved_percent(pchName):
        """
        Returns the percentage of users who received the specified achievement.
        """
        from ctypes import byref, c_bool

        rv = c_bool(False)

        if not steamapi.SteamUserStats().GetAchievementAchievedPercent(pchName.encode("utf-8"), byref(rv)):
            return None

        return rv.value

    def get_achievement_name(iAchievement):
        """
        Gets the "API Name" by the achievement index between 0 and GetNumAchievements.
        """
        return steamapi.SteamUserStats().GetAchievementName(iAchievement).decode("utf-8")

    def get_num_achievements():
        """
        Gets the number of achievements defined in the partner site administration panel.
        """
        return steamapi.SteamUserStats().GetNumAchievements()

    def get_user_achievement(user, pchName):
        """
        Gets the unblocking status of an achievement from a specific user.
        """
        from ctypes import byref, c_bool

        rv = c_bool(False)

        if not steamapi.SteamUserStats().GetUserAchievement(user, pchName.encode("utf-8"), byref(rv)):
            return None

        return rv.value

    def list_achievements():
        """
        Returns a list of achievement names.
        """
        rv = [ ]

        na = steamapi.SteamUserStats().GetNumAchievements()

        for i in range(na):
            rv.append(steamapi.SteamUserStats().GetAchievementName(i).decode("utf-8"))

        return rv

    def indicate_achievement_progress(name, cur_progress, max_progress):
        """
        Shows the user a pop-up notification with the status of achievement completion.
        Calling this function DOES NOT set the status of the achievement and does not unlock it,
        the game must explicitly do this using SetStat!
        """
        return steamapi.SteamUserStats().IndicateAchievementProgress(name.encode("utf-8"), cur_progress, max_progress)

    def store_stats():
        """
        Sends the changed statistics and achievements to the server for permanent storage.
        """
        steamapi.SteamUserStats().StoreStats()

    def retrieve_stats():
        """
        Asynchronously requests current statistics and user achievements from the server.
        """
        steamapi.SteamUserStats().RequestCurrentStats()

    def request_global_achievement_percentages():
        """
        synchronously receives data on the percentage of players who have
        globally received each of the achievements of this game.
        """
        steamapi.SteamUserStats().RequestGlobalAchievementPercentages()

    def reset_all_stats(achievementsToo=False):
        """
        Resets the statistics of the current user and, optionally, achievements.
        """
        return steamapi.SteamUserStats().ResetAllStats(achievementsToo)

    def grant_achievement(name):
        """
        Opens the achievement. Be sure to call the `_steamlib.store_stats`
        function to publish the changes to the server.
        """
        return steamapi.SteamUserStats().SetAchievement(name.encode("utf-8"))

    def clear_achievement(name):
        """
        Resets the unlock status of the achievement. Be sure to call
        the `_steamlib.store_stats` function to publish the changes to the server.
        """
        return steamapi.SteamUserStats().ClearAchievement(name.encode("utf-8"))

    # SteamUGC

    def show_workshop_eula():
        """
        Show the app's latest Workshop EULA to the user in an overlay window, where
        they can accept it or not
        """
        return steamapi.SteamUGC().ShowWorkshopEULA()

    def get_workshop_eula_status():
        """
        Asynchronously retrieves data about whether the user accepted the Workshop EULA for
        the current app.
        """
        return steamapi.SteamUGC().GetWorkshopEULAStatus()

    # SteamRemotePlay

    def get_session_count():
        """
        Gets the number of current Steam Remote Play sessions
        """
        return steamapi.SteamRemotePlay().GetSessionCount()

    def get_session_id(sessionIndex):
        """
        Gets the ID of the current Steam Remote Play session by the specified number
        """
        return steamapi.SteamRemotePlay().GetSessionID(sessionIndex)

    def get_session_steam_id(sessionId):
        """
        Get the SteamID of the connected user
        """
        return steamapi.SteamRemotePlay().GetSessionSteamID(sessionId)

    def get_session_client_name(sessionId):
        """
        Get the name of the session client device
        """
        return steamapi.SteamRemotePlay().GetSessionClientName(sessionId).decode('utf-8')

    def send_remote_play_together_invite(user):
        """
        Get the name of the session client device
        """
        return steamapi.SteamRemotePlay().BSendRemotePlayTogetherInvite(user)


    # SteamInventory

    def get_all_items():
        steam_user_id = get_steam_id()

        response = requests.get(f"https://api.crucialexperiments.com/durka_simulator/items/{steam_user_id}")
        data = response.json()
        return data

    def add_item(item_ids):
        steam_user_id = get_steam_id()
        api_url = "https://crucialexperiments.com/durka_simulator/steam/add"

        payload = {
            'steamid': steam_user_id,
            'itemsid[]': item_ids,
            'game': 'durkasim',
        }

        response = requests.post(api_url, data=payload)

        print(response.text)

        return response.text

    def destroy_result(resultHandle):
        """
        Destroys the result descriptor and frees up all associated memory
        """
        return steamapi.SteamInventory().DestroyResult(resultHandle)