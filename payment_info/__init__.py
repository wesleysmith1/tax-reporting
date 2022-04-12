from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    SURVEY_PYMT = Currency(3)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    total_earnings = models.CurrencyField(initial=0)


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        try:
            player.total_earnings = participant.work_earnings + C.SURVEY_PYMT
            work_earnings = participant.work_earnings
        except:
            player.total_earnings = Currency(999)
            work_earnings = Currency(999)
        return dict(work_earnings=work_earnings)


page_sequence = [PaymentInfo]
