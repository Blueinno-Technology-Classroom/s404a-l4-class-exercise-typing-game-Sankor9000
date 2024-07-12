import pgzrun
from pgzhelper import *
import random

WIDTH = 1000
HEIGHT = 700

zombie_run_img = ['zombie/run/tile002',
                  'zombie/run/tile003',
                  'zombie/run/tile004',
                  'zombie/run/tile005']

player_idle_img = ['player/idle/tile000',
                   'player/idle/tile001',
                   'player/idle/tile002',
                   'player/idle/tile003',
                   'player/idle/tile004',
                   'player/idle/tile005',
                   'player/idle/tile006',
                   'player/idle/tile007',
                   'player/idle/tile008',
                   'player/idle/tile009']

player_die_img = ['player/death/tile000',
                  'player/death/tile001',
                  'player/death/tile002',
                  'player/death/tile003',
                  'player/death/tile004',
                  'player/death/tile005',
                  'player/death/tile006',
                  'player/death/tile007',
                  'player/death/tile008']

player_attack_img = ['player/attack/tile000',
                     'player/attack/tile001',
                     'player/attack/tile002',
                     'player/attack/tile003']

zombie_die_img = ['zombie/die/tile014',
                  'zombie/die/tile015',
                  'zombie/die/tile016',
                  'zombie/die/tile017',
                  'zombie/die/tile018',
                  'zombie/die/tile019',
                  'zombie/die/tile020',
                  'zombie/die/tile021',
                  'zombie/die/tile022',
                  'zombie/die/tile023',
                  'zombie/die/tile024']

fireball_img = ['fireball/fb1',
                'fireball/fb2',
                'fireball/fb3',
                'fireball/fb4',
                'fireball/fb5']

fireball = Actor(fireball_img[0])
fireball.images = fireball_img
fireball.scale = 4
fireball.fps = 20
fireball.active = False
fireball.x = 0

zombie = Actor(zombie_run_img[0])
zombie.images = zombie_run_img
zombie.scale = 5
zombie.fps = 5
zombie.right = WIDTH + 100
zombie.bottom = HEIGHT

player = Actor(player_idle_img[0])
player.images = player_idle_img
player.left = 50
player.bottom = HEIGHT
player.scale = 2
player.fps = 5

word_list = ['James', 'Mary', 'Michael', 'Patricia', 'Robert', 'Jennifer', 'John', 'Linda', 'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Karen', 'Christopher', 'Sarah', 'Charles', 'Lisa', 'Daniel', 'Nancy', 'Matthew', 'Sandra', 'Anthony', 'Betty', 'Mark', 'Ashley', 'Donald', 'Emily', 'Steven', 'Kimberly', 'Andrew', 'Margaret', 'Paul', 'Donna', 'Joshua', 'Michelle', 'Kenneth', 'Carol', 'Kevin', 'Amanda', 'Brian', 'Melissa', 'Timothy', 'Deborah', 'Ronald', 'Stephanie', 'George', 'Rebecca', 'Jason', 'Sharon', 'Edward', 'Laura', 'Jeffrey', 'Cynthia', 'Ryan', 'Dorothy', 'Jacob', 'Amy', 'Nicholas', 'Kathleen', 'Gary', 'Angela', 'Eric', 'Shirley', 'Jonathan', 'Emma', 'Stephen', 'Brenda', 'Larry', 'Pamela', 'Justin', 'Nicole', 'Scott', 'Anna', 'Brandon', 'Samantha', 'Benjamin', 'Katherine', 'Samuel', 'Christine', 'Gregory', 'Debra', 'Alexander', 'Rachel', 'Patrick', 'Carolyn', 'Frank', 'Janet', 'Raymond', 'Maria', 'Jack', 'Olivia', 'Dennis',
             'Heather', 'Jerry', 'Helen', 'Tyler', 'Catherine', 'Aaron', 'Diane', 'Jose', 'Julie', 'Adam', 'Victoria', 'Nathan', 'Joyce', 'Henry', 'Lauren', 'Zachary', 'Kelly', 'Douglas', 'Christina', 'Peter', 'Ruth', 'Kyle', 'Joan', 'Noah', 'Virginia', 'Ethan', 'Judith', 'Jeremy', 'Evelyn', 'Christian', 'Hannah', 'Walter', 'Andrea', 'Keith', 'Megan', 'Austin', 'Cheryl', 'Roger', 'Jacqueline', 'Terry', 'Madison', 'Sean', 'Teresa', 'Gerald', 'Abigail', 'Carl', 'Sophia', 'Dylan', 'Martha', 'Harold', 'Sara', 'Jordan', 'Gloria', 'Jesse', 'Janice', 'Bryan', 'Kathryn', 'Lawrence', 'Ann', 'Arthur', 'Isabella', 'Gabriel', 'Judy', 'Bruce', 'Charlotte', 'Logan', 'Julia', 'Billy', 'Grace', 'Joe', 'Amber', 'Alan', 'Alice', 'Juan', 'Jean', 'Elijah', 'Denise', 'Willie', 'Frances', 'Albert', 'Danielle', 'Wayne', 'Marilyn', 'Randy', 'Natalie', 'Mason', 'Beverly', 'Vincent', 'Diana', 'Liam', 'Brittany', 'Roy', 'Theresa', 'Bobby', 'Kayla', 'Caleb', 'Alexis', 'Bradley', 'Doris', 'Russell', 'Lori', 'Lucas', 'Tiffany']

question = random.choice(word_list)
question = question.lower()
response = ''

def update():
    global response
    zombie.animate()
    player.animate()
    fireball.animate()
    if not(player.image in player_die_img) and not(zombie.image in zombie_die_img):
        zombie.x -= 5
        player.fps = 20
    if player.image == player_attack_img[-1]:
        player.images = player_idle_img
    if zombie.image == zombie_die_img [-1]:
            zombie.images = zombie_run_img
            zombie.x = WIDTH +100
    if player.image == player_die_img[-1]:
        player.images = player_idle_img
    if zombie.left <= 0:
        zombie.right = WIDTH + 100
        response = ''
    if zombie.collide_pixel(player) and not(player.image in player_attack_img):
        zombie.right = WIDTH + 100
        response = ''
        player.images = player_die_img
    if fireball.active:
        fireball.move_forward(10)
        if fireball.collide_pixel(zombie):
            fireball.active = False
            fireball.x = 0
            zombie.images = zombie_die_img

def on_key_down(key):
    global response, question

    if key in range(97, 123):
        print(chr(key))
        response += chr(key)
    elif key == keys.SPACE:
        if response == question:
            print('correct')
            response = ''
            question = random.choice(word_list).lower()
            player.images = player_attack_img
            fireball.y = player.y
            fireball.active = True
    elif key == keys.BACKSPACE:
        response = response[0:-1]

def draw():
    screen.clear()
    screen.draw.text(question, (50, 100), fontsize=120)
    screen.draw.text(response, (50, 100), fontsize=120, color= 'green')
    zombie.draw()
    player.draw()
    if fireball.active:
        fireball.draw()

pgzrun.go()