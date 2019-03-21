#metadata.py

#constants to be accessed (never altered) by the game file.

import pygame


#commands
CMD_MOVE=0
CMD_SELECTHEX=1
CMD_TARGETHEX=2
CMD_MOUSEHOVER=3
CMD_SKIPTURN=4



#sprites
SPR_KNIGHT = pygame.image.load("./art/knight.png")
SPR_THIEF = pygame.image.load("./art/thiefLarge.png")
SPR_MONK = pygame.image.load("./art/monk.png")


#colours
COLOURS={
    'deep'          : (20,20,0),
    'accent'        : (255,215,128),
    'neutral'       : (138,100,0),
    'blue'          : (26,125,160),
    'trueblue'      : (16,25,255),
    'ltblue'        : (140,183,217),
    'green'         : (0,170,30),
    'dkgreen'       : (0,95,17),
    'vdkgreen'      : (20,37,9),
    'truegreen'     : (0,255,0),
    'dkmagenta'     : (150,0,60),
    'orange'        : (255,177,0),
    'gold'          : (255,200,60),
    'brown'         : (125,91,0),
    'dkbrown'       : (55,36,6),
    'scarlet'       : (255,40,0),
    'red'           : (242,5,50),
    'dkred'         : (50,0,0),
    'truered'       : (255,0,0),
    'purple'        : (180,60,120),
    'yellow'        : (115,190,60),
    'trueyellow'    : (255,255,0),
    'white'         : (255,255,255),
    'ltgray'        : (200,200,200),
    'gray'          : (128,128,128),
    'dkgray'        : (80,80,80),
    'vdkgray'       : (50,50,50),
    'black'         : (0,0,0),
}




#keys
MENUITEMS=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0',
    ]
STR_TO_PYGAMECONST={
    'a' : pygame.K_a
    }
KEY_CHARGE = pygame.K_m
KEY_SKIPTURN = pygame.K_SPACE
KEY_DESELECT = pygame.K_ESCAPE
KEY_DEG0 = pygame.K_d
KEY_DEG60 = pygame.K_e
KEY_DEG120 = pygame.K_w
KEY_DEG180 = pygame.K_a
KEY_DEG240 = pygame.K_z
KEY_DEG300 = pygame.K_x


#Terrain Types
TER_GRASS=0
TER_SAND=1
TER_SNOW=2
TER_ROCK=3
TER_TAR=4
TER_FOGOFWAR=999


#Terrain colours
TERRAINCOLOURS={
    TER_FOGOFWAR : COLOURS['vdkgray'],
    TER_GRASS : COLOURS['dkgreen'],
    TER_SAND : COLOURS['brown'],
    TER_SNOW : COLOURS['ltgray'],
    TER_ROCK : COLOURS['gray'],
    TER_TAR : COLOURS['purple'],
    }


#SETTINGS
TILESIZE=20 #size from origin to corner
DISPW=1280
DISPH=728
GRIDXOFFSET=60 #where to draw the hex tilemap relative to the top-left corner
GRIDYOFFSET=60
HUDX1=60
HUDY1=480
RING_THICKNESS=3 #select unit tile rings

#GAME DATA
GRIDWIDTH=24
GRIDHEIGHT=15
BGCOLOUR=COLOURS['black']

#STATS DATA
HP_PER_LVL=2 #stats gained per level up, across the board for all characters
ACC_PER_LVL=2
EVA_PER_LVL=1
SKILLPTS_PER_LVL=1 #skill points gained per level up
ATTPTS_PER_LVL=1 #attribute points gained per level up
MAX_EVASION=95 #effective evasion during combat can never exceed this value
FULL_PROTECTION=100 #the max protection you need to ensure you won't get critted... unless your protection is broken by enemy crit value. Excess protection past this value grants effective resistance to crit.
CRIT_PROTECTION_MULT=0.5 #multiplier for defense value when a crit is scored
HIT_LEGS=12 #default chance to hit body parts
HIT_ARMS=13
HIT_HEAD=10
MP_PER_MOB=10 #you need this much mobility to gain 1 extra mp per turn
SPEED_FACTOR=20 #how much more speed you need to guarantee an extra attack
DESTROY_DAMAGE_DECIMAL=0.1 #0-1 how much of max durability is knocked from condition when you use Destroy Gear ability
MAX_CON_DEF_CUT=0.5 #0-1 gear's Def penalty multiplier from condition is capped at this value
MAX_CON_PROTECT_CUT=0.75 #0-1 " Protection "
TWOH_PARRY_BONUS=8 #when wielding a (1- or 2-handed weapon) w/ 2 hands, gain stat bonuses
TWOH_SPD_BONUS=10
TWOH_CRIT_BONUS=5
TWOH_ACC_BONUS=10
TWOH_ATK_BONUS=2
TWOH_DEFS_BONUS=4
TWOH_BLOCK_BONUS=25
TWOH_GRIP_BONUS=20
OFFHAND_ATK_PENALTY=1 #when wielding a weapon in the offhand, get penalties
OFFHAND_ACC_PENALTY=15
OFFHAND_SPD_PENALTY=20 #some penalties may only apply when attacking w/ offhand
EVA_LOSS_PER_EVADE=25 #temporary debuff to Eva after evading (nerfs evasion when you are being attacked from multiple foes at once)
MINREACH_ATKPENALTY=2 #penalties when hitting foes closer than your minimum reach
MINREACH_ACCPENALTY=25
MINREACH_SPDPENALTY=20
UNARMED_ATK1=5 #damage you do with your mainhand when trained in unarmed
UNARMED_ATK2=3 #left fist
UNARMED_SPD=0 #bonus when unarmed and trained in unarmed
STATLIMITER=4 #it costs 1 more pts every x attribute levels to gain another lvl in that attribute
#----derived stat bonuses from attributes
ACC_PER_DEX=3
CRIT_PER_DEX=1
PARRY_PER_DEX=0.75
HP_PER_END=3
DEF_PER_END=0.25
RESPHYSICAL_PER_END=2
RESHEAT_PER_END=1
RESCOLD_PER_END=1
ACCR_PER_PER=5
accm_PER_PER=1
ACCT_PER_PER=5
EVA_PER_PER=1
CRIT_PER_PER=0.25
VISION_PER_PER=2
#PROTECT_PER_AGI=1
ACC_PER_AGI=1
EVA_PER_AGI=2
SPD_PER_AGI=2
MOB_PER_AGI=1
POISE_PER_AGI=1
ATK_PER_STR=1
accm_PER_STR=3
MAXTECHS_PER_INT=1
MAXTECHLVL_PER_WIL=1
RESMAGICK_PER_WIL=1
#RESCHARM_PER_CHA=1
#CHARM_PER_CHA=1
#----base stats
ATTRIBUTEPOINTS=12 #every char gets x points to add to attribute base values.
BASE_STR=4
BASE_AGI=4
BASE_END=4
BASE_PER=4
BASE_WIL=4
BASE_INT=4
BASE_DEX=4
BASE_ACC=70
BASE_EVA=20
BASE_HP=5
BASE_ATK=0
BASE_DEF=0
BASE_SPD=30
BASE_MOB=30
BASE_MAXTECHS=0
BASE_MAXTECHLVL=0
BASE_VISION=0
BASE_POISE=0


#races
RACE_HUMAN=0


#item data
DURABILITY_MODIFIER=3.0 #multiplier for all max durability values


#attributes
STRENGTH=0
AGILITY=1
DEXTERITY=2
ENDURANCE=3
PERCEPTION=4
WILLPOWER=5
INTELLIGENCE=6
#CHARISMA=7


#status effect IDs
#each of these has a unique identifier because you cannot be dazed twice, etc.
SE_DAZE=0
SE_KO=1
SE_CONFUSE=2
SE_BLIND=3
SE_BLEED=4
SE_BURN=5
SE_FREEZE=6
SE_POISON=7
SE_MORALEHI=10
SE_MORALELO=11

#status effect constants
SE_DIE_BASE=0 #at what value of HP do you die?
SE_BLEED_BASE=0 #how much pierce damage you have to take at 0 res to bleed
SE_BLEED_TIMER=5
SE_DAZE_BASE=0 #how much shock damage you have to take at 0 res to become stunned
SE_DAZE_TIMER=3
SE_DAZE_MULTMODS={'accm':0.5,'accr':0.5,'eva':0.5,'vision':0.5}
SE_KO_BASE=10 #at what value of HP do you become K.O.'d?
SE_KO_MULTMODS={'accm':0,'accr':0,'acct':0,'eva':0,'vision':0,
                'parry':0,'parryAlly':0,
                'hand1Guard':0,'shield':0,
                'guardAlly':0,'shieldAlly':0,
                'mob':0,'def':0,
                'torsoProtect':0.25,'headProtect':0.25,
                'legsProtect':0.25,'armsProtect':0.25,}
SE_BLIND_MULTMODS={'vision':0,'accm':0,'acct':0,'accr':0,'eva':0.25,
                    'parry':0.25,'parryAlly':0.25,
                    'hand1Guard':0.25,'shield':0.25,
                    'guardAlly':0.25,'shieldAlly':0.25,}


#materials
MAT_IRON=0
MAT_STEEL=1
MAT_LEATHER=2
MAT_LINEN=3
MAT_WOOD=4
MAT_BONE=5
MAT_HEMP=6
MAT_FUR=7
MAT_LEAD=7
MAT_GUNPOWDER=8
MAT_BRONZE=9
MAT_SILVER=10
MAT_GOLD=11
MAT_MITHRIL=90


#weapon types
SHORTSWORDS=0
LONGSWORDS=1
AXES=2
HAMMERS=3
CLUBS=4
SPEARS=5
SLINGS=6
BOWS=7
CBOWS=8
KNIVES=9
GREATSWORDS=10
POLLARMS=11
SHIELDS=12
RAPIERS=13
CURVEDSWORDS=14
GUNS=15
STAVES=16
BOMBS=17
PIKES=18
PAVISES=19
PITCHING=90 #pitching; throwing bombs, and non-throwing weapons
THWKNIVES=91 #throwing knives
THWSPEARS=92 #throwing spears
THWAXES=93   #throwing axes
THWSWORDS=94 #throwing swords
INSTRUMENTS=99 #musical
UNARMED=100 #fisticuffs

#types of weapons that can be thrown + their associated skills
THROWNWEAPONS={
    AXES : THWAXES,
    SPEARS : THWSPEARS,
    KNIVES : THWKNIVES,
    SHORTSWORDS : THWSWORDS,
    LONGSWORDS : THWSWORDS,
    CURVEDSWORDS : THWSWORDS,
    BOMBS : PITCHING,
    HAMMERS : PITCHING,
    CLUBS : PITCHING,
    STAVES : THWSPEARS,
    }


#armour types
TORSOARMOUR=0
HEADARMOUR=1
LEGARMOUR=2
ARMARMOUR=3
CLOAK=4


#Equipment Slots
TORSO=0
HEAD=1
LEGS=2
ARMS=3
HAND1=4
HAND2=5
RANGED=6
AMMO=7
WRIST=8
PAVISE=9
CLOAK=10
JEWELRY=99


#stat scaling modifiers
SCALING_S=1.5
SCALING_A=1.25
SCALING_B=1
SCALING_C=0.75
SCALING_D=0.5
SCALING_E=0.25


#Manager IDs
MNG_COMMANDS=0
MNG_MENU=1



#skill metadata
MAX_SKILL_LEVEL=20 #no skill can exceed this level

#skill types
ST_PASSIVE=0
ST_WEAPONSKILL=1 #generic skill for allowing use of a weapon class
ST_ATTACKMAINHAND=10 #skill that modifies & performs a mainhand attack
ST_ATTACKOFFHAND=11 #skill that modifies & performs an offhand attack
ST_ATTACKBOTHHANDS=12 #attacks w/ both mainhand and offhand

#requirement types (for skills)
RQ_WIELDING_UNARMED=0
RQ_WIELDING_KNIVES=1
RQ_WIELDING_SHORTSWORDS=2
RQ_WIELDING_LONGSWORDS=3
RQ_WIELDING_AXES=4
RQ_WIELDING_CLUBS=5
RQ_WIELDING_HAMMERS=6
RQ_WIELDING_POLLARMS=7
RQ_WIELDING_RAPIERS=8
RQ_WIELDING_GREATSWORDS=9
RQ_WIELDING_SPEARS=10
RQ_WIELDING_CURVEDSWORDS=11
RQ_WIELDING_PIKES=12
RQ_WIELDING_BOWS=13
RQ_WIELDING_CBOWS=14
RQ_WIELDING_GUNS=15
RQ_WIELDING_SLINGS=16
RQ_WIELDING_STAVES=17
RQ_WIELDING_BOMBS=18
RQ_WIELDING_INSTRUMENTS=19
RQ_WIELDING_THWSWORDS=20
RQ_WIELDING_THWKNIVES=21
RQ_WIELDING_THWSPEARS=22
RQ_WIELDING_THROWING=23
RQ_ATTACK_WITH_UNARMED=100
RQ_ATTACK_WITH_KNIVES=101
RQ_ATTACK_WITH_SHORTSWORDS=102
RQ_ATTACK_WITH_LONGSWORDS=103
RQ_ATTACK_WITH_AXES=104
RQ_ATTACK_WITH_CLUBS=105
RQ_ATTACK_WITH_HAMMERS=106
RQ_ATTACK_WITH_POLLARMS=107
RQ_ATTACK_WITH_RAPIERS=108
RQ_ATTACK_WITH_GREATSWORDS=109
RQ_ATTACK_WITH_SPEARS=110
RQ_ATTACK_WITH_CURVEDSWORDS=111










#Character Classes
CLS_THIEF={
    "name":"Thief",
    "desc":'''
Cunning and agile rogue with skills in burglary and sneaking.
''',
    STRENGTH:4,
    AGILITY:8,
    DEXTERITY:8,
    ENDURANCE:4,
    INTELLIGENCE:6,
    WILLPOWER:4,
    PERCEPTION:6,
    "weaponTypes":[ #weapons training
        SHORTSWORDS,KNIVES,SHIELDS,
        THWKNIVES,UNARMED,RAPIERS,
        ],
    }
'''"skills":[ #starting skills
    (STEALTH,2,),
    (PICKPOCKET,2,),
    ],'''
CLS_KNIGHT={
    "name":"Knight",
    "desc":'''
Hardy and conditioned, this elite soldier has broad weapons training.
''',
    STRENGTH:8,
    AGILITY:6,
    DEXTERITY:4,
    ENDURANCE:8,
    INTELLIGENCE:4,
    WILLPOWER:6,
    PERCEPTION:4,
    "weaponTypes":[
        AXES,CLUBS,HAMMERS,
        POLLARMS,GREATSWORDS,
        SHORTSWORDS,LONGSWORDS,KNIVES,
        SHIELDS,UNARMED,
        ],
    }
CLS_SWORDSMASTER={
    "name":"Swordsmaster",
    "desc":'''
This skilled warrior is trained extensively in longsword combat.
''',
    STRENGTH:6,
    AGILITY:8,
    DEXTERITY:8,
    ENDURANCE:4,
    INTELLIGENCE:6,
    WILLPOWER:4,
    PERCEPTION:4,
    "weaponTypes":[
        LONGSWORDS,SHORTSWORDS,KNIVES,RAPIERS,
        ],
    }
CLS_WIZARD={
    "name":"Wizard",
    "desc":'''
Wise and keen spellcaster, learned in many skills
''',
    STRENGTH:4,
    AGILITY:4,
    DEXTERITY:4,
    ENDURANCE:4,
    INTELLIGENCE:9,
    WILLPOWER:9,
    PERCEPTION:4,
    "weaponTypes":[
        SHORTSWORDS,KNIVES,LONGSWORDS,
        SHIELDS,STAVES,
        ],
    }
'''CLS_CONJURER={
    "name":"Conjurer",
    "desc":'''
#A courageous and leaderly spellsword, learned in summoning magicks
''',
    STRENGTH:4,
    AGILITY:4,
    DEXTERITY:4,
    ENDURANCE:4,
    INTELLIGENCE:8,
    WILLPOWER:8,
    PERCEPTION:4,
    "weaponTypes":[
        SHORTSWORDS,LONGSWORDS,KNIVES,
        SHIELDS,UNARMED,STAVES,
        ],
    }'''
