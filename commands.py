
#commands.py


import pygame

from engine import *
from metadata import *
import unit as Unit
import game
import action
import manager




#CommandManager
    #Controls player commands
    #pc is the player that this manager controls
class CommandManager(manager.Manager):
    def __init__(self, pc):
        super(CommandManager,self).__init__()
        self.pc=pc
        self.paused=False
    def run(self, *args,**kwargs):
        if not self.paused:
            self.set_result(None)
            events = game.Game.getEvents()
            commands.getCommands(self.pc, events)
            commands.doCommands(self.pc)
    def pause(self): self.paused=True
    def resume(self): self.paused=False
    def close(self):
        super(CommandManager,self).close()




'''
    func getCommands
    player commands, key and mouse
    just saves the type of command given, doesn't do anything yet
'''
def getCommands(pc, events):
#NOTE: call game.Game.update() after each command if you want to refresh the screen.
    game.Game.setCommand() #reset command to null
    
    #get command from user input
    for event in events:
        globalCommands(events)
        if event.type == pygame.KEYDOWN:
            game.Game.setCommand(keyCommands(event.key))
        elif event.type == pygame.MOUSEMOTION:
            game.Game.setCommand({CMD_MOUSEHOVER : None})
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #LMB
                game.Game.setCommand({CMD_SELECTHEX : "mouse"})
            elif event.button == 3: #RMB
                game.Game.setCommand({CMD_TARGETHEX : "mouse"})
'''
    func doCommands
    perform player commands based on results gathered in getCommands()
'''
def doCommands(pc):
    for command,data in game.Game.getCommand():
        print("command info: ", command, data)
        #hover mouse
        if command == CMD_MOUSEHOVER:
            commandMouseHover()
        #select hex
        elif command == CMD_SELECTHEX:
            if data == None:
                commandDeselect()
            elif data == "mouse":
                commandSelectMouseHex()
        #target hex
        elif command == CMD_TARGETHEX:
            if data == "mouse":
                commandTargetMouseHex(pc)
        #move
        elif command == CMD_MOVE:
            direction = hex_direction(data)
        #skip turn
        elif command == CMD_SKIPTURN:
            commandSkipTurn()
#


#select a Hex using the mouse
def selectHex(_hex):
    if _hex == None:
        game.Game.setSelectedHex(None)
        game.Game.setSelectedUnit(None)
        return;
    else:
        game.Game.setSelectedHex(_hex)
        game.Game.setSelectedUnit(Unit.Unit.getFromHex(game.Game.getSelectedHex()))

'''
    func globalCommands
    functions dealing with pygame events should probably use this
'''
def globalCommands(events):
    for event in events:
        if event.type == pygame.QUIT:
            game.Game.end()

#keyCommands
#pass in pygame events' event.key
def keyCommands(key):
    if key == KEY_DEG0:
        return {CMD_MOVE : 0} #0//60
    elif key == KEY_DEG60:
        return {CMD_MOVE : 1} #60//60
    elif key == KEY_DEG120:
        return {CMD_MOVE : 2} #120//60
    elif key == KEY_DEG180:
        return {CMD_MOVE : 3} #180//60
    elif key == KEY_DEG240:
        return {CMD_MOVE : 4} #240//60
    elif key == KEY_DEG300:
        return {CMD_MOVE : 5} #300//60
    elif key == KEY_DESELECT:
        return {CMD_SELECTHEX : None}
    elif key == KEY_SKIPTURN:
        return {CMD_SKIPTURN : None}
        

def commandDeselect():
    game.Game.update()
    selectHex(None)
def commandSkipTurn():
    game.Game.update()
    game.Game.nextPlayerTurn()
def commandMouseHover():
    game.Game.update() #maybe don't need to update unless mouseHex changes...
    game.Game.findMouseHex() #set game.Game.mouseHex
def commandSelectMouseHex():
    game.Game.update()
    selectHex(game.Game.getMouseHex()) #set game.Game.selected and game.Game.selectedUnit

'''
    commandTargetMouseHex
    with the unit currently selected by the player: 
    -target the tile the mouse is hovering over.
        -attack if a foe is there
        -or move to the tile if the unit can

'''
def commandTargetMouseHex(pc):
    game.Game.update()
    unit = game.Game.getSelectedUnit() #unit being issued the command
    if not unit: return; #no unit selected
    if (unit.owner == pc and Unit.getStat(unit,'mp') > 0):
        mouseHex = game.Game.getMouseHex()
        newPos = mouseHex
        unitHere = Unit.Unit.getFromHex(mouseHex)
        if unitHere:
            if unitHere.owner == pc:
                alert("That space is occupied.")
                return;
            else:
                #ATTACK!!!
                action.attack(unit, unitHere, HAND1)
                return;
        #need to employ pathfinding!!!!! Mouse hover + draw the path char will take.
        dist = hex_distance(unit.pos, newPos)
        if (dist <= Unit.getStat(unit,'mob')
        and dist <= Unit.getStat(unit,'mp')):
            action.move(unit, newPos, dist)
            selectHex(newPos)
        else:
            alert(unit.name + " cannot move that far.")
    else:
        if not unit.owner == pc:
            alert(unit.name + " is not your unit!")
        elif Unit.getStat(unit,'mp') <= 0:
            alert(unit.name + " cannot move anymore this turn.")




