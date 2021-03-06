# -*- coding: utf-8 -*-

# Standard Library Imports
import os
import json
import logging
# 3rd Party Imports
# Local Imports
from Utils import get_path

log = logging.getLogger('Locale')


# Locale object is used to get different translations in other languages
class Locale(object):

    # Load in the locale information from the specified json file
    def __init__(self, language):
        # Load in English as the default
        with open(os.path.join(get_path('locales'), 'en.json')) as f:
            default = json.loads(f.read())
        # Now load in the actual language we want
        # (unnecessary for English but we don't want to discriminate)
        with open(os.path.join(
                get_path('locales'), '{}.json'.format(language))) as f:
            info = json.loads(f.read())

        # Pokemon ID -> Name
        self.__pokemon_names = {}
        pokemon = info.get("pokemon", {})
        for id_, val in default["pokemon"].iteritems():
            self.__pokemon_names[int(id_)] = pokemon.get(id_, val)

        # Move ID -> Name
        self.__move_names = {}
        moves = info.get("moves", {})
        for id_, val in default["moves"].iteritems():
            self.__move_names[int(id_)] = moves.get(id_, val)

        # Team ID -> Name
        self.__team_names = {}
        teams = info.get("teams", {})
        for id_, val in default["teams"].iteritems():
            self.__team_names[int(id_)] = teams.get(id_, val)

        # Team ID -> Team Leaders
        self.__leader_names = {}
        leaders = info.get("leaders", {})
        for id_, val in default["leaders"].iteritems():
            self.__leader_names[int(id_)] = leaders.get(id_, val)

        # Pokemon ID -> { Form ID -> Form Name)
        self.__form_names = {}
        all_forms = info.get("forms", {})
        for pkmn_id, forms in default["forms"].iteritems():
            self.__form_names[int(pkmn_id)] = {}
            pkmn_forms = all_forms.get(pkmn_id, {})
            for form_id, form_name in forms.iteritems():
                self.__form_names[int(pkmn_id)][int(form_id)] = pkmn_forms.get(
                    form_id, form_name)
        log.debug("Loaded '{}' locale successfully!".format(language))

        # Weather ID -> Weather Name
        self.__weather_names = {}
        wnames = info.get("weather_names", {})
        for id_,val in default["weather_names"].iteritems():
            self.__weather_names[int(id_)] = wnames.get(id_, val)

        # Weather ID -> Weather Name
        self.__display_levels = {}
        dlevels = info.get("display_levels", {})
        for id_,val in default["display_levels"].iteritems():
            self.__display_levels[int(id_)] = dlevels.get(id_, val)

        # Weather ID -> Weather Name
        self.__severity_names = {}
        snames = info.get("severity_names", {})
        for id_,val in default["severity_names"].iteritems():
            self.__severity_names[int(id_)] = snames.get(id_, val)

        # Weather ID -> Weather Name
        self.__world_times = {}
        wnames = info.get("world_times", {})
        for id_,val in default["world_times"].iteritems():
            self.__world_times[int(id_)] = wnames.get(id_, val)


    # Returns the name of the Pokemon associated with the given ID
    def get_pokemon_name(self, pokemon_id):
        return self.__pokemon_names.get(pokemon_id, '?')

    # Returns the name of the move associated with the move ID
    def get_move_name(self, move_id):
        return self.__move_names.get(move_id, '?')

    # Returns the name of the team associated with the Team ID
    def get_team_name(self, team_id):
        return self.__team_names.get(team_id, '?')

    # Returns the name of the team ledaer associated with the Team ID
    def get_leader_name(self, team_id):
        return self.__leader_names.get(team_id, '?')

    # Returns the name of the form of for the given Pokemon ID and Form ID
    def get_form_name(self, pokemon_id, form_id):
        return self.__form_names.get(pokemon_id, {}).get(form_id, '')

    # Returns the name of the weather of for the given weather ID
    def get_weather_name(self, weather_id):
        return self.__weather_names.get(weather_id, 'None')

    # Returns the name of the display level of for the given weather level ID
    def get_display_name(self, level):
        return self.__display_levels.get(level, 'None')

    # Returns the name of the severity of for the given severity ID
    def get_severity_name(self, severity):
        return self.__severity_names.get(severity, 'None')

    # Returns the name of the time of for the given world_time ID
    def get_time_name(self, world_time):
        return self.__world_times.get(world_time, 'None')

    # Returns the emoji of the weather condition
    def get_weather_emoji(self, weather_id):
        emojis = {
            1: u"☀️",
            2: u"☔️",
            3: u"⛅",
            4: u"☁️",
            5: u"💨",
            6: u"⛄️",
            7: u"🌁",
            11: u"🌙",
            13: u"☁️"
        }
        return emojis.get(weather_id, '')
