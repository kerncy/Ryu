# !/bin/python
# coding: utf8


class Container:
    m_yellow = 0
    m_blue = 0
    m_purple = 0
    m_orange = 0
    m_white = 0

    m_smuggler = 0
    m_governor = 0
    m_merchant = 0

    def __init__(self, yellow, blue, purple, orange, white, smuggler, governor, merchant):
        self.m_yellow = yellow
        self.m_blue = blue
        self.m_purple = purple
        self.m_orange = orange
        self.m_white = white
        self.m_smuggler = smuggler
        self.m_governor = governor
        self.m_merchant = merchant


    def updateYellow(self, count):
        self.m_yellow += count

    def updateBlue(self, count):
        self.m_blue += count

    def updatePurple(self, count):
        self.m_purple += count

    def updateOrange(self, count):
        self.m_orange += count

    def updateWhite(self, count):
        self.m_white += count

    def updateSmuggler(self, count):
        self.m_smuggler += count

    def updateGovernor(self, count):
        self.m_governor += count

    def updateMerchant(self, count):
        self.m_merchant += count


