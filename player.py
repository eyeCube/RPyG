
#player.py

from metadata import *


class Player:
    pID=0
    player1=None #player controlled by user (multiplayer not supported)
    humans={} #human players
    comps={} #computer players
    colours={} #player colours
    colourID=-1 #for auto-picking a colour from ColourList for players
    ColourList=[
        COLOURS['trueblue'],
        COLOURS['trueyellow'],
        ]
    def __init__(self, ID, typ, name):
        self.ID=ID
        self.name=name #player name
        self.type=typ #human or computer
    #getters
    @classmethod #team colour of a given player
    def getPlayerColour(cls, player): return cls.colours[player.ID]
    @classmethod #human player controlled locally
    def getP1(cls): return cls.player1
    @classmethod #human player list (just the Player objects, not the IDs)
    def getPCs(cls): return cls.humans.values()
    @classmethod #computer player list (just the Player objects)
    def getNPCs(cls): return cls.comps.values()
    #add:
    #call this to make & initialize a new Player object
    @classmethod
    def add(cls, typ, name, col=None, pc=False):
        newID = cls.pID
        cls.pID += 1
        p = Player(newID, typ, name)
        if pc: cls.player1 = p
        #human or computer
        if typ == "human":
            cls.humans.update({newID : p})
        elif typ == "computer":
            cls.comps.update({newID : p})
        #colour
        if col == None:
            cls.colours[newID] = cls.nextColour()
        else:
            cls.colours[newID] = col
        return p
    #nextColour:
    #get a default colour from a list, to represent the player.
    @classmethod
    def nextColour(cls):
        cls.colourID += 1
        return cls.ColourList[cls.colourID]





