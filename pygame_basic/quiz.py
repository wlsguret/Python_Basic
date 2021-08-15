import pygame
from random import *
######################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("운석 피하기") 

# background = pygame.image.load("C:\\Users\\USER\\Desktop\\PythonWorkspace\\pygame_basic\\background.png")
background = pygame.image.load("C:\\Users\\USER\\Desktop\\VSCode workspace\\Python\\pygame_basic\\background.png")

character = pygame.image.load("C:\\Users\\USER\\Desktop\\VSCode workspace\\Python\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

enemy = pygame.image.load("C:\\Users\\USER\\Desktop\\VSCode workspace\\Python\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0 - enemy_height

to_x_character = 0
character_speed = 0.5

to_y_enemy = 0
enemy_speed = 0.5

game_font = pygame.font.Font(None, 40)
game_result = "GameOver"
point = 0
score_taget = 5

# FPS
clock = pygame.time.Clock()
######################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True 
while running:
    dt = clock.tick(100)
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_character -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_character += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x_character = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                to_y_enemy += enemy_speed
       
    if enemy_y_pos >= screen_height:
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0 - enemy_height 
        
        point += 1
        if point >= score_taget:
            score_taget += 5         

    character_x_pos += to_x_character * dt
    enemy_y_pos += to_y_enemy * dt
        
    # 3. 게임 캐릭터 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running = False
        
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    score = game_font.render("Score : {}".format(point), True, (0, 255, 0))
    screen.blit(score,(10, 10))

    msg_score = game_font.render(str(score_taget), True, (0, 0, 255))
    msg_score_rect = msg_score.get_rect(center = (int(screen_width / 2), int(25))) 
    screen.blit(msg_score, msg_score_rect)

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() 

msg = game_font.render(game_result, True, (0, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update() 

pygame.time.delay(2000)

pygame.quit()
