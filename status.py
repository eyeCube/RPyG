

#StatusEffect
#has an owner, an effectID, & optionally: a mod, and a timer
#input 0 for timer to have an untimed status effect
#
#WARNING:
#-remove a unique status effect before overwriting it!
#
class StatusEffect:
    def __init__(self, owner, effID, timer=0):
        self.owner=owner
        self.effectID=effID
        self.timer=timer
        self.timed=(timer>0)
        self.mod=None
    def __del__(self):
        if self.mod is not None:
            self.owner.stats.removeModifier(self.mod.id)
    def update(self):
        if self.timed:
            self.timer -= 1


#status effects
class SE_KnockedOut(StatusEffect):
    def __init__(self, owner, timer):
        super().__init__(owner, SE_KO, timer)
        self.mod=Mod(mult=SE_KO_MULTMODS, ID=SE_KO)
        self.owner.stats.addModifier(self.mod)
    def update(self):
        super().update()
        
class SE_Dazed(StatusEffect):
    def __init__(self, owner, timer):
        super().__init__(owner, SE_DAZE, timer)
        self.mod=Mod(mult=SE_DAZE_MULTMODS, ID=SE_DAZE)
        self.owner.stats.addModifier(self.mod)
    def update(self):
        super().update()
        
class SE_Bleeding(StatusEffect):
    def __init__(self, owner, timer):
        super().__init__(owner, SE_BLEED, timer)
    def update(self):
        super().update()
        damage(self.owner, 1) #can't staunch the flow...

class SE_Blinded(StatusEffect):
    def __init__(self, owner, timer):
        super().__init__(owner, SE_BLIND, timer)
        self.mod=Mod(mult=SE_BLIND_MULTMODS, ID=SE_BLIND)
        self.owner.stats.addModifier(self.mod)
    def update(self):
        super().update()
        
'''class SE_ManaCharge(StatusEffect):
    def __init__(self, owner, timer):
        super().__init__(owner, SE_MANA, timer)
    def update(self):
        super().update()
'''


def addStatusEffect(unit, effID, obj, timer):
    effect = obj(unit, timer)
    unit.status.update({effID : effect})
def removeStatusEffect(unit, effID):
    if unit.status.get(effID):
        del unit.status[effID]
def updateStatusEffects():
    ses=[]
    for unit in Unit.getList():
        for se in unit.status.values():
            ses.append(se)
    for se in ses:
        se.update()
def removeExpiredEffects():
    for unit in Unit.getList():
        ids=[]
        for ID, se in unit.status.items():
            if (se.timed and se.timer <=0): #check Status Effects with a timer only
                ids.append(ID)
        for ID in ids:
            removeStatusEffect(unit, ID)
            print(str(ID) + " removed")
def applyKO(unit):
    if SE_KO not in unit.status.keys():
        msg("{u} is knocked out".format(u=unit.name))
        removeStatusEffect(unit, SE_KO)
        addStatusEffect(unit, SE_KO, SE_KnockedOut, 0)
def applyBleed(unit):
    msg("{u} is bleeding".format(u=unit.name))
    removeStatusEffect(unit, SE_BLEED)
    addStatusEffect(unit, SE_BLEED, SE_Bleeding, SE_BLEED_TIMER)
def applyDaze(unit):
    msg("{u} is dazed".format(u=unit.name))
    removeStatusEffect(unit, SE_DAZE)
    addStatusEffect(unit, SE_DAZE, SE_Dazed, SE_DAZE_TIMER)
def applyMana(unit):
    msg("{u} is charging mana".format(u=unit.name))
    se = unit.status.get(SE_MANA)
    mana = (se.timer if se else 0)
    removeStatusEffect(unit, SE_MANA)
    #charge = unit.skills.get('attunement', 0) #gain more mana per charge w/ this skill
    addStatusEffect(unit, SE_MANA, SE_ManaCharge, mana + 2)
    
        
