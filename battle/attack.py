'''
    Program: Create Class example
    Author: Jhonasttan Regalado
    Copyright: 2018
'''

#import random

from classes.enemy import Enemy
     
enemy1 = Enemy(200,60)
print("HP:", enemy1.get_hp())

#enemy2 = Enemy(75,90)
#enemy2.getAtk()
#enemy2.getHp()
        
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