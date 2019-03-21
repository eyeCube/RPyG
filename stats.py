
#stats.py

from metadata import *

class Stats:
    def __init__(self, dic):
        self.base = dic
        self.modifiers = {}
    def addModifier(self, mod):
        self.modifiers[mod.id] = mod
    def removeModifier(self, modID):
        del self.modifiers[modID]
    def getBase(self, stat):
        return self.base[stat]
    def setBase(self, stat, value):
        self.base[stat] = value
    def addBase(self, stat, value):
        self.base[stat] += value
    def __getitem__(self, i):
        base = self.base[i]
        total = base
        multiplier = 1.0
        for v in self.modifiers.values():
            if v.add:
                for stat, value in v.add.items():
                    if stat == i:
                        total += value
            if v.mult:
                for stat, value in v.mult.items():
                    if stat == i:
                        multiplier *= value
                        
        #derived stats modified by attributes
            
        if (i == 'hp'):
            total += int(HP_PER_END*self['end'])
            total = min(total, self['hpMax']) #cap at maximum HP
        if (i == 'hpMax'):
            total += int(HP_PER_END*self['end'])
        elif (i == 'def'):
            total += int(DEF_PER_END*self['end'])
        elif (i == 'resPhysical'):
            total += int(RESPHYSICAL_PER_END*self['end'])
        elif (i == 'resHeat'):
            total += int(RESHEAT_PER_END*self['end'])
        elif (i == 'resCold'):
            total += int(RESCOLD_PER_END*self['end'])
        elif (i == 'poise'):
            total += int(POISE_PER_AGI*self['agi'])
        elif (i == 'mob'):
            total += int(MOB_PER_AGI*self['agi'])
        elif (i == 'spd'):
            total += int(SPD_PER_AGI*self['agi'])
        elif (i == 'acc'):
            total += int(ACC_PER_DEX*self['dex'])
            total += int(ACC_PER_AGI*self['agi'])
            total += int(ACC_PER_PER*self['per'])
        elif (i == 'eva'):
            total += int(EVA_PER_AGI*self['agi'])
            total += int(EVA_PER_PER*self['per'])
        elif (i == 'atk'):
            total += int(ATK_PER_STR*max(0, self['str'] - 4))
        elif (i == 'crit'):
            total += int(CRIT_PER_PER*self['per'])
            total += int(CRIT_PER_DEX*self['dex'])
        elif (i == 'vision'):
            total += int(VISION_PER_PER*self['per'])
        elif (i == 'parry'):
            total += int(PARRY_PER_DEX*self['dex'])
        elif (i == 'maxTechs'):
            total += int(MAXTECHS_PER_INT*self['int'])
        elif (i == 'maxTechLvl'):
            total += int(MAXTECHLVL_PER_WIL*self['wil'])
        elif (i == 'resMagick'):
            total += int(RESMAGICK_PER_WIL*self['wil'])
        total = round(total*multiplier) #apply mult. mods
        return max(0, total)
    
    #initialize and return a Stats object for the given race
    @classmethod
    def init(cls, race):
        if race == RACE_HUMAN:
            stats = Stats({ #statistics for human
            #attributes
                STRENGTH : 0,
                AGILITY : 0,
                DEXTERITY : 0,
                ENDURANCE : 0, 
                PERCEPTION : 0,
                WILLPOWER : 0,
                INTELLIGENCE : 0,
            #derived stats
                'hp' : 0, #health
                'hpMax' : 0, #maximum health
                'mp' : 0, #movement points
                'mob' : 0, #mobility
                'balance': 0, #resistance to push, pull, stun, knockdown
                'poise': 0, #maximum balance
                'acc' : 0, #accuracy
                'eva' : 0, #evasion
                'spd' : 0, #speed
                'vision' : 0, #range of sight
                'defStrike' : 0, #general Def bonus to all body parts
                'defThrust': 0,
                'defSlash': 0,
                'protection': 0, #general protection bonus to all body parts
            #techniques
                'maxTechs' : 0, #max number of techniques (Skills/spells)
                'maxTechLvl' : 0, #max level of techniques
            #resistances
                'resMagick' : 0, #resist spells
                'resPhysical' : 0, #resist bleeding, dazed, stun,
                'resHeat' : 0,
                'resCold' : 0,
            #torso armour
                'torsoDefStrike' : 0,
                'torsoDefThrust' : 0,
                'torsoDefSlash' : 0,
                'torsoProtection' : 0,
            #head armour
                'headDefStrike' : 0,
                'headDefThrust' : 0,
                'headDefSlash' : 0,
                'headProtection' : 0,
            #legs armour
                'legsDefStrike' : 0,
                'legsDefThrust' : 0,
                'legsDefSlash' : 0,
                'legsProtection' : 0,
            #arms armour
                'armsDefStrike' : 0,
                'armsDefThrust' : 0,
                'armsDefSlash' : 0,
                'armsProtection' : 0,
                })
        return stats