CLS_MONK={
    "name":"Monk",
    "desc":'''
Willful and disciplined mystic warrior, capable of great skill potential
''',
    STRENGTH:4,
    AGILITY:8,
    DEXTERITY:4,
    ENDURANCE:8,
    INTELLIGENCE:4,
    WILLPOWER:8,
    PERCEPTION:4,
    "weaponTypes":[
        UNARMED,STAVES,
        ],
    }
CLS_ARCHER={
    "name":"Archer",
    "desc":'''
Perceptive and strong ranger, skilled marksman and hunter
''',
    STRENGTH:8,
    AGILITY:4,
    DEXTERITY:8,
    ENDURANCE:4,
    INTELLIGENCE:4,
    WILLPOWER:4,
    PERCEPTION:8,
    "weaponTypes":[
        BOWS,CBOWS,SLINGS,PAVISES,
        SHORTSWORDS,KNIVES,
        ],
    }
CLS_GUNMAN={
    "name":"Gunman",
    "desc":'''
Perceptive and hardy soldier, trained extensively in the art of gunmanship
''',
    STRENGTH:4,
    AGILITY:8,
    DEXTERITY:4,
    ENDURANCE:8,
    INTELLIGENCE:4,
    WILLPOWER:4,
    PERCEPTION:8,
    "weaponTypes":[
        GUNS,CBOWS,
        SHORTSWORDS,KNIVES,
        ],
    }
CLS_SPEARMAN={
    "name":"Spearman",
    "desc":'''
Quick and strong soldier, trained extensively in pollarm combat.
''',
    STRENGTH:8,
    AGILITY:6,
    DEXTERITY:8,
    ENDURANCE:6,
    INTELLIGENCE:4,
    WILLPOWER:4,
    PERCEPTION:4,
    "weaponTypes":[
        SPEARS,POLLARMS,STAVES,PIKES,
        SHORTSWORDS,KNIVES,
        ],
    }
'''CLS_BARD={
    "name":"Bard",
    "desc":'''
#Charming and sharp enchanter; virtuoso musician
''',
    STRENGTH:4,
    AGILITY:4,
    DEXTERITY:4,
    ENDURANCE:4,
    INTELLIGENCE:8,
    WILLPOWER:4,
    PERCEPTION:4,
    "weaponTypes":[
        SPEARS,SLINGS,
        INSTRUMENTS,
        ],
    }'''

















#------#
# Gear #
#------#


'''
Item data explanations:
desc    description
type    which slot is used for equipping? HAND1 items can be wielded in HAND2.
school  class of weapons, determines who can use it
hands   "1": 1-handed. "2": 2-handed. "1/2": 1 or 2-handed (gain bonuses for 2H wielding)
strReq  strength required to wield.
mat     materials
dur     durability (maximum condition)
value   cost
mass    weight, kg
stats   explanations elsewhere for stats.
'''




#-------------#
#   Armour    #
#-------------#

#torso armour
AR_LEATHERCUIRASS={
    'desc': '''A jacket of thick rawhide, uncommon to find in these parts. In some countries, where high-quality hide is more abundant, leather armours are popular among budget soldiers. Here the primary use of such armours is as heirlooms or decorations, and in arena fights where entertainment - rather than protection - is the goal; as this armour provides little protection compared to contemporary armours.''',
    'name': "leather cuirass",
    'type': TORSO,
    'strReq': 1,
    'mat': (MAT_LEATHER,),
    'dur': 50,
    'value': 490,
    'mass': 3.5,
    'stats': {
        'torsoDefStrike': 3,
        'torsoDefThrust': 5,
        'torsoDefSlash': 5,
        'torsoProtect': 77,
        'spd': -2,
        'eva': -5,
        'mob': -1,
        },
    }
AR_GAMBESON={
    'desc': '''A heavy, padded tunic of many layers of fine linen. A gambeson is typically worn underneath maille and plate armour for added impact defense; usually a gambeson by itself offers little defense compared to plate armour, though it is unencumbering and inexpensive in comparison. This gambeson is designed to be defensive enough to wear by itself, and this armour is very cost-effective for the amount of protection it provides.''',
    'name': "gambeson",
    'type': TORSO,
    'strReq': 1,
    'mat': (MAT_LINEN,),
    'dur': 80,
    'value': 300,
    'mass': 3.0,
    'stats': {
        'torsoDefStrike': 4,
        'torsoDefThrust': 4,
        'torsoDefSlash': 8,
        'torsoProtect': 103,
        'spd': -1,
        'accm': -3,
        'accr': -2,
        'eva': -3,
        'poise': 1,
        'resCold': 5,
        'resHeat': -5,
        },
    }
