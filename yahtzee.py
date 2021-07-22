import pygame
import random

pygame.init()   #초기화

#화면 크기 설정
screen_width = 750
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

#주사위 변수
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

#주사위 변수들을 list에 넣음
dice_list = [dice1,dice2,dice3,dice4,dice5]

#주사위 표시 위치 설정
dice_y_pos = (screen_height/4)

#주사위 이미지 불러오기, 크기 조정
d1_img = pygame.image.load("yahtzee/dice1.png")
d1_img = pygame.transform.scale(d1_img, (75,75))

d2_img = pygame.image.load("yahtzee/dice2.png")
d2_img = pygame.transform.scale(d2_img, (75,75))

d3_img = pygame.image.load("yahtzee/dice3.png")
d3_img = pygame.transform.scale(d3_img, (75,75))

d4_img = pygame.image.load("yahtzee/dice4.png")
d4_img = pygame.transform.scale(d4_img, (75,75))

d5_img = pygame.image.load("yahtzee/dice5.png")
d5_img = pygame.transform.scale(d5_img, (75,75))

d6_img = pygame.image.load("yahtzee/dice6.png")
d6_img = pygame.transform.scale(d6_img, (75,75))

#화면 제목
pygame.display.set_caption("야추")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_list[0] = random.randint(1,6)
                dice_list[1] = random.randint(1,6)
                dice_list[2] = random.randint(1,6)
                dice_list[3] = random.randint(1,6)
                dice_list[4] = random.randint(1,6)
             
    #배경 설정
    screen.fill((255,255,255))
    
    dice_list.sort()

    #주사위 값에 따른 주사위 이미지 출력
    if dice_list[0] == 1:
        screen.blit(d1_img,(100,dice_y_pos))
    elif dice_list[0] ==2:
        screen.blit(d2_img,(100,dice_y_pos))
    elif dice_list[0] ==3:
        screen.blit(d3_img,(100,dice_y_pos))
    elif dice_list[0] ==4:
        screen.blit(d4_img,(100,dice_y_pos))
    elif dice_list[0] ==5:
        screen.blit(d5_img,(100,dice_y_pos))
    elif dice_list[0] ==6:
        screen.blit(d6_img,(100,dice_y_pos))
    
    if dice_list[1] == 1:
        screen.blit(d1_img,(200,dice_y_pos))
    elif dice_list[1] ==2:
        screen.blit(d2_img,(200,dice_y_pos))
    elif dice_list[1] ==3:
        screen.blit(d3_img,(200,dice_y_pos))
    elif dice_list[1] ==4:
        screen.blit(d4_img,(200,dice_y_pos))
    elif dice_list[1] ==5:
        screen.blit(d5_img,(200,dice_y_pos))
    elif dice_list[1] ==6:
        screen.blit(d6_img,(200,dice_y_pos))

    if dice_list[2] == 1:
        screen.blit(d1_img,(300,dice_y_pos))
    elif dice_list[2] ==2:
        screen.blit(d2_img,(300,dice_y_pos))
    elif dice_list[2] ==3:
        screen.blit(d3_img,(300,dice_y_pos))
    elif dice_list[2] ==4:
        screen.blit(d4_img,(300,dice_y_pos))
    elif dice_list[2] ==5:
        screen.blit(d5_img,(300,dice_y_pos))
    elif dice_list[2] ==6:
        screen.blit(d6_img,(300,dice_y_pos))

    if dice_list[3] == 1:
        screen.blit(d1_img,(400,dice_y_pos))
    elif dice_list[3] ==2:
        screen.blit(d2_img,(400,dice_y_pos))
    elif dice_list[3] ==3:
        screen.blit(d3_img,(400,dice_y_pos))
    elif dice_list[3] ==4:
        screen.blit(d4_img,(400,dice_y_pos))
    elif dice_list[3] ==5:
        screen.blit(d5_img,(400,dice_y_pos))
    elif dice_list[3] ==6:
        screen.blit(d6_img,(400,dice_y_pos))

    if dice_list[4] == 1:
        screen.blit(d1_img,(500,dice_y_pos))
    elif dice_list[4] ==2:
        screen.blit(d2_img,(500,dice_y_pos))
    elif dice_list[4] ==3:
        screen.blit(d3_img,(500,dice_y_pos))
    elif dice_list[4] ==4:
        screen.blit(d4_img,(500,dice_y_pos))
    elif dice_list[4] ==5:
        screen.blit(d5_img,(500,dice_y_pos))
    elif dice_list[4] ==6:
        screen.blit(d6_img,(500,dice_y_pos))

    #화면 그리기
    pygame.display.update()

pygame.quit