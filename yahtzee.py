import pygame
import random

pygame.init()   #초기화

#화면 크기 설정
screen_width = 750
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

# 프레임 설정
clock = pygame.time.Clock()

#주사위 변수
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

#주사위 변수들을 list에 넣음
dice_list = [dice1,dice2,dice3,dice4,dice5]

#주사위 굴리는 횟수 제한
#dice_count = 0

#주사위 선택 여부 변수
dice_selected = [False, False, False, False, False]

#주사위 표시 위치 설정
dice_x_pos_list = [screen_width/11 * i for i in (1,3,5,7,9)]
dice_y_pos = (screen_height/4)

bgm = pygame.mixer.Sound("yahtzee/기둥속 사내 ost.mp3")
bgm.set_volume(0.1)
bgm.play(-1)

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

#황금 테두리 이미지
gold_frame_img = pygame.image.load("yahtzee/gold_frame.png")
gold_frame_img = pygame.transform.scale(gold_frame_img,(75,75))

#화면 제목
pygame.display.set_caption("야추")

#주사위 이미지 출력
def show_dice(dice, img1, img2, img3, img4, img5, img6, x_pos, y_pos):
    if dice == 1:
        screen.blit(img1,(x_pos,y_pos))
    elif dice ==2:
        screen.blit(img2,(x_pos,y_pos))
    elif dice ==3:
        screen.blit(img3,(x_pos,y_pos))
    elif dice ==4:
        screen.blit(img4,(x_pos,y_pos))
    elif dice ==5:
        screen.blit(img5,(x_pos,y_pos))
    elif dice ==6:
        screen.blit(img6,(x_pos,y_pos))

#이벤트 루프
running = True
while running:
    
    clock.tick(60) #60 프레임 제한

    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:       #종료
             running = False
        if pressed[pygame.K_SPACE]:         #스페이스바 이벤트
            for i in range(0,5):
                if dice_selected[i] == False:
                    dice_list[i] = random.randint(1,6)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:          #마우스 클릭시 이벤트
            current_pos = pygame.mouse.get_pos()
            if dice_x_pos_list[0] <= current_pos[0] <= dice_x_pos_list[0] + 75 and dice_y_pos <= current_pos[1] <= dice_y_pos +75:
                if dice_selected[0] == False:
                    dice_selected[0] = True
                else:
                    dice_selected[0] = False
            elif dice_x_pos_list[1] <= current_pos[0] <= dice_x_pos_list[1] + 75 and dice_y_pos <= current_pos[1] <= dice_y_pos +75:
                if dice_selected[1] == False:
                    dice_selected[1] = True
                else:
                    dice_selected[1] = False
            elif dice_x_pos_list[2] <= current_pos[0] <= dice_x_pos_list[2] + 75 and dice_y_pos <= current_pos[1] <= dice_y_pos +75:
                if dice_selected[2] == False:
                    dice_selected[2] = True
                else:
                    dice_selected[2] = False
            elif dice_x_pos_list[3] <= current_pos[0] <= dice_x_pos_list[3] + 75 and dice_y_pos <= current_pos[1] <= dice_y_pos +75:
                if dice_selected[3] == False:
                    dice_selected[3] = True
                else:
                    dice_selected[3] = False
            elif dice_x_pos_list[4] <= current_pos[0] <= dice_x_pos_list[4] + 75 and dice_y_pos <= current_pos[1] <= dice_y_pos +75:
                if dice_selected[4] == False:
                    dice_selected[4] = True
                else:
                    dice_selected[4] = False


    #배경 설정
    screen.fill((255,255,255))

    #주사위 값 정렬
    #dice_list.sort()

    #주사위 값에 따른 주사위 이미지 출력
    show_dice(dice_list[0], d1_img, d2_img, d3_img, d4_img, d5_img, d6_img, dice_x_pos_list[0], dice_y_pos)   
    show_dice(dice_list[1], d1_img, d2_img, d3_img, d4_img, d5_img, d6_img, dice_x_pos_list[1], dice_y_pos)
    show_dice(dice_list[2], d1_img, d2_img, d3_img, d4_img, d5_img, d6_img, dice_x_pos_list[2], dice_y_pos)
    show_dice(dice_list[3], d1_img, d2_img, d3_img, d4_img, d5_img, d6_img, dice_x_pos_list[3], dice_y_pos)
    show_dice(dice_list[4], d1_img, d2_img, d3_img, d4_img, d5_img, d6_img, dice_x_pos_list[4], dice_y_pos)

    # 주사위 선택 정하기
    def gold_frame():
        if dice_selected[0]:
            screen.blit(gold_frame_img,(dice_x_pos_list[0],dice_y_pos))
        if dice_selected[1]:
            screen.blit(gold_frame_img,(dice_x_pos_list[1],dice_y_pos))
        if dice_selected[2]:
            screen.blit(gold_frame_img,(dice_x_pos_list[2],dice_y_pos))
        if dice_selected[3]:
            screen.blit(gold_frame_img,(dice_x_pos_list[3],dice_y_pos))
        if dice_selected[4]:
            screen.blit(gold_frame_img,(dice_x_pos_list[4],dice_y_pos))
    gold_frame()

    #화면 그리기
    pygame.display.update()

pygame.quit