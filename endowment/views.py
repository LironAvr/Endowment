from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    timeout_seconds = 120


class WaitGroupPage(Page):
    timeout_seconds = 60
    group_by_arrival_time = True
    #wait_for_all_groups = True

    #def after_all_players_arrive(self):
    pass


class GroupQuestion(Page):
    form_model = 'player'
    form_fields = ['pay_amount', 'sell_amount']
    pass


class GroupAssign(Page):
    form_model = 'player'
    form_fields = ['pay_amount', 'sell_amount']
    pass


class Finish(Page):
    pass


page_sequence = [
    Instructions,
    WaitGroupPage,
    GroupAssign,
    GroupQuestion,
    Finish
]
