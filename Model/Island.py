# !/bin/python
# coding: utf8


class IslandType:
    PLAYER = 1
    NON_PLAYER = 2
    NEUTRAL = 3


class Island:
    m_available = True
    m_name = ""
    m_islandType = ""
    m_action1 = ""
    m_action2 = ""

    def __init__(self, name, islandType, action1, action2):
        self.m_name = name
        self.m_available = True
        self.m_islandType = islandType
        self.m_action1 = action1
        self.m_action2 = action2

    def flip(self):
        if self.m_islandType == 1 or self.m_islandType == 2:
            self.m_available = not self.m_available


class Merchant(Island):

    def __init__(self):
        action1 = "Dépenser 2 cubes jaunes pour prendre 1 jeton d'influence \"gouverneur\"."
        action2 = "Dépenser 1 jeton d'influence \"marchand\" et 1 jeton d'influence \"Contrebandier\" pour prendre un cube jaune."

        super(Island, self).__init__("Marchand", IslandType.NEUTRAL, action1, action2)

    def action1Allowed(self, player):
        return player.m_yellow >= 2

    def action1(self, player):
        player.m_yellow -= 2
        player.m_governor += 1

    def action2Allowed(self, player):
        return player.m_merchant >= 1 and player.m_smuggler >= 1

    def action2(self, player):
        player.m_merchant -= 1
        player.m_smuggler -= 1
        player.m_yellow += 1


class Smuggler(Island):
    def __init__(self):
        action1 = "Dépenser 1 cube jaune pour prendre 1 cube au hasard dans le sac puis prendre 2 jetons d'influence \"contrebandier\"."
        action2 = "Echanger autant de cubes bleus, violets, et orange contre un nombre égal de jeonts d'influence \"contrebandier\" et/ou \"marchand\"."

        super(Island, self).__init__("Contrebandier", IslandType.NEUTRAL, action1, action2)

    def action1Allowed(self, player):
        return player.m_yellow >= 1

    def action1(self, player):
        player.m_yellow -= 1

    def action2Allowed(self, player):
        return player.blue + player.m_orange + player.m_purple > 1

    def action2(self, player):
        player.m_merchant -= 1
        player.m_smuggler -= 1
        player.m_yellow += 1

