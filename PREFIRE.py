import time
import pyautogui as p

WITHDRAW_COLOR = (0,199,77)
WITHDRAW_REGION = (1843,319,10,7)
WITHDRAW_BTN = (4,3)

def SolveCaptcha():
    start_time = time.time()
    seconds = 3

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        p.click(750,620)

        if elapsed_time > seconds:
            p.click()
            break 
    main()

def main():
    while True:
        p.click(400,620)
        
        im = p.screenshot(region=WITHDRAW_REGION)
        
        withdraw_pos = im.getpixel(WITHDRAW_BTN)
        
        if withdraw_pos == WITHDRAW_COLOR:
            p.click(1638,350)
            SolveCaptcha()
           
print("Running PSYCHO-FAST...")
main()
