import pickle
import random


#monsters = {} 
'''
monster name (key), monster level, monster hp
'''


playerProfile = pickle.load( open( "character.p", "rb" ))
monsters = pickle.load( open( "monsters.p", "rb" ))


#Player profile dictionary order: playerName (key), playerClass, level, hp, gold, strg, dext, intel, wisd, charm

#todo: Hit points calculation --done //need to figure out leveling and adding hp for new level.
#todo: level claculation
#todo: gold and reward calculation
#todo: priest heal module / visit a healer module / healing potions
#idea. Adding an adventure module system.  Can't play a module until level is reached.
#idea. Module replayability.  Create random monster generator module.
#idea. Game could support multiple users.  Into screen asks if new player or not. If nnot, load player from list of names ... password protect?


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
	level = 1
	gold = 1
	hp = strg + dext + intel + wisd + charm / 2
	
	print(name+', here are your stats: Strength:',strg,'Dexterity:',dext,'Intelligence:',intel,'Wisdom:',wisd,'Charisma:',charm)
	
	playerClass = input('Now that you have seen your stats, what type of adventurer are you: [warrior, rogue, mage]')
	
	playerProfile[name] = playerClass, level, round(hp), gold, strg, dext, intel, wisd, charm
	
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


def loadStats(playerName):
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
	
	#print('Name:',x,'Class:',playerClass,'Level:',level,'HP:',hp,'Strength:',strg,'Dexterity:',dext,'Intel:',intel,'Wisdom:',wisd,'Charisma:',charm)
	
	#print (playerProfile[x][0]) #lists items from playerProfile
	#mainMenu(x)		


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
	
	print('Name:',x,'\nClass:',playerClass,'\nLevel:',level,'\nHP:',hp,'\nGold:',gold,'\nStrength:',strg,'\nDexterity:',dext,'\nIntel:',intel,'\nWisdom:',wisd,'\nCharisma:',charm)
	
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
		
		
	elif adminChoice ==3:
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
	




def enterTavern(playerName):
	
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
	
	print('You walk throuh the door of the Shady Oak tavern and notice that the place is \
almost empty.  The fire in the hearth has mostly gone out and the only sources of light \
are a greasy oil lap close to the bar and the small amount of light coming through the door\
and the filthy windows.  You walk up to the bar and knock three times.')
	print('	After a minute or so the tavern owner comes out from the back and looks up up and down \
with a sneer.  "Where the hell did you come from?"  Can''t you tell we are closed for business?!')
	
	print('What would you like to do:')
	print('[1] Ask for a drink.')
	print('[2] Ask for some food?)')
	print('[3] Ask where all the customers are.')
	print('[4] Exit the Tavern.')
	
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
		print('"Where are all ths customers," you ask.  The bar keep softens his tone a bit and says," All \
	gone due to this rat infestation!  Those little monsters are eating me out of house and home!  I can''t\
	make ale or bread without grain and nobody wants stew without some hearty bread along with it!')
		
		x = input('Do you offer your services in echange for a small fee? (y/n) ')
		
		if x == 'y' or x == 'Y':
			print('I will help rid your tavern of Rats!')
		else:
			print('That is tough luck! cya!')
				
	
	
	elif act1 == 4:
		mainMenu(playerName)
		
	else:
		print('The barkeep screams, "What the hell to you mean by that!" \
		and throws a punch at you.'	)		
	
	


						
def mainMenu(playerName):

	playerName = playerName
	
	print('Welcome',playerName+'!')
	print('--------------------------')
	print('[1] Visit local tavern.')
	print('[2] Hunt in the forrest.')
	print('[3] Check for bounties.')
	print('[4] Player Stats.')
	print('[5] Save game.')
	print('[6] Game Admin')
	print('[7] Exit game.')
			
	print('--------------------------')	
	
	actionChoice = input('What would you like to do today? (1-5)')
	
	actionChoice = int(actionChoice)
	
	if actionChoice == 1:
		#print('You enter the tavern.')
		enterTavern(playerName)
		mainMenu(playerName)
	
	elif actionChoice == 2:
		print('You enter the forrest.')
		mainMenu(playerName)
		
	elif actionChoice == 3:
		print('You ask around about bounties')
		mainMenu(playerName)
		
	elif actionChoice == 4:
		showStats(playerName)
		mainMenu(playerName)
	
	elif actionChoice == 5:
		pickle.dump( playerProfile, open( "character.p","wb") )	
		print('Saving adventurer data.')
		mainMenu(playerName)
		
	elif actionChoice == 6:
		gameAdmin(playerName)	
	
	elif actionChoice == 7:
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
