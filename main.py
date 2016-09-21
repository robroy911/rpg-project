import pickle
import random
import os


#create character and monster files i they don;t already exist.

if not os.path.exists('character.p'):
    open('character.p', 'w').close()
    
if not os.path.exists('monsters.p'):
    open('monsters.p', 'w').close()    

'''
monster name (key), monster level, monster hp
'''

#load character and monster dictionaries or create new ones.

try:

	playerProfile = pickle.load( open( "character.p", "rb" ))

except:
	playerProfile = {}

try:
	monsters = pickle.load( open( "monsters.p", "rb" ))

except:
	monsters = {}
	 

#todo: Hit points calculation --done
#todo: visit a healer module --done. 
#idea. Game could support multiple users.  Into screen asks if new player or not. If not, load player from list of names // done.
#todo: need to figure out leveling and adding hp for new level. --done.
#todo: gold and reward calculation --gold added as reward for quests
#idea. Adding an adventure module system.  Can't play a module until level is reached.
#idea. Module replayability.  Create random monster generator module.



'''
I/O commands for loading and saving dictionary.

#opens file
playerProfile = pickle.load( open( "character.p", "rb" ))

#saves file
pickle.dump( studentList, open( "character.p","wb") )	

'''

def rollStats(playerName):

	name = playerName
	strg = random.randint(1,18)
	dext = random.randint(1,18)
	intel = random.randint(1,18)
	wisd = random.randint(1,18)
	charm = random.randint(1,18)
	level = 0
	gold = 1
	hp = strg + dext + intel + wisd + charm / 2
	xp = 0
	currentHP = strg + dext + intel + wisd + charm / 2
	
	print(name+', here are your stats: Strength:',strg,'Dexterity:',dext,'Intelligence:',intel,'Wisdom:',wisd,'Charisma:',charm)
	
	playerClass = input('Now that you have seen your stats, what type of adventurer are you: [warrior, rogue, mage]')
	
	playerProfile[name] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, xp, round(currentHP)
	
	mainMenu(playerName)


def newPlayer():
	print('Before we start down the trail to legenary adventures and fame ...')
	playerName = input('What is your name? ')

	alreadyExists = existingPlayer(playerName)
						
	print('Well met',playerName)
	playerAge = input('How old are you? ')
	playerAge = int(playerAge)
	
	if playerAge < 15:
		print('You are scrappy, but I am afraid you aren''t old enough for this adventure.  Come back in a few years.')
		exit()
	elif playerAge >= 15 and playerAge <= 18:
		print('You have spirit, I''ll give you that.  Know which end of a sword to use? Haha!')
		rollStats(playerName)
	elif playerAge > 18 and playerAge < 45:
		print('Welcome!  Looking forward to seeing what you can do!')
		rollStats(playerName)
	elif playerAge >= 45 and playerAge < 60:
		print('You are getting a bit up there, but we will what you can do!')
		rollStats(playerName)
	else:
		race = input('Are you an elf or dwarf? y/n')
		if race == 'y' or race == 'Y':
			rollStats(playerName)
		else:
			print('Unless you are an elf or dwarf this isn''t the adventure for you!')
			exit()		  	

		
def loadPlayer():

		print('Here are the existing players name:',playerProfile.keys())
		playerName = input('Which player would you like you load? ')
		
		if playerName in playerProfile.keys():
			mainMenu(playerName)
		else:
			'Invalid Character.  Returning to start ...'



def showStats(playerName):
	x = playerName
	
	playerClass = playerProfile[x][0] 
	level = playerProfile[x][1] 
	hp = playerProfile[x][2]
	gold = playerProfile[x][3] 
	strg = playerProfile[x][4]  
	dext = playerProfile[x][5] 
	intel = playerProfile[x][6] 
	wisd = playerProfile[x][7] 
	charm = playerProfile[x][8]
	xp = playerProfile[x][9]
	currentHP = playerProfile[x][10]	
	
	print('Name:',x,'\nClass:',playerClass,'\nLevel:',level,'\nXP:',xp,'\nHP:',hp,'\nCurrent hp:',currentHP,'\nGold:',gold,'\nStrength:',strg,'\nDexterity:',dext,'\nIntel:',intel,'\nWisdom:',wisd,'\nCharisma:',charm)
	
	#print (playerProfile[x][0]) #lists items from playerProfile
	mainMenu(x)		



