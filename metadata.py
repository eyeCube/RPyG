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
#UNARMED_ATK1=5 #damage you do with your mainhand when trained in unarmed
#UNARMED_ATK2=3 #left fist
#UNARMED_SPD=0 #bonus when unarmed and trained in unarmed
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
#ACCR_PER_PER=5
ACC_PER_PER=5
#ACCT_PER_PER=5
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
#accm_PER_STR=3
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
                'guard':0,'shield':0,
                'guardAlly':0,'shieldAlly':0,
                'mob':0,'def':0,
                'torsoProtect':0.25,'headProtect':0.25,
                'legsProtect':0.25,'armsProtect':0.25,}
SE_BLIND_MULTMODS={'vision':0,'accm':0,'acct':0,'accr':0,'eva':0.25,
                    'parry':0.25,'parryAlly':0.25,
                    'guard':0.25,'shield':0.25,
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
















