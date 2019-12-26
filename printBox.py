from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyscreenshot as ImageGrab

h_top, h_bottom, w_left, w_right = 378, 428, 369, 884

# TIRANDO SCREENSHOT DO PLACAR

if __name__=='__main__':
    imscore = ImageGrab.grab(bbox=(w_left + 200, h_top-40, w_right - 205, h_bottom-40), childprocess=False)
    imscore.save("last.png")
    imscore.show()
