#main.py

import game

import pygame
import random

from action import *
from ai import *
from combat import *
from commands import *
from draw import *
from engine import *
from game import *
from hexmap import *
from item import *
from manager import *
from metadata import *
from player import *
from stats import *
from status import *
from unit import *



pygame.init()
pygame.display.set_caption('RPGO')

#turn these into functions
Game.clock=pygame.time.Clock()
Game.disp=pygame.display.set_mode((DISPW,DISPH))
Game.ft_hud=pygame.font.SysFont('Lucida Console', 20)



def main():
    
    #human player 1
    p1=Player.add("human", "The Beatles", pc=True)
    #add the player input/command manager
    Game.addManager(MNG_COMMANDS, CommandManager(p1), "p1 perturn")
    
    #computer player
    c1=Player.add("computer", "Computer")
    Game.addAI(c1, aiBarbarian) #give computer an AI function
    #
    
    #init
    Game.disp.fill(BGCOLOUR)
    Map.create(GRIDWIDTH, GRIDHEIGHT)
    Game.begin(p1, c1) #begin game with the given players


    
    ###TESTING######
    jake=Unit.create(CLS_KNIGHT, SPR_KNIGHT, "Joel", Hex(5,5), p1)
    a=Unit.create(CLS_THIEF, SPR_THIEF, "Chase", Hex(4,5), p1)
    ad=Unit.create(CLS_MONK, SPR_MONK, "Jake", Hex(3,3), p1)
    #jake.stats.addBase('hp',1000)
    #jake.stats.addBase('hpMax',1000)
    juek=Unit.create(CLS_KNIGHT, SPR_KNIGHT, "Billibob", Hex(8,9), c1)
    asd=Unit.create(CLS_KNIGHT, SPR_KNIGHT, "Bobjoe", Hex(10,9), c1)
    asdf=Unit.create(CLS_KNIGHT, SPR_KNIGHT, "Joebob", Hex(7,7), c1)
    #
    #equip(jake, newItem(WP_BALANCEDSWORD), HAND1)
    equip(ad, newItem(WP_QUARTERSTAFF), HAND1)
    equip(a, newItem(WP_DAGGER), HAND1)
    equip(a, newItem(WP_BUCKLER), HAND2)
    #equip(jake, newItem(WP_HALLEBARDE), HAND1)
    #equip(jake, newItem(WP_KATANA), HAND1)
    #equip(jake, newItem(WP_HEATERSHIELD), HAND2)
    equip(jake, newItem(AR_HAUBERK), TORSO)
    equip(jake, newItem(AR_LEATHERGLOVES), ARMS)
    equip(jake, newItem(AR_MAILLELEGGINGS), LEGS)
    equip(jake, newItem(AR_MAILLECOIF), HEAD)
    equip(a, newItem(AR_HAUBERK), TORSO)
    equip(a, newItem(AR_LEATHERGLOVES), ARMS)
    equip(a, newItem(AR_MAILLELEGGINGS), LEGS)
    equip(a, newItem(AR_MAILLECOIF), HEAD)
    equip(ad, newItem(AR_HAUBERK), TORSO)
    equip(ad, newItem(AR_LEATHERGLOVES), ARMS)
    equip(ad, newItem(AR_MAILLELEGGINGS), LEGS)
    equip(ad, newItem(AR_MAILLECOIF), HEAD)
    equip(asd, newItem(AR_FULLPLATE), TORSO)
    equip(asd, newItem(AR_VAMBRACES), ARMS)
    equip(asd, newItem(AR_GREAVES), LEGS)
    equip(asd, newItem(AR_GREATHELM), HEAD)
    
    
    equip(asd, newItem(WP_KATANA), HAND1)
    equip(asdf, newItem(WP_SCIMITAR), HAND1)
    equip(asdf, newItem(WP_MAINGAUCHE), HAND2)
    #equip(asd, newItem(AR_HAUBERK), TORSO)
    equip(asdf, newItem(AR_HAUBERK), TORSO)
    equip(juek, newItem(WP_RAPIER), HAND1)
    equip(juek, newItem(WP_BUCKLER), HAND2)
    #equip(juek, newItem(WP_QUARTERSTAFF), HAND1)
    equip(juek, newItem(AR_HAUBERK), TORSO)
    equip(juek, newItem(AR_LEATHERGLOVES), ARMS)
    equip(juek, newItem(AR_MAILLELEGGINGS), LEGS)
    equip(juek, newItem(AR_MAILLECOIF), HEAD)
    ##/TESTING#####
    
    
    rechargeUnits()
    
    #main loop
    while Game.getIsRunning():
        Game.clock.tick(Game.getFPS())
        
        # Player 1 turn
        print("~~~~~~~~~~~~")
        print(Game.getCurrentPlayer().name)
        print(p1.name)
        if Game.getCurrentPlayer() == p1:
            print('p1')
            drawPhase(p1)
            pc = p1
            
            #check for failure conditions
            if failure(pc):
                drawPhase(pc)
                gameOver()
                continue;

            #pygame events stored into Game object
            Game.inputEvents() 

            #player-turn managers
            Game.runPlayer1Managers()
            
            #check for end of turn conditions
            if playerTurnForcedEnd(pc):
                Game.nextPlayerTurn()
              
        # Other's turn      
        else:
            msg("~~~~~~~~~~~~~~~~ENEMY TURN~~~~~~~~~~~~~~~~")

            player = Game.getCurrentPlayer()
                
            while player != p1:
                print('oi')
                #check for victory conditions
                if failure(player):
                    victory()
                    continue;
                    
                print(Game.aiTurn()) #perform AI fxn for current player
                Game.nextPlayerTurn() #pass the torch
            
            #end the round
            updateStatusEffects()
            removeExpiredEffects()
            unitUpkeep()
            rechargeUnits()
            Game.endRound()
            Game.update()
            msg("~~~~~~~~~~~~~~~~YOUR  TURN~~~~~~~~~~~~~~~~")
        
        
    #/loop
#/main


if __name__ == "__main__":
    main()
    


