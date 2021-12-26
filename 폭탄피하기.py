import pygame
from random import*
###############################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640   # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()
 
# 화면 타이틀 설정
pygame.display.set_caption("폭탄 피하기")  # 게임 이름

###############################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\폭탄피하기\\background.png")

character = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\폭탄피하기\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2  
character_y_pos = screen_height - character_height

enemy = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\폭탄피하기\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0,screen_width-enemy_width)
enemy_y_pos = 0

enemy2 = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\폭탄피하기\\enemy.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = -enemy2_width
enemy2_y_pos = randint(0,screen_height-enemy2_height)

bomb = pygame.image.load("C:\\Users\\yuoko\\Desktop\\PythonWorkspace\\pygame_basic\\폭탄피하기\\bomb.png")

character_to_x = 0
character_to_y = 0


enemy_to_y = 0
direction = 1

enemy2_to_x = 0
direction2 = 1

game_font = pygame.font.Font(None, 50)

score_num = 0

runing = True 
while runing:
    dt = clock.tick(60) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enemy_to_y = 5
            if event.key == pygame.K_LEFT:
                character_to_x -= 10
            if event.key == pygame.K_RIGHT:
                character_to_x += 10
            if event.key == pygame.K_UP:
                character_to_y -= 10
            if event.key == pygame.K_DOWN:
                character_to_y += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_x = 0
            if event.key == pygame.K_RIGHT:
                character_to_x = 0
            if event.key == pygame.K_UP:
                character_to_y = 0
            if event.key == pygame.K_DOWN:
                character_to_y = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    if character_x_pos <= 0:
        character_x_pos = 0
    if character_x_pos >= screen_width-character_width:
        character_x_pos = screen_width-character_width
    character_y_pos += character_to_y
    if character_y_pos <= 0:
        character_y_pos = 0
    if character_y_pos >= screen_height-character_height:
        character_y_pos = screen_height-character_height

    if direction == 1:
        enemy_y_pos += enemy_to_y
    elif direction == 2:
        enemy_y_pos -= enemy_to_y

    if enemy_y_pos > screen_height:
        direction = 2
        enemy_x_pos = randint(0, screen_width-enemy_width)
        enemy_y_pos = screen_height
        enemy_to_y += 0.6
        score_num += 10
    if enemy_y_pos < -enemy_height:
        direction = 1
        enemy_x_pos = randint(0, screen_width-enemy_width)
        enemy_y_pos = -enemy_height
        score_num += 10

    if score_num == 100:
        enemy2_to_x = 4

    if  score_num >= 100:
        if direction2 == 1:
            enemy2_x_pos += enemy2_to_x
        if direction2 == 2:
            enemy2_x_pos -= enemy2_to_x
        
        if enemy2_x_pos > screen_width:
            direction2 = 2
            enemy2_y_pos = randint(0, screen_height-enemy2_height)
            enemy2_x_pos = screen_width
            enemy2_to_x += 0.6
            score_num += 10
        if enemy2_x_pos < -enemy2_width:
            direction2 = 1
            enemy2_y_pos = randint(0, screen_height-enemy2_height)
            enem2_x_pos = -enemy_width
            score_num += 10


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        print(f"점수 : {score_num}")
        runing = False
    
    if character_rect.colliderect(enemy2_rect):
        print("충돌했습니다.")
        print(f"점수 : {score_num}")
        runing = False
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
    score = game_font.render(str(score_num), True, (255, 255, 255))  # 출력할 글자, True, 글자 색상
    screen.blit(score, (10,10))

    if enemy_to_y == 0:
        game_start = ("Game Start")
        start_word = ("Press Spacebar")

        game_start_msg = game_font.render(str(game_start), True, (255, 255, 255))
        screen.blit(game_start_msg, (220,screen_height*(1/3)-50))
        last = game_font.render(str(start_word), True, (255, 255, 255))
        screen.blit(last, (185,screen_height*(1/3)))

    if character_rect.colliderect(enemy_rect):
        screen.blit(bomb, ((character_x_pos+enemy_x_pos)/2-150, (character_y_pos+enemy_y_pos)/2-150))

        game_over = ("Game Over!!!")    
        word = (f"Your Score : {score_num}")    
        
        game_over_msg = game_font.render(str(game_over), True, (255, 255, 255))
        last = game_font.render(str(word), True, (255, 255, 255))

        screen.blit(game_over_msg, (200, screen_height*(1/3)-50))  
        screen.blit(last, (175,screen_height*(1/3)))
        
    if character_rect.colliderect(enemy2_rect):
        screen.blit(bomb, ((character_x_pos+enemy2_x_pos)/2-150, (character_y_pos+enemy2_y_pos)/2-150))

        game_over = ("Game Over!!!")    
        word = (f"Your Score : {score_num}")    
        
        game_over_msg = game_font.render(str(game_over), True, (255, 255, 255))
        last = game_font.render(str(word), True, (255, 255, 255))

        screen.blit(game_over_msg, (200, screen_height*(1/3)-50))
        screen.blit(last, (175,screen_height*(1/3)))

    pygame.display.update() # 개임화면을 다시 그리기

pygame.time.delay(2000)

pygame.quit() 