import  pygame as pg
vec = pg.math.Vector2

TITLE ="Cry and Wipe"
WIDTH = 1024 # 16 *64 or 32*32 or 64 * 16
HEIGHT = 768 # 16*48 or 32*24 or 64 * 12
FPS = 60


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)
YELLOW = (255, 255, 0)
BROWN =(106,55,5)

BGCOLOR = BROWN
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# WALL_IMG
WALL_IMG = "/Tiles/tile_538.png"

# level

LEVEL = [0,'level1.tmx','level2.tmx']

# Player setttings

PLAYER_SPEED = 300
PLAYER_IMAGE = "manBlue_hold.png"
PLAYER_ROT_SPEED = 250
PLAYER_HIT_RECT = pg.Rect(0,0,35,35)
BARREL_OFFSET = vec(30, 0)
KICKBACK = 200
PLAYER_HEALTH = 100


# Weapon settings
BULLET_IMG = '/bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,#how fast the bullet go
                     'bullet_lifetime': 10000,#how long it exists
                     'rate': 250,# how fast can you shoot it
                     'kickback': 200,# push back
                     'spread': 5,# accuracy
                     'damage': 100,
                     'bullet_size': 'lg',
                     'bullet_count': 1,
                     'weapon_img':'weapon_gun.png',
                     'max_bullets': 2,
                     'left': 4,
                     }
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 5,
                      'bullet_size': 'sm',
                      'bullet_count': 12,
                      'weapon_img':'weapon_gun.png',
                      'max_bullets': 4,
                      'left': 30}
WEAPONS['bazuka'] = {'bullet_speed': 400,
                      'bullet_lifetime':999999,
                      'rate': 900,
                      'kickback': 1000,
                      'spread': 0,
                      'damage': 555,
                      'bullet_size': 'lg',
                      'bullet_count': 1,
                      'weapon_img':'weapon_gun.png',
                      'max_bullets': 1,
                      'left': 30}

# Mob
MOB_IMG = "zoimbie1_hold.png"
MOB_SPEED = [200,400,350,250,125]
MOB_HIT_RECT = pg.Rect(0,0,30,30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400
SPLAT = 'splat green.png'

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]



# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEM_LAYER = 1

# items
ITEM_IMAGE = {'health': 'health_pack.png',
              'shotgun':'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 30
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sound
# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav'],
                 'bazuka':['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}