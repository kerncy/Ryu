# !/bin/python
# coding: utf8


class Player:
    m_yellow = 2
    m_blue = 0
    m_purple = 0
    m_orange = 0

    m_smuggler = 0
    m_governor = 0
    m_merchant = 0

    m_color = ""
    m_name = ""

    m_dragonStep = 1

    def __init__(self, name):
        self.m_name = name

    def buildDragon(self):
        self.m_dragonStep = self.m_dragonStep + 1