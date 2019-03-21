
#game.py

from engine import *
from metadata import *
from unit import Unit
from hexmap import Map
import manager



        #-------------------#
        #     CLASSES       #
        #-------------------#


'''
    Game
    stores global information about the state of the game

    All variables are private and should be accessed through getters/setters

'''
class Game:
    #values to be completed in main()
    clock = None
    disp = None
    ft_hud = None
    #
    events = None #pygame events
    refresh = True #draw screen?
    mouseHex = Hex(-10,-10) #offscreen until player input
    selected = Hex(-1,-1) #value of -1 means nothing selected.
    selectedUnit = None
    programRunning = False
    fpsLimit = 30
    players = queue.Queue()
    currentPlayer = None #which player's turn is it?
    _round = 0 #quantity rounds elapsed in game (each player going == 1 round)
    ai = {}
    cmd = {}
    p1managers = {}
    #getters
    @classmethod
    def getIsReadyToDraw(cls): return cls.refresh
    @classmethod
    def getMouseHex(cls): return cls.mouseHex
    @classmethod    
    def getCurrentPlayer(cls): return cls.currentPlayer #whose turn is it?
    @classmethod    
    def getSelectedHex(cls): return cls.selected
    @classmethod    
    def getSelectedUnit(cls): return cls.selectedUnit
    @classmethod    
    def getIsRunning(cls): return cls.programRunning
    @classmethod    
    def getFPS(cls): return cls.fpsLimit
    @classmethod    
    def getTurn(cls): return cls._round
    @classmethod
    def getCommand(cls): return cls.cmd.items()
    #setters
    @classmethod
    def setCommand(cls, cmd={}):
        if isinstance(cmd, dict): #only accept dict objects
            cls.cmd = cmd
            return True
        else:
            cls.cmd = {}
            return False
    @classmethod
    def setSelectedUnit(cls, value):
        cls.selectedUnit = value
    @classmethod
    def setSelectedHex(cls, value):
        if value == None:
            cls.selected = Hex(-1,-1)
        else:
            cls.selected = value
    #begin:
    #call to initialize the game before starting the main loop
    #players: list containing all the players that will play in the game
    @classmethod
    def begin(cls, *players):
        cls.programRunning = True
        for player in players: #add players into the queue
            cls.players.put(player)
        cls.nextPlayerTurn()
    @classmethod
    def end(cls):
        cls.programRunning = False
    @classmethod
    def nextPlayerTurn(cls):
    #get next player, put them at end of the queue for next turn
        cls.currentPlayer = cls.players.get()
        cls.players.put(cls.currentPlayer)
        print('next is: ', cls.currentPlayer.name)
    #managers
    @classmethod
    def addManager(cls, _id, manager, _type):
        if _type == "p1 perturn":
            cls.p1managers.update({_id : manager})
    @classmethod
    def runPlayer1Managers(cls):
        for ID, manager in cls.p1managers.items():
            manager.run()
    @classmethod
    def closeAllManagers(cls):
        for ID, manager in cls.p1managers.items():
            manager.close()
    #
    @classmethod    
    def endRound(cls): #call when all players have spent their turns
        cls._round += 1
    @classmethod    
    def addAI(cls, player, fxn): #set AI function for a player in the game
        cls.ai[player.ID] = fxn
    @classmethod    
    def update(cls): #call to tell screen to refresh at end of this frame
        cls.refresh = True
    @classmethod
    def drawPhaseInit(cls):
        cls.refresh = False
    @classmethod    
    def findMouseHex(cls): #set + return mouseHex, the Hex the mouse is over
        m = pygame.mouse.get_pos()
        cls.mouseHex = pixel_to_hex(Point(m[0], m[1]), TILESIZE,
                                    GRIDXOFFSET, GRIDYOFFSET)
        return cls.mouseHex
    @classmethod
    def aiTurn(cls): #perform the AI function for the current player
        if cls.ai.get(cls.currentPlayer.ID):
            cls.ai[cls.currentPlayer.ID](cls.currentPlayer)
            return True;
        else:
            return False;
    @classmethod
    def inputEvents(cls): #get pygame events from user
        cls.events = pygame.event.get()
    @classmethod
    def getEvents(cls): return cls.events



        #-------------------#
        #   -FUNCTIONS      #
        #-------------------#


#small functions
def allies(unit1, unit2): return unit1.owner == unit2.owner
def foes(unit1, unit2): return unit1.owner != unit2.owner
def ownedBy(unit, player): return unit.owner == player
def msg(string): print(string)
def isOn(unit, _status): return (_status in unit.status.keys())
#end of game conditions
def gameOver():
    msg("You hast failed.")
    msg("Game Ober")
    #tally up final gamestats
    msg("Ultimate score: 0")
    Game.end()
def victory():
    msg("You hast succeeded!")
    Game.end()

#pathfind avoiding units
def aStar(start, goal):
    posDict = {}
    for unit in Unit.getList():
        posDict[unit.pos] = True
    return get_path(start, goal, Map, posDict)
#pathfind searching for many different goals, avoiding units
'''def aStarManyGoals(start, goals):
    posDict = {}
    for unit in Unit.getList():
        posDict[unit.pos] = True
    return get_path(start, goals, Map, posDict)
    '''


#MenuManager
    #Controls a menu when it is open
class MenuManager(manager.Manager):
    def __init__(self):
        super(MenuManager,self).__init__()
        self.paused=False
    def run(self, *args,**kwargs):
        for event in Game.getEvents():
            if event.type == pygame.KEYDOWN:
                name = pygame.key.name(event.key) #convert keycode to string
                print("name of key is: ", name)
                if name in choices:
                    self.set_result(name)
                    return;
    def close(self):
        super(MenuManager,self).close()
    
def initMenu(disp, x,y, rowh, font, fg, bg, options):
    choices = [] 

    i=0
    for key,opt in options.items():
        choices.append(key)
        #draw the option on surface disp
        text = key + ") " + opt + "\n"
        surf = font.render(text, False, fg, bg)
        disp.blit(surf, (x, y + i*rowh))
        i+=1
    #
    Game.addManager(MNG_MENU, MenuManager(options), "p1 perturn")

def menu(x,y,options):
    ft_menu=Game.ft_hud
    rowh=20
    fg=COLOURS['white']
    bg=COLOURS['black']
    initMenu(Game.disp, x,y, rowh, ft_menu, fg,bg,options)








