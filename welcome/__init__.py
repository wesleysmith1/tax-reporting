from otree.api import *
import datetime



doc = """
Each player decides if to free ride or to volunteer from which all will
benefit.
See: Diekmann, A. (1985). Volunteer's dilemma. Journal of Conflict
Resolution, 605-610.
"""


class C(BaseConstants):
    NAME_IN_URL = 'welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    num_volunteers = models.IntegerField()


class Player(BasePlayer):
    consent_time = models.StringField(null=True)


# FUNCTIONS

# PAGES
class Consent(Page):

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.consent_time = str(datetime.datetime.now())


page_sequence = [Consent]
