#draw.py

import math

from engine import *
from metadata import *
import unit as Unit
from hexmap import Map
from player import Player
import item
import game


#-drawing
def alert(text):
    game.Game.disp.fill(BGCOLOUR)
    surf = game.Game.ft_hud.render(text, False, COLOURS['white'])
    game.Game.disp.blit(surf,(0,0))
def drawText(point, text, fg): #draw text (w/ no background)
    '''#game.Game.disp.fill(bg) #REPLACE WITH RECTANGLE
    #create rectangle
    #find width of text
    #pygame.draw.rect(disp, fg, (point.x,point.y),())) '''
    surf = game.Game.ft_hud.render(text, False, fg)
    game.Game.disp.blit(surf,(point.x,point.y))
def drawTile(_hex, fillcol, linecol, width=1):
    x = _hex.q
    y = _hex.r
    w = math.sqrt(3)*TILESIZE
    h = 2*TILESIZE
    xt = x*w + GRIDXOFFSET + y*w/2 #comment out y multiple to make it like reg. grid.
    yt = y*(h*3/4) + GRIDYOFFSET
    if fillcol != None:
        hex_draw(game.Game.disp,Point(xt,yt),TILESIZE,fillcol)
    if linecol != None:
        hex_draw_outline(game.Game.disp,Point(xt,yt),TILESIZE,linecol,width)
def drawSpriteHex(_hex, image, xoffset,yoffset):
    x = _hex.q
    y = _hex.r
    w = math.sqrt(3)*TILESIZE
    h = 2*TILESIZE
    xt = x*w + GRIDXOFFSET + y*w/2 - xoffset
    yt = y*(h*3/4) + GRIDYOFFSET - yoffset
    game.Game.disp.blit(image,(xt,yt))


#drawing phase
#pc is Player1
def drawPhase(pc):
    if not game.Game.getIsReadyToDraw():
        return
    game.Game.drawPhaseInit()
    
    game.Game.disp.fill(BGCOLOUR) #probably a better way to do this...?

    #draw map
    visibleTiles = Unit.getVisibleTiles(pc)
    for _hex in visibleTiles:
        if _hex in visibleTiles:
            fg = TERRAINCOLOURS[Map.getTerrain(_hex)]
            drawTile(_hex, fg, COLOURS['deep'])
        else:
            fg = TERRAINCOLOURS[TER_FOGOFWAR]
            drawTile(_hex, fg, COLOURS['black'])

    #draw unit data and HUD
    drawUnitHUD(visibleTiles)

    #draw mouse hover
    drawTile(game.Game.getMouseHex(),None,COLOURS['white'], RING_THICKNESS)
    #draw mouse select
    if (not game.Game.selected.q == -1 and
        game.Game.getSelectedHex() in Map.getMap()):
        unit = game.Game.getSelectedUnit()
        if unit:
            col = Player.getPlayerColour(unit.owner)
        else:
            col = COLOURS['accent']
        drawTile(game.Game.getSelectedHex(), None, col, RING_THICKNESS)
    #draw units
    for unit in Unit.Unit.getList():
        if unit.pos not in visibleTiles: #can't see it
            continue
        
        #draw sprite
        if unit.owner == Player.getP1():
            img = unit.sprite
        else:
            img = pygame.transform.flip(unit.sprite, True, False)
        drawSpriteHex(unit.pos, img,
                      unit.sprXoffset, unit.sprYoffset)
        
        #show unit HP bar
        col = COLOURS['green']
        point = hex_to_pixel(unit.pos, TILESIZE,
                              GRIDXOFFSET, GRIDYOFFSET)
        x1 = point.x - int(TILESIZE/2)
        y1 = point.y + int(TILESIZE/2)
        w = int(TILESIZE)
        h = 3
        hpMult = Unit.getStat(unit,'hp') / Unit.getStat(unit,'hpMax')
        pygame.draw.rect(game.Game.disp, COLOURS['black'], (x1,y1,w+1,h+1))
        pygame.draw.rect(game.Game.disp, col, (x1,y1,int(w*hpMult),h))
    #end for
    pygame.display.update()
#

#draw overlay for when a unit is selected
def drawUnitHUD(visibleTiles):
    if game.Game.getSelectedUnit():
        unit = game.Game.getSelectedUnit()
        drawUnitData(unit, 20, 520, 204, 20)

        #Get reach data from weapons wielded
        if item.getEquipment(unit,HAND1) == None: #Bare hands
            reachMin = 1
            reachMax = 1
        else:
            if item.getEquipment(unit,HAND2): #Dual wielding
                reachMin = min(Unit.getStat(unit,'hand1reachMin'), Unit.getStat(unit,'hand2reachMin'))
                reachMax = max(Unit.getStat(unit,'hand1reachMax'), Unit.getStat(unit,'hand2reachMax'))
            else: #Two-handed / one weapon
                reachMin = Unit.getStat(unit,'hand1reachMin')
                reachMax = Unit.getStat(unit,'hand1reachMax')
        reachMin = max(1, reachMin)
        reachMax = max(1, reachMax)
        for rr in range(reachMin, reachMax + 1):
            tiles = hex_ring(unit.pos, rr)
            for _hex in tiles:
                if _hex in Map.getMap():
                    drawTile(_hex, None, COLOURS['truered'], RING_THICKNESS)
        
        #draw path for movement
        #Note: path should only be calculated if the mouse has moved to a different hex. Waste of CPU time...
        goal = game.Game.getMouseHex()
        if goal in visibleTiles:
            path = game.aStar(unit.pos, goal)
            for _hex in path:
                drawTile(_hex, None, COLOURS['white'], RING_THICKNESS)