AR_HAUBERGEON={
    'desc': '''A maille haubergeon, or half-shirt of maille, with a gambeson for wear underneath to add shock protection. This light armour is considered the minimum level of protection for warriors on the battlefield, and typically plate armour is preferred for its superior defense. When plate armour is too heavy, impractical, or expensive, a hauberk can provide adequate defense with few drawbacks. A haubergeon is a small hauberk, which only protects the upper body and upper arms. It's cheaper, but a full hauberk is better if you can afford it.''',
    'name': "maille haubergeon",
    'type': TORSO,
    'strReq': 1,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 100,
    'value': 2690,
    'mass': 7.5,
    'stats': {
        'torsoDefStrike': 3,
        'torsoDefThrust': 6,
        'torsoDefSlash': 12,
        'torsoProtect': 85,
        'spd': -1,
        'accm': -3,
        'accr': -2,
        'eva': -3,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_HAUBERK={
    'desc': '''A full maille tunic with a padded gambeson for wear underneath to add shock protection. This light armour is considered the minimum level of protection for warriors on the battlefield, and typically plate armour is preferred for its superior defense. When plate armour is too heavy, impractical, or expensive, a hauberk can provide adequate defense with few drawbacks.''',
    'name': "maille hauberk",
    'type': TORSO,
    'strReq': 1,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 110,
    'value': 3990,
    'mass': 9.0,
    'stats': {
        'torsoDefStrike': 3,
        'torsoDefThrust': 6,
        'torsoDefSlash': 12,
        'torsoProtect': 101,
        'spd': -1,
        'accm': -3,
        'accr': -2,
        'eva': -3,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_IRONSCALE={
    'desc': '''Scale armour made of iron. Scale armour consists of hundreds of scales made of metal, hide or bone, assembled and strapped by lacing and rivets and sewn onto a backing. Scale armour is primitive by modern standards, but because it is cheap to produce and offers better defense against blunt trauma than maille on gambeson alone, this style of armour still sees common use.''',
    'name': "iron lamellar armour",
    'type': TORSO,
    'strReq': 3,
    'mat': (MAT_IRON,MAT_LEATHER,),
    'dur': 130,
    'value': 750,
    'mass': 11.75,
    'stats': {
        'torsoDefStrike': 5,
        'torsoDefThrust': 8,
        'torsoDefSlash': 14,
        'torsoProtect': 84,
        'spd': -4,
        'accm': -7,
        'accr': -7,
        'eva': -9,
        'mob': -2,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_HIDESCALE={
    'desc': '''Scale armour made of thick rawhide. Scale armour consists of hundreds of scales made of metal, hide or bone, assembled and strapped by lacing and rivets and sewn onto a backing. Scale armour is primitive by modern standards, but because it is cheap to produce and offers better defense against blunt trauma than maille, this style of armour still sees common use. It doesn't provide as much coverage as a shirt of maille, however, and is more encumbering, so those who can afford it typically prefer maille, and better yet, full plate.''',
    'name': "rawhide lamellar armour",
    'type': TORSO,
    'strReq': 3,
    'mat': (MAT_LEATHER),
    'dur': 95,
    'value': 1510,
    'mass': 10.25,
    'stats': {
        'torsoDefStrike': 5,
        'torsoDefThrust': 8,
        'torsoDefSlash': 10,
        'torsoProtect': 89,
        'spd': -4,
        'accm': -7,
        'accr': -7,
        'eva': -7,
        'mob': -2,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_BONESCALE={
    'desc': '''Scale armour made of carved jackhorn and other bones. Scale armour consists of hundreds of scales made of metal, hide or bone, assembled and strapped by lacing and rivets and sewn onto a backing. Scale armour is primitive by modern standards, but because it is cheap to produce and offers better defense against blunt trauma than maille, this style of armour still sees common use. It doesn't provide as much coverage as a shirt of maille, however, and is more encumbering, so those who can afford it typically prefer maille, and better yet, full plate.''',
    'name': "bone lamellar armour",
    'type': TORSO,
    'strReq': 3,
    'mat': (MAT_BONE,MAT_LEATHER,),
    'dur': 80,
    'value': 3045,
    'mass': 10.65,
    'stats': {
        'torsoDefStrike': 5,
        'torsoDefThrust': 8,
        'torsoDefSlash': 12,
        'torsoProtect': 89,
        'spd': -4,
        'accm': -7,
        'accr': -7,
        'eva': -8,
        'mob': -2,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_BRIGANDINE={
    'desc': '''Armour consisting of steel plates riveted onto a sleeveless leather jacket and worn over a gambeson. This is often the armour of choice for common soldiers who desire the greatest protection to encumberance ratio. Though it is more encumbering than maille and has less coverage, it offers far superior defense. Brigandines are generally easier to build and repair than plate armour, so they are an excellent middle ground between full plate and maille.''',
    'name': "brigandine",
    'type': TORSO,
    'strReq': 2,
    'mat': (MAT_LINEN, MAT_LEATHER, MAT_STEEL,),
    'dur': 210,
    'value': 5890,
    'mass': 11.0,
    'stats': {
        'torsoDefStrike': 5,
        'torsoDefThrust': 12,
        'torsoDefSlash': 16,
        'torsoProtect': 84,
        'spd': -2,
        'accm': -4,
        'accr': -4,
        'eva': -4,
        'mob': -1,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_PLATEDMAILLE={
    'desc': '''This shirt of maille has affixed plates of steel across the breast and ribcage areas, providing increased defense for the most vital spots. It is not as sophisticated as a proper brigandine, but it is very cost-effective as an armour for budget heavy infantry.''',
    'name': "plated maille hauberk",
    'type': TORSO,
    'strReq': 2,
    'mat': (MAT_LINEN, MAT_STEEL,),
    'dur': 120,
    'value': 4350,
    'mass': 11.5,
    'stats': {
        'torsoDefStrike': 5,
        'torsoDefThrust': 12,
        'torsoDefSlash': 20,
        'torsoProtect': 65,
        'spd': -3,
        'accm': -3,
        'accr': -3,
        'eva': -5,
        'mob': -2,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_BREASTPLATE={
    'desc': '''Part of a full suit of plate armour, but though a backplate is included, this armour has no attachments for pauldrons or faulds. A cuirass by itself still offers excellent defense, but its coverage is severely lacking compared to a modern suit of plate armour.''',
    'name': "breastplate",
    'type': TORSO,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 450,
    'value': 9890,
    'mass': 11.25,
    'stats': {
        'torsoDefStrike': 6,
        'torsoDefThrust': 16,
        'torsoDefSlash': 24,
        'torsoProtect': 74,
        'spd': -3,
        'accm': -5,
        'accr': -5,
        'eva': -5,
        'mob': -2,
        'poise': 1,
        'resHeat': -5,
        },
    }
AR_FULLPLATE={
    'desc': '''Torso plate cuirass complete with pauldrons and faulds. This is part of the standard full suit of plate armour worn by the heavy infantry of modern empires. It is painstakingly crafted of dozens of large plates of worked steel and fitted to an arming jacket for covering the chinks in the plate. It offers superior protection compared with the lesser coverage of a simple cuirass, and vastly superior defense compared with maille on gambeson. Though it restricts movement, a trained soldier can still move mostly freely even in a full suit of plate.''',
    'name': "full plate armour",
    'type': TORSO,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 360,
    'value': 25490,
    'mass': 12.5,
    'stats': {
        'torsoDefStrike': 6,
        'torsoDefThrust': 16,
        'torsoDefSlash': 24,
        'torsoProtect': 99,
        'spd': -4,
        'accm': -7,
        'accr': -7,
        'eva': -6,
        'mob': -3,
        'poise': 2,
        'resHeat': -10,
        },
    }
AR_CUIR={
    'desc': '''The cuir bouilli is a composite armour formed from various materials with tough, boiled hide plates forming the bulk; a crude arming jacket is worn underneath. On this particular piece of armour, the chest has a plate of low-carbon steel (practically iron) protecting the ribcage; the shoulders are covered in thick fur, and the upper arms protected with leather vambraces. Though the cuir bouilli offers incredible protection for the cost, it is very encumbering, difficult to repair and maintain, and does not fit as well as a genuine suit of plate armour.''',
    'name': "cuir bouilli",
    'type': TORSO,
    'strReq': 3,
    'mat': (MAT_LINEN, MAT_IRON, MAT_LEATHER, MAT_FUR),
    'dur': 70,
    'value': 3620,
    'mass': 11.0,
    'stats': {
        'torsoDefStrike': 6,
        'torsoDefThrust': 8,
        'torsoDefSlash': 13,
        'torsoProtect': 94,
        'spd': -5,
        'accm': -9,
        'accr': -9,
        'eva': -8,
        'mob': -5,
        'coldRes': 10,
        'poise': 2,
        'resCold': 5,
        'resHeat': -10,
        },
    }
AR_JOUSTINGPLATE={
    'desc': '''Thick full plate armour designed to be worn from horseback in jousting matches. The armour is extremely heavy and would surely significantly encumber an infantryman, but provides perfect protection, with rondels covering the armpit and inner elbow of the right side. It is also thicker and provides better defense than typical full plate suits.''',
    'name': "jousting plate armour",
    'type': TORSO,
    'strReq': 4,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 520,
    'value': 31490,
    'mass': 16.0,
    'stats': {
        'torsoDefStrike': 7,
        'torsoDefThrust': 18,
        'torsoDefSlash': 24,
        'torsoProtect': 105,
        'spd': -10,
        'accm': -12,
        'accr': -50,
        'eva': -26,
        'mob': -10,
        'poise': 3,
        'resHeat': -10,
        },
    }


#headpieces
AR_PADDEDCOIF={
    'desc': '''A padded coif. It barely offers any protection by itself but is inexpensive, lightweight, and does not restrict movement. Typically a padded coif is worn with a maille aventail and bascinet, but this particular coif was designed for wear by itself.''',
    'name': "padded coif",
    'type': HEAD,
    'strReq': 0,
    'mat': (MAT_LINEN,),
    'dur': 80,
    'value': 60,
    'mass': 1.5,
    'stats': {
        'headDefStrike': 3,
        'headDefThrust': 4,
        'headDefSlash': 5,
        'headProtect': 61,
        'eva': -1,
        },
    }
AR_MAILLECOIF={
    'desc': '''A padded coif with a maille hood. It offers good defense to slashes, and though it offers minimal coverage, it is light and does not restrict movement.''',
    'name': "maille coif",
    'type': HEAD,
    'strReq': 1,
    'mat': (MAT_LINEN, MAT_STEEL,),
    'dur': 120,
    'value': 1320,
    'mass': 2.5,
    'stats': {
        'headDefStrike': 2,
        'headDefThrust': 6,
        'headDefSlash': 10,
        'headProtect': 71,
        'eva': -1,
        },
    }
AR_SKULLCAP={
    'desc': '''A basic steel cap that covers the cranium, and a padded coif. It's old-fashioned and quite ineffective compared to modern great bascinets, though it is far cheaper and more durable.''',
    'name': "skull cap",
    'type': HEAD,
    'strReq': 2,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 350,
    'value': 1220,
    'mass': 2.8,
    'stats': {
        'headDefStrike': 4,
        'headDefThrust': 11,
        'headDefSlash': 20,
        'headProtect': 64,
        'eva': -3,
        'spd': -1,
        'mob': -1,
        },
    }
AR_BASCINET={
    'desc': '''A headpiece consisting of a steel plate helmet with bolted-in padding and a maille aventail for neck and shoulder protection. The face of this bascinet is mostly exposed.''',
    'name': "bascinet",
    'type': HEAD,
    'strReq': 2,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 250,
    'value': 3690,
    'mass': 3.0,
    'stats': {
        'headDefStrike': 5,
        'headDefThrust': 11,
        'headDefSlash': 24,
        'headProtect': 81,
        'eva': -3,
        'accm': -5,
        'accr': -5,
        'spd': -1,
        'mob': -1,
        },
    }
AR_BASCINET_VISORUP={
    'desc': '''A headpiece consisting of a pointed steel plate helmet with bolted-in padding and a maille aventail for neck and shoulder protection. The face can be covered with a visor, at the cost of greatly reduced vision.''',
    'name': "bascinet with visor (visor up)",
    'type': HEAD,
    'strReq': 2,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 225,
    'value': 4150,
    'mass': 3.35,
    'stats': {
        'headDefStrike': 5,
        'headDefThrust': 11,
        'headDefSlash': 24,
        'headProtect': 81,
        'eva': -5,
        'accm': -5,
        'accr': -5,
        'spd': -2,
        'mob': -2,
        },
    }
AR_BASCINET_VISORDOWN={
    'desc': '''A headpiece consisting of a pointed steel plate helmet with bolted-in padding and a maille aventail for neck and shoulder protection. The visor can be pulled up for increased vision but reduced protection.''',
    'name': "bascinet with visor (visor down)",
    'type': HEAD,
    'strReq': 2,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 225,
    'value': 4150,
    'mass': 3.35,
    'stats': {
        'headDefStrike': 5,
        'headDefThrust': 11,
        'headDefSlash': 24,
        'headProtect': 96,
        'eva': -5,
        'accm': -20,
        'accr': -33,
        'spd': -2,
        'mob': -2,
        'vision': -4,
        'resHeat': -5,
        },
    }
'''
    'use': ("transform",AR_BASCINET_VISORDOWN),
    'use': ("transform",AR_BASCINET_VISORUP),'''

AR_HELM={
    'desc': '''Old-fashioned helm with odd-styled padding and a full maille coif. The face is exposed; this helm is somewhat less effective than modern headgear in terms of coverage and speed, but it is certainly far better than nothing.''',
    'name': "helm",
    'type': HEAD,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 300,
    'value': 1850,
    'mass': 3.1,
    'stats': {
        'headDefStrike': 5,
        'headDefThrust': 13,
        'headDefSlash': 20,
        'headProtect': 73,
        'spd': -2,
        'accm': -5,
        'accr': -5,
        'eva': -6,
        'mob': -2,
        },
    }
AR_BARBUTE={
    'desc': '''A helmet that covers everything except a T-shape hole in the face for breathing and vision; this compromises protection compared to a close helm but it is much more practical for long term use in combat.''',
    'name': "helm",
    'type': HEAD,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 310,
    'value': 2850,
    'mass': 3.2,
    'stats': {
        'headDefStrike': 4,
        'headDefThrust': 8,
        'headDefSlash': 16,
        'headProtect': 93,
        'spd': -2,
        'accm': -11,
        'accr': -11,
        'eva': -8,
        'mob': -2,
        },
    }
AR_GREATHELM={
    'desc': '''An old-fashioned steel great helm worn over a special bascinet, with a padded coif for shock defense and an aventail for shoulder and neck coverage. It offers extremely good protection at the cost of heavily reduced speed and vision.''',
    'name': "great helm",
    'type': HEAD,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 270,
    'value': 3250,
    'mass': 3.65,
    'stats': {
        'headDefStrike': 5,
        'headDefThrust': 13,
        'headDefSlash': 20,
        'headProtect': 98,
        'spd': -3,
        'accm': -20,
        'accr': -33,
        'eva': -8,
        'mob': -2,
        'vision': -4,
        'resHeat': -5,
        },
    }
'''use': (transform, (AR_GREATHELM_BASCINET,ITEM_GREATHELM),),'''
AR_GREATHELM_BASCINET={
    'desc': '''A special headpiece designed to be worn with a great helm, with a padded coif for shock defense and an aventail for shoulder and neck coverage. Combine this with a great helm face to form a completed great helm.''',
    'name': "bascinet of great helm",
    'type': HEAD,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 230,
    'value': 2150,
    'mass': 3.0,
    'stats': {
        'headDefStrike': 5,
        'headDefThrust': 11,
        'headDefSlash': 20,
        'headProtect': 76,
        'spd': -1,
        'accm': -5,
        'accr': -5,
        'eva': -5,
        'mob': -1,
        },
    }
AR_BATTLEHELM={
    'desc': '''A fully enclosed helmet with dozens of tiny slits for seeing through. It grants truly exceptional coverage but is encumbering, and greatly restrictive in vision and movement.''',
    'name': "battle helm",
    'type': HEAD,
    'strReq': 4,
    'mat': (MAT_LEATHER,MAT_STEEL,),
    'dur': 350,
    'value': 3885,
    'mass': 3.5,
    'stats': {
        'headDefStrike': 6,
        'headDefThrust': 14,
        'headDefSlash': 20,
        'headProtect': 106,
        'spd': -3,
        'accm': -25,
        'accr': -40,
        'eva': -10,
        'mob': -3,
        'vision': -6,
        'resHeat': -5,
        },
    }
AR_BEARDEDHELM={
    'desc': '''An old-fashioned Viking-style helm with a glorious beard of maille covering most of the face.''',
    'name': "bearded helm",
    'type': HEAD,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 360,
    'value': 5650,
    'mass': 3.6,
    'stats': {
        'headDefStrike': 4,
        'headDefThrust': 10,
        'headDefSlash': 16,
        'headProtect': 87,
        'spd': -2,
        'accm': -15,
        'accr': -15,
        'eva': -8,
        'mob': -2,
        'vision': -2,
        'resHeat': -5,
        },
    }
AR_CONICALHELM={
    'desc': '''Conical-shaped helms deflect incoming strikes well, but are encumbering due to their size. The face on this helm is mostly exposed.''',
    'name': "conical helm",
    'type': HEAD,
    'strReq': 3,
    'mat': (MAT_LINEN,MAT_IRON,),
    'dur': 380,
    'value': 2580,
    'mass': 3.25,
    'stats': {
        'headDefStrike': 6,
        'headDefThrust': 11,
        'headDefSlash': 20,
        'headProtect': 80,
        'spd': -3,
        'accm': -5,
        'accr': -5,
        'eva': -8,
        'mob': -3,
        },
    }


#leggings
AR_PADDEDLEGGINGS={
    'desc': '''n/a''',
    'name': "padded hosen",
    'type': LEGS,
    'strReq': 1,
    'mat': (MAT_LINEN,),
    'dur': 80,
    'value': 255,
    'mass': 2.0,
    'stats': {
        'legsDefStrike': 4,
        'legsDefThrust': 4,
        'legsDefSlash': 5,
        'legsProtect': 110,
        'spd': -2,
        'eva': -5,
        'mob': -1,
        'resCold': 5,
        'resHeat': -5,
        },
    }
AR_MAILLELEGGINGS={
    'desc': '''n/a''',
    'name': "maille chausses",
    'type': LEGS,
    'strReq': 2,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 120,
    'value': 2950,
    'mass': 2.75,
    'stats': {
        'legsDefStrike': 3,
        'legsDefThrust': 8,
        'legsDefSlash': 10,
        'legsProtect': 104,
        'spd': -3,
        'eva': -5,
        'mob': -1,
        'resHeat': -5,
        },
    }
AR_SPLINTLEGGINGS={
    'desc': '''Splint armour consists of plates of steel riveted onto a padded backing. It is popular for wear on the limbs, due to its lack of restriction of movement compared to full plate, though it is generally worn in addition to plate.''',
    'name': "splint chausses",
    'type': LEGS,
    'strReq': 2,
    'mat': (MAT_LINEN,MAT_STEEL,),
    'dur': 160,
    'value': 3550,
    'mass': 3.25,
    'stats': {
        'legsDefStrike': 5,
        'legsDefThrust': 6,
        'legsDefSlash': 16,
        'legsProtect': 94,
        'spd': -4,
        'eva': -7,
        'mob': -2,
        'poise': 1,
        'resHeat': -3,
        },
    }
AR_CUISSES={
    'desc': '''Thigh chuisses and steel plate greaves over splint armour leggings, complete with a knee-plate and combat boots; this is part of a full suit of plate armour. It offers the best protection for the legs that modern technology can produce, but it restricts movement.''',
    'name': "chuisses",
    'type': LEGS,
    'strReq': 3,
    'mat': (MAT_STEEL, MAT_LINEN,),
    'dur': 380,
    'value': 8850,
    'mass': 4.65,
    'stats': {
        'legsDefStrike': 6,
        'legsDefThrust': 14,
        'legsDefSlash': 20,
        'legsProtect': 99,
        'spd': -5,
        'eva': -10,
        'mob': -3,
        'poise': 2,
        'resHeat': -6,
        },
    }
AR_GREAVES={
    'desc': '''Steel plate greaves, complete with a knee-plate and combat boots. Protecting only the shins and knees, greaves are often worn in modern times with thigh armour to protect the upper legs and groin. Compared to full leg armour, simply greaves by themselves are less encumbering, but offer far less protection.''',
    'name': "greaves",
    'type': LEGS,
    'strReq': 3,
    'mat': (MAT_STEEL, MAT_LINEN,),
    'dur': 350,
    'value': 3850,
    'mass': 2.5,
    'stats': {
        'legsDefStrike': 6,
        'legsDefThrust': 14,
        'legsDefSlash': 20,
        'legsProtect': 72,
        'spd': -3,
        'eva': -5,
        'mob': -1,
        'poise': 1,
        'resHeat': -3,
        },
    }


#arm armour
AR_LEATHERGLOVES={
    'desc': '''A pair of thick leather work gloves, adopted for use in combat.''',
    'name': "leather gloves",
    'type': ARMS,
    'strReq': 0,
    'mat': (MAT_LEATHER,),
    'dur': 60,
    'value': 20,
    'mass': 0.25,
    'stats': {
        'armsDefStrike': 2,
        'armsDefThrust': 2,
        'armsDefSlash': 3,
        'armsProtect': 65,
        'accm': -3,
        'accr': 2,
        },
    }
AR_BRACER={
    'desc': '''An archer's bracer for use with a war bow. The bracer's design offers virtually no protection but improves the archer's accuracy.''',
    'name': "bracer",
    'type': ARMS,
    'strReq': 1,
    'mat': (MAT_LEATHER,),
    'dur': 80,
    'value': 50,
    'mass': 0.2,
    'stats': {
        'armsDefStrike': 2,
        'armsDefThrust': 4,
        'armsDefSlash': 6,
        'armsProtect': 42,
        'accm': -10,
        'accr': 8,
        },
    }
AR_SPLINTVAMBRACES={
    'desc': '''Splint armour consists of plates of steel riveted onto a padded backing. It is popular for wear on the limbs, due to its lack of restriction of movement compared to full plate, though it is generally worn in addition to plate.''',
    'name': "splint vambraces",
    'type': ARMS,
    'strReq': 1,
    'mat': (MAT_LINEN, MAT_STEEL,),
    'dur': 120,
    'value': 1875,
    'mass': 0.95,
    'stats': {
        'armsDefStrike': 4,
        'armsDefThrust': 6,
        'armsDefSlash': 11,
        'armsProtect': 68,
        'accm': -5,
        'accr': -5,
        },
    }
AR_DEMIGAUNTS={
    'desc': '''Demigaunts, or half-gaunts, are leather gloves with fixed plate armour on only key areas, providing an excellent mix of protection and light-weight design. Those who desire protection with less restriction of movement enjoy this style of gaunt, but soldiers will rarely go into battle with half-gaunts if they can afford full plate.''',
    'name': "demigaunts",
    'type': ARMS,
    'strReq': 1,
    'mat': (MAT_LEATHER, MAT_STEEL,),
    'dur': 200,
    'value': 1950,
    'mass': 0.8,
    'stats': {
        'armsDefStrike': 4,
        'armsDefThrust': 6,
        'armsDefSlash': 12,
        'armsProtect': 64,
        'accm': -5,
        'accr': -5,
        'spd': -1,
        },
    }
AR_GAUNTLETS={
    'desc': '''A pair of steel gauntlets for protecting the hands and wrists. Typically this is worn along with a full suit of plate armour; gauntlets by themselves do not offer very good protection.''',
    'name': "gauntlets",
    'type': ARMS,
    'strReq': 2,
    'mat': (MAT_STEEL, MAT_LEATHER,),
    'dur': 250,
    'value': 2450,
    'mass': 1.25,
    'stats': {
        'armsDefStrike': 5,
        'armsDefThrust': 7,
        'armsDefSlash': 14,
        'armsProtect': 75,
        'accm': -5,
        'accr': -5,
        'spd': -2,
        },
    }
AR_VAMBRACES={
    'desc': '''A pair of steel gauntlets with vambraces of steel splint armour, typically worn as part of a full suit of plate armour. This style of arm wear offers great protection.''',
    'name': "gauntlets with vambraces",
    'type': ARMS,
    'strReq': 2,
    'mat': (MAT_STEEL, MAT_LEATHER,),
    'dur': 250,
    'value': 3950,
    'mass': 2.1,
    'stats': {
        'armsDefStrike': 5,
        'armsDefThrust': 10,
        'armsDefSlash': 14,
        'armsProtect': 96,
        'accm': -5,
        'accr': -8,
        'spd': -2,
        },
    }









#---------#
# Weapons #
#---------#


#pikes
WP_PIKE={
    'desc': '''The pike is the weapon with the greatest reach of all melee weapons; though it is rather useless at typical fighting distances, at longer range it can devastate foes with rapid thrusts that cannot be retaliated.''',
    'name': "pike",
    'type': HAND1,
    'school': PIKES,
    'hands': "2",
    'strReq': 6,
    'dexReq': 2,
    'mat': (MAT_STEEL, MAT_WOOD,),
    'dur': 95,
    'value': 265,
    'mass': 5.25,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': -5,
        'hand1Strike': 3,
        'hand1Thrust': 12,
        'hand1Slash': 0,
        'hand1Stagger': 4,
        'hand1ReachMin': 4,
        'hand1ReachMax': 5,
        'hand1Grip': 60,
        'mob': -14,
        'spd': -12,
        'accm': -9,
        'eva': -25,
        'parry': 6,
        'parryAlly': 6,
        'counter': 5,
        'hitAdjFoe': 33,
        },
    }


#bombs
WP_HANDBOMB={
    'desc': '''This hand-held canister contains a mixture of chemicals including gunpowder, designed to mix upon impact and explode, causing blindness. Concussions can occur if the explosion occurs near the head.''',
    'name': "handbomb",
    'type': HAND1,
    'school': BOMBS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_GUNPOWDER, MAT_LEAD,),
    'dur': 1,
    'value': 25,
    'mass': 0.25,
    'damageScaling': {
        },
    'stats': {
        'hand1Grip': 50,
        'throwAtks': 2,
        'throwAtkp': 0,
        'throwRangeMin': 3,
        'throwRangeMax': 15,
        'acct': 10,
        },
    'effect': {
        #bomb explosion effect
        }
    }


#greatswords
WP_ZWEIHANDER={
    'desc': '''n/a''',
    'name': "zweihander",
    'type': HAND1,
    'school': GREATSWORDS,
    'hands': "2",
    'strReq': 6,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 165,
    'value': 1250,
    'mass': 2.6,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': 7,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Strike': 6,
        'hand1Thrust': 9,
        'hand1Slash': 14,
        'hand1DefStrike': 6,
        'hand1DefThrust': 12,
        'hand1DefSlash': 24,
        'hand1Guard': 15,
        'hand1Grip': 90,
        'hand1Stagger': 4,
        'dismember': 3,
        'mob': -7,
        'spd': -5,
        'accm': 5,
        'eva': -8,
        'parry': 10,
        'parryAlly': 10,
        'counter': 9,
        'hitAdjFoe': 33,
        'ignoreParry': 9,
        'ignoreBlock': 9,
        },
    }
WP_KRIEGSMESSER={
    'desc': '''This massive, single-bladed slashing weapon is wielded with two hands. Known as a peasant weapon, messers are rarely found on the battlefield. This particular sword, however, is indeed a weapon of war, designed for chopping through peasants rather than being wielded by one. Its large curved edge delivers a devastating blow that absolutely destroys unarmoured foes.''',
    'name': "kriegsmesser",
    'type': HAND1,
    'school': GREATSWORDS,
    'hands': "2",
    'strReq': 7,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 225,
    'value': 960,
    'mass': 2.8,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': 3,
        'hand1Strike': 3,
        'hand1Thrust': 4,
        'hand1Slash': 21,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 60,
        'hand1DefStrike': 4,
        'hand1DefThrust': 16,
        'hand1Guard': 9,
        'dismember': 15,
        'mob': -6,
        'spd': -12,
        'accm': -5,
        'eva': -5,
        'parry': 5,
        'counter': 5,
        'hitAdjFoe': 33,
        'ignoreParry': 8,
        },
    }
WP_EXECUTIONERSWORD={
    'desc': '''This hand-held guillotine is designed for use by an executioner for decapitation, and is not made for battle. It is capable of extreme power and damage, but it is extremely unwieldy and not suited for combat. The executioner's sword has the advantage of being more accurate compared to an axe, and is more likely to successfully decapitate criminals.''',
    'name': "executioner's sword",
    'type': HAND1,
    'school': GREATSWORDS,
    'hands': "2",
    'strReq': 9,
    'dexReq': 3,
    'mat': (MAT_IRON,),
    'dur': 80,
    'value': 805,
    'mass': 4.7,
    'damageScaling': {
        STRENGTH : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': -31,
        'hand1Strike': 18,
        'hand1Thrust': 0,
        'hand1Slash': 26,
        'hand1Stagger': 4,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 35,
        'dismember': 44,
        'mob': -13,
        'spd': -42,
        'accm': -15,
        'eva': -15,
        'hitAdjFoe': 50,
        'ignoreBlock': 5,
        'ignoreParry': 15,
        },
    }
WP_ODACHI={
    'desc': '''The odachi, or no-dachi, is a Japanese sword with a very long, curved blade. It is designed to strike fear into the hearts of their foes; it also excels in mowing down unarmoured peasants.''',
    'name': "odachi",
    'type': HAND1,
    'school': GREATSWORDS,
    'hands': "2",
    'strReq': 6,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 70,
    'value': 1575,
    'mass': 2.9,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': -4,
        'hand1Strike': 2,
        'hand1Thrust': 4,
        'hand1Slash': 17,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 75,
        'dismember': 15,
        'mob': -8,
        'spd': -17,
        'accm': 8,
        'eva': -5,
        'hitAdjFoe': 33,
        'ignoreParry': 6,
        },
    }
WP_KAMIGATANA={
    'desc': '''The kamigatana or "sword of the gods" is an infamous style of sword resembling a very long katana, with a blade length of approximately 4m. Feared more greatly than any other sword, this weapon is quite unwieldy but absolutely devastating when mowing down unarmoured peasants. Still, it is not made for use in battle, especially against armoured foes. Legends tell of warriors who fought off armies with the use of such massive swords, believed to be enchanted with the divine grace of their gods; but these are just legends.''',
    'name': "kamigatana",
    'type': HAND1,
    'school': GREATSWORDS,
    'hands': "2",
    'strReq': 7,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 55,
    'value': 8090,
    'mass': 3.5,
    'damageScaling': {
        STRENGTH : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': -25,
        'hand1Strike': 3,
        'hand1Thrust': 2,
        'hand1Slash': 19,
        'hand1Stagger': 4,
        'hand1ReachMin': 2,
        'hand1ReachMax': 4,
        'hand1Grip': 70,
        'dismember': 10,
        'mob': -10,
        'spd': -25,
        'accm': 5,
        'eva': -5,
        'hitAdjFoe': 33,
        'ignoreParry': 11,
        },
    }


#staves
WP_BOSTAFF={
    'desc': '''n/a''',
    'name': "bo staff",
    'type': HAND1,
    'school': STAVES,
    'hands': "2",
    'strReq': 3,
    'dexReq': 3,
    'mat': (MAT_WOOD,),
    'dur': 200,
    'value': 50,
    'mass': 1.5,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 3,
        'hand1Strike': 8,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 5,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 75,
        'hand1DefStrike': 8,
        'hand1DefThrust': 16,
        'hand1Guard': 40,
        'mob': -5,
        'spd': 9,
        'accm': 8,
        'eva': -2,
        'parry': 15,
        'counter': 12,
        'push': 7,
        'disarm': 12,
        'atkBalance': 1,
        'foeBalance': -2,
        },
    }




#longswords
WP_KATANA={
    'desc': '''A two-handed sword of Eastern origin, with a slightly curved blade designed to be excellent at cutting; its signature drawing slash is extremely powerful against unarmoured foes.''',
    'name': "katana",
    'type': HAND1,
    'school': LONGSWORDS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 120,
    'value': 1150,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 7,
        'hand1Strike': 1,
        'hand1Thrust': 5,
        'hand1Slash': 17,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 4,
        'hand1DefThrust': 16,
        'hand1Guard': 16,
        'dismember': 5,
        'mob': -3,
        'spd': 3,
        'accm': 12,
        'eva': 10,
        'parry': 9,
        'counter': 9,
        'hitAdjFoe': 7,
        },
    }
WP_TWOHANDEDSWORD={
    'desc': '''The European longsword is one of the most sophisticated of modern bladed weapons, maximizing many of the best qualities of swords while minimizing the drawbacks. This versatile sword is effective in cutting, thrusting, bludgeoning, and parrying, as well as being effective in finding weak spots in armour.''',
    'name': "two-handed sword",
    'type': HAND1,
    'school': LONGSWORDS,
    'hands': "2", 
    'strReq': 4,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 230,
    'value': 890,
    'mass': 1.6,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 18,
        'hand1Strike': 4,
        'hand1Thrust': 9,
        'hand1Slash': 12,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 6,
        'hand1DefThrust': 16,
        'hand1Guard': 35,
        'mob': -3,
        'spd': 6,
        'accm': 10,
        'eva': 6, #all swords should give some Eva
        'parry': 16,
        'parryAlly': 5,
        'counter': 4,
        },
    }
WP_BASTARDSWORD={
    'desc': '''The bastard sword is like a cross between a short sword and a longsword, that can be wielded effectively with 1 or 2 hands, hence its name. It is a very versatile weapon and the choice sword of many knights and fighters.''',
    'name': "bastard sword",
    'type': HAND1,
    'school': LONGSWORDS,
    'hands': "1/2",
    'strReq': 3,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 280,
    'value': 745,
    'mass': 1.8,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 14,
        'hand1Strike': 2,
        'hand1Thrust': 7,
        'hand1Slash': 11,
        'hand1Stagger': 2,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 85,
        'hand1DefStrike': 1,
        'hand1DefThrust': 16,
        'hand1Guard': 9,
        'dismember': 1,
        'mob': -3,
        'spd': -5,
        'accm': 4,
        'eva': 6,
        'parry': 9,
        'counter': 3,
        },
    }
WP_ESTOC={
    'desc': '''The estoc is a tapered longsword that is designed largely around one function: thrusting, at which it excels beautifully. It can be wielded in one or two hands, and remains quite versatile despite its specialized purpose.''',
    'name': "estoc",
    'type': HAND1,
    'school': LONGSWORDS,
    'hands': "1/2",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 90,
    'value': 1490,
    'mass': 1.6,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 26,
        'hand1Strike': 0,
        'hand1Thrust': 10,
        'hand1Slash': 5,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 85,
        'hand1DefStrike': 0,
        'hand1DefThrust': 16,
        'hand1Guard': 7,
        'mob': -2,
        'spd': 2,
        'accm': 10,
        'eva': 7,
        'parry': 11,
        'counter': 6,
        'hitAdjFoe': 7,
        },
    }
WP_WARSWORD={
    'desc': '''This longsword is longer than most, and wider and thicker, too, which facilitates increased striking power at the cost of some versatility.''',
    'name': "war sword",
    'type': HAND1,
    'school': LONGSWORDS,
    'hands': "2", 
    'strReq': 5,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 240,
    'value': 1250,
    'mass': 1.85,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 5,
        'hand1Strike': 6,
        'hand1Thrust': 6,
        'hand1Slash': 15,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 90,
        'hand1DefStrike': 7,
        'hand1DefThrust': 16,
        'hand1Guard': 25,
        'mob': -5,
        'spd': 3,
        'accm': 13,
        'eva': 4, 
        'parry': 12,
        'parryAlly': 7,
        'counter': 5,
        },
    }



#rapiers
#MAYBE RAPIERS SHOULD JUST NOT BE IN THE GAME AT ALL.
WP_RAPIER={
    'desc': '''Rapiers are one-handed thrusting swords designed to maximize the thrust damage; it is bottom-heavy to allow very swift movements and effective parrying. It is designed for use in duels against unarmoured opponents where its speed and defensive capabilities give a huge advantage.''',
    'name': "rapier",
    'type': HAND1,
    'school': RAPIERS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 5,
    'mat': (MAT_STEEL,),
    'dur': 120,
    'value': 1150,
    'mass': 1.2,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 15,
        'hand1Strike': 0,
        'hand1Thrust': 9,
        'hand1Slash': 2,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 10,
        'mob': -2,
        'spd': 13,
        'accm': 12,
        'eva': 6,
        'parry': 22,
        'counter': 13,
        'stickInTarget': 6,
        },
    }
WP_SMALLSWORD={
    'desc': '''A long, thin rapier-like sword with an extreme taper towards the tip, making the blade flimsy but excellent at thrusting. It is a side-arm and not intended for use in battle against armed warriors.''',
    'name': "smallsword",
    'type': HAND1,
    'school': RAPIERS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 5,
    'mat': (MAT_STEEL,),
    'dur': 65,
    'value': 820,
    'mass': 0.9,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 16,
        'hand1Strike': 0,
        'hand1Thrust': 7,
        'hand1Slash': 1,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 1,
        'hand1DefThrust': 8,
        'hand1Guard': 5,
        'mob': -2,
        'spd': 15,
        'accm': 15,
        'eva': 7,
        'parry': 14,
        'counter': 12,
        'stickInTarget': 3,
        },
    }
WP_BROADSWORD={
    'desc': '''A rapier-like sword with a "basket-hilt" that provides excellent protection for the hand; it absolutely excels in parry and riposte, but like other rapiers its damage potential against armoured foes is limited. Compared to a standard rapier, this sword has a thicker blade, hence its name; this results in greater damage output, and the protective hilt also consists of a small hook for leveraging away enemy's shields while fighting in close quarters.''',
    'name': "basket-hilt broadsword",
    'type': HAND1,
    'school': RAPIERS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 5,
    'mat': (MAT_STEEL,),
    'dur': 100,
    'value': 1280,
    'mass': 1.4,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 18,
        'hand1Strike': 1,
        'hand1Thrust': 9,
        'hand1Slash': 11,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 105,
        'hand1DefStrike': 2,
        'hand1DefThrust': 12,
        'hand1Guard': 10,
        'mob': -4,
        'accm': 10,
        'eva': 5,
        'spd': 10,
        'parry': 30,
        'counter': 15,
        'ignoreBlock': 13,
        'stickInTarget': 5,
        },
    }


