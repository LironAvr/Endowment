from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Liron Avraham & Stav Yanovsky'

doc = """
An endowment effect research in AI&GT course by Dr. Kobi Gal
"""


class Constants(BaseConstants):
    name_in_url = 'endowment'
    players_per_group = 4
    num_rounds = 1
    max_amount = c(5)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def getId(self):
        matrix = Subsession.get_group_matrix()
        in_group = self.get_player_by_id(1)
        for group, i in enumerate(matrix):
            if group.__contains__(in_group):
                return i


class Player(BasePlayer):
    pay_amount = models.CurrencyField(
        min=0, max=Constants.max_amount,
        doc="Amount to pay by this player.",
        label="Please enter an amount from 0 to 5 dollars",
        blank=True
    )

    sell_amount = models.CurrencyField(
        min=0, max=Constants.max_amount,
        doc="Amount to sell by this player.",
        label="Please enter an amount from 0 to 5 dollars",
        blank=True
    )
