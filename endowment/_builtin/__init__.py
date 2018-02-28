# This file is auto-generated.
# It's used to aid autocompletion in code editors.

import otree.api
from .. import models

__version__ = '1.4.38'

default_app_config = 'otree.apps.OtreeConfig'


def get_version():
    return __version__

class Page(otree.api.Page):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()


class WaitPage(otree.api.WaitPage):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()


class Bot(otree.api.Bot):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()
