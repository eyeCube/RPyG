
#item.py

from metadata import *
from stats import *
import game

#Item
class Item:
    def __init__(self, itemID):
        for k, v in itemID.items():
            self.__dict__[k] = v
            
#-items
def newItem(_dict):
    item = Item(_dict)
    item.condition = item.dur
    return item


    #-----------------------#
    # Equipment / Equipping #
    #-----------------------#

#EquipSlot  
class EquipSlot:
    def __init__(self, item, modID):
        self.item = item
        self.modID = modID

def getEquipment(unit, slot):
    if unit.equipment[slot]:
        return unit.equipment[slot].item
    else:
        return None
def getWeapData(unit, hand):
    if unit.equipment[hand]:
        atkWeap = unit.equipment[hand].item
        atkWeapName = atkWeap.name
    else:
        atkWeap = None
        atkWeapName = "bare hand"
    return (atkWeap, atkWeapName,)

#equip an item to a unit.
#Returns whether the item was successfully equipped.
#unit is a Unit, item is an Item, slot is an Equipment Slot Constant
def equip(unit, item, slot):
    canEquip = False
    toOffHand = False #flag for equipping weapon in offhand
    equip = getEquipment(unit,slot)
    if equip: #slot unavailable
        game.msg("{u} cannot equip {i} (equip slot unavailable)".format(
            u=unit.name, i=item.name))
    else:
        #weapons
        if item.type == HAND1:
            if slot == HAND1: #equipping to mainhand
                if item.hands == "2":
                    if getEquipment(unit,HAND2) == None:
                        canEquip = True
                else:
                    canEquip = True
            elif slot == HAND2: #equipping to offhand
                if item.hands != "2":
                    if getEquipment(unit,HAND1):
                        if getEquipment(unit,HAND1).hands != "2":
                            canEquip = True
                            toOffHand = True
                    else:
                        canEquip = True
                        toOffHand = True
                
        #others
        elif item.type == slot: #right type?
            canEquip = True
            
    if canEquip:
        modDict = None
        if toOffHand: #equipping a weapon in the offhand, need to change values
            dic = item.stats
            newDic = {}
            #make all stats for hand1 to hand2
            for k, v in dic.items():
                if k[:5] == "hand1":
                    string = "hand2" + k[5:]
                    newDic[string] = v
                else:
                    newDic[k] = v
            modDict = newDic
        else:
            modDict = item.stats
        mod = Mod(modDict)
        unit.equipment[slot] = EquipSlot(item, mod.id)
        unit.stats.addModifier(mod) #modify stats of unit
        game.msg("{u} equipped {i}".format(
            u=unit.name, i=item.name))
        return True
    else:
        return False #failure to equip

#same as equip but in reverse. Returns the item if successful
def unequip(unit, slot):
    #check if you have an item equipped in that slot
    equipSlot = unit.equipment[slot]
    if equipSlot:
        item = equipSlot.item
        unit.stats.removeModifier(equipSlot.modID)
        unit.equipment[slot] = None
        return item
    else:
        return None

