
#unit.py

from engine import *
from metadata import *
from stats import *
from item import *
from hexmap import Map
import game


'''
    Unit
    object representing a character in the game
    
'''
class Unit:
    newIDnum = 0
    units = {}
    
    def __init__(self, owner, sprite, pos, name, race):
        self.name=name
        self.race=race
        self.pos=pos #position (location)
        self.sprite=sprite
        self.owner=owner
        
        self.ID=None
        self.dead=False #flag for garbage collection
        self.knockedDown=False #flag for being knocked off feet
        self.dazeCounter=0 #counters for status effects 
        self.bleedCounter=0
        self.poisonCounter=0
        self.evadeCounter=0
        self.sprXoffset=0 #offset = sprite X,Y origin
        self.sprYoffset=0
        self.lvl=0 #level
        self.exp=0 #experience
        self.skillPts=0
        self.attributePts=0
        self.mass=0 #kg
        self.clas=None #character class
        self.classDescription=None
        self.activeCommand=None
        self.weaponTypes=[] #weapons training
        self.equipment={} #gear slots
        self.status = {} #status effects
        self.stats = Stats.init(self.race)

    @classmethod
    def getList(cls):   return list(cls.units.values())
    @classmethod
    def getDict(cls):   return cls.units

    @classmethod
    def create(cls, charClass, sprite, name, pos, owner, lvl=1, race=RACE_HUMAN):
        unit = Unit(owner, sprite, pos, name, race)
        unit.ID = cls.newIDnum
        cls.units.update({unit.ID : unit})
        cls.newIDnum += 1

        #default values
        unit.sprXoffset=16
        unit.sprYoffset=16
        
        unit.lvl=1
        unit.skillPts=0
        unit.attributePts=0
        
        unit.clas = charClass['name']
        unit.classDescription = charClass['desc']
        unit.weaponTypes = charClass['weaponTypes']
        unit.stats.setBase('str', charClass[STRENGTH])
        unit.stats.setBase('agi', charClass[AGILITY])
        unit.stats.setBase('dex', charClass[DEXTERITY])
        unit.stats.setBase('end', charClass[ENDURANCE])
        unit.stats.setBase('per', charClass[PERCEPTION])
        unit.stats.setBase('wil', charClass[WILLPOWER])
        unit.stats.setBase('int', charClass[INTELLIGENCE])
        unit.stats.setBase('hpMax', BASE_HP)
        unit.stats.setBase('hp', BASE_HP)
        unit.stats.setBase('atk', BASE_ATK)
        unit.stats.setBase('def', BASE_DEF)
        unit.stats.setBase('acc', BASE_ACC)
        unit.stats.setBase('eva', BASE_EVA)
        unit.stats.setBase('mob', BASE_MOB)
        unit.stats.setBase('spd', BASE_SPD)
        unit.stats.setBase('maxTechs', BASE_MAXTECHS)
        unit.stats.setBase('maxTechLvl', BASE_MAXTECHLVL)
        unit.stats.setBase('vision', BASE_VISION)
        unit.stats.setBase('poise', BASE_POISE)
        unit.equipment = {
            HEAD : None,
            TORSO : None,
            LEGS : None,
            ARMS : None,
            HAND1 : None,
            HAND2 : None,
            }
        '''unit.body = {
            HEAD : BodyPart(HEAD),
            TORSO : BodyPart(TORSO),
            LEG1 : BodyPart(LEG),
            LEG2 : BodyPart(LEG),
            ARM1 : BodyPart(ARM),
            ARM2 : BodyPart(ARM),
            HAND1 : BodyPart(HAND),
            HAND2 : BodyPart(HAND),
            FOOT1 : BodyPart(FOOT),
            FOOT2 : BodyPart(FOOT),
            EYE1 : BodyPart(EYE),
            EYE2 : BodyPart(EYE),
            }'''

        #Level up
        #set_stat(unit,"hpmax",20)
        for i in range(lvl - 1):
            levelUpAuto(unit)
            
        return unit
    
    @classmethod
    def destroy(cls, unitID):
        if unitID in cls.units:
            del cls.units[unitID]
            return True
        else:
            return False
    @classmethod
    def getList(cls):   return list(cls.units.values())
    @classmethod        
    def getFromHex(cls, _hex):  #find unit on a hex
        for unit in cls.units.values():
            if unit.pos == _hex:
                return unit
        return None




#-units

def kill(unit):
    unit.dead = True
    if Game.getSelectedUnit() == unit:
        Game.setSelectedUnit(None)
def exhaustTurn(unit):
    unit.stats.setBase('mp', 0)
        