def existingPlayer(playerName):
	if playerName in playerProfile.keys():
		print('Player name already in use.  Please try another name.')
		main()
	else:
		pass
		

def gameAdmin(playerName):

	playerName = playerName
		
	print('Admin Options')
	print('------------------------')
	print('[1] Create a monster.')
	print('[2] Save monster changes.')
	print('[3] List all monsters.')
	print('[4] Delete a player profile.')
	print('[5] Save player profile changes.')
	print('[6] Return to main menu.') 	
	print('--------------------------')	

	adminChoice = input('What would you like to do? (1-5)')
	
	adminChoice = int(adminChoice)
	
	if adminChoice == 1:# Create a monster
		createMonster()
		gameAdmin(playerName)

	elif adminChoice == 2: #save monster changes
		pickle.dump(monsters, open( "monsters.p","wb"))
		gameAdmin(playerName)
		
		
	elif adminChoice ==3: #list existing monsters
		m = list(monsters.keys())
		m.sort()
		print(m)
		gameAdmin(playerName)
		
	elif adminChoice == 4: #delete a player profile
		l = list(playerProfile.keys())
		l.sort()
		print(l)
		x = input('Which player would you like to delete? ')
		
		if x in playerProfile.keys():
			del playerProfile[x]
			gameAdmin(playerName)
		else:
			print('Player profile not found.')
			gameAdmin(playerName)
		
	elif adminChoice == 5: #save player profile changes
		pickle.dump( playerProfile, open( "character.p","wb") )	
		gameAdmin(playerName)
	
	elif adminChoice == 6: #return to main menu.
		mainMenu(playerName)


def createMonster():
	
	m = input('Enter monster name: ')
	mLevel = input('Enter monster level:')
	mHP = int(mLevel) + random.randint(1,6)
	mHP = mHP
	monsters[m]=[mLevel,mHP]
	


def randomMob(playerName):
	
	x = playerName
	
	playerClass = playerProfile[x][0] 
	level = playerProfile[x][1] 
	hp = playerProfile[x][2]
	gold = playerProfile[x][3] 
	strg = playerProfile[x][4]  
	dext = playerProfile[x][5] 
	intel = playerProfile[x][6] 
	wisd = playerProfile[x][7] 
	charm = playerProfile[x][8]
	xp = playerProfile[x][9]
	currentHP = playerProfile[x][10]			
	
	m = random.choice(list(monsters.keys()))
			
	mob = monsters[m][1]

	numMob = random.randint(1,4)
	mob = mob * numMob
	mobXP = mob * numMob
	playerHP = playerProfile[x][10]
		
	playerDamage = random.randint(1,6)
	mobDamage = random.randint(1,monsters[m][1])
			

	while True:
				
			if mob < 0:
				print('The',m,'have been defeated!')
				rewardGold = random.randint(1,10)
									
				del playerProfile[x]
				gold = gold + rewardGold
				xp = xp + mobXP
				playerProfile[x] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, xp, round(playerHP)
				
				break
			elif playerHP < 0:
				print('You have been killed.')
				
				xp = xp - mobXP
				del playerProfile[x]
				playerProfile[x] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, xp, round(playerHP)
				break

			else:
				mob = mob - playerDamage
				print('You did',playerDamage,'damage!')
				
				playerHP = playerHP - mobDamage
				print(m,'did',mobDamage,'damage!')
			

def huntingAccident(playerName):
	
	x = playerName
	
	playerClass = playerProfile[x][0] 
	level = playerProfile[x][1] 
	hp = playerProfile[x][2]
	gold = playerProfile[x][3] 
	strg = playerProfile[x][4]  
	dext = playerProfile[x][5] 
	intel = playerProfile[x][6] 
	wisd = playerProfile[x][7] 
	charm = playerProfile[x][8]
	xp = playerProfile[x][9]
	currentHP = playerProfile[x][10]
	
	PlayerXP = playerProfile[x][9]
	
	deathPenaltyXP = PlayerXP - 100
	
	del playerProfile[x]
	playerProfile[x] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, deathPenaltyXP, round(0)
				


