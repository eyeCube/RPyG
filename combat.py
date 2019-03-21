#combat.py



#strike (hit) dfndr unit once with attkr unit
#(this is not the full attack function)
def strike(attkr, dfndr, atkHand, atkWeap, atkWeapName, reachPenalty=False):
    destroy=False
    crit=False
    blocked=None
    blocker=None
    #twoHanded=False

    #BLOCKING
    #get possible blockers
    suitors=[dfndr,]
    for unit in getAdjacentUnits(dfndr):
        if allies(unit, dfndr):
            suitors.append(unit)
    for unit in suitors: #for each potential blocker, get % to block his ally
        hand1block = getStat(unit,"hand1blockAllym")
        hand2block = getStat(unit,"hand2blockAllym")
        #try to block with offhand
        if (random.random()*100 < hand2block):
            blocker = unit.name
            blocked = getEquipment(unit,HAND2).name
            blockedDefs = getStat(unit,'hand2defs')
            blockedDefp = getStat(unit,'hand2defp')
        #try to block with mainhand
        elif (random.random()*100 < hand1block):
            blocker = unit.name
            blocked = getEquipment(unit,HAND1).name
            blockedDefs = getStat(unit,'hand1defs')
            blockedDefp = getStat(unit,'hand1defp')
        if blocked:
            break #only one person can block an attack.

    #cancelling the block
    #ignore Block stat
    if (random.random()*100 < getStat(attkr, 'ignoreBlock')):
        blocked = False
        
    #pick a body part
    hit = pickTargetBodyPart(dfndr)
    
    #what armour are we hitting, if any?    
    gear = getEquipment(dfndr,bpFromName(hit))
    
    #get protect and defense values from proper body part
    protectStr = hit + "Protect"
    defsStr = hit + "Defs"
    defpStr = hit + "Defp"
    protect = getStat(dfndr,protectStr)
    defs = getStat(dfndr,defsStr)
    defp = getStat(dfndr,defpStr)
    protect += getStat(dfndr,'protect') #general protection value
    
    if gear != None:
        #destroy gear
        if random.random()*100 < getStat(attkr,'destroy'):
            damageGear(gear)
            destroy=True
        
        #condition of the protective gear being attacked (after Destroy calculated)
        gearCon = gear.condition
        
        #modify protect and defense values based on gear condition
        conDefValue = (gearCon/gear.dur)*MAX_CON_DEF_CUT + (1 - MAX_CON_DEF_CUT)
        conProtectValue = (gearCon/gear.dur)*MAX_CON_PROTECT_CUT + (1 - MAX_CON_PROTECT_CUT)
        protect *= conProtectValue
        defs *= conDefValue
        defp *= conDefValue
    
    #you can resist a crit by having greater than 100 protection
    #crit lowers protection value of defender
    protect -= getStat(attkr,'crit')
    
    #Critical hit
    #if defender blocks, there's no chance of a crit happening
    if blocked:
        crit=False
    elif random.random()*FULL_PROTECTION < protect: #armour successfully protected
        crit=False
    else:
        #Crit - Bypass armour (reduce defense armour gives)
        defs = math.floor(defs*CRIT_PROTECTION_MULT)
        defp = math.floor(defp*CRIT_PROTECTION_MULT)
        crit=True
    
    #CALCULATE DAMAGE
    #get damage from weapon
    if atkHand == HAND1:
        dmgs = getStat(attkr,'hand1atks')
        dmgp = getStat(attkr,'hand1atkp')
    elif atkHand == HAND2:
        dmgs = getStat(attkr,'hand2atks')
        dmgp = getStat(attkr,'hand2atkp')
    #add general damage and general armour
    dmgs += getStat(attkr,'atk')
    dmgp += getStat(attkr,'atk')
    dmgs -= getStat(dfndr,'def')
    dmgp -= getStat(dfndr,'def')
    #add counter bonuses
    if protect > 0:
        dmgs += getStat(attkr,'vsArmoured')
        dmgp += getStat(attkr,'vsArmoured')
    else:
        dmgs += getStat(attkr,'vsUnarmoured')
        dmgp += getStat(attkr,'vsUnarmoured')
    #subtract damage from armour
    dmgs -= defs
    dmgp -= defp
    #subtract damage from shield defense if defender blocked
    if blocked:
        dmgs -= blockedDefs
        dmgp -= blockedDefp

    #Penalties
    #REDUCE DAMAGE IF CLOSER THAN MINIMUM REACH
    if reachPenalty:
        dmgs -= MINREACH_ATKPENALTY
        dmgp -= MINREACH_ATKPENALTY
        
    #floor at 0
    #final damage values
    dmgs = max(0, round(dmgs))
    dmgp = max(0, round(dmgp))
    totalDamage = dmgs + dmgp
    
    #messages
    h=""
    suffix=""
    xs=" "
    if blocked:
        h="{hit} through {bkr}'s {blk}".format(
            hit=hit, bkr=blocker, blk=blocked)
        suffix=" (blocked)"
    elif crit:
        xs="*"
        h=hit
        suffix=" (critical hit)"
    else:
        h=hit
    msg("{xs}{x}{xs} damage to {d}'s {h} from {a}'s {w}{sf}".format(
            h=h, xs=xs, sf=suffix,
            a=attkr.name, d=dfndr.name, x=totalDamage, w=atkWeapName))
    
    #DEAL DAMAGE
    shock(dfndr, dmgs)
    pierce(dfndr, dmgp)
        
    return totalDamage