def drawUnitData(unit, x, y, dx, dy):

    #first two columns and owner name
    
    i = 0
    drawText(Point(x + dx*0,y + dy*i),
             "Team " + unit.owner.name, COLOURS['white'])
    i += 1
    drawText(Point(x + dx*0,y + dy*i),unit.name, COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "HP  " + str(Unit.getStat(unit,'hp')) + "(" + str(Unit.getStat(unit,'hpMax')) + ")",
             COLOURS['white'])
    i += 1
    drawText(Point(x + dx*0,y + dy*i),
             unit.clas, COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "MP  " + str(Unit.getStat(unit,'mp')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*0,y + dy*i),
             "Lvl " + str(unit.lvl), COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "Mob " + str(Unit.getStat(unit,'mob')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*0,y + dy*i),
             "Vis " + str(Unit.getStat(unit, 'vision')), COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "Spd " + str(Unit.getStat(unit,'spd')), COLOURS['white'])
    #Acc
    i += 1
    drawText(Point(x + dx*0,y + dy*i),
             "Acc " + str(Unit.getStat(unit,'accm')),
             COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "Ranged " + str(Unit.getStat(unit,'accr')),
             COLOURS['white'])
    #Atk
    i += 1
    atk1s = Unit.getStat(unit,'hand1atks')
    atk1p = Unit.getStat(unit,'hand1atkp')
    atk2s = Unit.getStat(unit,'hand2atks')
    atk2p = Unit.getStat(unit,'hand2atkp')
    atk = Unit.getStat(unit,'atk')
    drawText(Point(x + dx*0,y + dy*i),
             "Atk " + str(atk1s) + "/" + str(atk1p) + "(+" + str(atk) + ")",
             COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "Hand2 " + str(atk2s) + "/" + str(atk2p) + "(+" + str(atk) + ")",
             COLOURS['white'])
    #Reach
    i += 1
    drawText(Point(x + dx*0,y + dy*i),
             "Reach " + str(Unit.getStat(unit,'hand1reachMin')) + "-" + str(Unit.getStat(unit,'hand1reachMax')),
             COLOURS['white'])
    drawText(Point(x + dx*1,y + dy*i),
             "Hand2 " + str(Unit.getStat(unit,'hand2reachMin')) + "-" + str(Unit.getStat(unit,'hand2reachMax')),
             COLOURS['white'])
    #wielding
    i += 1
    hand1 = item.getEquipment(unit,HAND1)
    if hand1:
        string = str(hand1.name)
    else:
        string = "bare"
    drawText(Point(x + dx*0,y + dy*i),
             "Wielding " + string,
             COLOURS['white'])
    #offhand
    i += 1
    hand2 = item.getEquipment(unit,HAND2)
    if hand2:
        string = "Offhand  " + str(hand2.name)
    else:
        if (hand1 and
            (hand1.hands == "2" or hand1.hands == "1/2")):
            string = "Two-handed"
        else:
            string = "Offhand  bare"
    drawText(Point(x + dx*0,y + dy*i), string, COLOURS['white'])

    #3rd column, other stats
    i = -1
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "Evasion   " + str(Unit.getStat(unit,'eva')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "Crit Hit  " + str(Unit.getStat(unit,'crit')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
            "Parry     " + str(Unit.getStat(unit,'parry')),
             COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
            "ParryAlly " + str(Unit.getStat(unit,'parryAlly')),
             COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "Counter   " + str(Unit.getStat(unit,'counter')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "HitAdjFoe " + str(Unit.getStat(unit,'hitAdjFoe')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "IgnrShld  " + str(Unit.getStat(unit,'ignoreBlock')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "Destroy   " + str(Unit.getStat(unit,'destroy')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "Push      " + str(Unit.getStat(unit,'push')), COLOURS['white'])
    i += 1
    drawText(Point(x + dx*2,y + dy*i),
             "Pull      " + str(Unit.getStat(unit,'pull')), COLOURS['white'])
    
    #4th column - status
    xx = dx*3
    i = 0
    if not unit.status:
        drawText(Point(xx,y + dy*i), "Status Clear", COLOURS['white'])
    else:
        drawText(Point(xx,y + dy*i), "Status", COLOURS['white'])
        i += 1
        if unit.status.get(SE_MANA):
            drawText(Point(xx,y + dy*i),
                     "Mana " +  str(unit.status[SE_MANA].timer),
                     COLOURS['white'])
        i += 1
        if unit.status.get(SE_DAZE):
            drawText(Point(xx,y + dy*i),
                     "Dazed    " + str(unit.status[SE_DAZE].timer),
                     COLOURS['white'])
        i += 1
        if unit.status.get(SE_BLEED):
            drawText(Point(xx,y + dy*i),
                     "Bleeding " +  str(unit.status[SE_BLEED].timer),
                     COLOURS['white'])
        i += 1
        if unit.status.get(SE_KO):
            drawText(Point(xx,y + dy*i), "K.O.'d ", COLOURS['white'])
    
    #armour
    torsoDefs = Unit.getStat(unit,'torsoDefs')
    torsoDefp = Unit.getStat(unit,'torsoDefp')
    torsoProtect = Unit.getStat(unit,'torsoProtect')
    headDefs = Unit.getStat(unit,'headDefs')
    headDefp = Unit.getStat(unit,'headDefp')
    headProtect = Unit.getStat(unit,'headProtect')
    armsDefs = Unit.getStat(unit,'armsDefs')
    armsDefp = Unit.getStat(unit,'armsDefp')
    armsProtect = Unit.getStat(unit,'armsProtect')
    legsDefs = Unit.getStat(unit,'legsDefs')
    legsDefp = Unit.getStat(unit,'legsDefp')
    legsProtect = Unit.getStat(unit,'legsProtect')
    hand1defs = Unit.getStat(unit,'hand1defs')
    hand1defp = Unit.getStat(unit,'hand1defp')
    hand1blockm = Unit.getStat(unit,'hand1blockm')
    hand1blockr = Unit.getStat(unit,'hand1blockr')
    hand1blockAllym = Unit.getStat(unit,'hand1blockAllym')
    hand1blockAllyr = Unit.getStat(unit,'hand1blockAllyr')
    hand2defs = Unit.getStat(unit,'hand2defs')
    hand2defp = Unit.getStat(unit,'hand2defp')
    hand2blockm = Unit.getStat(unit,'hand2blockm')
    hand2blockr = Unit.getStat(unit,'hand2blockr')
    hand2blockAllym = Unit.getStat(unit,'hand2blockAllym')
    hand2blockAllyr = Unit.getStat(unit,'hand2blockAllyr')
    #general protection values get added to all body part protection values
    protect = Unit.getStat(unit, 'protect')
    #general defense value
    df = Unit.getStat(unit,'def')
    #header
    i = -1
    i += 1
    drawText(Point(x + dx*4,y + dy*i),
             "Equipment", COLOURS['white'])
    i += 1
    drawText(Point(x + dx*4,y + dy*i),
             "Part", COLOURS['white'])
    drawText(Point(x + dx*4.5,y + dy*i),
             "Def", COLOURS['white'])
    drawText(Point(x + dx*5,y + dy*i),
             "Protection", COLOURS['white'])
    #body parts
    xs = x + dx*4
    i += 1
    drawText(Point(xs,y + dy*i),
             "Torso  " + str(torsoDefs) + "/" + str(torsoDefp) + "(+" + str(df) + ")",
             COLOURS['white'])
    drawText(Point(xs + dx*1,y + dy*i),
             "   " + str(torsoProtect) + "(+" + str(protect) + ")",
             COLOURS['white'])
    i += 1
    drawText(Point(xs,y + dy*i),
             "Head   " + str(headDefs) + "/" + str(headDefp) + "(+" + str(df) + ")",
             COLOURS['white'])
    drawText(Point(xs + dx*1,y + dy*i),
             "   " + str(headProtect) + "(+" + str(protect) + ")",
             COLOURS['white'])
    i += 1
    drawText(Point(xs,y + dy*i),
             "Arms   " + str(armsDefs) + "/" + str(armsDefp) + "(+" + str(df) + ")",
             COLOURS['white'])
    drawText(Point(xs + dx*1,y + dy*i),
             "   " + str(armsProtect) + "(+" + str(protect) + ")",
             COLOURS['white'])
    i += 1
    drawText(Point(xs,y + dy*i),
             "Legs   " + str(legsDefs) + "/" + str(legsDefp) + "(+" + str(df) + ")",
             COLOURS['white'])
    drawText(Point(xs + dx*1,y + dy*i),
             "   " + str(legsProtect) + "(+" + str(protect) + ")",
             COLOURS['white'])
    i += 1
    drawText(Point(xs,y + dy*i),
             "Hand1  " + str(hand1defs) + "/" + str(hand1defp) + "  Block " + str(hand1blockm) + "/" + str(hand1blockr) + " | " + str(hand1blockAllym) + "/" + str(hand1blockAllyr),
             COLOURS['white'])
    i += 1
    drawText(Point(xs,y + dy*i),
             "Hand2  " + str(hand2defs) + "/" + str(hand2defp) + "  Block " + str(hand2blockm) + "/" + str(hand2blockr) + " | " + str(hand2blockAllym) + "/" + str(hand2blockAllyr),
             COLOURS['white'])











    
