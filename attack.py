'''
    Program: Create Class example
    Author: Jhonasttan Regalado
    Copyright: 2018
'''

import random

class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
            self.atkl = atkl
            self.atkh = atkh
        
                
    def getAtk(self):
        print("atk is", self.atkl)
        
    def getHp(self):
        print("HP is", self.hp)
        
enemy1 = Enemy(40,49)
enemy1.getAtk()
enemy1.getHp()


enemy2 = Enemy(75,90)
enemy2.getAtk()
enemy2.getHp()
        
'''

playerhp = 260
enemytkl = 60
enemytkh = 80

while playerhp > 0:
    dmg = random.randrange(enemytkl, enemytkh)
    playerhp = playerhp - dmg
    
    if playerhp <= 30:
            playerhp = 30
            
    print("Enemy strikes for", dmg, "points of damange. Current HP is", playerhp)
    
    if playerhp > 30:
        continue
        
    print("You have low health")
    break
        
'''      