#Mod
#Stat modifier
#has an ID that is automatically set to a unique ID by default.
#has:
#optional add and mult dictionaries which contain info about stat modifiers
#Note on intended use:
#   add is for linear modifiers; mult is for multipliers.
#WARNING:
#-a Mod ID must be unique to all other Mods that are applied to the same unit
class Mod:
    modID=10000 #leave plenty room for constant Mods w/ low ID values.
    def __init__(self, add={}, mult={}, ID=None):
        if ID == None:
            self.id = Mod.modID
            Mod.modID += 1
        else:
            self.id = ID
        self.add = {}
        self.mult = {}
        for k, v in add.items():
            self.add[k] = v
        for k, v in mult.items():
            self.mult[k] = v







#stun and knockdown could be covered by balDmg (balance damage on strike) 
'''

                'stun': 0, #chance to stun enemy on attack (can be resisted)
                'knockdown': 0, #chance to (attempt to) knock enemy off their feet
                'blind': 0, #chance to blind enemy
                'mortalWound': 0, #chance to HURT & cause bleeding or other S.E.'s

'''
'''
        elif (i == 'accr'):
            total += int(ACC_PER_DEX*self['dex'])
            total += int(ACC_PER_AGI*self['agi'])
            total += int(ACCR_PER_PER*self['per'])
        elif (i == 'acct'):
            total += int(ACC_PER_DEX*self['dex'])
            total += int(ACC_PER_AGI*self['agi'])
            total += int(ACCT_PER_PER*self['per'])

            #THESE ARE STATS THAT WEAPONS HAVE, NOT PEOPLE
                'disarm': 0, #chance to attempt to disarm opponent
                'dismember': 0, #chance to chop off targeted body part
                'hitAdjFoe' : 0, #chance to also hit a foe adjacent to your target when you melee attack
                'ignoreBlock' : 0, #chance to bypass block
                'ignoreParry' : 0, #chance to bypass parry
                'destroy' : 0, #chance to seriously damage gear when you hit it
                'pull' : 0, #chance to pull enemy (hook)
                'push': 0, #chance to push enemy (knockback)
                'aimForHead': 0, #additional chance to hit enemy's head
                'crit' : 0, #critical hit chance bonus
            #blocking/parrying
                'parry' : 0, #parry chance (parry only works for melee attacks)
                'parryAlly' : 0, #chance to parry for an ally
                'blockDefs' : 0, #defense granted when you block (shock)
                'blockDefp' : 0,
                'blockm' : 0, #m= chance to block melee attacks
                'blockr' : 0, #r= " ranged attacks
                'blockAllym' : 0, #block for an ally (melee)
                'blockAllyr' : 0,
            #COMBINE THESE INTO REGULAR WEAPON STATS HELD BY THE WEAPON NOT THE UNIT
            #thrown
                'throwAtks': 0, #you can only throw the weapon in your mainhand
                'throwAtkp': 0, #... so all these stats apply to mainhand
                'throwRangeMin': 0,
                'throwRangeMax': 0,
            #ranged
                'rangeAtks': 0,
                'rangeAtkp': 0,
                'rangeMin': 0,
                'rangeMax': 0,
            #STATS HANDLED BY THE WEAPONS YOU WIELD NOT THE UNIT
            #hand 1 weapon (mainhand)
                'hand1AtkStrike' : 0,
                'hand1atkp' : 0,
                'hand1reachMin' : 0,
                'hand1reachMax' : 0,
                'hand1grip': 0, #resistance to disarm
            #hand 2 weapon (offhand)
                'hand2atks' : 0,
                'hand2atkp' : 0,
                'hand2reachMin' : 0,
                'hand2reachMax' : 0,
                'hand2grip': 0,
            '''

