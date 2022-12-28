import json
import time
import pyautogui, sys

# Using Opensea minting upload all your nfts with metadata

# Mouse coordinates vary based on machine

desc = "Little nft cats each made unique"
try:
    pyautogui.click(x=64, y=957)
    for i in range(954,955):
        pyautogui.moveTo(1015,117)
        time.sleep(7)
        pyautogui.click(x=1015, y=117)
        time.sleep(6)
        pyautogui.click(x=430, y=200)
        time.sleep(6)
        pyautogui.write(str(i+1))
        time.sleep(0.2)
        pyautogui.press('enter')
        s = '[FILEPATH]/json/'+ str(i+1) +'.json' # Folder with nft json files
        with open(s) as f:
            data = json.load(f)
            time.sleep(4)
            pyautogui.click(x=430, y=276)
            pyautogui.write(data['name'])
            pyautogui.click(x=446, y=324)
            pyautogui.write(data['image'])
            time.sleep(1)
            #desc
            pyautogui.click(x=460, y=367)
            pyautogui.write(desc)
            #add button
            pyautogui.click(x=652, y=461)
            pyautogui.click(x=468, y=292)
            pyautogui.click(x=468, y=317)
            pyautogui.click(x=468, y=345)
            #properties
            pyautogui.click(x=505, y=270)
            pyautogui.write("Eyes")
            pyautogui.click(x=565, y=270)
            pyautogui.write(data['attributes'][1]['value'])
            pyautogui.click(x=505, y=295)
            pyautogui.write("Tail")
            pyautogui.click(x=565, y=295)
            pyautogui.write(data['attributes'][2]['value'])
            pyautogui.click(x=505, y=319)
            pyautogui.write("Mouth")
            pyautogui.click(x=565, y=319)
            pyautogui.write(data['attributes'][3]['value'])
            pyautogui.click(x=505, y=345)
            pyautogui.write("Ears")
            pyautogui.click(x=565, y=345)
            pyautogui.write(data['attributes'][4]['value'])
            pyautogui.click(x=536, y=400)
            #end
            pyautogui.click(x=421, y=787)
            time.sleep(5)
            pyautogui.click(x=282, y=61)
            pyautogui.write("https://opensea.io/collection/[COLLECTIONNAME]")
            pyautogui.press('enter')
            time.sleep(5)
except KeyboardInterrupt:
    print('\n')