def unitUpkeep():
    garbage=[]
    for unit in Unit.getList():
        if unit.dead:
            msg("{u} is dead".format(u=unit.name))
            garbage.append(unit.ID)
            continue
        unit.bleedCounter = 0
        unit.dazeCounter = 0
        unit.evadeCounter = 0
        unit.poisonCounter = 0
    for ID in garbage:
        Unit.destroy(ID)
        
def getVisibleTiles(player):
    tiles=set()
    for unit in Unit.getList():
        if game.ownedBy(unit, player):
            for tile in hex_range(unit.pos, getStat(unit, 'vision')):
                if tile in Map.getMap():
                    tiles.add(tile)
    return tiles

#use this to retrieve a stat from a unit
#instead of getting it directly from the unit's stats
#this can add bonuses from gear, enchantments, terrain, etc.
def getStat(unit, stat):
    value = unit.stats[stat]
    hand1slot = getEquipment(unit,HAND1)
    hand2slot = getEquipment(unit,HAND2)
          
    #Bonuses from wielding a 1/2 weapon with 2 hands
    if hand1slot:
        if (hand1slot.hands == "1/2" and
            hand2slot == None):
            if   stat == "spd": value += TWOH_SPD_BONUS
            elif stat == "hand1atks": value += TWOH_ATK_BONUS
            elif stat == "hand1atkp": value += TWOH_ATK_BONUS
            elif stat == "blockDefs": value += TWOH_DEFS_BONUS
            elif stat == "blockm": value += TWOH_BLOCK_BONUS
            elif stat == "crit": value += TWOH_CRIT_BONUS
            elif stat == "parry": value += TWOH_PARRY_BONUS
            elif stat == "parryAlly": value += int(TWOH_PARRY_BONUS/2)
            elif stat == "accm": value += TWOH_ACC_BONUS
    
    #penalty for weapons in the offhand
    if hand2slot:
        if   stat == "hand2atks": value -= OFFHAND_ATK_PENALTY
        elif stat == "hand2atkp": value -= OFFHAND_ATK_PENALTY
        elif stat == "accm": value -= OFFHAND_ACC_PENALTY

    #unarmed
    if (hand1slot == None and hand2slot == None):
        if   stat == "hand1atks": value += UNARMED_ATK1
        elif stat == "hand2atks": value += UNARMED_ATK2
        elif stat == "spd": value += UNARMED_SPD
    
    value = max(0, value)    
    return value

    
#recharge every unit
        #if MP_PER_MOB is 10, values will be the following:
        #recharge 0 MP if you have 0 mobility,
        #1 MP if you have 1-19 mobility,
        #2 MP if you have 20-29,
        #3 MP for 30-39 mobility, etc.
def rechargeUnits():
    for unit in Unit.getList():
        mob = getStat(unit,'mob')
        value = max(1, mob//MP_PER_MOB)*(0 if mob==0 else 1)
        unit.stats.setBase('mp', value)
'''def levelUpAuto(unit):
    unit.lvl += 1
    unit.hpmax += 1
    unit.acc += 1
    unit.eva += 1
    trainAttribute(unit, int(random.random()*7))
    #unit.skillPts += 1
    #unit.attributePts += 1'''
def levelUp(unit):
    unit.lvl += 1
    unit.hpmax += HP_PER_LVL
    unit.acc += ACC_PER_LVL
    unit.eva += EVA_PER_LVL
    unit.skillPts += SKILLPTS_PER_LVL
    unit.attributePts += ATTPTS_PER_LVL
def canLevelUp(unit): return (unit.exp >= expRequired(unit.lvl))
def expRequired(lvl): return 100
def awardExp(unit, amount):
    amt = max(0, amount - unit.lvl)
    unit.exp += amt
def trainAttribute(unit, att):
    #check to see if you have enough att. points.
    if unit.attributePts > 0:
        unit.__dict__[ATTRIBUTES[att]] += 1
        unit.attributePts -= 1
        
def getAdjacentUnits(unit):
    _list=[]
    for neighbor in hex_neighbors(unit.pos):
        unitHere = Unit.getFromHex(neighbor)
        if unitHere:
            _list.append(unitHere)
    return _list



#Player
#fxn to check for conditions for a player losing
def failure(player):
    failed=False
    hpOut=True #assume positively first
    for unit in Unit.getList():
        if (game.ownedBy(unit, player) and
            getStat(unit,'hp') > 0):
            hpOut = False
            break
    if hpOut:
        failed = True
    return (failed)
            
#fxn to check for conditions for ending the player's turn.
def playerTurnForcedEnd(player):
    #condition: no Movement Points remaining on any units.
    mpOut=True #assume positively first
    for unit in Unit.getList():
        if (game.ownedBy(unit, player) and
            getStat(unit,'mp') > 0):
            mpOut = False
            break
    return (mpOut)
