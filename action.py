
#action.py

import random

from engine import *
from metadata import *
import unit as Unit
import item
import game


#Actions
#move a unit to a new position and use some energy
def move(unit, pos, mp):
    if not Unit.Unit.getFromHex(pos):
        unit.pos = pos
        unit.stats.addBase('mp', -mp)
        
#Melee attack a unit with another unit
        #attkr: unit attacking
        #dfndr: unit being attacked
        #atkHand: which body part is attacking?
        #canParry: can this attack be parried/countered?
def attack(attkr, dfndr, atkHand):
    crit=False
    blocked=False
    reachPenalty=False
    
    #get weapon values
    atkWeap, atkWeapName = item.getWeapData(attkr, atkHand)
    if atkHand == HAND1:
        reach = Unit.getStat(attkr,'hand1reachMax')
        reachMin = Unit.getStat(attkr,'hand1reachMin')
    elif atkHand == HAND2:
        reach = Unit.getStat(attkr,'hand2reachMax')
        reachMin = Unit.getStat(attkr,'hand2reachMin')
        
    #unit stats
    acc = Unit.getStat(attkr,"accm")
    spd = Unit.getStat(attkr,'spd')

    if acc <= 0:
        return False #unit cannot attack, no accuracy.
        
    #check if in range
    dist = hex_distance(attkr.pos, dfndr.pos)
    if reach < dist:
        game.msg("{a} cannot hit {d} with {w}! (out of reach)".format(
            d=dfndr.name, a=attkr.name, w=atkWeapName))
        return False #cannot go through with attack.
    if dist < reachMin:
        reachPenalty = True
        acc -= MINREACH_ACCPENALTY
        spd -= MINREACH_SPDPENALTY
    
    game.msg("> {a} targets {d} ...".format(
        d=dfndr.name,a=attkr.name))
    
    #attacking uses up your unit's turn
    Unit.exhaustTurn(attkr)
    
    #hit adjacent foe
    if (random.random()*100 < Unit.getStat(attkr, 'hitAdjFoe')):
        unitList=[]
        for unit in Unit.getAdjacentUnits(dfndr): #create list of possible targets
            if foes(unit, attkr): #don't friendly fire!
                unitList.append(unit)
        #pick a random unit from the list of possible targets
        randIndex = int(random.random() * len(unitList))
        unit = unitList[randIndex]
        d = hex_distance(unit.pos, attkr.pos)
        if (d <= reach and d >= reachMin): #check if within ideal range.
            strike(attkr, unit, HAND1, atkWeap, atkWeapName) #deal one hit
    
    #speed, multi-hits
    remainder = spd % SPEED_FACTOR
    hits = spd//SPEED_FACTOR
    if (random.random()*100 < remainder*(100//SPEED_FACTOR)):
        hits += 1
    
    #attempt to hit as many times as we can
    for hitNum in range(hits):
        _continue=False
        #check aim
        if (random.random()*100 >= acc):
            game.msg("{d} is missed by {a}'s {w}".format(
                d=dfndr.name,a=attkr.name, w=atkWeapName))
            continue #attack failed
        
        #parry
        if (random.random()*100 < Unit.getStat(dfndr,"parry")):
            result = parryAttack(dfndr, attkr, atkWeap, atkWeapName)
            if result == "counter":
                return False #counter breaks chains of attacks
            else:
                continue #attack failed
        #parry from ally
        for unit in Unit.getAdjacentUnits(dfndr):
            if unit:
                if not allies(unit, dfndr):
                    continue
                if (random.random()*100 < Unit.getStat(unit,'parryAlly')):
                    result = parryAttack(unit, attkr, atkWeap, atkWeapName)
                    if result == "counter":
                        return False #counter breaks chains of attacks
                    else:
                        _continue=True
                        break #attack failed
        if _continue:
            continue #attack failed
            
        #evade
        realEva = Unit.getStat(dfndr,'eva')
        eva = realEva - max(0, acc - 100)
        eva -= dfndr.evadeCounter*EVA_LOSS_PER_EVADE
        if eva < realEva//2:
            eva = realEva//2 #Acc cut of Eva at maximum cuts Eva in half.
        eva = min(MAX_EVASION, eva) #evasion cap
        if (random.random()*100 < eva):
            game.msg("{d} evades {a}'s {w}".format(
                d=dfndr.name,a=attkr.name, w=atkWeapName))
            dfndr.evadeCounter += 1
            continue #attack failed
        
        #Attack!
        strike(attkr, dfndr, HAND1, atkWeap, atkWeapName, reachPenalty)
    #end for
#
