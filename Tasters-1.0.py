import pgzero
import pgzrun
from pgzhelper import *
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Tasters"

timer = 0
current_time = timer
score = 0
countdown = 61
need = 4
x = random.randint(1, 5)
scenario = " "
scene = "menu_one"
main_enter = "newgame"
level = 1
level_list = [["Yard", "Entrance", "Ghetto", "Dump"], ["Bar", "Restaurant", "Villa", "Yacht"]]
level_name = " "


eat_list = ['morkov.png', 'bread.png', 'sausage1.png', 'batlevin.png', 'chips.png',
       'tomat.png', 'ogurets.png', 'kognak.png', 'cheese.png', 'ice.png',
       'sausage.png', 'banan.png', 'vodka.png', 'beer1.png', 'beer2.png',
       'vine.png', 'doshik.png', 'burger.png', 'crab.png']

noeat_list = ['duck.png', 'ball.png', 'mysor.png', 'flowers.png', 'wheel.png',
         'sigar.png', 'sponge.png', 'candom.png', 'trunks.png', 'scovoroda.png',
         'shoe.png', 'socks.png', 'cat.png', 'batary.png', 'golub.png',
         'kal.png', 'kanistra.png', 'shpric.png',
         'iron.png', 'korobka.png', 'shapka.png']

poor = [['dvor_1.png', 'dvor_3.png','dvor_2.png', 'dvor_5.png', 'dvor_4.png'],
        ['padik_2.png','padik_3.png', 'padik_1.png', 'padik_4.png'],
        ['dvor_getto1.png', 'dvor_getto2.png', 'dvor_getto3.png'],
        ['pomoika_1.png', 'pomoika_2.png', 'pomoika_3.png']]

rich = [['bar_2.png', 'bar_3.png', 'bar_1.png'],
        ['rest_5.png', 'rest_4.png', 'rest_3.png', 'rest_2.png', 'rest_1.png'],
        ['villa_2.png', 'villa_3.png', 'villa_1.png'],
        ['yaht_1.png', 'yaht_2.png', 'yaht_3.png']]

poorman = ["poor", "poor_opn", "poor_blev"]
richman = ["rich", "rich_opn", "rich_blev"]

player = Actor(poorman[0], pos = (400, 450))
location = Actor(random.choice(poor[0]), topleft = (0,0))
obj = Actor(random.choice(eat_list), pos = (random.randint(50, 750), random.randint(-100, -50)))
object_list = [obj]

main_logo = Actor("logo", topleft = (0,0))
main_menu = Actor("main_menu", pos = (400,700))
main_tasters = Actor("tasters", pos = (400,-50))
menu_empty = Actor("menu_2", topleft = (0,0))
menu_empty_2 = Actor("menu_empty", topleft = (0,0))
newgame_text = Actor("newgame_text", pos = (400, 800))
rulesgame_text = Actor("jim_rulesgame_text", pos = (400, 700))
about_text = Actor("about_text", pos = (400, 700))
letsgo_text = Actor("letsgo_text", pos = (400, 300))
gameover_text = Actor("gameover_text", pos = (400, 300))
win_text = Actor("win_text", pos = (400, 300))

pers_choise = Actor("persons_choise", topleft = (0,0))
press_space = Actor("press_space", pos = (400, 700))
kursor = Actor("kursor", pos = (330,690))

clocks = Actor("clock", pos = (35, 30))
eatdrink = Actor("eatdrink", pos = (35 ,85))

##### MUSIC #####

tracks = [["kabak_1", "kabak_2", "kabak_3", "kabak_4", "kabak_5"],
          ["lounge_1", "lounge_2", "lounge_3", "lounge_4", "lounge_5", "lounge_6"]]
track = " "

music.set_volume(0.7)
music.play("main_theme")

def music_main_theme():
    music.fadeout(0.5)
    music.set_volume(0.7)
    music.play("main_theme")

def music_theme():
    global track
    if scenario == "poorman":
        track = random.choice(tracks[0])
    elif scenario == "richman":
        track = random.choice(tracks[1])
    music.fadeout(1)
    music.set_volume(0.5)
    music.play_once(track)



##### SOUND FX #####

eat = ["eat1", "eat2", "eat3"]
roar = ["roar1", "roar2", "roar3", "roar4"]
blev = ["blev1", "blev2"]

def fx_eat():
    fx = random.choice(eat)
    if fx == "eat1":    
        sounds.eat1.play()
    elif fx == "eat2":    
        sounds.eat2.play()
    elif fx == "eat3":    
        sounds.eat3.play()