#curved swords
WP_SCIMITAR={
    'desc': '''This exotic curved sword is very effective for slashing.''',
    'name': "scimitar",
    'type': HAND1,
    'school': CURVEDSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 5,
    'mat': (MAT_STEEL,),
    'dur': 110,
    'value': 645,
    'mass': 1.2,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 6,
        'hand1Strike': 0,
        'hand1Thrust': 4,
        'hand1Slash': 15,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 90,
        'hand1DefStrike': 4,
        'hand1DefThrust': 16,
        'hand1Guard': 9,
        'mob': -2,
        'accm': 5,
        'spd': 7,
        'eva': 7,
        'parry': 9,
        'counter': 9,
        'ignoreBlock': 16,
        },
    }
WP_SBLADE={
    'desc': '''This blade was forged in faraway lands, for purposes of skirmishing against lightly armoured, but well-shielded, opponents. It's exotic S-like shape makes it very effective for getting around shields, though it suffers slightly in damage and durability.''',
    'name': "s-blade",
    'type': HAND1,
    'school': CURVEDSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 7,
    'mat': (MAT_STEEL,),
    'dur': 80,
    'value': 780,
    'mass': 1.15,
    'damageScaling': {
        STRENGTH : SCALING_E,
        DEXTERITY : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': 5,
        'hand1Strike': 0,
        'hand1Thrust': 5,
        'hand1Slash': 11,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 1,
        'hand1DefThrust': 8,
        'hand1Guard': 4,
        'mob': -2,
        'accm': 5,
        'eva': 4,
        'spd': 5,
        'parry': 11,
        'counter': 12,
        'ignoreBlock': 24,
        },
    }
WP_SABRE={
    'desc': '''A curved sword for slashing, with a crescent-moon guard down to the pommel for shielding the wielder's hand during sword-on-sword combat. The side-arm of choice for many skirmishers and pirates.''',
    'name': "sabre",
    'type': HAND1,
    'school': CURVEDSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 5,
    'mat': (MAT_STEEL,),
    'dur': 115,
    'value': 640,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 9,
        'hand1Strike': 0,
        'hand1Thrust': 6,
        'hand1Slash': 14,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 4,
        'hand1DefThrust': 12,
        'hand1Guard': 15,
        'mob': -2,
        'accm': 5,
        'eva': 7,
        'spd': 8,
        'parry': 24,
        'counter': 15,
        'ignoreBlock': 12,
        },
    }
WP_SHAMSHIR={
    'desc': '''n/a''',
    'name': "shamshir",
    'type': HAND1,
    'school': CURVEDSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 6,
    'mat': (MAT_STEEL, MAT_BONE,),
    'dur': 100,
    'value': 1105,
    'mass': 1.1,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 7,
        'hand1Strike': 0,
        'hand1Thrust': 5,
        'hand1Slash': 12,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 90,
        'hand1DefStrike': 2,
        'hand1DefThrust': 16,
        'hand1Guard': 13,
        'mob': -2,
        'accm': 3,
        'eva': 7,
        'spd': 12,
        'parry': 16,
        'counter': 13,
        'ignoreBlock': 10,
        },
    }



#short swords
WP_GLADIUS={
    'desc': '''Similar in design to the favored sword of the Roman legionary (hence the name), this swift blade is ideal for parrying and for fighting lightly armoured foes. This style of sword has long since fallen out of popularity and it is uncommon to find in this day and age.''',
    'name': "gladius",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 1,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 170,
    'value': 310,
    'mass': 0.8,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 17,
        'hand1Strike': 0,
        'hand1Thrust': 8,
        'hand1Slash': 5,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'mob': -1,
        'accm': 18,
        'eva': 6,
        'spd': 9,
        'parry': 15,
        'counter': 7,
        'ignoreBlock': 22,
        },
    }
WP_BRONZESWORD={
    'desc': '''Bronze swords are cheap and old-fashioned, from a time in which iron was rare. Nowadays almost nobody uses bronze weapons, though because they are cheap, some still find uses for them.''',
    'name': "bronze sword",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 3,
    'mat': (MAT_BRONZE,),
    'dur': 60,
    'value': 36,
    'mass': 1.0,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 18,
        'hand1Strike': 1,
        'hand1Thrust': 6,
        'hand1Slash': 7,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 9,
        'mob': -2,
        'accm': 14,
        'eva': 8,
        'spd': 6,
        'parry': 19,
        'counter': 7,
        'ignoreBlock': 12,
        },
    }
WP_IRONSWORD={
    'desc': '''This cheap sword is forged of a low-quality steel that is basically just iron. Being made of inferior material, it will never stand up to modern steels in terms of performance, but low-carbon steel is much cheaper to produce, making them a popular choice when higher quality materials are unavailable.''',
    'name': "iron sword",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 3,
    'mat': (MAT_IRON,),
    'dur': 110,
    'value': 85,
    'mass': 1.2,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 18,
        'hand1Strike': 2,
        'hand1Thrust': 7,
        'hand1Slash': 9,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 8,
        'mob': -2,
        'accm': 10,
        'eva': 6,
        'spd': 5,
        'parry': 13,
        'counter': 10,
        'ignoreBlock': 4,
        },
    }
WP_CELTICSWORD={
    'desc': '''This ancient sword was forged long ago in the north; it has seen many moons and many battles.''',
    'name': "Ancient Celtic sword",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON,),
    'dur': 70,
    'value': 300,
    'mass': 1.45,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': 7,
        'hand1Strike': 5,
        'hand1Thrust': 5,
        'hand1Slash': 11,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 3,
        'hand1DefThrust': 8,
        'hand1Guard': 12,
        'mob': -2,
        'accm': 7,
        'eva': 6,
        'spd': 4,
        'parry': 13,
        'counter': 9,
        'ignoreBlock': 8,
        },
    }
