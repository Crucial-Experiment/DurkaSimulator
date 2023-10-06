#Created by: Xrisofor
#GitHub link: https://github.com/Xrisofor

init python:
    config.hyperlink_handlers['steam_web_overlay'] = _steamlib.activate_overlay_to_web_page
    config.hyperlink_handlers['steam_store_overlay'] = _steamlib.activate_overlay_to_store
    config.hyperlink_handlers['steam_inv_dialog'] = _steamlib.activate_game_overlay_invite_dialog

    if not persistent.vkplay:
        _steamlib.load()

init -1499 python in _steamlib:

    import steamapi, requests, json, ctypes

    key = "568CA1AA499B476D63D8916235263697"

    def load():
        dll = None

        if renpy.windows:
            dll = ctypes.WinDLL("lib/py3-windows-x86_64/steam_api64.dll")
        elif renpy.linux:
            dll = ctypes.cdll.LoadLibrary('lib/py3-linux-x86_64/libsteam_api.so')

        steamapi.load(dll)

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

        if not steamapi.SteamUserStats().GetLaunchCommandLine(byref(rv).decode("utf-8"), pint):
            return None

        return rv.value

    def attach_leaderboard_ugc(leaderboard, UGCHandle):
        """
        Attaches a user content item to the current user's position in the leaderboard.
        """
        return steamapi.SteamUserStats().AttachLeaderboardUGC(leaderboard, UGCHandle)

    # SteamUGC

    def create_item(appid, flag=None):
        """
        Resets the unlock status of the achievement. Be sure to call
        the `_steamlib.store_stats` function to publish the changes to the server.
        """
        if flag is None:
            flag = steamapi.k_EWorkshopFileTypeCommunity

        return steamapi.SteamUGC().CreateItem(appid, flag)

    def start_item_update(appid, itemid):
        """
        Starts the item update process.
        This gets you a handle that you can use to modify the item before finally
        sending off the update to the server with SubmitItemUpdate.
        """
        return steamapi.SteamUGC().StartItemUpdate(appid, itemid)

    def set_item_title(UGCUpdateHandle, name):
        """
        Sets a new title for an item.
        You can set what language this is for by using SetItemUpdateLanguage,
        if no language is set then "english" is assumed.
        """
        return steamapi.SteamUGC().SetItemTitle(UGCUpdateHandle, name.encode('utf-8'))

    def set_item_description(UGCUpdateHandle, desc):
        """
        Sets a new description for an item.
        You can set what language this is for by using SetItemUpdateLanguage,
        if no language is set then "english" is assumed.
        """
        return steamapi.SteamUGC().SetItemDescription(UGCUpdateHandle, desc.encode('utf-8'))

    def set_item_content(UGCUpdateHandle, folder):
        """
        Sets the folder that will be stored as the content for an item.
        For efficient upload and download, files should not be merged or compressed
        into single files (e.g. zip files).
        """
        return steamapi.SteamUGC().SetItemContent(UGCUpdateHandle, folder.encode('utf-8'))

    def set_item_preview(UGCUpdateHandle, imgpath):
        """
        Sets the primary preview image for the item.
        The format should be one that both the web and the application (if necessary) can render.
        Suggested formats include JPG, PNG and GIF.
        Be sure your app has its Steam Cloud quota and number of files set, aspreview images
        are stored under the user's Cloud. If your app has no Cloud values set, this call will fail.
        """
        return steamapi.SteamUGC().SetItemPreview(UGCUpdateHandle, imgpath.encode('utf-8'))

    def set_item_visibility(UGCUpdateHandle, flag=None):
        """
        Sets the visibility of an item.
        Flags: steamapi.k_ERemoteStoragePublishedFileVisibilityPrivate, steamapi.k_ERemoteStoragePublishedFileVisibilityFriendsOnly,
        steamapi.k_ERemoteStoragePublishedFileVisibilityPublic, steamapi.k_ERemoteStoragePublishedFileVisibilityUnlisted
        """
        if flag is None:
            flag = steamapi.k_ERemoteStoragePublishedFileVisibilityPrivate

        return steamapi.SteamUGC().SetItemVisibility(UGCUpdateHandle, flag)

    def set_item_tags(UGCUpdateHandle, array):
        """
        Sets arbitrary developer specified tags on an item.
        Each tag must be limited to 255 characters. Tag names can only include printable characters,
        excluding ','. For reference on what characters are allowed, refer to
        http://en.cppreference.com/w/c/string/byte/isprint
        """
        return steamapi.SteamUGC().SetItemTags(UGCUpdateHandle, array.encode('utf-8'))

    def set_item_update_language(UGCUpdateHandle, language):
        """
        Sets the language of the title and description that will be set in this item update.
        """
        return steamapi.SteamUGC().SetItemUpdateLanguage(UGCUpdateHandle, language.encode('utf-8'))

    def set_item_metadata(UGCUpdateHandle, metadata):
        """
        Sets arbitrary metadata for an item. This metadata can be returned from queries without having to download and install the actual content.
        """
        return steamapi.SteamUGC().SetItemMetadata(UGCUpdateHandle, metadata.encode('utf-8'))

    def submit_item_update(UGCUpdateHandle, changeNote=""):
        """
        Uploads the changes made to an item to the Steam Workshop.
        """
        return steamapi.SteamUGC().SubmitItemUpdate(UGCUpdateHandle, changeNote.encode('utf-8'))

    def get_app_dependencies(itemid):
        """
        Returns any app dependencies that are associated with the given item.
        """
        return steamapi.SteamUGC().GetAppDependencies(itemid)

    def subscribe_item(itemid):
        """
        Subscribe to a workshop item. It will be downloaded and installed as soon as possible.
        """
        return steamapi.SteamUGC().SubscribeItem(itemid)

    def unsubscribe_item(itemid):
        """
        Unsubscribe from a workshop item. This will result in the item being removed after the game quits.
        """
        return steamapi.SteamUGC().UnsubscribeItem(itemid)

    def suspend_downloads(suspend=True):
        """
        Suspends and resumes all workshop downloads.
        """
        steamapi.SteamUGC().SuspendDownloads(Suspend)

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

    def remove_item_preview(UGCUpdateHandle, indexu32):
        return steamapi.SteamUGC().RemoveItemPreview(UGCUpdateHandle, indexu32)

    def remove_item_from_favorites(appid, itemid):
        """
        Removes a workshop item from the users favorites list.
        """
        return steamapi.SteamUGC().RemoveItemFromFavorites(appid, itemid)

    def remove_dependency(parentItemId, childItemId):
        """
        Removes a workshop item as a dependency from the specified item.
        """
        return steamapi.SteamUGC().RemoveDependency(parentItemId, childItemId)

    def remove_app_dependency(itemid, appid):
        """
        Removes the dependency between the given item and the appid.
        This list of dependencies can be retrieved by calling GetAppDependencies.
        """
        return steamapi.SteamUGC().RemoveAppDependency(itemid, appid)

    def get_user_item_vote(itemid):
        """
        Gets the users vote status on a workshop item.
        """
        return steamapi.SteamUGC().GetUserItemVote(itemid)

    def get_num_subscribed_items():
        """
        Gets the total number of items the current user is subscribed to for the game or application.
        """
        return steamapi.SteamUGC().GetNumSubscribedItems()

    def get_item_update_progress(UGCUpdateHandle):
        """
        Gets the progress of an item update.
        """
        from ctypes import c_ulonglong, byref

        done = c_ulonglong(0)
        total = c_ulonglong(0)

        if steamapi.SteamUGC().GetItemUpdateProgress(UGCUpdateHandle, byref(done), byref(total)):
            return done.value, total.value
        else:
            return None

    def get_item_state(itemid):
        """
        Gets the current state of a workshop item on this client.
        """
        return steamapi.SteamUGC().GetItemState(itemid)

    def download_item(itemid, highPriority=True):
        """
        Download or update a workshop item.
        """
        return steamapi.SteamUGC().DownloadItem(itemid, highPriority)

    def delete_item(itemid):
        """
        Deletes the item without prompting the user.
        """
        return steamapi.SteamUGC().DeleteItem(itemid)

    def add_item_to_favorites(appid, itemid):
        """
        Adds the Workshop item to the user's favorites.
        """
        return steamapi.SteamUGC().AddItemToFavorites(appid, itemid)

    def add_item_preview_video(UGCUpdateHandle, videoID):
        """
        Adds a YouTube video as an additional preview for the subject.
        """
        return steamapi.SteamUGC().AddItemPreviewVideo(UGCUpdateHandle, videoID.encode('utf-8'))

    def add_item_preview_file(UGCUpdateHandle, previewFile, flag=None):
        """
        Adds an additional preview file for the subject.
        The image format should be such that both the browser and the application can handle,
        and the size should be less than 1 MB. Recommended formats are JPG, PNG and GIF.
        Flags: https://partner.steamgames.com/doc/api/ISteamUGC#EItemPreviewType
        """
        if flag is None:
            flag = steamapi.k_EItemPreviewType_Image

        return steamapi.SteamUGC().AddItemPreviewFile(UGCUpdateHandle, previewFile.encode('utf-8'), flag)

    def add_dependency(parentItemId, childItemId):
        """
        Adds the dependency of the Workshop item on the specified item.
        If the nParentPublishedFileID item is of type k_EWorkshopFileTypeCollection,
        then nChildPublishedFileID is only added to that collection. Otherwise, dependency is
        a soft dependency displayed on the network, which can be obtained via the ISteamUGC API
        using a combination of the m_unNumChildren structure member
        variable SteamUGCDetails_tand GetQueryUGCChildren.
        """
        return steamapi.SteamUGC().AddDependency(parentItemId, childItemId)

    def add_app_dependency(itemid, appid):
        """
        Adds a dependency between this subject and the application.
        The list of dependencies can be obtained by calling GetAppDependencies.
        This is a soft dependency displayed on the network.
        The decision on whether the item will actually be used is up to the application.
        """
        return steamapi.SteamUGC().AddAppDependency(itemid, appid)

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

    # SteamMusic

    def is_enabled():
        """
        Checks if the player is turned on.
        """
        return steamapi.SteamMusic().BIsEnabled()

    def is_playing():
        """
        Checks if the player is active. This does not necessarily mean
        that the song is being played, it can be paused.
        """
        return steamapi.SteamMusic().BIsPlaying()

    def get_playback_status():
        """
        Retrieves the current state of the Steam player.
        """
        return steamapi.SteamMusic().GetPlaybackStatus()

    def get_volume():
        """
        Gets the current volume of the Steam player.
        """
        return steamapi.SteamMusic().GetVolume()

    def pause():
        """
        Pauses the player.
        """
        steamapi.SteamMusic().Pause()

    def play():
        """
        Notifies the player to resume playback.
        """
        steamapi.SteamMusic().Play()

    def play_next():
        """
        Notifies the player to skip the next track.
        """
        steamapi.SteamMusic().PlayNext()

    def play_previous():
        """
        Tells the player to play the previous song.
        """
        steamapi.SteamMusic().PlayPrevious()

    def set_volume(flVolume):
        """
        Sets the current volume of the Steam player. Volume in the range of 0.0 and 1.0.
        """
        steamapi.SteamMusic().SetVolume(flVolume)

    # SteamMusicRemote

    def activation_success(value):
        return steamapi.SteamMusicRemote().BActivationSuccess(value)

    def is_current_music_remote():
        return steamapi.SteamMusicRemote().BIsCurrentMusicRemote()

    def current_entry_did_change():
        return steamapi.SteamMusicRemote().CurrentEntryDidChange()

    def current_entry_is_available(available):
        return steamapi.SteamMusicRemote().CurrentEntryIsAvailable(available)

    def current_entry_will_change():
        return steamapi.SteamMusicRemote().CurrentEntryWillChange()

    def deregister_steam_music_remote():
        return steamapi.SteamMusicRemote().DeregisterSteamMusicRemote()

    def enable_looped(value):
        return steamapi.SteamMusicRemote().EnableLooped(value)

    #https://partner.steamgames.com/doc/api/ISteamMusicRemote#EnablePlaylists

    # SteamInventory

    def get_all_items():
        """
        GetItemDefs is used to retrieve the itemdefs for a given application.
        """
        global key

        appid = get_app_id()

        url = 'https://api.steampowered.com/IInventoryService/GetItemDefs/v1'
        params = {'appid': appid, 'key': key}

        response = requests.get(url, params=params)
        data = response.content.decode('utf-8')
        output = json.loads(data)
        itemdefs = json.loads(output['response']['itemdef_json'])

        return itemdefs

    def get_user_inventory():
        """
        GetInventory is used to retrieve a user's inventory.
        """
        global key

        appid = get_app_id()
        steamid = get_steam_id()

        url = 'https://partner.steam-api.com/IInventoryService/GetInventory/v1/'
        params = {'appid': appid, 'key': key, 'steamid': steamid}

        response = requests.get(url, params=params)
        data = response.content.decode('utf-8')
        output = json.loads(data)
        items = json.loads(output['response']['item_json'])

        return items

    def get_inventory():
        """
        Starts receiving all items in the current user's inventory.
        """
        itemdefs = get_all_items()
        invitems = get_user_inventory()
        items = []
        
        for item in invitems:
            for itemdef in itemdefs:
                if item['itemdefid'] == itemdef['itemdefid']:
                    items.append(itemdef)

        return items

    def add_item(itemdefid):
        """
        AddItem is used to add new items directly to the user's inventory.
        For each item definition (itemdef), an instance of the corresponding type is created,
        which is added to the target account.
        """
        global key

        appid = get_app_id()
        steamid = get_steam_id()

        data = {
            'key': key,
            'appid': appid,
            'steamid': steamid,
            'notify': True,
        }

        for i, item in enumerate(itemdefid):
            data[f'itemdefid[{i}]'] = item

        response = requests.post('http://api.steampowered.com/IInventoryService/AddItem/v1', data=data)

        if response.status_code == 200 and response.json().get('result', None) == 'SUCCESS':
            print(f'{len(itemdefid)} items have been successfully added to inventory')
        else:
            print('An error occurred while adding items to inventory')
            print(response.json())