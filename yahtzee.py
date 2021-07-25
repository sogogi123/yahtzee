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
sorted_dice_list = [0,0,0,0,0]

#주사위 굴리는 횟수 제한
#dice_count = 0

#주사위 선택 여부 변수
dice_selected = [False, False, False, False, False]

#주사위 표시 위치 설정
dice_x_pos_list = [screen_width/11 * i for i in (1,3,5,7,9)]
dice_y_pos = (screen_height/4)

# 게임 음악
bgm = pygame.mixer.Sound("yahtzee/기둥속 사내 ost.mp3")
#yacht_bgm = pygame.mixer.Sound("yahtzee\죠죠 5부 죠르노 죠바나 처형브금 하이라이트 1시간 반복(초반 노이즈X, only 하이라이트).mp3")
bgm.set_volume(0.1)
#yacht_bgm.set_volume(0.3)
bgm.play(-1)

#점수 변수
aces = 0
deuces = 0
threes = 0
fours = 0
fives = 0
sixes = 0
choice = 0
four_of_kind = 0
full_house = 0
small_straight = 0
large_straight = 0
yacht = 0

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

#주사위 선택 함수
def fix_dice(c_pos, x_pos, y_pos, i):
    if x_pos[i] <= c_pos[0] <= x_pos[i] + 75 and y_pos <= c_pos[1] <= y_pos + 75:
        if dice_selected[i] == False:
            dice_selected[i] = True
        else:
            dice_selected[i] = False

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

#이벤트 루프
running = True
while running:

    # 정렬 된 주사위값들을 가지는 리스트
    sorted_dice_list = sorted(dice_list)

    #텍스트 출력
    color_black = (0, 0, 0)
    score_font = pygame.font.SysFont("arial", 30, True, False)
    text_aces = score_font.render("Aces : " + str(aces), True, color_black)
    text_deuces = score_font.render("Deuces : " + str(deuces), True, color_black)
    text_threes = score_font.render("Threes : " + str(threes), True, color_black)
    text_fours = score_font.render("Fours : " + str(fours), True, color_black)
    text_fives = score_font.render("Fives : " + str(fives), True, color_black)
    text_sixes = score_font.render("Sixes : " + str(sixes), True, color_black)
    text_choice = score_font.render("Choice : " + str(choice), True, color_black)
    text_four_of_kind = score_font.render("4 of a Kind : " + str(four_of_kind), True, color_black)
    text_full_house = score_font.render("Full House : " + str(full_house), True, color_black)
    text_small_straight = score_font.render("S. Straight : " + str(small_straight), True, color_black)
    text_large_straight = score_font.render("L. Straight : " + str(large_straight), True, color_black)
    text_yacht = score_font.render("Yacht : " + str(yacht), True, color_black)

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
            for i in range(0,5):
                fix_dice(current_pos, dice_x_pos_list, dice_y_pos, i)

    aces = dice_list.count(1) * 1
    deuces = dice_list.count(2) * 2
    threes = dice_list.count(3) * 3
    fours = dice_list.count(4) * 4
    fives = dice_list.count(5) * 5
    sixes = dice_list.count(6) * 6
    choice = sum(dice_list)
    
    def cal_four_of_kind():
        for i in range(1,7):
            cnt = 0
            cnt = dice_list.count(i)
            if cnt >= 4:
                return sum(dice_list)
        return 0

    four_of_kind = cal_four_of_kind()

    def cal_full_house():
        if sorted_dice_list[0] == sorted_dice_list[1] == sorted_dice_list[2] and sorted_dice_list[3] == sorted_dice_list[4]:
            return sum(sorted_dice_list)
        elif sorted_dice_list[0] == sorted_dice_list[1] and sorted_dice_list[2] == sorted_dice_list[3] == sorted_dice_list[4]:
            return sum(sorted_dice_list)
        return 0

    full_house = cal_full_house()

    def cal_small_straight():
        if sorted_dice_list[0] == 1 and sorted_dice_list[1] == 2 and sorted_dice_list[2] == 3 and sorted_dice_list[3] == 4:
            return 15
        elif sorted_dice_list[1] == 1 and sorted_dice_list[2] == 2 and sorted_dice_list[3] == 3 and sorted_dice_list[4] == 4:
            return 15
        elif sorted_dice_list[0] == 2 and sorted_dice_list[1] == 3 and sorted_dice_list[2] == 4 and sorted_dice_list[3] == 5:
            return 15
        elif sorted_dice_list[1] == 2 and sorted_dice_list[2] == 3 and sorted_dice_list[3] == 4 and sorted_dice_list[4] == 5:
            return 15
        return 0
    
    small_straight = cal_small_straight()

    def cal_large_straight():
        if sorted_dice_list[0] == 1 and sorted_dice_list[1] == 2 and sorted_dice_list[2] == 3 and sorted_dice_list[3] == 4 and sorted_dice_list[4] == 5:
            return 30
        elif sorted_dice_list[0] == 2 and sorted_dice_list[1] == 3 and sorted_dice_list[2] == 4 and sorted_dice_list[3] == 5 and sorted_dice_list[4] == 6:
            return 30
        return 0

    large_straight = cal_large_straight()

    def cal_yacht():
        dice_set = list(set(dice_list))
        if len(dice_set) == 1:
            #bgm.stop()
            #yacht_bgm.play(30)
            return 50
        return 0

    yacht = cal_yacht()

    #배경 설정
    screen.fill((255,255,255))

    #주사위 값 정렬
    #dice_list.sort()

    #주사위 값에 따른 주사위 이미지 출력
    for i in range(0,5):
        show_dice(dice_list[i], d1_img, d2_img, d3_img, d4_img, d5_img, d6_img, dice_x_pos_list[i], dice_y_pos)

    #화면에 텍스트 출력하기
    screen.blit(text_aces, (50, dice_y_pos * 1.5))
    screen.blit(text_deuces, (50, dice_y_pos * 1.5 + 30))
    screen.blit(text_threes, (50, dice_y_pos * 1.5 + 60))
    screen.blit(text_fours, (50, dice_y_pos * 1.5 + 90))
    screen.blit(text_fives, (50, dice_y_pos * 1.5 + 120))
    screen.blit(text_sixes, (50, dice_y_pos * 1.5 + 150))
    screen.blit(text_choice, (50, dice_y_pos * 1.5 + 180))
    screen.blit(text_four_of_kind, (50, dice_y_pos * 1.5 + 210))
    screen.blit(text_full_house, (50, dice_y_pos * 1.5 + 240))
    screen.blit(text_small_straight, (50, dice_y_pos * 1.5 + 270))
    screen.blit(text_large_straight, (50, dice_y_pos * 1.5 + 300))
    screen.blit(text_yacht, (50, dice_y_pos * 1.5 + 330))

    # 주사위 선택하면 테두리가 나타남
    gold_frame()

    #화면 그리기
    pygame.display.update()

pygame.quit