def fx_blev():
    fx = random.choice(blev)
    if fx == "blev1":    
        sounds.blev1.play()
    elif fx == "blev2":    
        sounds.blev2.play()


def fx_roar():
    fx = random.choice(roar)
    if fx == "roar1":    
        sounds.roar1.play()
    elif fx == "roar2":    
        sounds.roar2.play()
    elif fx == "roar3":    
        sounds.roar3.play()
    elif fx == "roar4":    
        sounds.roar4.play()


    

##### SCORE LEVEL #####

def score_level():
    global timer, current_time, score, scene, level, need, object_list
    if int(countdown - timer) <= 0:
        object_list = [obj]
        if score >= need:
            sounds.bell.play()
            level += 1
            need += 1
            timer = 0
            current_time = timer
            score = 0
            if level != 5:
                select_location()
                scene = "menu_letsgo"             
                
            else:
                scene = "menu_win"
                level = 1
                need = 4
        else:
            sounds.blev2.play()
            scene = "game_over"
            level = 1
            need = 4



##### LOCATION #####        
        
def select_location():
    global level_name
    if scenario == "poorman":
        if level == 1:
            location.image = random.choice(poor[0])
            level_name = level_list[0][0]
        elif level == 2:
            location.image = random.choice(poor[1])
            level_name = level_list[0][1]
        elif level == 3:
            location.image = random.choice(poor[2])
            level_name = level_list[0][2]
        elif level == 4:
            location.image = random.choice(poor[3])
            level_name = level_list[0][3]
    
    elif scenario == "richman":
        if level == 1:
            location.image = random.choice(rich[0])
            level_name = level_list[1][0]
        elif level == 2:
            location.image = random.choice(rich[1])
            level_name = level_list[1][1]
        elif level == 3:
            location.image = random.choice(rich[2])
            level_name = level_list[1][2]
        elif level == 4:
            location.image = random.choice(rich[3])
            level_name = level_list[1][3]
        
        


##### PLAYER #####

def select_person():
    global scenario
    if kursor.flip_x == False:
        player.image = poorman[0]
        rulesgame_text.image = "jim_rulesgame_text"
        scenario = "poorman"
    else:
        player.image = richman[0]
        rulesgame_text.image = "james_rulesgame_text"
        scenario = "richman"
    select_location()

def player_pic():
    if str(player.image) in poorman:
        player.image = poorman[0]
    elif str(player.image) in richman:
        player.image = richman[0]

def player_open():
    fx_eat()
    if str(player.image) in poorman:
        player.image = poorman[1]
    elif str(player.image) in richman:
        player.image = richman[1]

def player_blev():
    fx_blev()
    if str(player.image) in poorman:
        player.image = poorman[2]
    elif str(player.image) in richman:
        player.image = richman[2]
        



def player_movie():
    if keyboard.left and not keyboard.right and player.x != 70:
        player.x -= 5
    elif keyboard.right and not keyboard.left and player.x != 730:
        player.x += 5

def obj_movie():
    for i in object_list:
        i.y += 3
        if i.y > 700:
            object_list.remove(i)
            

def obj_create():
    global x
    global current_time
    if current_time + x < timer:
        current_time = timer
        x = random.randint(1, 6) # !!!
        obj1 = Actor(random.choice(eat_list + noeat_list), pos = (random.randint(50, 750), random.randint(-100, -50)))
        object_list.append(obj1)
    
def obj_colide():
    for i in object_list:
        if player.collidelist(object_list) != -1:
            eat_index = player.collidelist(object_list)
            
            if i.collidepoint(player.pos):
                global score
                if str(i.image) in eat_list: 
                    player_open()
                    clock.schedule(player_pic, 0.5)
                    score += 1
                else:
                    player_open()
                    #player_blev()
                    clock.schedule(player_blev, 0.5)
                    clock.schedule(player_pic, 1.5)
                    score -= 2       
                del object_list[eat_index]
    
############################################################
    
##### MENU #####
    
