
#ai.py

from engine import *
from unit import *
import game
import action

#AI (enemy computer controller) functions#

#Barbarian AI
#Stupid AI that computer could resort to when all tactics fail.
#Charge toward closest enemy and attack weakest enemy in range.
def aiBarbarian(plyr):
    myUnits = []
    enemies = []
    #first get list of all my available units and all enemies...
    for unit in Unit.getList():
        if unit.dead: continue
        if unit.owner == plyr:
            if not game.isOn(unit, SE_KO):
                myUnits.append(unit)
        else: #diplomacy settings could go here
            enemies.append(unit)
            
    #find out which tiles are visible to my units

    #iterate through fighting units...
    for unit in myUnits:
        #distances = {}
        closest = None; target = None;
        distMin = 9999999; hpMin = 9999999;
        noTargetsInRange = True
        for enemy in enemies:
            dist = hex_distance(unit.pos, enemy.pos)
            #distances[unit.id] = dist
            #in reach of weapon?
            if dist <= getStat(unit,'hand1reachMax'): #barb. only attacks w/ mainhand?
                enemyHP = getStat(enemy,'hp')
                if enemyHP < hpMin:
                    hpMin = enemyHP
                    target = enemy
                    noTargetsInRange = False
            #get closest enemy to move toward
            if noTargetsInRange:
                if dist < distMin:
                    distMin = dist
                    closest = enemy
        #Move
        if noTargetsInRange:
            target = closest
            path = game.aStar(unit.pos, target.pos)
            #while energy is left, move along the path
            for _hex in path:
                #if _hex == unit.pos: continue
                if getStat(unit,'mp') <= 0:
                    break
                action.move(unit, _hex, 1)
                #print('move')
        #Attack
        else:
            action.attack(unit, target, HAND1)
        