WP_ARMINGSWORD={
    'desc': '''This medium-length, double-bladed tapered sword is the side-arm of choice for many knights. It is very effective for parry and riposte, and can easily slip between the chinks in plate armour.''',
    'name': "arming sword",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 145,
    'value': 680,
    'mass': 1.15,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 15,
        'hand1Strike': 2,
        'hand1Thrust': 8,
        'hand1Slash': 10,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 100,
        'hand1DefStrike': 3,
        'hand1DefThrust': 16,
        'hand1Guard': 10,
        'mob': -2,
        'accm': 12,
        'eva': 7,
        'spd': 7,
        'parry': 19,
        'counter': 12,
        'ignoreBlock': 6,
        },
    }
WP_FALCHION={
    'desc': '''This sword's blade widens toward the tip, facilitating a devastating chopping strike like that of an axe. Though it is more swift and accurate than axes, it is not as powerful.''',
    'name': "falchion",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 280,
    'value': 495,
    'mass': 1.35,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 2,
        'hand1Strike': 6,
        'hand1Thrust': 3,
        'hand1Slash': 13,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 80,
        'hand1DefStrike': 2,
        'hand1DefThrust': 12,
        'hand1Guard': 10,
        'mob': -2,
        'accm': 12,
        'eva': 4,
        'spd': 4,
        'parry': 11,
        'counter': 3,
        'ignoreBlock': 13,
        },
    }
WP_KOPIS={
    'desc': '''The versatile "axe-sword" which is slightly faster and better for parrying than an axe, and can get around shields too, but it delivers a weaker blow than axes do. Still it packs a powerful impact compared to most other short swords.''',
    'name': "kopis",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 250,
    'value': 745,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': -4,
        'hand1Strike': 7,
        'hand1Thrust': 0,
        'hand1Slash': 9,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 2,
        'hand1DefThrust': 6,
        'hand1Guard': 7,
        'mob': -2,
        'accm': 9,
        'eva': 3,
        'spd': 3,
        'parry': 7,
        'counter': 3,
        'destroy': 1,
        'ignoreBlock': 23,
        },
    }


#hammers
WP_WARHAMMER={
    'desc': '''A one-handed weapon of war, designed to be versatile; however, where it excels is in close quarters combat against armoured foes. Because it lacks defensive capabilities, as with axes, users of war hammers are almost always seen wielding a shield in the offhand.''',
    'name': "warhammer",
    'type': HAND1,
    'school': HAMMERS,
    'hands': "1",
    'strReq': 4,
    'dexReq': 3,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 520,
    'value': 90,
    'mass': 1.25,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -3,
        'hand1Strike': 10,
        'hand1Thrust': 3,
        'hand1Slash': 1,
        'hand1Stagger': 4,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 2,
        'hand1DefThrust': 4,
        'hand1Guard': 5,
        'mob': -4,
        'spd': -12,
        'accm': -11,
        'eva': -5,
        'parry': 6,
        'hitAdjFoe': 7,
        'destroy': 33,
        'push': 3,
        'ignoreBlock': 5,
        },
    }
WP_STEELWARHAMMER={
    'desc': '''A warhammer of pure steel. Virtually unbreakable, this anti-armour weapon delivers a devastating concussive blow.''',
    'name': "steel warhammer",
    'type': HAND1,
    'school': HAMMERS,
    'hands': "1",
    'strReq': 4,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 1350,
    'value': 230,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -3,
        'hand1Strike': 10,
        'hand1Thrust': 3,
        'hand1Slash': 1,
        'hand1Stagger': 4,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 65,
        'hand1DefStrike': 2,
        'hand1DefThrust': 4,
        'hand1Guard': 5,
        'mob': -4,
        'spd': -13,
        'accm': -11,
        'eva': -6,
        'parry': 6,
        'hitAdjFoe': 7,
        'destroy': 33,
        'push': 3,
        'ignoreBlock': 6,
        },
    }


#clubs
WP_CLUB={
    'desc': '''Perhaps the most basic of manmade weapons, the simple wooden club is still a very powerful force to be reckoned with; however, it is rather obselete by the invention of steel maces. This club can be wielded in one or two hands.''',
    'name': "club",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 2,
    'mat': (MAT_WOOD,),
    'dur': 675,
    'value': 2,
    'mass': 1.7,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -26,
        'hand1Strike': 9,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 50,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 1,
        'mob': -6,
        'spd': -29,
        'accm': -10,
        'eva': -11,
        'hitAdjFoe': 6,
        'destroy': 3,
        'push': 6,
        'aimForHead': 5,
        },
    }
WP_SPIKEDCLUB={
    'desc': '''This bat with nails can be wielded in one or two hands. Essentially a poor man's mace, this brutish weapon causes horrific wounds.''',
    'name': "spiked club",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 305,
    'value': 6,
    'mass': 1.75,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -18,
        'hand1Strike': 11,
        'hand1Thrust': 0,
        'hand1Slash': 1,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 50,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': -1,
        'mob': -7,
        'spd': -32,
        'accm': -12,
        'eva': -13,
        'hitAdjFoe': 3,
        'destroy': 8,
        'push': 8,
        'aimForHead': 5,
        },
    }
WP_IRONMACE={
    'desc': '''A braze-welded iron war mace. Its forward-heavy design along with its elegant flanged warhead make it pack a powerful punch despite being quite lightweight. It is very durable, being made almost entirely of pure iron.''',
    'name': "iron mace",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1",
    'strReq': 4,
    'dexReq': 1,
    'mat': (MAT_IRON,),
    'dur': 950,
    'value': 50,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -23,
        'hand1Strike': 11,
        'hand1Thrust': 0,
        'hand1Slash': 2,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 90,
        'hand1DefStrike': 2,
        'hand1DefThrust': 6,
        'hand1Guard': 5,
        'mob': -4,
        'spd': -15,
        'accm': -5,
        'eva': -4,
        'hitAdjFoe': 6,
        'destroy': 12,
        'push': 3,
        'aimForHead': 5,
        },
    }
WP_STEELMACE={
    'desc': '''A forge-welded war mace of pure low-carbon steel. It is virtually indestructible, and delivers a devastingly powerful blow against armoured foes.''',
    'name': "steel mace",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1",
    'strReq': 4,
    'dexReq': 1,
    'mat': (MAT_STEEL,),
    'dur': 1550,
    'value': 180,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -23,
        'hand1Strike': 11,
        'hand1Thrust': 0,
        'hand1Slash': 2,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 90,
        'hand1DefStrike': 2,
        'hand1DefThrust': 6,
        'hand1Guard': 5,
        'mob': -4,
        'spd': -15,
        'accm': -5,
        'eva': -4,
        'hitAdjFoe': 6,
        'destroy': 16,
        'push': 4,
        'aimForHead': 5,
        },
    }
WP_MORNINGSTAR={
    'desc': '''A dreadfully spiked warhead atop a shaft of pure steel. This weapon delivers a devastating blow to amoured and unarmoured foes alike.''',
    'name': "morning star",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 580,
    'value': 245,
    'mass': 1.85,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -27,
        'hand1Strike': 14,
        'hand1Thrust': 0,
        'hand1Slash': 2,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 75,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 1,
        'mob': -6,
        'spd': -18,
        'accm': -7,
        'eva': -8,
        'hitAdjFoe': 8,
        'destroy': 16,
        'push': 6,
        'aimForHead': 5,
        },
    }
WP_FLAIL={ #should this have its own weap. school?
    'desc': '''The flail is a mace with a short chain connecting the warhead to the handle. The chain allows additional centripetal force to deliver massive shock damage, though it makes the weapon severely lack speed and defensive capabilities. Despite its power, their extreme and numerous drawbacks make flails not very popular.''',
    'name': "flail",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1",
    'strReq': 6,
    'dexReq': 7,
    'mat': (MAT_WOOD, MAT_LEAD,),
    'dur': 320,
    'value': 260,
    'mass': 1.5,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': -33,
        'hand1Strike': 15,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 4,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 50,
        'mob': -7,
        'spd': -28,
        'accm': -26,
        'eva': -14,
        'hitAdjFoe': 20,
        'destroy': 15,
        'push': 10,
        },
    }
WP_MAUL={
    'desc': '''An improvised weapon made from a stake-driving hammer, this hammer packs an absurdly forceful blow, but is quite unwieldy. It can be wielded in either one or two hands. Despite technically being a hammer, it has little in common with modern warhammers, instead being used more like a club or mace for raw destructive power.''',
    'name': "militia's maul",
    'type': HAND1,
    'school': CLUBS,
    'hands': "1/2",
    'strReq': 5,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 690,
    'value': 20,
    'mass': 2.45,
    'damageScaling': {
        STRENGTH : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': -41,
        'hand1Strike': 17,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 2,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 60,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': -4,
        'mob': -7,
        'spd': -45,
        'accm': -12,
        'eva': -12,
        'hitAdjFoe': 10,
        'destroy': 5,
        'push': 12,
        },
    }


#axes
WP_WARAXE={
    'desc': '''n/a''',
    'name': "war axe",
    'type': HAND1,
    'school': AXES,
    'hands': "1",
    'strReq': 4,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_STEEL),
    'dur': 580,
    'value': 45,
    'mass': 1.25,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': -9,
        'hand1Strike': 9,
        'hand1Thrust': 3,
        'hand1Slash': 7,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 80,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 5,
        'mob': -2,
        'spd': -13,
        'accm': -15,
        'acct': -20,
        'eva': -3,
        'parry': 7,
        'pull': 13,
        'hitAdjFoe': 8,
        'destroy': 20,
        'ignoreBlock': 17,
        'atkBalance': -1,
        'stickInTarget': 5,
        },
    }
WP_FRANCISCA={
    'desc': '''A small throwing axe that is used to damage enemy morale and disable their shields at a distance.''',
    'name': "francisca",
    'type': HAND1,
    'school': AXES,
    'hands': "1",
    'strReq': 3,
    'dexReq': 3,
    'mat': (MAT_WOOD, MAT_STEEL),
    'dur': 150,
    'value': 25,
    'mass': 0.6,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': -6,
        'hand1Strike': 6,
        'hand1Thrust': 0,
        'hand1Slash': 5,
        'hand1Stagger': 2,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 85,
        'mob': -2,
        'spd': -12,
        'accm': -12,
        'acct': 10,
        'eva': 2,
        'parry': 2,
        'hitAdjFoe': 8,
        'destroy': 20,
        'pull': 8,
        'ignoreBlock': 15,
        'stickInTarget': 10,
        'bounce': 75,
        'atkBalance': -1,
        },
    }
WP_MILITARYPICK={
    'desc': '''This pickaxe has been altered to function as a weapon of war. It is a cheap, effective militia armament.''',
    'name': "military pick",
    'type': HAND1,
    'school': AXES,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 390,
    'value': 22,
    'mass': 1.4,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': 8,
        'hand1Strike': 16,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 3,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': -2,
        'mob': -3,
        'spd': -31,
        'accm': -26,
        'acct': -50,
        'eva': -7,
        'parry': 3,
        'pull': 24,
        'destroy': 25,
        'ignoreBlock': 19,
        'atkBalance': -1,
        'stickInTarget': 67,
        },
    }
WP_HANDSCYTHE={
    'desc': '''A military pick-like weapon with a scythe-head instead of a pick; this 1-handed weapon is devastating but ineffective for battle since it always ends up stuck in the target.''',
    'name': "hand scythe",
    'type': HAND1,
    'school': AXES,
    'hands': "1",
    'strReq': 4,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 450,
    'value': 570,
    'mass': 1.5,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': -9,
        'hand1Strike': 7,
        'hand1Thrust': 0,
        'hand1Slash': 9,
        'hand1Stagger': 2,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 2,
        'mob': -2,
        'spd': -24,
        'accm': -30,
        'acct': -50,
        'eva': -5,
        'parry': 3,
        'pull': 22,
        'destroy': 25,
        'ignoreBlock': 19,
        'atkBalance': -1,
        'stickInTarget': 75,
        },
    }
WP_CLEAVER={
    'desc': '''The massive blade on this tool is designed for hacking limbs apart; it is rather ineffective in combat, but excels in delivering clean cuts. Despite technically being a butcher knife, the thick blade and top-heavy design make this blade function more along the lines of an axe than a combat knife.''',
    'name': "cleaver",
    'type': HAND1,
    'school': AXES,
    'hands': "1",
    'strReq': 4,
    'dexReq': 3,
    'mat': (MAT_WOOD, MAT_STEEL),
    'dur': 350,
    'value': 85,
    'mass': 1.0,
    'damageScaling': {
        STRENGTH : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': -37,
        'hand1Strike': 8,
        'hand1Thrust': 0,
        'hand1Slash': 15,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 70,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 3,
        'dismember': 25,
        'mob': -2,
        'spd': -16,
        'accm': -22,
        'acct': -50,
        'eva': -4,
        'parry': 7,
        'hitAdjFoe': 4,
        'destroy': 7,
        'ignoreBlock': 10,
        'atkBalance': -2,
        },
    }
WP_BATTLEAXE={
    'desc': '''A large, 2-handed axe designed for use in short battles. Its large warhead delivers a devastating chop, but its wielder suffers in speed, mobility, and defense, making this weapon ill-suited for war.''',
    'name': "battleax", #class
    'type': HAND1,      #weapon
    'school': AXES,     #skill required, skills useable influenced by this
    'hands': "2",       #1 or 2 handed, or 1/2 which is either 1 or 2
    'strReq': 5,
    'dexReq': 3,
    'mat': (MAT_WOOD, MAT_STEEL),
    'dur': 315,
    'value': 140,
    'mass': 1.9,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': -15,
        'hand1Strike': 13,
        'hand1Thrust': 0,
        'hand1Slash': 14,
        'hand1Stagger': 2,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 90,
        'hand1DefStrike': 4,
        'hand1DefThrust': 16,
        'hand1Guard': 12,
        'dismember': 9,
        'mob': -5,
        'spd': -15,
        'accm': -10,
        'acct': -50,
        'eva': -13,
        'pull': 8,
        'hitAdjFoe': 16,
        'destroy': 33,
        'ignoreBlock': 5,
        'atkBalance': -2,
        },
    }
WP_EXECUTIONERAXE={
    'desc': '''This hand-held guillotine is designed for use by an executioner for decapitation, and is not made for battle. It is capable of extreme power and damage, but it is extremely unwieldy and not suited for combat. Executioner's axes are brutal tools, which often fail to make a clean cut; but the blow is still absolutely devastating.''',
    'name': "executioner's axe",
    'type': HAND1,
    'school': AXES,
    'hands': "2",
    'strReq': 10,
    'dexReq': 3,
    'mat': (MAT_IRON,),
    'dur': 425,
    'value': 700,
    'mass': 4.5,
    'damageScaling': {
        STRENGTH : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': -47,
        'hand1Strike': 23,
        'hand1Thrust': 0,
        'hand1Slash': 8,
        'hand1Stagger': 4,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 35,
        'dismember': 31,
        'mob': -13,
        'spd': -52,
        'accm': -40,
        'eva': -50,
        'hitAdjFoe': 50,
        },
    }


#pollarms
WP_JAVELIN={
    'desc': '''This cheap skirmishing weapon is lightweight and excellent for PITCHING, though it isn't much good for anything else.''',
    'name': "javelin",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 10,
    'value': 6,
    'mass': 0.5,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': 5,
        'hand1Strike': 3,
        'hand1Thrust': 7,
        'hand1Slash': 2,
        'hand1Stagger': 1,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 40,
        'hand1DefStrike': 1,
        'hand1DefThrust': 4,
        'hand1Guard': 5,
        'throwAtks': 2,
        'throwAtkp': 6,
        'throwRangeMin': 4,
        'throwRangeMax': 18,
        'mob': -4,
        'spd': -2,
        'accm': 10,
        'acct': 25,
        'stickInTarget': 33,
        },
    }
WP_WARDART={
    'desc': '''An inexpensive throwing weapon, these broad-headed javelins with goose-feather fletching are designed to dispatch of unarmoured foes and disable shield formations from a distance.''',
    'name': "war dart",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 10,
    'value': 10,
    'mass': 0.35,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 1,
        'hand1Strike': 1,
        'hand1Thrust': 5,
        'hand1Slash': 1,
        'hand1Stagger': 1,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 40,
        'throwAtk': 5,
        'throwRangeMin': 4,
        'throwRangeMax': 22,
        'mob': -4,
        'spd': -4,
        'accm': 10,
        'acct': 60,
        'stickInTarget': 40,
        },
    }