def on_key_down(key): 
    global scene
    if scene == "menu_one": # Обработка нажатия клавиш в главном меню
        global main_enter
        if key == keys.UP:
            sounds.chok.play()
            if main_enter == "about":
                kursor.pos = (320, 230)
                main_enter = "newgame"
            elif main_enter == "quit":
                kursor.pos = (350, 290)
                main_enter = "about"
        elif key == keys.DOWN:
            sounds.chok.play()
            if main_enter == "newgame":
                kursor.pos = (350, 290)
                main_enter = "about"
            elif main_enter == "about":
                kursor.pos = (370, 345)
                main_enter = "quit"
        elif key == keys.SPACE:
            if main_enter == "newgame":
                sounds.bell.play()
                scene = "menu_two"
            elif main_enter == "about":
                scene = "menu_about"
            elif main_enter == "quit":
                music_main_theme()
                quit()
    elif scene == "menu_about": # меню об игре
        if key == keys.SPACE:
            scene = "menu_one"
                
                
    elif scene == "menu_two": # меню история, начало новой игры
        if key == keys.SPACE:
            scene = "menu_three"
            kursor.image = "kursor_2"
            kursor.pos = (320, 190)
            kursor.flip_x = False
    
    elif scene == "menu_three": # меню выбор персонажа
        if key == keys.LEFT:
            sounds.chok.play()
            kursor.flip_x = False
            kursor.pos = (320, 190)
        elif key == keys.RIGHT:
            sounds.chok.play()
            kursor.flip_x = True
            kursor.pos = (490, 190)
        elif key == keys.SPACE:
            sounds.bell.play()
            select_person()
            scene = "menu_rules"
            
            
    elif scene == "menu_rules": # меню с правилами игры
        if key == keys.SPACE:
            scene = "menu_level"
            
    elif scene == "menu_level": # меню показывает номер уровня. Запуск игры!
        global timer, current_time, score
        if key == keys.SPACE:
            timer = 0
            current_time = timer
            score = 0
            scene = "game"
            sounds.bell2.play()
            music_theme()
            
    elif scene == "menu_letsgo": # меню перехода на следующий уровень
        if key == keys.SPACE:
            scene = "menu_level"
    
    elif scene == "menu_win": # you win
        if key == keys.SPACE:
            kursor.image = "kursor"
            kursor.pos = (320,230)
            scene = "menu_one"
            music_main_theme()
            
    elif scene == "game_over": # GAME OVER
        if key == keys.SPACE:
            kursor.image = "kursor"
            kursor.pos = (320,230)
            scene = "menu_one"
            music_main_theme()
            
    elif scene == "game":
        if key == keys.SPACE:
            player_open()
            clock.schedule(player_pic, 1)
            fx_roar()
    
            
    
         

def update(dt):
    global timer
    timer += dt
    if scene == "menu_one":
        if main_tasters.y < 100:
            main_tasters.y += 3
        elif main_menu.y > 300:
            main_menu.y -= 5
            kursor.pos = (320, 230)
        elif press_space.y > 550:
            press_space.y -= 3
    elif scene == "menu_about":
        if about_text.y > 300:
            about_text.y -= 1
            
    elif scene == "menu_two":
        press_space.y =  700
        if newgame_text.y > 300:
            newgame_text.y -= 1
    elif scene == "menu_three":
        if press_space.y > 550:
            press_space.y -= 3
    elif scene == "menu_rules":
        press_space.y =  700
        if rulesgame_text.y > 300:
            rulesgame_text.y -= 1            
    elif scene == "menu_level":
        if press_space.y > 40:
            press_space.y -= 20
        
    elif scene == "game":
        press_space.y =  700
        player_movie()
        obj_movie()
        obj_create()
        obj_colide()
        score_level()
    




def draw():
    screen.clear()
    if scene == "menu_one":
        main_logo.draw()
        main_tasters.draw()
        main_menu.draw()
        press_space.draw()
        kursor.draw()
    elif scene == "menu_about":
        menu_empty.draw()
        about_text.draw()
    elif scene == "menu_two":
        menu_empty.draw()
        newgame_text.draw()
    elif scene == "menu_three":
        pers_choise.draw()
        kursor.draw()
        press_space.draw()
    elif scene == "menu_rules":
        menu_empty.draw()
        rulesgame_text.draw()
    elif scene == "menu_level":
        menu_empty_2.draw()
        press_space.draw()
        screen.draw.text("LEVEL " + str(level) + "\n\n" + level_name, center=(400,300), color=(255,255,255), fontsize=70)
    
    elif scene == "game":
        location.draw()
        player.draw()
        for obj in object_list:
            obj.draw()
        clocks.draw()
        eatdrink.draw()
        screen.draw.text('      = ' + str(int(score)) + "/" + str(need), (15,70), color=(255,255,255), owidth=1, ocolor="black", fontsize=40)
        screen.draw.text('      = ' + str(int(countdown - timer)), (15,17), color=(255,255,255), owidth=1, ocolor="black", fontsize=40)
    
    elif scene == "menu_letsgo":
        menu_empty.draw()
        letsgo_text.draw()
     
    elif scene == "menu_win":
        menu_empty.draw()
        win_text.draw()

    elif scene == "game_over":
        menu_empty.draw()
        gameover_text.draw()

pgzrun.go()