#parryAttack
#for use in melee attack functions
#defender parries (and possibly counters) attack from the attacker
    #attacker may then parry the counter if applicable
#ARGS:
#dfndr is the one parrying the attkr's attack.
#atkWeap is weapon of the attacker
def parryAttack(dfndr, attkr, atkWeap, atkWeapName):
    #counter-attack
    #make sure defender is in reach of attacker to counter
    reach = getStat(dfndr,'hand1reachMax')
    reachMin = getStat(dfndr,'hand1reachMin')
                            #dfndr.equipment[HAND1] and
    d = hex_distance(dfndr.pos, attkr.pos)
    if (d <= reach and d >= reachMin and
        random.random()*100 < getStat(dfndr,'counter')):
        #attacker tries to parry the counter-attack
        if (random.random()*100 < getStat(attkr,"parry")): 
            msg("{d} counters {a}'s {w}, and {a} parries the counter".format(
                d=dfndr.name,a=attkr.name, w=atkWeapName))
        #successful counter-attack
        else:
            msg("{d} counters {a}'s {w} ...".format(
                d=dfndr.name,a=attkr.name, w=atkWeapName))
            #defender becomes the attacker
            atkWeap, atkWeapName = getWeapData(dfndr, HAND1)
            strike(dfndr, attkr, HAND1, atkWeap, atkWeapName)
        return "counter"
    else:
        msg("{d} parries {a}'s {w}".format(
                d=dfndr.name,a=attkr.name, w=atkWeapName))
        return "parry"

def damage(unit, dmg):
    if unit.dead: return False
    unit.stats.addBase('hp', -dmg)
    if getStat(unit,'hp') <= SE_DIE_BASE:
        kill(unit)
    #elif getStat(unit,'hp') <= SE_KO_BASE:
    #    applyKO(unit)
def shock(unit, dmg):
    if unit.dead: return False
    unit.dazeCounter += dmg
    damage(unit, dmg)
    if unit.dazeCounter >= getStat(unit,'resPhysical') + SE_DAZE_BASE:
        applyDaze(unit)
def pierce(unit, dmg):
    if unit.dead: return False
    unit.bleedCounter += dmg
    damage(unit, dmg)
    if unit.bleedCounter >= getStat(unit,'resPhysical') + SE_BLEED_BASE:
        applyBleed(unit)
    
        


#automatically pick a body part to target with your attack
def pickTargetBodyPart(unit):
    #if unit.race == HUMAN:
    #you can block with arm armour if you have no torso armour.
    armsMult = 1.0
    if (getEquipment(unit,TORSO) == None and getEquipment(unit,ARMS) != None):
        armsMult = 2.5 #increase chance to protect self w/ arms.
        
    area = random.random()*100
    if area <= HIT_LEGS:
         hit = 'legs'
    elif area <= HIT_ARMS*armsMult + HIT_LEGS:
         hit = 'arms'
    elif area <= HIT_HEAD + HIT_ARMS*armsMult + HIT_LEGS:
         hit = 'head'
    else:
         hit = 'torso'
    return hit

def bpFromName(name):
    if name == "torso": return TORSO
    if name == "head": return HEAD
    if name == "legs": return LEGS
    if name == "arms": return ARMS

def damageGear(item):
    item.condition -= item.dur * DESTROY_DAMAGE_DECIMAL
    item.condition = max(0, item.condition)










