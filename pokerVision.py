import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
import honestplayer
import expected_value

#define where tesseract is intalled
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img, config='--psm 6')
    return text

#Grayscale
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Remove noise
def remove_noise(image):
    return cv2.medianBlur(image, 5)

#Thresholding
def thresholding(image):
    return cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)[1]


first_card_rank = ""
first_card_suit = ""
second_card_rank = ""
second_card_suit = ""
remaining = ""
total_pot = ""
to_call = ""

first_card = ""
second_card = ""

AllIn_Loses = 0
AllIn_Winnings = 0
Fold_Winnings = 0
Fold_Percent = .25
Equity = 0
Call_Amount = 0


def scan_screen(nump):
    #1920x1080
    #Grabs an image of the area of the screen we play poker in
    printscreen_pil = ImageGrab.grab(bbox=(0, 40, 1920, 1080))
    printscreen_pil2 = np.array(printscreen_pil)
    #First card in hand
    #Suit
    #Determines the suit based of the color of the suit
    pixel = printscreen_pil.getpixel((1183, 731))
    #print(pixel)
    if pixel == (217, 74, 50):
        #hearts if the color is red
        first_card_suit = "H"
    elif pixel == (45, 49, 57):
        #spades if the color is black
        first_card_suit = "S"
    elif pixel == (49, 169, 75):
        #clubs if the color is green
        first_card_suit = "C"
    elif pixel == (57, 126, 203):
        #Diamonds if the color is blue
        first_card_suit = "D"

    #We take that image and specify what we are interested in
    #in this case: the pot, my money and my hand
    my_hand1 = cv2.cvtColor(printscreen_pil2[655:600+250, 1145:792+490], cv2.COLOR_BGR2RGB)
    me = cv2.cvtColor(printscreen_pil2[660:600+200, 800:1100], cv2.COLOR_BGR2RGB)
    pot = cv2.cvtColor(printscreen_pil2[250:200+230, 800:1100], cv2.COLOR_BGR2RGB)
    #Some image processing
    ###################
    my_hand_proc = cv2.bitwise_not(my_hand1)
    my_hand_proc = get_grayscale(my_hand_proc)
    my_hand_proc = cv2.threshold(my_hand_proc, 50, 255, cv2.THRESH_BINARY)[1] #125 - 131
    my_hand_proc = cv2.resize(my_hand_proc, (260, 360))
    ###################
    me_proc = get_grayscale(me)
    me_proc = cv2.threshold(me_proc, 180, 255, cv2.THRESH_BINARY)[1]
    me_proc = cv2.resize(me_proc, (800, 360))
    ##################
    pot_proc = get_grayscale(pot)
    pot_proc = cv2.threshold(pot_proc, 170, 255, cv2.THRESH_BINARY)[1]
    pot_proc = cv2.resize(pot_proc, (600, 360))
    #################
    #the image consists of three parts: the pot, my money and my hand
    img = cv2.hconcat([pot_proc, me_proc, my_hand_proc])
    cv2.rectangle(img, (1400, 95), (1680, 380), (0, 0, 0), -1)
    cv2.rectangle(img, (0, 0), (600, 130), (0, 0, 0), -1)
    #Use this for setting up the image
    #print(ocr_core(img))
    #cv2.imshow('window', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #The next part splits the string into the data we wish to use. You may need som tweaking to get this to work.
    text = ocr_core(img).split()
    ind = ""
    for word in text:
        if "pot:" == word:
            print("Total pot: " + text[text.index('pot:') + 1].replace("€", ""))
            total_pot = text[text.index('pot:') + 1].replace("€", "")
        if "Snorris" == word:
            ind = "Snorris"
            if len(text[text.index('Snorris') + 1]) >= 2 and not text[text.index('Snorris') + 1] == "10":
                first_card_rank = text[text.index('Snorris') + 1][0]
                second_card_rank = text[text.index('Snorris') + 1][1]
            else:
                first_card_rank = text[text.index('Snorris') + 1]
                second_card_rank = text[text.index('Snorris') + 2]
            print("Remaining: " + text[text.index('pot:') + 2].replace("€", ""))
            remaining = text[text.index('pot:') + 2].replace("€", "")
        if "snorris" == word:
            ind = "snorris"
            if len(text[text.index('snorris') + 1]) >= 2 and not text[text.index('snorris') + 1] == "10":
                first_card_rank = text[text.index('snorris') + 1][0]
                second_card_rank = text[text.index('snorris') + 1][1]
            else:
                first_card_rank = text[text.index('snorris') + 1]
                second_card_rank = text[text.index('snorris') + 2]
            print("Remaining: " + text[text.index('pot:') + 2].replace("€", ""))
            remaining = text[text.index('pot:') + 2].replace("€", "")

    ##########################
    #Second card in hand
    #Suit
    #Determines the suit based of the color of the suit
    pixel = printscreen_pil.getpixel((1243, 731))
    #print(pixel)
    if pixel == (217, 74, 50):
        #Hearts if color is red
        second_card_suit = "H"
    elif pixel == (45, 49, 57):
        #Spades if color is black
        second_card_suit = "S"
    elif pixel == (49, 169, 75):
        #clubs if color is green
        second_card_suit = "C"
    elif pixel == (57, 126, 203):
        #diamonds if color is blue
        second_card_suit = "D"
    #Rank
    #Determines the rank of the cards and combines it with the suit
    if first_card_rank == '10' or first_card_rank == '1':
        first_card_rank = 'T'
        second_card_rank = text[text.index(ind) + 1][2]
    first_card = first_card_suit + first_card_rank
    if second_card_rank == '10' or second_card_rank == '1':
        second_card_rank = 'T'
    second_card = second_card_suit + second_card_rank
    print("Card one: " + first_card)
    print("Card two: " + second_card)
    ######################

    # use this to calculate the expected value
    #cv2.imshow('window', cv2.cvtColor(printscreen_pil2, cv2.COLOR_BGR2RGB))
    Equity = honestplayer.estimate_win_rate(first_card, second_card, nump)
    #AllIn_Loses = 0 - float(remaining)
    #AllIn_Winnings = float(total_pot) + float(remaining)
    #Fold_Winnings = float(total_pot)
    #Fold_Percent = .25
    #if to_call != '' and float(to_call):
    #Call_Amount = float(to_call)

    expected_value.AllInExpectedValue(AllIn_Loses, AllIn_Winnings, Fold_Winnings, Fold_Percent, Equity, 0)