WP_SPEAR={
    'desc': '''A typical soldier's spear that can be wielded in either one or two hands. Spears are cheap and have more reach than most weapons; they are versatile weapons which can be used in a number of combat situations.''',
    'name': "spear",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 150,
    'value': 55,
    'mass': 2.5,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': 9,
        'hand1Strike': 4,
        'hand1Thrust': 11,
        'hand1Slash': 2,
        'hand1Stagger': 2,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 3,
        'throwAcc': 20,
        'mob': -7,
        'spd': -4,
        'accm': 10,
        'eva': -3,
        'parry': 18,
        'parryAlly': 11,
        'counter': 8,
        'hitAdjFoe': 20,
        'stickInTarget': 25,
        },
    }
WP_DAGGERSPEAR={
    'desc': '''A spear with a very long, thick warhead designed for thrusting into chinks in the foes' armour. It has excellent penetrative capability at the cost of versatility.''',
    'name': "daggerspear",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 150,
    'value': 105,
    'mass': 3.1,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 6,
        'hand1Strike': 2,
        'hand1Thrust': 10,
        'hand1Slash': 7,
        'hand1Stagger': 2,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 3,
        'throwAcc': 10,
        'mob': -8,
        'spd': -8,
        'accm': 5,
        'eva': -5,
        'parry': 16,
        'parryAlly': 11,
        'counter': 5,
        'hitAdjFoe': 12,
        'stickInTarget': 33,
        },
    }
WP_WINGEDSPEAR={
    'desc': '''n/a''',
    'name': "winged spear",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 150,
    'value': 90,
    'mass': 2.7,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 7,
        'hand1Strike': 7,
        'hand1Thrust': 8,
        'hand1Slash': 3,
        'hand1Stagger': 2,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 3,
        'throwAcc': 20,
        'mob': -7,
        'spd': -5,
        'accm': 10,
        'eva': -3,
        'parry': 18,
        'parryAlly': 11,
        'counter': 8,
        'hitAdjFoe': 20,
        'stickInTarget': 5,
        },
    }
WP_HEWINGSPEAR={
    'desc': '''n/a''',
    'name': "hewing spear",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "1/2",
    'strReq': 4,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_STEEL,),
    'dur': 150,
    'value': 180,
    'mass': 2.9,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 3,
        'hand1Strike': 4,
        'hand1Thrust': 4,
        'hand1Slash': 17,
        'hand1Stagger': 2,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 1,
        'throwAcc': 20,
        'dismember': 2,
        'mob': -7,
        'spd': -7,
        'accm': 5,
        'eva': -3,
        'parry': 18,
        'parryAlly': 11,
        'counter': 8,
        'hitAdjFoe': 25,
        'stickInTarget': 15,
        },
    }

#pollarms, cont'd
WP_QUARTERSTAFF={
    'desc': '''n/a''',
    'name': "quarterstaff",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 4,
    'dexReq': 2,
    'mat': (MAT_WOOD,),
    'dur': 180,
    'value': 55,
    'mass': 1.75,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': 0,
        'hand1Strike': 12,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 4,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 8,
        'hand1DefThrust': 16,
        'hand1Guard': 36,
        'mob': -7,
        'spd': 7,
        'accm': 6,
        'eva': -3,
        'parry': 22,
        'parryAlly': 16,
        'counter': 12,
        'hitAdjFoe': 33,
        'push': 6,
        },
    }
WP_LONGSTAFF={
    'desc': '''n/a''',
    'name': "longstaff",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 6,
    'dexReq': 2,
    'mat': (MAT_WOOD,),
    'dur': 100,
    'value': 175,
    'mass': 3.0,
    'damageScaling': {
        STRENGTH : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': -13,
        'hand1Strike': 14,
        'hand1Thrust': 0,
        'hand1Slash': 0,
        'hand1Stagger': 4,
        'hand1ReachMin': 3,
        'hand1ReachMax': 4,
        'hand1Grip': 75,
        'mob': -9,
        'spd': -16,
        'accm': -5,
        'eva': -15,
        'parry': 11,
        'parryAlly': 11,
        'counter': 5,
        'hitAdjFoe': 50,
        'push': 10,
        },
    }
WP_HALLEBARDE={
    'desc': '''The hallebarde is a mix of an axe and a spear, which excels in fighting armoured foes. Like any pollarm it has great reach but must be wielded in two hands. It is perhaps the most versatile of pollarms, performing well in cuts, thrusts, and crushing blows.''',
    'name': "hallebarde",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 4,
    'mat': (MAT_STEEL, MAT_WOOD,),
    'dur': 250,
    'value': 580,
    'mass': 2.6,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': 16,
        'hand1Strike': 11,
        'hand1Thrust': 12,
        'hand1Slash': 2,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 6,
        'hand1DefThrust': 16,
        'hand1Guard': 14,
        'mob': -8,
        'spd': -8,
        'accm': -12,
        'eva': -14,
        'parry': 15,
        'parryAlly': 13,
        'counter': 5,
        'hitAdjFoe': 20,
        'destroy': 10,
        'pull': 12,
        'stickInTarget': 10,
        },
    }
WP_PARTISAN={
    'desc': '''A partisan is similar to a winged spear, with larger blades instead of small wings protruding from the sides. It is a versatile weapon that is especially effective against unarmoured foes.''',
    'name': "partisan",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 4,
    'mat': (MAT_STEEL, MAT_WOOD,),
    'dur': 180,
    'value': 345,
    'mass': 2.75,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'hand1Penetrate': 5,
        'hand1Strike': 8,
        'hand1Thrust': 8,
        'hand1Slash': 12,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 6,
        'hand1DefThrust': 16,
        'hand1Guard': 18,
        'mob': -8,
        'spd': -3,
        'accm': -10,
        'eva': -12,
        'parry': 16,
        'parryAlly': 12,
        'counter': 5,
        'hitAdjFoe': 30,
        },
    }
WP_BARDICHE={
    'desc': '''A bardiche has properties of the sword and spear. Its wide, cutting blade is exceptionally devastating to unarmoured foes.''',
    'name': "bardiche",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 3,
    'mat': (MAT_STEEL, MAT_WOOD,),
    'dur': 220,
    'value': 345,
    'mass': 2.75,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 2,
        'hand1Strike': 6,
        'hand1Thrust': 5,
        'hand1Slash': 19,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 6,
        'hand1DefThrust': 16,
        'hand1Guard': 14,
        'dismember': 3,
        'mob': -8,
        'spd': -12,
        'accm': -15,
        'eva': -16,
        'parry': 6,
        'parryAlly': 5,
        'counter': 2,
        'hitAdjFoe': 30,
        },
    }
WP_POLLHAMMER={
    'desc': '''Pollhammers cross quarterstaves with hammers. They are designed to defeat foes in armour, and can easily cause serious damage the enemy's equipment. Its massive size makes it encumbering, but it delivers a deadly shock.''',
    'name': "pollhammer",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 2,
    'mat': (MAT_IRON, MAT_WOOD,),
    'dur': 520,
    'value': 405,
    'mass': 2.5,
    'damageScaling': {
        STRENGTH : SCALING_S,
        },
    'stats': {
        'hand1Penetrate': 4,
        'hand1Strike': 16,
        'hand1Thrust': 6,
        'hand1Slash': 2,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 6,
        'hand1DefThrust': 16,
        'hand1Guard': 10,
        'mob': -7,
        'spd': -19,
        'accm': -15,
        'eva': -16,
        'parry': 8,
        'parryAlly': 4,
        'counter': 3,
        'hitAdjFoe': 12,
        'destroy': 50,
        'pull': 5,
        },
    }
WP_POLLAXE={
    'desc': '''A pollaxe is quite simply an axehead attached to a long pole, with a spearhead for thrusting and a hammerhead for crushing. In function it is similar to a hallebarde, but more focused on chopping than thrusting. The powerful chop is devastating to armoured and unarmoured foes alike.''',
    'name': "pollaxe",
    'type': HAND1,
    'school': POLLARMS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 3,
    'mat': (MAT_STEEL, MAT_WOOD,),
    'dur': 350,
    'value': 405,
    'mass': 2.75,
    'damageScaling': {
        STRENGTH : SCALING_A,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': 10,
        'hand1Strike': 14,
        'hand1Thrust': 6,
        'hand1Slash': 3,
        'hand1Stagger': 3,
        'hand1ReachMin': 2,
        'hand1ReachMax': 3,
        'hand1Grip': 80,
        'hand1DefStrike': 6,
        'hand1DefThrust': 16,
        'hand1Guard': 10,
        'mob': -7,
        'spd': -17,
        'accm': -19,
        'eva': -17,
        'parry': 7,
        'parryAlly': 4,
        'counter': 1,
        'hitAdjFoe': 15,
        'destroy': 25,
        'pull': 15,
        'stickInTarget': 6,
        },
    }


#knives
WP_MAINGAUCHE={
    'desc': '''A parrying knife for use in the off-hand to grant additional defensive capability. It has quillons for trapping the opponent's blade and a wide knuckleguard for added protection.''',
    'name': "main gauche",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 135,
    'value': 390,
    'mass': 1.1,
    'damageScaling': {
        STRENGTH : SCALING_E,
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 13,
        'hand1Strike': 0,
        'hand1Thrust': 6,
        'hand1Slash': 1,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 100,
        'spd': 6,
        'accm': 5,
        'eva': 5,
        'parry': 23,
        'counter': 12,
        },
    }
WP_SWORDBREAKER={
    'desc': '''A parrying knife for use in the off-hand to grant additional defensive capability. The blade of this knife is deeply serrated, allowing the wielder to catch opponent's blades and follow-up with many different styles of counter-attacks. Unfortunately the serrated blade makes its penetrative potential suffer, though it remains effective against unarmoured foes.''',
    'name': "swordbreaker",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 6,
    'mat': (MAT_STEEL,),
    'dur': 60,
    'value': 1390,
    'mass': 0.9,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 4,
        'hand1Strike': 0,
        'hand1Thrust': 3,
        'hand1Slash': 5,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 90,
        'spd': 4,
        'accm': 5,
        'eva': 5,
        'parry': 19,
        'counter': 16,
        },
    }
WP_TRIDENTDAGGER={
    'desc': '''A parrying knife for use in the off-hand to grant additional defensive capability. This knife has 3 blades in total, which all form together into one blade for thrusting; a sophisticated trigger mechanism in the hilt allows the wielder to release the 2 additional blades along the central blade lengthwise, forming a large double-V that can easily catch the foe's blades. This design makes it excellent for parrying but it lacks offensive power.''',
    'name': "trident dagger",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 6,
    'mat': (MAT_STEEL,),
    'dur': 30,
    'value': 1930,
    'mass': 1.05,
    'damageScaling': {
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 7,
        'hand1Strike': 0,
        'hand1Thrust': 4,
        'hand1Slash': 2,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 82,
        'hand1DefStrike': 2,
        'hand1DefThrust': 8,
        'hand1Guard': 18,
        'spd': 4,
        'accm': 3,
        'eva': 5,
        'parry': 17,
        'counter': 8,
        },
    }
WP_DAGGER={
    'desc': '''A long, tapered war-dagger which knights make use of to dispatch of armoured foes in disadvantageous positions. It excels in close-range, amoured combat, where one can take advantage of its exceptional ability to thrust into the chinks in the foes' armour.''',
    'name': "dagger",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 140,
    'value': 130,
    'mass': 0.9,
    'damageScaling': {
        STRENGTH : SCALING_E,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 31,
        'hand1Strike': 0,
        'hand1Thrust': 9,
        'hand1Slash': 4,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 95,
        'spd': 11,
        'accm': 9,
        'eva': 5,
        'parry': 16,
        'counter': 5,
        },
    }
WP_SPIKE={
    'desc': '''A large spike with a hilt, designed for thrusting into the chinks in the foes' armour, at which it excels; but it provides little defense for the wielder.''',
    'name': "war spike",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 360,
    'value': 35,
    'mass': 0.5,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'hand1Penetrate': 39,
        'hand1Strike': 0,
        'hand1Thrust': 8,
        'hand1Slash': 0,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 95,
        'spd': 7,
        'accm': -3,
        'parry': 4,
        'counter': 5,
        },
    }
WP_DIRK={
    'desc': '''A short war-knife for overhand thrusting, popular for its deadly damage to size ratio.''',
    'name': "dirk",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 185,
    'value': 160,
    'mass': 0.7,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 21,
        'hand1Strike': 0,
        'hand1Thrust': 10,
        'hand1Slash': 0,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 95,
        'spd': 11,
        'accm': 5,
        'eva': 5,
        'parry': 8,
        'counter': 5,
        },
    }
WP_KRIS={
    'desc': '''A wavy-bladed dagger designed for overhanded downward thrusting.''',
    'name': "kris",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 90,
    'value': 320,
    'mass': 0.9,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 11,
        'hand1Strike': 0,
        'hand1Thrust': 8,
        'hand1Slash': 9,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 95,
        'spd': 9,
        'accm': 5,
        'eva': 5,
        'parry': 10,
        'counter': 5,
        },
    }
WP_RONDELDAGGER={
    'desc': '''A beautiful work of art; this jeweled knife with a deadly tri-sided high-carbon steel blade is capable of puncturing most armours except steel plate.''',
    'name': "ornate Rondel dagger",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL, MAT_GOLD,),
    'dur': 170,
    'value': 9895,
    'mass': 1.1,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 8,
        'hand1Strike': 0,
        'hand1Thrust': 13,
        'hand1Slash': 2,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 100,
        'spd': 8,
        'accm': 7,
        'eva': 5,
        'parry': 9,
        'counter': 5,
        },
    }
WP_HUNTERKNIFE={
    'desc': '''n/a''',
    'name': "hunter's knife",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 240,
    'value': 25,
    'mass': 0.5,
    'damageScaling': {
        STRENGTH : SCALING_E,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 10,
        'hand1Strike': 0,
        'hand1Thrust': 6,
        'hand1Slash': 8,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 90,
        'spd': 12,
        'accm': 12,
        'eva': 5,
        'parry': 4,
        'counter': 5,
        },
    }
WP_BONEKNIFE={
    'desc': '''n/a''',
    'name': "bone knife",
    'type': HAND1,
    'school': KNIVES,
    'hands': "1",
    'strReq': 2,
    'dexReq': 4,
    'mat': (MAT_BONE,),
    'dur': 95,
    'value': 55,
    'mass': 0.65,
    'damageScaling': {
        STRENGTH : SCALING_E,
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'hand1Penetrate': 23,
        'hand1Strike': 0,
        'hand1Thrust': 9,
        'hand1Slash': 1,
        'hand1Stagger': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Grip': 95,
        'spd': 13,
        'accm': 8,
        'eva': 5,
        'parry': 6,
        'counter': 5,
        },
    }


#Bows

WP_HUNTERBOW={
    'desc': '''This bow is designed for hunting game, though it can be used in battle in a pinch. Some rangers like the raw speed and accuracy of a lightweight hunting bow, but its power is severely lacking, making it quite worthless against armoured foes.''',
    'name': "hunter's bow",
    'type': RANGED,
    'school': BOWS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_HEMP,),
    'dur': 55,
    'value': 8,
    'mass': 1.4,
    'damageScaling': {
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'hand1Penetrate': 9,
        'hand1Strike': 0,
        'hand1Thrust': 2,
        'hand1Slash': 0,
        'reachMin': 2,
        'reachMax': 40,
        'spd': -8, 
        'mob': -2,
        'accr': 36,
        'eva': -8,
        },
    }
WP_SHORTBOW={
    'desc': '''n/a''',
    'name': "short bow",
    'type': RANGED,
    'school': BOWS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 5,
    'mat': (MAT_WOOD, MAT_HEMP,),
    'dur': 70,
    'value': 32,
    'mass': 1.5,
    'damageScaling': {
        DEXTERITY : SCALING_A,
        },
    'stats': {
        'rangeAtks': 0,
        'rangeAtkp': 5,
        'rangeMin': 2,
        'rangeMax': 45,
        'spd': -18,
        'mob': -3,
        'accr': 28,
        'eva': -10,
        'penetration': 5,
        },
    }