def enterForrest(playerName):

	x = playerName
	q = random.randint(1,20)
	p = ['deer','chicken','beaver','moose','squirrl','owl','bobcat','chipmunk','hedgehog']
	animal = random.choice(p)
	
		
	print('You arrise early in the morning and head into the forrest to hunt.')
	
	if q >= 17:
		#no encounters
		print('You spend an uneventuful day hunting.)')
		mainMenu(x)
	elif q < 17 and q >= 13:
		#animal encounter
		print('Not log after entering the forrest you head a twig snap and a sound\
		coming from the woods around you.  You aren''t alone.  You brace yourself for \
		attack knowing that some foul creatures inhabit this forrest.  Just as you are about\
		to flee a',animal,'runs right past you.  You are so statled that you forget to shoot at it.\
		You decide to head back home empty handed.')
		mainMenu(x) 
	elif q < 13 and q >= 2:
		#monster encounter
		print('Not log after entering the forrest you head a twig snap and a sound\
		coming from the woods around you.  You aren''t alone.  You brace yourself for \
		attack knowing that some foul creatures inhabit this forrest.')
		randomMob(x)
		mainMenu(x)
		
	elif q == 1:
		huntingAccident(x)
		print('You have a fatal hunting accident and die.')
		mainMenu(x)
		

def fightRats(playerName):
	
	x = playerName
	
	playerClass = playerProfile[x][0] 
	level = playerProfile[x][1] 
	hp = playerProfile[x][2]
	gold = playerProfile[x][3] 
	strg = playerProfile[x][4]  
	dext = playerProfile[x][5] 
	intel = playerProfile[x][6] 
	wisd = playerProfile[x][7] 
	charm = playerProfile[x][8]
	xp = playerProfile[x][9]
	currentHP = playerProfile[x][10]			
	
	print('"Where are all ths customers," you ask.  The bar keep softens his tone a bit and says," All \
	gone due to this rat infestation!  Those little monsters are eating me out of house and home!  I can''t\
	make ale or bread without grain and nobody wants stew without some hearty bread along with it!')
		
	s = input('Do you offer your services in echange for a small fee? (y/n) ')
		
	if s == 'y' or x == 'Y':
		print('I will help rid your tavern of Rats!')
		print('Excellent!  Some of those jokers are pretty big!  Take this old sword some drunk fool left \
		as payment for his tab.  If you make it out I might have a gold piece for you as well.')
		
		m =  'Rat'
		
		rats = monsters[m][1]

				
		numRats = random.randint(1,5)
		rats = rats * numRats
		ratsXP = rats * numRats
		playerHP = playerProfile[x][10]
		
		playerDamage = random.randint(1,6)
		ratsDamage = random.randint(1,3)
		
		
		print('You head past the bar and straight to the cellar door.  Opening the door reveals the foul stench of overripe \
		 yeast mixed with the smell of vermin.  You look down at the sword in your hand.  It''s heavy, spotted with rust,\
		and very dull, but should do the job.  As you head down the stairs, you light a candle to see by and are stunned to see \
		',numRats,'very large rats digging though sacks of grain and bags of rotten fruit.  One of them stops and sniffs the air and growls\
		in a way no rodent you have ever seen before growls.  In unison they turn and head in your direction.')
		

		while True:
				
				if rats < 0:
					print('The rats have been exterminated!')
					rewardGold = random.randint(1,3)
					print('You leave the basement and report your sucess to the owner.  He is over joyed and offers you \
					',rewardGold,'gold for your work.')
										
					del playerProfile[x]
					gold = gold + rewardGold
					xp = xp + ratsXP
					playerProfile[x] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, xp, round(playerHP)
					
					break
				elif playerHP < 0:
					print('You have been killed.')
					
					xp = xp - ratsXP
					del playerProfile[x]
					playerProfile[x] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, xp, round(playerHP)
					break

				else:
					rats = rats - playerDamage
					print('You did',playerDamage,'damage!')
					
					playerHP = playerHP - ratsDamage
					print('Rats did',ratsDamage,'damage!')
						
	else:
		print('That is tough luck! cya!')
	



