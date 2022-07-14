from otree.api import *


doc = """
In a common value auction game, players simultaneously bid on the item being
auctioned.<br/>
Prior to bidding, they are given an estimate of the actual value of the item.
This actual value is revealed after the bidding.<br/>
Bids are private. The player with the highest bid wins the auction, but
payoff depends on the bid amount and the actual value.<br/>
"""


class C(BaseConstants):
    NAME_IN_URL = 'main'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # INSTRUCTIONS_TEMPLATE = 'main/InstructionsTemplate.html'

    PAY_PER_GRID = Currency(.09)

    TAX_RATE = 40
    # INFO ON ADDITIONAL INFO PAGE ABOUT SAMPLE OF PARTICIPANTS
    PERCERT_OF_PARTICIPANTS = 32

    PARTICIPATION_PYMT = Currency(2)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    honesty_oath = models.BooleanField(widget=widgets.CheckboxInput, label = "I agree:")
    practice_grids_attempted = models.IntegerField(initial=0, doc="""Number of practice work tasks completed correctly""")
    grids_completed = models.IntegerField(initial=0, doc="""Number of work tasks completed correctly""")
    reported = models.CurrencyField(label="What do you want to report?", doc="""payoff as reported by participant""")

# FUNCTIONS
def honesty_oath_error_message(player, value):
    if not value:
        return 'You must accept before you can proceed.'

def reported_error_message(player, value):
    if value > player.payoff or value < 0:
        return 'You cannot report more than you earned'

def creating_session(subsession: Subsession):
    for g in subsession.get_groups():
        pass


def set_winner(group: Group):
    pass


def generate_value_estimate(group: Group):
    pass


def set_payoff(player: Player):
    pass
    # group = player.group

    # if player.is_winner:
    #     player.payoff = group.item_value - player.bid_amount
    #     if player.payoff < 0:
    #         player.payoff = 0
    # else:
    #     player.payoff = 0


# PAGES
class Introduction(Page):
    pass


class Instructions(Page):
    pass


class Instructions2(Page):
    pass


class HonestyOath(Page):
    form_model = 'player'
    form_fields = ['honesty_oath']


class Practice(Page):

    @staticmethod
    def live_method(player, data):
        player.practice_grids_attempted += 1

        return {player.id_in_group: player.practice_grids_attempted}


class WorkIntro(Page):
    pass


class Work(Page):
    timer_text = 'Time remaining:'
    timeout_seconds = 600

    @staticmethod
    def vars_for_template(player: Player):
        player.payoff = player.field_maybe_none('grids_completed') * C.PAY_PER_GRID
        return dict(earnings=cu(player.grids_completed*C.PAY_PER_GRID))

    @staticmethod
    def live_method(player, data):
        player.grids_completed += 1 

        return {player.id_in_group: {'earnings': str(cu(player.grids_completed * C.PAY_PER_GRID)), 'num_grids': player.grids_completed}}


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.payoff = player.field_maybe_none('grids_completed') * C.PAY_PER_GRID
        return dict()


class AdditionalInfo(Page):
    pass

class Reporting(Page):
    form_model = 'player'
    form_fields = ['reported']

    @staticmethod
    def vars_for_template(player: Player):
        player.payoff = player.field_maybe_none('grids_completed') * C.PAY_PER_GRID
        return dict(income=float(player.payoff))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.work_earnings = player.payoff - ( player.reported * C.TAX_RATE / 100 )


# page_sequence = [Introduction, Instructions, Instructions2, HonestyOath, Practice, Work, Results, AdditionalInfo, Reporting]
page_sequence = [Introduction, Instructions, Instructions2, Practice, Work, Results, Reporting]