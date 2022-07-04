import time
import pyautogui as p


#COLORS (USE OWN VALUES)
BLITZ_COLOR = (0,226,88)
WITHDRAW_COLOR = (0,199,77)
CAPTCHA_COLOR = (249,249,249)
RED_COLOR = (222,76,65)
WHITE_COLOR = (255,255,255)

#SCREENSHOT REGIONS (FULLHD)

BLITZ_REGION = (447,649,1135,19)
WITHDRAW_REGION = (1843,319,10,7)
CAPTCHA_REGION = (734,591,37,49)
ODKLIK_REGION = (733,601,528,367)

#BLITZ 
B1_POS=(14,5)
B2_POS=(199,5)
B3_POS=(384,5)
B4_POS=(569,5)
B5_POS=(754,5)
B6_POS=(939,5)
B7_POS=(1124,5)

#WITHDRAW
WITHDRAW_BTN = (4,3) 

#CAPTCHA
CAPTCHA_PX = (17,3)

#WHATEVER
VOID_POS = (300,300)

def SolveCaptcha():
    start_time = time.time()
    seconds = 3

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # SCREENSHOT
        im = p.screenshot(region=CAPTCHA_REGION)

        # CHECKING PHASE
        cap_pos = im.getpixel(CAPTCHA_PX)
        if cap_pos == CAPTCHA_COLOR:
            p.click(750,620)
            break
        if elapsed_time > seconds:
            p.click()
            break
    main()

def StartWithdraw():
    start_time = time.time()
    seconds = 2

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # SCREENSHOT
        im = p.screenshot(region=WITHDRAW_REGION)
        
        # CHECKING PHASE
        withdraw_pos = im.getpixel(WITHDRAW_BTN)
        if withdraw_pos == WITHDRAW_COLOR:
            p.click(1638,350)
            break

        if elapsed_time > seconds:
            main()
    SolveCaptcha()

def main():
    while True:
        # SCREENSHOT for blitz
        im = p.screenshot(region=BLITZ_REGION)

        # CHECKING PHASE
        b_pos1 = im.getpixel(B1_POS)
        if b_pos1 == BLITZ_COLOR:
            p.click(460, 612)
            StartWithdraw()

        b_pos2 = im.getpixel(B2_POS)
        if b_pos2 == BLITZ_COLOR:
            p.click(645, 612)
            StartWithdraw()

        b_pos3 = im.getpixel(B3_POS)
        if b_pos3 == BLITZ_COLOR:
            p.click(830, 612)
            StartWithdraw()

        b_pos4 = im.getpixel(B4_POS)
        if b_pos4 == BLITZ_COLOR:
            p.click(1015, 612)
            StartWithdraw()

        b_pos5 = im.getpixel(B5_POS)
        if b_pos5 == BLITZ_COLOR:
            p.click(1200, 612)
            StartWithdraw()

        b_pos6 = im.getpixel(B6_POS)
        if b_pos6 == BLITZ_COLOR:
            p.click(1385, 612)
            StartWithdraw()

        b_pos7 = im.getpixel(B7_POS)
        if b_pos7 == BLITZ_COLOR:
            p.click(1570, 612)
            StartWithdraw()
            
        # SCREENSHOT for the rest
        sc = p.screenshot(region=ODKLIK_REGION)

        captcha_avoid = sc.getpixel((50,269))
        if captcha_avoid == WHITE_COLOR:
            p.click(VOID_POS)
            time.sleep(0.05)
            p.click(VOID_POS)
            time.sleep(0.05)
            p.click(VOID_POS)
            
        trade_red = sc.getpixel((110,160))
        if trade_red == RED_COLOR:
            p.click(VOID_POS)
            
        trade_ok = sc.getpixel((105,138))
        if trade_ok == WITHDRAW_COLOR:
            p.click(VOID_POS)  

        viewT = sc.getpixel((103,180))
        if viewT == WITHDRAW_COLOR:
            p.click(VOID_POS)
            
            
print("Running HAJBER...")
main()
            