def enterTavern(playerName):
	
	x = playerName
	
	print('You walk throuh the door of the Shady Oak tavern and notice that the place is \
		   almost empty.  The fire in the hearth has mostly gone out and the only sources of light \
are a greasy oil lap close to the bar and the small amount of light coming through the door\
and the filthy windows.  You walk up to the bar and knock three times.')
	print('	After a minute or so the tavern owner comes out from the back and looks up up and down \
with a sneer.  "Where the hell did you come from?"  Can''t you tell we are closed for business?!')
	
	print('What would you like to do:')
	print('------------------------')
	print('[1] Ask for a drink.')
	print('[2] Ask for some food?)')
	print('[3] Ask where all the customers are.')
	print('[4] Exit the Tavern.')
	print('------------------------')
	
	
	act1 = input('Choose [1-4]')
	act1 = int(act1)
	
	if act1 == 1:
		print('"Got anything to drink," you ask as politely as possible.  The bar tenders looks at you\
	like you are daft and asked if you understant common or are just a smart mouth.  He tells you to get \
	the hell out and don''t come back unil you have more sense')
				
	elif act1 == 2:
		print('"Got anything to eat," you ask as politely as possible.  The bar tenders looks at you\
	like you are daft and asked if you understant common or are just a smart mouth.  He tells you to get \
	the hell out and don''t come back unil you have more sense')
		
	elif act1 == 3:
		fightRats(x)

	
	elif act1 == 4:
		mainMenu(playerName)
		
	else:
		print('The barkeep screams, "What the hell to you mean by that!" \
		and throws a punch at you.'	)		
	
	
def visitHealer(playerName):
	
	x = playerName
	
	playerClass = playerProfile[x][0] 
	level = playerProfile[x][1] 
	hp = playerProfile[x][2]
	gold = playerProfile[x][3] 
	strg = playerProfile[x][4]  
	dext = playerProfile[x][5] 
	intel = playerProfile[x][6] 
	wisd = playerProfile[x][7] 
	charm = playerProfile[x][8]
	xp = playerProfile[x][9]
	currentHP = playerProfile[x][10]	
	
	playerHP = playerProfile[x][2]
	
	if gold >0:
	
		healChoice = input('Healing costs 1 gold ... are you sure? (y/n)')
	
		if healChoice == 'y' or healChoice=='Y':
			print('begin healing')
			gold = gold -1
			playerHP = hp
			
			del playerProfile[x]
			
			playerProfile[x] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm, xp, round(playerHP)
						
		else:
			print('Sorry, come back when you are a little less cheap!')
			mainMenu(x)
			
	else:
		
		print('I am sorry, but you don''t have enough gold to pay the healer.')
		mainMenu(x)		


def updateLevel(playerName):
	
	x = playerName
	
	playerClass = playerProfile[x][0] 
	level = playerProfile[x][1] 
	hp = playerProfile[x][2]
	gold = playerProfile[x][3] 
	strg = playerProfile[x][4]  
	dext = playerProfile[x][5] 
	intel = playerProfile[x][6] 
	wisd = playerProfile[x][7] 
	charm = playerProfile[x][8]
	xp = playerProfile[x][9]
	currentHP = playerProfile[x][10]	
	
	currentLevel = playerProfile[x][1]
	newLevel = xp / 1000
	
	
	if currentLevel > newLevel:
		print('No level increase has been earned.')
	
	elif currentLevel < newLevel:
	
		level = level + 1
		newLevelXP = hp + random.randint(1,20)
		
		del playerProfile[x]
			
		playerProfile[x] = playerClass, level, round(newLevelXP), gold, strg, dext, intel, wisd, charm, xp, round(currentHP)
							
	mainMenu(x)			   


def millersDaughter(playerName):
	print('You decide to looking into the kidnapping of the millers daughter.')
	
def thievesForrest(playerName):
	print('You decide to help tame the thieves forrest.')
	
def silverTooth(playerName):
	print('You have decided to hunt down ole silvertooth.')

def hauntedMine(playerName):
	
	x = playerName
	
	print('The local mine has been a constant source of wealth for the community for many, many years.\
	while not the only source of income, it has been a staple until recently.  Workers have become more and more \
	fearful that somehting other worldly is enhabiting the mines.  As with all mines, this mine has seen it''s fair share of tragedy.\
	There are well marked tunnles deep in the mine that have never been fully explored and more than a few miners have gone missing down\
	those unexplored corridors.\
	\
	Rumor has it that even a rescurer or two has gone down to help finder lost miners and never returned.')
	print('------------------------')
	mineChoice = input('Investigate the haunted mine? (y/n)')
	
	if mineChoice =='y' or mineChoice =='Y':
		print('Start mine adventure.')
		
	else:
		print('You big chicken!!! ... Returning to main menu.')
		mainMenu(x)	
	
	
	
