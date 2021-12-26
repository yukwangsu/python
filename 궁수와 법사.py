import pygame
from random import*
###############################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 1200   # 가로 크기
screen_height = 700   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()
 
# 화면 타이틀 설정
pygame.display.set_caption("궁수와 법사")  # 게임 이름

###############################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\궁수와 법사_background.png")

character1 = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\character_1.png")
character1_size = character1.get_rect().size
character1_width = character1_size[0]
character1_height = character1_size[1]
character1_x_pos = 10
character1_y_pos = screen_height/2 - character1_height/2

character2 = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\character_2.png")
character2_size = character2.get_rect().size
character2_width = character2_size[0]
character2_height = character2_size[1]
character2_x_pos = screen_width  - character2_width - 10
character2_y_pos = screen_height/2 - character2_height/2

c_1_c = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\character_1_c.png")
c_1_c_size = c_1_c.get_rect().size
c_1_c_width = c_1_c_size[0]
c_1_c_height = c_1_c_size[1]
c_1_c_x_pos = 0
c_1_c_y_pos = 0

c_2_c = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\character_2_c.png")
c_2_c_size = c_2_c.get_rect().size
c_2_c_width = c_2_c_size[0]
c_2_c_height = c_2_c_size[1]
c_2_c_x_pos = 0
c_2_c_y_pos = 0

c_1_r = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\character_1_r.png")
c_1_r_size = c_1_r.get_rect().size
c_1_r_width = c_1_r_size[0]
c_1_r_height = c_1_r_size[1]
c_1_r_x_pos = 0
c_1_r_y_pos = 0

c_2_r = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\character_2_r.png")
c_2_r_size = c_2_r.get_rect().size
c_2_r_width = c_2_r_size[0]
c_2_r_height = c_2_r_size[1]
c_2_r_x_pos = randint(20, int(screen_width/2)-c_2_r_width-20)
c_2_r_y_pos = - c_2_r_height

bomb = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\궁수와 법사\\bomb.png")

character1_heart = 5
character2_heart = 7

character1_speed = 7
character2_speed = 7

character1_to_x = 0
character1_to_y = 0

character2_to_x = 0
character2_to_y = 0

event_c_1_c = False
re_event_c_1_c = True
c_1_c_to_x = 13

event_c_2_c = False
re_event_c_2_c = True
c_2_c_to_x = -13

re_event_c_1_s = True
re_event_c_1_s_stack = -1

re_event_c_2_s = True
re_event_c_2_s_stack = -1

event_c_1_r = False
re_event_c_1_r = True
c_1_r_to_x = 10
re_event_c_1_r_stack = -1
stun = False
stun_stack = -3

event_c_2_r = False
re_event_c_2_r = True
c_2_r_to_y = 15
re_event_c_2_r_stack = -1

start = 0

stun2 = True


game_font = pygame.font.Font(None, 50)