WP_COMPOSITEBOW={
    'desc': '''This bow is made of a composite of tapwood, hemp rope and bone, which makes up the handle. The design makes it much easier to use than most warbows while retaining much of the power of a warbow. However, these bows are more expensive to make and maintain.''',
    'name': "composite bow",
    'type': RANGED,
    'school': BOWS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_HEMP, MAT_BONE,),
    'dur': 35,
    'value': 370,
    'mass': 1.35,
    'damageScaling': {
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'rangeAtks': 0,
        'rangeAtkp': 10,
        'rangeMin': 2,
        'rangeMax': 50,
        'spd': -14,
        'mob': -3,
        'accr': 23,
        'eva': -12,
        'penetration': 8,
        },
    }
WP_YEAMANBOW={
    'desc': '''The tribe of the Yeamen are known for their ingenuity and craftsmanship, and these exotic bows are imported from across the world for use in war by trained archers. Though most rangers prefer the longbow for long-ranged attacking, this bow is somewhat more versatile than traditional longbows but they slightly lack power and range.''',
    'name': "yeaman warbow",
    'type': RANGED,
    'school': BOWS,
    'hands': "2",
    'strReq': 7,
    'dexReq': 6,
    'mat': (MAT_WOOD, MAT_HEMP, MAT_BONE,),
    'dur': 45,
    'value': 465,
    'mass': 2.0,
    'damageScaling': {
        DEXTERITY : SCALING_C,
        },
    'stats': {
        'rangeAtks': 0,
        'rangeAtkp': 13,
        'rangeMin': 3,
        'rangeMax': 70,
        'spd': -28,
        'mob': -11,
        'accr': 18,
        'eva': -15,
        'penetration': -1,
        },
    }
WP_LONGBOW={
    'desc': '''n/a''',
    'name': "longbow",
    'type': RANGED,
    'school': BOWS,
    'hands': "2",
    'strReq': 8,
    'dexReq': 6,
    'mat': (MAT_WOOD, MAT_HEMP,),
    'dur': 65,
    'value': 50,
    'mass': 1.8,
    'damageScaling': {
        DEXTERITY : SCALING_D,
        },
    'stats': {
        'rangeAtks': 0,
        'rangeAtkp': 16,
        'rangeMin': 4,
        'rangeMax': 75,
        'spd': -38,
        'mob': -12,
        'accr': 10,
        'eva': -13,
        'penetration': -3,
        },
    }
WP_GREATBOW={
    'desc': '''n/a''',
    'name': "greatbow",
    'type': RANGED,
    'school': BOWS,
    'hands': "2",
    'strReq': 10,
    'dexReq': 5,
    'mat': (MAT_WOOD, MAT_HEMP,),
    'dur': 85,
    'value': 1785,
    'mass': 2.75,
    'damageScaling': {
        STRENGTH : SCALING_D,
        DEXTERITY : SCALING_E,
        },
    'stats': {
        'rangePenetrate': -10,
        'rangeAtkThrust': 16,
        'rangeMin': 5,
        'rangeMax': 67,
        'spd': -55,
        'mob': -16,
        'accr': -30,
        'eva': -33,
        'penetration': -10,
        },
    }



#crossbows
WP_CROSSBOW={
    'desc': '''Long considered the most powerful weapon of all time, crossbows are slow to reload but deliver a deadly missile that can penetrate steel plates and kill its wearer. This crossbow is light enough to be wielded effectively in battle, but it is nowhere near as powerful as heavy arbalests.''',
    'name': "crossbow",
    'type': RANGED,
    'school': CBOWS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON, MAT_HEMP,),
    'dur': 120,
    'value': 1540,
    'mass': 4.0,
    'damageScaling': {
        },
    'stats': {
        'rangeAtks': 0,
        'rangeAtkp': 22,
        'rangeMin': 2,
        'rangeMax': 40,
        'spd': -99,
        'mob': -7,
        'accr': 10,
        'eva': -23,
        'penetration': 5,
        'atkCooldown': 1,
        },
    }
WP_ARBALEST={
    'desc': '''Long considered the most powerful weapon of all time, crossbows are slow to reload but deliver a deadly missile that can penetrate steel plates and kill its wearer. The arbalest is a heavy crossbow designed to be used in sieges, and due to its slow reload time, it is ineffective in combat.''',
    'name': "crossbow",
    'type': RANGED,
    'school': CBOWS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON, MAT_HEMP,),
    'dur': 120,
    'value': 3865,
    'mass': 6.5,
    'damageScaling': {
        },
    'stats': {
        'rangeAtks': 0,
        'rangeAtkp': 44,
        'rangeMin': 4,
        'rangeMax': 45,
        'spd': -99,
        'mob': -10,
        'accr': 5,
        'eva': -33,
        'penetration': -5,
        'atkCooldown': 3,
        },
    }


#guns
WP_HANDCANNON={
    'desc': '''Hand cannons use gunpowder to fire an inaccurate projectile short distances. It can cause mortal wounds, but its main effect is as a demoralizer, as its loud percussive shot causes disorientation. It thus functions better as a weapon against ranks of foes, where firing volleys into the crowd is sure to do some damage even if individual targets cannot be hit.''',
    'name': "hand cannon",
    'type': RANGED,
    'school': GUNS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON,),
    'dur': 170,
    'value': 650,
    'mass': 16.0,
    'damageScaling': {
        },
    'stats': {
        'rangeAtks': 16,
        'rangeAtkp': 16,
        'rangeMin': 4,
        'rangeMax': 35,
        'spd': -30, #speed of striking with the gun as a melee weapon
        'mob': -10,
        'accr': -55,
        'eva': -35,
        'penetration': 13,
        'atkCooldown': 3, #reload time
        'failure': 25,
        },
    }
WP_ARQUEBUS={
    'desc': '''The future of weaponry; this sophisticated handcannon consists of a matchlock mechanism and a trigger for ease of reloading and firing. It outperforms traditional handcannons in every regard except raw power.''',
    'name': "hand cannon",
    'type': RANGED,
    'school': GUNS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON, MAT_WOOD,),
    'dur': 120,
    'value': 1550,
    'mass': 9.0,
    'damageScaling': {
        },
    'stats': {
        'rangeAtks': 13,
        'rangeAtkp': 13,
        'rangeMin': 4,
        'rangeMax': 30,
        'spd': -15,
        'mob': -10,
        'accr': -45,
        'eva': -13,
        'penetration': 16,
        'atkCooldown': 2,
        'failure': 20,
        },
    }
WP_MUSKET={
    'desc': '''The future of weaponry; this sophisticated handcannon consists of a matchlock mechanism and a trigger for ease of reloading and firing. This weapon is far more accurate and has longer range than other gunpowder weapons, but a drawback is it takes longer to reload.''',
    'name': "musket",
    'type': RANGED,
    'school': GUNS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON, MAT_WOOD,),
    'dur': 140,
    'value': 2950,
    'mass': 11.0,
    'damageScaling': {
        },
    'stats': {
        'hand1atks': 6,
        'rangeAtks': 15,
        'rangeAtkp': 15,
        'reachMin': 1,
        'reachMax': 3,
        'rangeMin': 4,
        'rangeMax': 35,
        'hand1DefStrike': 4,
        'hand1DefThrust': 8,
        'hand1Guard': 10,
        'shield': 1,
        'parry': 8,
        'counter': 4,
        'spd': -10, #speed not taken into account with ranged attacks/ throwing.
        'mob': -10,
        'accr': -36,
        'eva': -15,
        'penetration': 19,
        'atkCooldown': 3, #muskets could shoot 5 rounds/minute
        'failure': 15,
        },
    }
WP_BAYONETMUSKET={
    'desc': '''The future of weaponry; this sophisticated handcannon consists of a matchlock mechanism and a trigger for ease of reloading and firing. This weapon is far more accurate and has longer range than other gunpowder weapons, but a drawback is it takes longer to reload. This musket has an attached bayonet for improved melee capability.''',
    'name': "musket with bayonet",
    'type': RANGED,
    'school': GUNS,
    'hands': "2",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_IRON, MAT_WOOD,),
    'dur': 140,
    'value': 3050,
    'mass': 11.6,
    'damageScaling': {
        },
    #'parts': [
    #    ATT_BAYONET,
    #    ],
    'stats': {
        'hand1atks': 6,
        'hand1atkp': 6,
        'rangeAtks': 15,
        'rangeAtkp': 15,
        'reachMin': 1,
        'reachMax': 3,
        'rangeMin': 4,
        'rangeMax': 35,
        'hand1DefStrike': 4,
        'hand1DefThrust': 8,
        'hand1Guard': 10,
        'shield': 1,
        'parry': 8,
        'counter': 4,
        'spd': -10,
        'mob': -10,
        'accr': -36,
        'eva': -15,
        'penetration': 19,
        'atkCooldown': 3, #muskets could shoot 5 rounds/minute
        'failure': 15,
        },
    }




#Shields

WP_BUCKLER={
    'desc': '''The standard offhand tool for self-defense, the buckler is a small, round, shield-like weapon with a center grip. Excellent for parrying, the buckler is preferred over larger shields when mobility and encumberance are factors. Due to its light weight and small size, it effectively grants an increase in combat speed and evasive capability rather than a penalty like large shields; however, it is ineffective at blocking.''',
    'name': "buckler",
    'type': HAND1,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 280,
    'value': 195,
    'mass': 1.3,
    'damageScaling': {
        STRENGTH : SCALING_D,
        },
    'stats': {
        'hand1atks': 4,
        'hand1atkp': 0,
        'hand1DefStrike': 4,
        'hand1DefThrust': 16,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Guard': 25,
        'shield': 5,
        'hand1Grip': 85,
        'spd': 4,
        'eva': 5,
        'mob': -1,
        'parry': 26,
        'counter': 10,
        },
    }
WP_SKIRMSHIELD={
    'desc': '''An old-fashioned large skirmishing shield for use in melee combat. The design of this shield makes it ideal for blocking arrows, but it performs poorly in melee combat.''',
    'name': "skirmishing shield",
    'type': HAND1,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 4,
    'dexReq': 4,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 65,
    'value': 85,
    'mass': 4.5,
    'damageScaling': {
        STRENGTH : SCALING_E,
        },
    'stats': {
        'hand1atks': 3,
        'hand1atkp': 0,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1DefStrike': 4,
        'hand1DefThrust': 8,
        'hand1Guard': 30,
        'shield': 50,
        'guardAlly': 5,
        'shieldAlly': 10,
        'hand1Grip': 75,
        'spd': 1,
        'parry': 20,
        'mob': -3,
        'eva': -2,
        'counter': 4,
        },
    }
WP_ROUNDSHIELD={
    'desc': '''An old-fashioned large hoplon for use in melee combat. Since its design makes it encumbering and impossible to wield from a mount, these styles of shields are uncommon nowadays among infantrymen who have no need for such a large shield, being fully equipped in plate armour; nor is it needed for mounted knights who prefer smaller wrist shields.''',
    'name': "round shield",
    'type': WRIST,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 5,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_LEATHER,),
    'dur': 90,
    'value': 155,
    'mass': 7.5,
    'damageScaling': {
        STRENGTH : SCALING_E,
        },
    'stats': {
        'hand1atks': 2,
        'hand1atkp': 0,
        'hand1DefStrike': 8,
        'hand1DefThrust': 10,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Guard': 40,
        'shield': 40,
        'guardAlly': 35,
        'shieldAlly': 15,
        'hand1Grip': 100,
        'spd': -4,
        'parry': 12,
        'counter': 5,
        'mob': -6,
        'eva': -5,
        },
    }
WP_ROTELLA={
    'desc': '''A medium-sized, round shield of pure steel, worn on the wrist.''',
    'name': "rotella",
    'type': WRIST,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 2,
    'dexReq': 2,
    'mat': (MAT_STEEL,),
    'dur': 210,
    'value': 500,
    'mass': 3.5,
    'damageScaling': {
        STRENGTH : SCALING_E,
        },
    'stats': {
        'hand1atks': 2,
        'hand1atkp': 0,
        'hand1DefStrike': 6,
        'hand1DefThrust': 18,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Guard': 60,
        'shield': 35,
        'hand1Grip': 115,
        'spd': 1,
        'parry': 24,
        'counter': 5,
        'mob': -3,
        'eva': 2,
        },
    }
WP_KITESHIELD={
    'desc': '''Designed to be worn from horseback or on foot, this kite-shaped shield is not ideal for use by infantrymen. It is perfect for those mounted knights, however, who desire some additional defense.''',
    'name': "kite shield",
    'type': WRIST,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 2,
    'mat': (MAT_WOOD,),
    'dur': 80,
    'value': 420,
    'mass': 5.5,
    'damageScaling': {
        STRENGTH : SCALING_E,
        },
    'stats': {
        'hand1atks': 2,
        'hand1atkp': 0,
        'hand1DefStrike': 10,
        'hand1DefThrust': 16,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Guard': 60,
        'shield': 45,
        'guardAlly': 25,
        'shieldAlly': 25,
        'hand1Grip': 120,
        'spd': -2,
        'parry': 10,
        'counter': 6,
        'mob': -6,
        'eva': -4,
        },
    }
WP_TOWERSHIELD={
    'desc': '''This massive, solid wall of hardwood and iron is virtually impenetrable to all but the most powerful attacks, though its wielder suffers a significant penalty to mobility. Similar to the Roman scutum, the tower shield grants excellent protection but is generally ineffective in one-on-one combat due to its encumberance.''',
    'name': "tower shield",
    'type': WRIST,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 5,
    'dexReq': 2,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 145,
    'value': 450,
    'mass': 8.25,
    'damageScaling': {
        },
    'stats': {
        'hand1atks': 0,
        'hand1atkp': 0,
        'hand1DefStrike': 10,
        'hand1DefThrust': 14,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Guard': 60,
        'shield': 60,
        'guardAlly': 25,
        'shieldAlly': 25,
        'hand1Grip': 105,
        'spd': -6,
        'parry': 5,
        'counter': 8,
        'mob': -7,
        'eva': -13,
        },
    }
WP_HEATERSHIELD={
    'desc': '''This modern style of shield is popular among knights whose fighting tactics have evolved away from the shield wall. Being fully armoured in plate, some infantrymen see no need for a shield, but those who do generally prefer a thick, high-quality small shield for parrying -- and/or one which can be wielded on horseback -- and this style of shield is ideal for fitting both of those needs.''',
    'name': "heater shield",
    'type': WRIST,
    'school': SHIELDS,
    'hands': "1",
    'strReq': 5,
    'dexReq': 2,
    'mat': (MAT_WOOD,),
    'dur': 130,
    'value': 895,
    'mass': 4.5,
    'damageScaling': {
        STRENGTH : SCALING_D,
        },
    'stats': {
        'hand1atks': 1,
        'hand1atkp': 0,
        'hand1DefStrike': 8,
        'hand1DefThrust': 16,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'hand1Guard': 40,
        'shield': 30,
        'guardAlly': 5,
        'shieldAlly': 15,
        'hand1Grip': 100,
        'spd': 1,
        'parry': 24,
        'counter': 8,
        'mob': -3,
        'eva': 2,
        },
    }
WP_PAVISE={
    'desc': '''The pavise is a development of the standard infantry tower shield; it is heavier and offers superior protection. However, this massive wall of protection is so heavy and cumbersome that it cannot be wielded effectively in melee combat. Instead, crossbowmen make use of this shield to provide extra defense while shooting and reloading. The convex shape allows this shield to be planted in the ground, freeing up the archer's hands while providing excellent defense against enemy missiles.''',
    'name': "pavise",
    'type': PAVISE,
    'strReq': 6,
    'dexReq': 3,
    'mat': (MAT_WOOD, MAT_IRON,),
    'dur': 180,
    'value': 575,
    'mass': 8.1,
    'damageScaling': {
        },
    'stats': {
        'hand1DefStrike': 8,
        'hand1DefThrust': 20,
        'hand1ReachMin': 1,
        'hand1ReachMax': 1,
        'shield': 70, #only blocks ranged
        'shieldAlly': 10,
        'hand1Grip': 50,
        'mob': -9,
        'eva': -33,
        },
    }









#Debuffs