def rumorMill():
	p = ['The blacksmith''s son has''t been seen since the millers daughter went missing.',
		 'I hear that the mine is haunted.  Voices are always echoing around, even after everyone is gone.',
		 'Someone has been stealing the lord''s horses again!  I bet they are all over in the thieves forrest.',
		 'The harvest this year had better be better than the last.  If not, we all might starve this winter.',
		 'Someone said the Shady Oak is back in business.  Wonder if it'' cleaner in there now>?',
		 'Someone needs to kill silvertooth once and for all.  We can;t keep loosing our livestock to that beast!',
		 'It''s hardly safe to go into the forrest to hunt these days.  You never know what kind of monsters are lurking there!'
		 ]
	
	rumor = random.choice(p)
	
	print(rumor)			
	




def checkBounties(playerName):
	
	x = playerName
	
	print('You enter the local constables office and see a list of bounties.')
	print('------------------------')
	print('[1] Millers daughter kidnapped.')
	print('[2] Thieves forrest.')
	print('[3] Kill ole silvertooth.')
	print('[4] The Haunted mine.')
	print('[5] Ask about rumors.')
	print('[6] Leave the office.')
	print('------------------------')

	bountyChoice = input('What would you like to do?')
	bountyChoice = int(bountyChoice)
	
	
	if bountyChoice == 1:
		
		millersDaughter(x)
		mainMenu(x)	
		
	elif bountyChoice == 2:
		
		thievesForrest(x)
		mainMenu(x)	
		
		
	elif bountyChoice == 3:
		
		silverTooth(x)
		mainMenu(x)	
		
	elif bountyChoice == 4:
		
		hauntedMine(x)
		mainMenu(x)	
			
		
	elif bountyChoice == 5:
		
		rumorMill()
		mainMenu(x)		
		
	elif bountyChoice == 6:
		
		mainMenu(x)	
		
	else:
		print('We didn''t understand that.  Get out!')
		mainMenu(x)									
	
	
				
def mainMenu(playerName):

	playerName = playerName
	
	print('Welcome',playerName+'!')
	print('--------------------------')
	print('[1] Visit local tavern.')
	print('[2] Hunt in the forrest.')
	print('[3] Check for bounties.')
	print('[4] Visit a healer or get resurrected.')
	print('[5] Player Stats.')
	print('[6] Save game.')
	print('[7] Game Admin')
	print('[8] Level Up.')
	print('[9] Exit game.')
			
	print('--------------------------')	
	
	actionChoice = input('What would you like to do today? (1-9)')
	
	actionChoice = int(actionChoice)

	
	playerXP = playerProfile[playerName][10]
	
	if playerXP <= 0:
		print('You must be healed before continuing ...')
		visitHealer(playerName)
	else:		
		if actionChoice == 1:
			enterTavern(playerName)
			mainMenu(playerName)
		
		elif actionChoice == 2:
			
			enterForrest(playerName)
			mainMenu(playerName)
			
		elif actionChoice == 3:
			checkBounties(playerName)
			mainMenu(playerName)
		
		elif actionChoice == 4:

			visitHealer(playerName)
			
		elif actionChoice == 5:
			showStats(playerName)
			mainMenu(playerName)
		
		elif actionChoice == 6:
			pickle.dump( playerProfile, open( "character.p","wb") )	
			print('Saving adventurer data.')
			mainMenu(playerName)
			
		elif actionChoice == 7:
			gameAdmin(playerName)
			
		elif actionChoice == 8:
			updateLevel(playerName) 		
		
		elif actionChoice == 9:
			pickle.dump( playerProfile, open( "character.p","wb") )	
			print('Saving adventurer data.')
			exit()
			
		else:
			print('Invalid selection.')			 	
	

def main():
	firstTime = input('Welcome!  Is this your first time playing? (y/n) ')
	
	if firstTime =='Y' or firstTime =='y':
		print('welcome to this game.  It''s rather buggy and you will likely be killed at \
some point along the way.  Don''t let a little thing like death ruin the fun though!  If you die, \
visit a healer and get resurrected ... for a small fee of course.  You will be after all only \
"mostly dead".  Anyway, have fun and send me bug notes.  Thanks!')
		
		
		newPlayer()
		
	else:
		
		loadPlayer()
		

	
main()	
