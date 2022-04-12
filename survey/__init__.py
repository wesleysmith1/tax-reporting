from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

int_choices = [i for i in range(10)]
survey_choices = [[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither agree nor disagree'], [4, 'Agree'], [5, 'Strongly agree']]
class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125, blank=True)
    age_no_answer = models.BooleanField(label='Prefer not the answer')
    race_asian = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="Asian")
    race_black = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="Black/African American")
    race_white = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="White or Caucasian")
    race_native_am = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="Native American")
    race_multiracial = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="Multiracial")
    race_other = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="Other")
    race_no_answer = models.BooleanField(blank=True, widget=widgets.CheckboxInput, label="Prefer not to answer")

    #===============================================================================================================

    marital_status = models.StringField(
        choices=['Married', 'Single', 'Divorced', 'Widowed', 'Other', 'Prefer not to answer'],
        label='What is your marital status?',
    )
    birth_order = models.StringField(
        choices=['The only child', 'Oldest child in the family', 'Youngest child in the family', 'Middle child', 'Prefer not to answer'],
        label='What is your birth order?',
    )
    religious_affiliation = models.StringField(
        choices=['Atheism', 'Buddhism', 'Christianity', 'Hinduism', 'Islam', 'Judaism', 'Nonreligious or agnostic other', 'Prefer not to answer'],
        label='What is your religious affiliation?',
    )
    last_election = models.StringField(
        choices=['Yes', 'No', 'Prefer not to answer'],
        label='Did you vote in the last election?',
    )
    gender = models.StringField(
        choices=['Man', 'Woman', 'Non-binary', 'Prefer to self-describe', 'Prefer not to answer'],
        label='What is your gender?',
    )
    gender_self_describe = models.StringField(
        label='Enter your self described gender.',
        blank=True,
    )
    willingness_risk = models.IntegerField(
        choices=int_choices,
        label='How do you see yourself: are you a person who is generally willing ot take risks, or do you try to avoid taking risks? Please use a scale from 0 to 10, where 0 means you are "completly unwilling ot take risks" and a 10 means you are "very willing to take risks". You can also use the value in-between to indicate where you fall on the scale.',
        widget=widgets.RadioSelectHorizontal,
    )
    people_assumptions = models.IntegerField(
        choices=int_choices,
        label='How well does thee following statement describe you as a person? As long as i\'m not convinced otherwise, I assume that people have only the best intentions. Please use a scale from 0 - 10, where 0 means "does not describe me at all" and a 10 means you are "desribes me perfectly".',
        widget=widgets.RadioSelectHorizontal,
    )
    willingness_share = models.IntegerField(
        choices=int_choices,
        label='How do you assess your willingness to share with others without expecting anything in return when it comes to charity? Please use a scale from 0 to 10, where 0 means you are "completly unwilling to share" and a 10 means you are "very willing to share". You can also use the values in-between to indicate where you fall on the scale.',
        widget=widgets.RadioSelectHorizontal,
    )
    generosity = models.StringField(
        choices=['$5 bottle', '$10 bottle', '$15 bottle', '$20 bottle' ,'$25 bottle', '$30 bottle'],
        label='Imagine the following situation: you are shopping in an unfamiliar city and realize you lost your way. You ask a stranger for directions. The stranger offers to take you with their car to your destination. The ride takes about 20 minutes and costs the stranger about $20 dollars in total. The stranger does not want money for it. You carry six bottles of wine with you. The cheapest bottle costs $5, the most expensive on is $30. You decide to give one of the bottles to the stranger as a thank-you gift. Which bottle do you give?',
    )
    willingness_punish = models.IntegerField(
        choices=int_choices,
        label='How do you see yourself: Are you a person who is generally willing to punish unfair behavior even if this is costly? Please use a scale from 0 to 10, where 0 means you are "not willing at all to incur costs to punish unfair behavior" and a 10 means you are "very willing to incur costs to punish unfair behavior". You can also use the values in-between to indicate where you fall on the scale.',
        widget=widgets.RadioSelectHorizontal,
    )

    #===============================================================================

    sd3_1 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="It's not wise to tell your secrets."
    )

    sd3_2 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I like to use clever manipulation to get my way."
    )

    sd3_3 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="Whatever it takes, you must get the important people on yourside."
    )

    sd3_4 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="Avoid direct conflict with others because they may be useful inthe future."
    )

    sd3_5 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="It’s wise to keep track of information that you can use againstpeople later."
    )

    sd3_6 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="You should wait for the right time to get back at people."
    )

    sd3_7 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="There are things you should hide from other people because they don’t need to know."
    )

    sd3_8 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="Make sure your plans benefit you, not others."
    )

    sd3_9 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="Most people can be manipulated."
    )

    sd3_10 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="People see me as a natural leader."
    )

    sd3_11 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I hate being the center of attention."
    )

    sd3_12 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="Many group activities tend to be dull without me."
    )

    sd3_13 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I know that I am special because everyone keeps telling me so."
    )

    sd3_14 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I like to get acquainted with important people."
    )

    sd3_15 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I feel embarrassed if someone compliments me."
    )

    sd3_16 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I have been compared to famous people."
    )

    sd3_17 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I am an average person."
    )

    sd3_18 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I insist on getting the respect I deserve."
    )

    sd3_19 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I like to get revenge on authorities."
    )

    sd3_20 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I avoid dangerous situations."
    )

    sd3_21 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="Payback needs to be quick and nasty."
    )

    sd3_22 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="People often say I’m out of control."
    )

    sd3_23 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="It’s true that I can be mean to others."
    )

    sd3_24 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="People who mess with me always regret it."
    )

    sd3_25 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I have never gotten into trouble with the law."
    )

    sd3_26 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I enjoy having sex with people I hardly know."
    )

    sd3_27 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        label="I’ll say anything to get what I want."
    )

    # ==============================================================================================

    # Big five
    OCEAN1 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Extraverted, enthusiastic"
    )

    OCEAN2 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Critical, inclined to argue with others"
    )

    OCEAN3 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Dependable, self-disciplined"
    )

    OCEAN4 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Anxious, easily upset"
    )

    OCEAN5 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="A deep thinker, creative"
    )

    OCEAN6 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Reserved, quiet"
    )

    OCEAN7 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Sympathetic, warm"
    )

    OCEAN8 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Disorganized, careless"
    )

    OCEAN9 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Calm, emotionally stable"
    )

    OCEAN10 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),                                  
        label="Conventional, preferring work that is routine"
    )

    # ==============================================================================================

    crt_bat = models.StringField(
        label='''
        A bat and a ball cost $1.10 dollars in total.
        The bat costs $1.00 dollar more than the ball.
        How much does the ball cost in dollars?'''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads. 
        Every day, the patch doubles in size. 
        If it takes 48 days for the patch to cover the entire lake, how many days would it take for the patch to cover half the lake?
        '''
    )
    crt_widget = models.IntegerField(
        label='''
        If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?
        '''
    )


# FUNCTIONS
def crt_bat_error_message(player, value):
    try:
        float(value)
    except:
        return 'Please enter a number'

# PAGES
class Survey1(Page):
    form_model = 'player'
    form_fields = ['age', 'age_no_answer', 'race_asian', 'race_black', 'race_white', 'race_native_am', 'race_multiracial', 'race_other', 'race_no_answer', 'marital_status', 'birth_order', 'religious_affiliation', 'last_election', 'gender', 'gender_self_describe',]

    @staticmethod
    def error_message(player, values):
        if not (values['race_asian'] or values['race_black'] or values['race_white'] or values['race_native_am'] or values['race_multiracial'] or values['race_other'] or values['race_no_answer']):
            return "Please select your Race/ethnicity"

        if not values['age'] and not values['age_no_answer']:
            return 'Please enter your age'

        if values['gender'] == 'Prefer to self-describe' and not values['gender_self_describe']:
            return 'Please enter your gender'


class Survey2(Page):
    form_model = 'player'
    form_fields = ['willingness_risk', 'people_assumptions', 'willingness_share', 'generosity', 'willingness_punish']


class Survey3(Page):
    form_model = 'player'
    form_fields = [f"sd3_{i}" for i in range(1, 28)]

class Survey4(Page):
    form_model = 'player'
    form_fields = [f"OCEAN{i}" for i in range(1, 11)]


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_lake', 'crt_widget']


page_sequence = [Survey1, Survey2, Survey3, Survey4, CognitiveReflectionTest]
