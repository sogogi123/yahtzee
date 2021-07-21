import pygame
import random

pygame.init()   #초기화

#화면 크기 설정
screen_width = 750
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

#주사위 변수
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

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
             
    #배경 설정
    screen.fill((255,255,255))

    #주사위 값에 따른 주사위 이미지 출력
    if dice1 == 1:
        screen.blit(d1_img,(100,dice_y_pos))
    elif dice1 ==2:
        screen.blit(d2_img,(100,dice_y_pos))
    elif dice1 ==3:
        screen.blit(d3_img,(100,dice_y_pos))
    elif dice1 ==4:
        screen.blit(d4_img,(100,dice_y_pos))
    elif dice1 ==5:
        screen.blit(d5_img,(100,dice_y_pos))
    elif dice1 ==6:
        screen.blit(d6_img,(100,dice_y_pos))
    
    if dice2 == 1:
        screen.blit(d1_img,(200,dice_y_pos))
    elif dice2 ==2:
        screen.blit(d2_img,(200,dice_y_pos))
    elif dice2 ==3:
        screen.blit(d3_img,(200,dice_y_pos))
    elif dice2 ==4:
        screen.blit(d4_img,(200,dice_y_pos))
    elif dice2 ==5:
        screen.blit(d5_img,(200,dice_y_pos))
    elif dice2 ==6:
        screen.blit(d6_img,(200,dice_y_pos))

    if dice3 == 1:
        screen.blit(d1_img,(300,dice_y_pos))
    elif dice3 ==2:
        screen.blit(d2_img,(300,dice_y_pos))
    elif dice3 ==3:
        screen.blit(d3_img,(300,dice_y_pos))
    elif dice3 ==4:
        screen.blit(d4_img,(300,dice_y_pos))
    elif dice3 ==5:
        screen.blit(d5_img,(300,dice_y_pos))
    elif dice3 ==6:
        screen.blit(d6_img,(300,dice_y_pos))

    if dice4 == 1:
        screen.blit(d1_img,(400,dice_y_pos))
    elif dice4 ==2:
        screen.blit(d2_img,(400,dice_y_pos))
    elif dice4 ==3:
        screen.blit(d3_img,(400,dice_y_pos))
    elif dice4 ==4:
        screen.blit(d4_img,(400,dice_y_pos))
    elif dice4 ==5:
        screen.blit(d5_img,(400,dice_y_pos))
    elif dice4 ==6:
        screen.blit(d6_img,(400,dice_y_pos))

    if dice5 == 1:
        screen.blit(d1_img,(500,dice_y_pos))
    elif dice5 ==2:
        screen.blit(d2_img,(500,dice_y_pos))
    elif dice5 ==3:
        screen.blit(d3_img,(500,dice_y_pos))
    elif dice5 ==4:
        screen.blit(d4_img,(500,dice_y_pos))
    elif dice5 ==5:
        screen.blit(d5_img,(500,dice_y_pos))
    elif dice5 ==6:
        screen.blit(d6_img,(500,dice_y_pos))

    #화면 그리기
    pygame.display.update()

pygame.quit