runing = True 
while runing:
    dt = clock.tick(60) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = 1
                stun2 = False
            if stun == False and stun2 == False:
                if event.key == pygame.K_LEFT:
                    character2_to_x -= character2_speed
                if event.key == pygame.K_RIGHT:
                    character2_to_x += character2_speed
                if event.key == pygame.K_UP:
                    character2_to_y -= character2_speed
                if event.key == pygame.K_DOWN:
                    character2_to_y += character2_speed
            if stun2 == False:
                if event.key == pygame.K_a:
                    character1_to_x -= character1_speed
                if event.key == pygame.K_d:
                    character1_to_x += character1_speed
                if event.key == pygame.K_w:
                    character1_to_y -= character1_speed
                if event.key == pygame.K_s:
                    character1_to_y += character1_speed

            if  re_event_c_1_c == True:
                if event.key == pygame.K_v:
                    c_1_c_x_pos = character1_x_pos + character1_width + 5
                    c_1_c_y_pos = character1_y_pos + character1_height/2 - c_1_c_height/2
                    event_c_1_c = True
                    re_event_c_1_s_stack -= 1
                    re_event_c_1_r_stack -= 1
                    re_event_c_1_c = False
            if  re_event_c_1_c == False:
                if event.key == pygame.K_v:
                    re_event_c_1_c == False
            if  re_event_c_2_c == True:
                if event.key == pygame.K_i:
                    c_2_c_x_pos = character2_x_pos - character2_width - 5
                    c_2_c_y_pos = character2_y_pos + character2_height/2 - c_2_c_height/2
                    event_c_2_c = True
                    re_event_c_2_s_stack -= 1
                    stun_stack -= 1
                    re_event_c_2_r_stack -= 1
                    re_event_c_2_c = False

            if  re_event_c_1_s == True and event.key == pygame.K_b:
                character1_speed += 5
                re_event_c_1_s_stack = 3

            if  re_event_c_2_s == True and event.key == pygame.K_o:
                character2_speed += 5
                re_event_c_2_s_stack = 3

            if  re_event_c_1_r == True and event.key == pygame.K_n:
                c_1_r_x_pos = character1_x_pos + character1_width + 5
                c_1_r_y_pos = character1_y_pos + character1_height/2 - c_1_r_height/2
                event_c_1_r = True
                re_event_c_1_r_stack = 0

            if  re_event_c_2_r == True and event.key == pygame.K_p:
                c_2_r_x_pos = randint(20, int(screen_width/2)-c_2_r_width-20)
                c_2_r_y_pos = - c_2_r_height
                event_c_2_r = True
                re_event_c_2_r_stack = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character2_to_x = 0
            if event.key == pygame.K_RIGHT:
                character2_to_x = 0
            if event.key == pygame.K_UP:
                character2_to_y = 0
            if event.key == pygame.K_DOWN:
                character2_to_y = 0
            if event.key == pygame.K_a:
                character1_to_x = 0
            if event.key == pygame.K_d:
                character1_to_x = 0
            if event.key == pygame.K_w:
                character1_to_y = 0
            if event.key == pygame.K_s:
                character1_to_y = 0

            if event.key == pygame.K_b:
                re_event_c_1_s = False

            if event.key == pygame.K_o:
                re_event_c_2_s = False

            if event.key == pygame.K_n:
                re_event_c_1_r = False

    # 3. 게임 캐릭터 위치 정의
    character1_x_pos += character1_to_x
    if character1_x_pos <= 20:
        character1_x_pos = 20
    if character1_x_pos >= screen_width/2-character1_width-20:
        character1_x_pos = screen_width/2-character1_width-20
    character1_y_pos += character1_to_y
    if character1_y_pos <= 20:
        character1_y_pos = 20
    if character1_y_pos >= screen_height-character1_height-20:
        character1_y_pos = screen_height-character1_height-20

    character2_x_pos += character2_to_x
    if character2_x_pos <= screen_width/2+20:
        character2_x_pos = screen_width/2+20
    if character2_x_pos >= screen_width-character2_width-20:
        character2_x_pos = screen_width-character2_width-20
    character2_y_pos += character2_to_y
    if character2_y_pos <= 20:
        character2_y_pos = 20
    if character2_y_pos >= screen_height-character2_height-20:
        character2_y_pos = screen_height-character2_height-20

    if c_1_c_x_pos >= screen_width:
        event_c_1_c = False
        re_event_c_1_c = True
        c_1_c_x_pos = -10

    if c_2_c_x_pos <= -c_2_c_width:
        event_c_2_c = False
        re_event_c_2_c = True
        c_2_c_x_pos = screen_width + 10

    if c_1_r_x_pos > screen_width:
        event_c_1_r = False

    if c_2_r_y_pos > screen_height:
        event_c_2_r = False

    if re_event_c_1_s_stack == 0:
        character1_speed -= 5
        re_event_c_1_s_stack = -1
    
    if re_event_c_1_s_stack == -8:
        re_event_c_1_s = True
    
    if re_event_c_2_s_stack == 0:
        character2_speed -= 5
        re_event_c_2_s_stack = -1
    
    if re_event_c_2_s_stack == -5:
        re_event_c_2_s = True

    if re_event_c_1_r_stack == -12:
        re_event_c_1_r = True

    if re_event_c_2_r_stack == -8:
        re_event_c_2_r = True
    

    if stun_stack <= 0:
        stun = False

    # 4. 충돌 처리

    character1_rect = character1.get_rect()
    character1_rect.left = character1_x_pos
    character1_rect.top = character1_y_pos

    character2_rect = character2.get_rect()
    character2_rect.left = character2_x_pos
    character2_rect.top = character2_y_pos

    c_1_c_rect = c_1_c.get_rect()
    c_1_c_rect.left = c_1_c_x_pos
    c_1_c_rect.top = c_1_c_y_pos

    c_2_c_rect = c_2_c.get_rect()
    c_2_c_rect.left = c_2_c_x_pos
    c_2_c_rect.top = c_2_c_y_pos

    c_1_r_rect = c_1_r.get_rect()
    c_1_r_rect.left = c_1_r_x_pos
    c_1_r_rect.top = c_1_r_y_pos

    c_2_r_rect = c_2_r.get_rect()
    c_2_r_rect.left = c_2_r_x_pos
    c_2_r_rect.top = c_2_r_y_pos

    if character2_rect.colliderect(c_1_c_rect):
        character2_heart -= 1
        character1_speed += 0.5
        event_c_1_c = False
        re_event_c_1_c = True
        c_1_c_x_pos = -10

    if character1_rect.colliderect(c_2_c_rect):
        character1_heart -= 1
        event_c_2_c = False
        re_event_c_2_c = True
        c_2_c_x_pos = screen_width + 10

    if character2_rect.colliderect(c_1_r_rect):
        character2_heart -= 2
        event_c_1_r = False
        c_1_r_x_pos = -10
        stun = True
        stun_stack = 2
    
    if character1_rect.colliderect(c_2_r_rect):
        character1_heart -= 2
        event_c_2_r = False
        c_2_r_y_pos = -c_2_r_height
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character1, (character1_x_pos, character1_y_pos))
    screen.blit(character2, (character2_x_pos, character2_y_pos))

    if event_c_1_c == True:
        c_1_c_x_pos += c_1_c_to_x
        screen.blit(c_1_c, (c_1_c_x_pos, c_1_c_y_pos))

    if event_c_2_c == True:
        c_2_c_x_pos += c_2_c_to_x
        screen.blit(c_2_c, (c_2_c_x_pos, c_2_c_y_pos))
    
    if event_c_1_r == True:
        c_1_r_x_pos += c_1_r_to_x
        screen.blit(c_1_r, (c_1_r_x_pos, c_1_r_y_pos))

    if event_c_2_r == True:
        c_2_r_y_pos += c_2_r_to_y
        screen.blit(c_2_r, (c_2_r_x_pos, c_2_r_y_pos))

    character1_heart_num = game_font.render(str(character1_heart), True, (255, 0, 0))
    screen.blit(character1_heart_num, (30,20))
    character2_heart_num = game_font.render(str(character2_heart), True, (255, 0, 0))
    screen.blit(character2_heart_num, (screen_width-50, 20))

    if start == 0:
        game_start = ("Game Start")
        start_word = ("Press Spacebar")
        game_start_msg = game_font.render(str(game_start), True, (0, 0, 255))
        screen.blit(game_start_msg, (500,screen_height*(1/3)-50))
        last = game_font.render(str(start_word), True, (0, 0, 255))
        screen.blit(last, (465,screen_height*(1/3)))

    if character1_heart <= 0:
        screen.blit(bomb, (character1_x_pos, character1_y_pos - character1_height))
        game_over = ("Game Over!!!")      
        word = ("Player 2 Win !!!")
        game_over_msg = game_font.render(str(game_over), True, (255, 0, 0))
        last = game_font.render(str(word), True, (255, 0, 0))
        screen.blit(game_over_msg, (480, screen_height*(1/3)-50))  
        screen.blit(last, (455, screen_height*(1/3)))
        stun2 = True
        runing = False
        
    if character2_heart <= 0:
        screen.blit(bomb, (character2_x_pos-character2_width, character2_y_pos - character2_height))
        game_over = ("Game Over!!!")      
        word = ("Player 1 Win !!!")
        game_over_msg = game_font.render(str(game_over), True, (255, 0, 0))
        last = game_font.render(str(word), True, (255, 0, 0))
        screen.blit(game_over_msg, (480, screen_height*(1/3)-50))  
        screen.blit(last, (455, screen_height*(1/3)))
        stun2 = True
        runing = False

    pygame.display.update() # 개임화면을 다시 그리기

pygame.time.delay(3500)

pygame.quit()