DEBUFF_FEINT={
    'name': 'Misdirection',
    'savingThrow': INTELLIGENCE,
    'affects': 'foe',
    'duration': (1,0,),
    'radius': (0,0,),
    'stats': {
        'eva': (-10, -3,),
        'parry': (-5, -3,),
        'hand1Guard': (-5, -3,),
        'shield': (-5, -3,),
        'hand2guard': (-5, -3,),
        'hand2shield': (-5, -3,),
        'guardAlly': (-5, -3,),
        'shieldAlly': (-5, -3,),
        'hand2guardAlly': (-5, -3,),
        'hand2shieldAlly': (-5, -3,),
        },
    }















#-----------#
#  Skills   #
#-----------#


#values for skill stat mods are tuples where
#the first value is the base
#the second value is the delta, or change per level


#knives skills
SKL_KNIVES={
    'name': 'Knives',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_KNIVES,
    'stats': {
        'atks':     (0, 0,),
        'atkp':     (0, 1,),
        'accm':     (0, 6,),
        'eva':      (0, 2.25,),
        'parry':    (0, 1.25,),
        'counter':  (0, 1,),
        'spd':      (0, 1.25,),
        'penetration':     (0, 1.33,),
        },
    }

#short swords skills
SKL_SHORTSWORDS={
    'name': 'Shortswords',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_SHORTSWORDS,
    'stats': {
        'atks':     (0, 0.33,),
        'atkp':     (0, 0.67,),
        'accm':     (0, 5,),
        'eva':      (0, 2,),
        'parry':    (0, 1,),
        'counter':  (0, 1.25,),
        'spd':      (0, 1.33,),
        'penetration':     (0, 1.25,),
        'hand1Guard':(0, 1,),
        },
    }

#longswords skills
SKL_LONGSWORDS={
    'name': 'Longswords',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_LONGSWORDS,
    'stats': {
        'hand1atks':(0, 0.5,),
        'hand1atkp':(0, 0.5,),
        'accm':     (0, 6,),
        'eva':      (0, 2,),
        'parry':    (0, 1.25,),
        'counter':  (0, 1,),
        'spd':      (0, 1.25,),
        'penetration':     (0, 1,),
        'hand1Guard':(0, 1,),
        },
    }

#rapiers skills
SKL_RAPIERS={
    'name': 'Rapiers',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_RAPIERS,
    'stats': {
        'hand1atks':(0, 0,),
        'hand1atkp':(0, 0.75,),
        'accm':     (0, 5,),
        'eva':      (0, 2,),
        'parry':    (0, 2,),
        'counter':  (0, 1.5,),
        'spd':      (0, 1.5,),
        'hand1Guard':(0, 0.5,),
        },
    }

#curved swords skills
SKL_CURVEDSWORDS={
    'name': 'Curved Swords',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_CURVEDSWORDS,
    'stats': {
        'hand1atks':(0, 0,),
        'hand1atkp':(0, 1,),
        'accm':     (0, 6,),
        'eva':      (0, 2,),
        'parry':    (0, 1.25,),
        'counter':  (0, 1.25,),
        'spd':      (0, 1.25,),
        'hand1Guard':(0, 1,),
        },
    }
SKL_GREATSWORDS={
    'name': 'Greatswords',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_GREATSWORDS,
    'stats': {
        'hand1atks':(0, 0.67,),
        'hand1atkp':(0, 0.67,),
        'accm':     (0, 5,),
        'eva':      (0, 2,),
        'parry':    (0, 0.5,),
        'counter':  (0, 1,),
        'spd':      (0, 1,),
        'hand1Guard':(0, 1.25,),
        },
    }

#axes skills
SKL_AXES={
    'name': 'Axes',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_AXES,
    'stats': {
        'hand1atks':(0, 1,),
        'hand1atkp':(0, 0.5,),
        'accm':     (0, 3,),
        'eva':      (0, 1,),
        'spd':      (0, 1,),
        'hand1Guard':(0, 1,),
        },
    }
SKL_AXEDRIVE={
    'name': 'Axe Drive',
    'desc': '''Strike with the blunt of the axe's hammerhead or the flat side of the blade, dealing increased shock damage.''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_ATTACKMAINHAND,
    'preReq': SKL_AXES,
    'requirements:': RQ_ATTACK_WITH_AXES,
    'strReq': 4,
    'dexReq': 2,
    'stats': {
        'atks': (2, 1,),
        'accm': (-5, 5,),
        'spd': (-10, 2,),
        'ignoreParry': (5, 5,),
        'aimForHead': (1, 1,),
        },
    'statsMult': {
        'atkp': (0, 0,),
        'hook': (0, 0,),
        'dismember': (0, 0,),
        },
    }
SKL_AXESPIKE={
    'name': 'Axe Spike',
    'desc': '''Strike with the axe's spike or the inferior edge of the blade, dealing increased pierce damage and cleaving armour.''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_ATTACKMAINHAND,
    'preReq': SKL_AXES,
    'requirements:': RQ_ATTACK_WITH_AXES,
    'strReq': 4,
    'dexReq': 2,
    'stats': {
        'atkp': (1, 1,),
        'accm': (-25, 5,),
        'spd': (-15, 2,),
        'destroy': (8, 3),
        'stickInTarget': (10, 0,),
        },
    'statsMult': {
        'dismember': (0, 0,),
        },
    }
SKL_HOOKANDGRAB={
    'name': 'Hook and Grab',
    'desc': '''Hook your blade around the foe's limb, armour, or weapon, giving you more leverage and pulling them towards you, knocking them off balance and preparing them for being wrestled to the ground in close quarters combat.''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_ATTACKMAINHAND,
    'preReq': SKL_AXES,
    'requirements:': RQ_ATTACK_WITH_AXES,
    'strReq': 6,
    'dexReq': 4,
    'stats': {
        'hand1atks': (-4, 0.25,),
        'hand1atkp': (-4, 0.25,),
        'accm': (-50, 5,),
        'spd': (-25, 2,),
        'pull': (15, 5,),
        'hand1Stagger': (1, 1,),
        'ignoreParry': (10, 5,),
        },
    'statsMult': {
        },
    'debuff': {
        'name': 'Hooking',
        'affects': 'self',
        'savingThrow': None,
        'duration': (1, 0,),
        'radius': (0, 0,),
        'stats': {
            'advantage': (1, 0,),
            'eva': (-25, 1,),
            'parry': (-25, 1,),
            'parryAlly': (-25, 1),
            'hand1Guard': (-25, 1,),
            'shield': (-25, 1,),
            'guardAlly': (-25, 1),
            'shieldAlly': (-25, 1),
            },
        },
    'debuff': {
        'name': 'Hooked',
        'affects': 'foe',
        'savingThrow': STRENGTH,
        'duration': (1, 0,),
        'radius': (0, 0,),
        'stats': {
            'advantage': (-1, 0,),
            'mob': (-8, -3,),
            'acc': (-25, -5,),
            'eva': (-25, -5,),
            'parry': (-5, -3,),
            'parryAlly': (-5, -3),
            'hand1Guard': (-5, -3,),
            'guardAlly': (-5, -3),
            'shield': (-5, -3,),
            'shieldAlly': (-5, -3),
            },
        },
    }

#clubs skills
SKL_CLUBS={
    'name': 'Clubs',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_CLUBS,
    'stats': {
        'hand1atks':(0, 1.25,),
        'hand1atkp':(0, 0,),
        'accm':     (0, 4,),
        'eva':      (0, 1,),
        'spd':      (0, 1,),
        'hand1Guard':(0, 1,),
        },
    }

#hammers skills
SKL_HAMMERS={
    'name': 'Hammers',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_HAMMERS,
    'stats': {
        'hand1atks':(0, 1,),
        'hand1atkp':(0, 0.33,),
        'accm':     (0, 4,),
        'eva':      (0, 1,),
        'spd':      (0, 1,),
        'hand1Guard':(0, 1,),
        },
    }

#POLLARMS skills
SKL_SPEARS={
    'name': 'Spears',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_SPEARS,
    'stats': {
        'hand1atks':(0, 0.25,),
        'hand1atkp':(0, 1,),
        'accm':     (0, 5,),
        'eva':      (0, 1,),
        'parry':    (0, 0.75,),
        'counter':  (0, 0.5,),
        'spd':      (0, 1,),
        'hand1Guard':(0, 1,),
        },
    }

#pollarms skills
SKL_POLLARMS={
    'name': 'Pollarms',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_POLLARMS,
    'stats': {
        'hand1atks':(0, 0.75,),
        'hand1atkp':(0, 0.75,),
        'accm':     (0, 4,),
        'eva':      (0, 1,),
        'parry':    (0, 0.67,),
        'counter':  (0, 0.5,),
        'spd':      (0, 1,),
        'hand1Guard':(0, 1,),
        },
    }

#pikes skills
SKL_PIKES={
    'name': 'Pikes',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_PIKES,
    'stats': {
        'hand1atks':(0, 0.25,),
        'hand1atkp':(0, 1,),
        'accm':     (0, 4,),
        'eva':      (0, 0.5,),
        'parry':    (0, 0.5,),
        'counter':  (0, 0.5,),
        'spd':      (0, 1,),
        },
    }

#bows skills
SKL_BOWS={
    'name': 'Bows',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_BOWS,
    'stats': {
        'rangeAtks':(0, 0,),
        'rangeAtkp':(0, 0.67,),
        'rangeMax': (0, 1,),
        'accr':     (0, 6,),
        'spd':      (0, 1.5,),
        },
    }

#cbows skills
SKL_CBOWS={
    'name': 'Crossbows',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_CBOWS,
    'stats': {
        'rangeAtks':(0, 0,),
        'rangeAtkp':(0, 0.25,),
        'accr':     (0, 6,),
        'spd':      (0, 1.5,),
        },
    }

#guns skills
SKL_GUNS={
    'name': 'Guns',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_GUNS,
    'stats': {
        'rangeAtks':(0, 0.25,),
        'rangeAtkp':(0, 0.25,),
        'accr':     (0, 4,),
        'spd':      (0, 1.5,),
        },
    }

#slings skills
SKL_SLINGS={
    'name': 'Slings',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_SLINGS,
    'stats': {
        'rangeAtks':(0, 1.25,),
        'rangeAtkp':(0, 0,),
        'accr':     (0, 3,),
        'spd':      (0, 1,),
        },
    }

#instruments skills
SKL_INSTRUMENTS={
    'name': 'Musical Instruments',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_INSTRUMENTS,
    'stats': {
        'charm':    (0, 1,),
        },
    }

#throwing knives skills
SKL_THWKNIVES={
    'name': 'Throwing Knives',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_KNIVES,
    'stats': {
        'throwAtks':(0, 0,),
        'throwAtkp':(0, 1,),
        'acct':     (0, 5,),
        'spd':      (0, 1.25,),
        },
    }

#throwing spears skills
SKL_THWSPEARS={
    'name': 'Throwing Spears',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_SPEARS,
    'stats': {
        'throwAtks':(0, 0.25,),
        'throwAtkp':(0, 1,),
        'acct':     (0, 7,),
        'spd':      (0, 1,),
        },
    }

#throwing axes skills
SKL_THWAXES={
    'name': 'Throwing Axes',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_AXES,
    'stats': {
        'throwAtks':(0, 0.5,),
        'throwAtkp':(0, 0.75,),
        'acct':     (0, 5,),
        'spd':      (0, 1,),
        },
    }

#throwing swords skills
SKL_THWSWORDS={
    'name': 'Throwing Swords',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_THWSWORDS,
    'stats': {
        'throwAtks':(0, 0.25,),
        'throwAtkp':(0, 1,),
        'acct':     (0, 6,),
        'spd':      (0, 1.25,),
        },
    }

#pitching skills
SKL_PITCHING={
    'name': 'Pitching',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_WEAPONSKILL,
    'preReq': None,
    'requirements:': RQ_WIELDING_THROWING,
    'stats': {
        'throwAtks':(0, 0.5,),
        'throwAtkp':(0, 0.5,),
        'acct':     (0, 6,),
        'spd':      (0, 1.25,),
        },
    }

#general combat skills
SKL_FEINT_ATTACK={
    'name': 'Feint Attack',
    'desc': '''n/a''',
    'maxLevel': MAX_SKILL_LEVEL,
    'type': ST_ATTACKMAINHAND,
    'preReq': None,
    'requirements:': None,
    'stats': {
        'atks': (-1, 0,),
        'atkp': (-1, 0,),
        'accm': (10, 1,),
        'spd': (-15, 1,),
        'advantage': (1, 0,),
        },
    'debuff': DEBUFF_FEINT,
    }

















# UNUSED



'''
    'onUse': {
        'cooldown': (0, 0,),
        'morale': (0, 0,),
        'foeMorale': (0, 0,),
        },'''

'''Format template concept

~~~~~~~~~~~~~~~~~~~~~~~~~~~
Feint Attack
Level 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Attack with your mainhand.
On Attack:
Atk -1/-1
Acc Melee +11
Spd -19
Balance -1
Target Balance -1
~~~~~~~~~~~~~~~~~~~~~~~~~~~
DeBuff: Misdirection
*Affects foe
*Duration 1
*Saving Throw: Perception
    Eva -13
    Parry -8
    Block -8
~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~
Feint Attack
Level 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Attack with your mainhand.
On Attack:
Atk -1/-1
Acc Melee +12
Spd -18
Balance -1
Target Balance -2
~~~~~~~~~~~~~~~~~~~~~~~~~~~
DeBuff: Misdirection
*Affects foe
*Duration 1
*Saving Throw: Intelligence
    Eva -16
    Parry -11
    Block -11
~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''


















WP_SCOTTISHSWORD={
    'desc': '''A large war sword with a hefty blade, wielded with two hands. This particular sword is somewhat of a cross between an English longsword and a greatsword, and though it is very heavy, its blade length is closer to that of a longsword.''',
    'name': "Scottish 2-handed sword",
    'type': HAND1,
    'school': LONGSWORDS,
    'hands': "2",
    'strReq': 5,
    'dexReq': 3,
    'mat': (MAT_STEEL,),
    'dur': 230,
    'value': 1090,
    'mass': 2.25,
    'damageScaling': {
        STRENGTH : SCALING_B,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1atks': 6,
        'hand1atkp': 11,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1DefStrike': 4,
        'hand1DefThrust': 16,
        'hand1Guard': 17,
        'hand1Grip': 90,
        'mob': -6,
        'spd': 2,
        'accm': 5,
        'eva': -5,
        'parry': 18,
        'parryAlly': 5,
        'counter': 12,
        'hitAdjFoe': 15,
        },
    }
#super-heavy weapons
WP_SOULREAVER={
    'desc': '''n/a''',
    'name': "soul reaver",
    'type': HAND1,
    'school': None,#SUPERWEAPONS,
    'hands': "2",
    'strReq': 13,
    'dexReq': 2,
    'mat': (MAT_STEEL,),
    'dur': 75,
    'value': 8540,
    'mass': 18.5,
    'damageScaling': {
        STRENGTH : SCALING_B,
        },
    'stats': {
        'hand1atks': 14,
        'hand1atkp': 10,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 30,
        'dismember': 30,
        'mob': -30,
        'spd': -99,
        'accm': -75,
        'eva': -60,
        'hitAdjFoe': 75,
        },
    }
WP_STRAIGHTSWORD={
    'desc': '''Straight swords are basic short swords effective at slashing, chopping, and thrusting.''',
    'name': "straight sword",
    'type': HAND1,
    'school': SHORTSWORDS,
    'hands': "1",
    'strReq': 3,
    'dexReq': 4,
    'mat': (MAT_STEEL,),
    'dur': 180,
    'value': 580,
    'mass': 1.35,
    'damageScaling': {
        STRENGTH : SCALING_C,
        DEXTERITY : SCALING_B,
        },
    'stats': {
        'hand1Penetrate': 13,
        'hand1Strike': 2,
        'hand1Thrust': 6,
        'hand1Slash': 12,
        'hand1Stagger': 1,
        'hand1ReachMin': 1,
        'hand1ReachMax': 2,
        'hand1Grip': 95,
        'hand1DefStrike': 2,
        'hand1DefThrust': 16,
        'hand1Guard': 12,
        'mob': -2,
        'accm': 10,
        'eva': 6,
        'spd': 7,
        'parry': 14,
        'counter': 12,
        'ignoreBlock': 5,
        },
    }


'''ATTRIBUTES=[ #variable names
    "str","agi","end","per","wil","int","cha",
    ]'''
'''ATTRIBUTESLONG=[ #long string names
    "Strength",
    "Agility",
    "Endurance",
    "Perception",
    "Willpower",
    "Intelligence",
    "Charisma",
    ]'''
