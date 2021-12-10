import numpy as np
from PIL import ImageGrab
from PIL import Image
import os
import cv2
import tensorflow as tf
import pytesseract
import time
import honestplayer
import expected_value

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img, config='--psm 6')
    return text

#img = cv2.imread('data/42.png')

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
    #1080 x 640
    printscreen_pil = ImageGrab.grab(bbox=(0, 40, 1920, 1080))
    printscreen_pil2 = np.array(printscreen_pil)
    #width: 14, height: 19
    #firstCard = cv2.rectangle(printscreen_pil2, (645, 820), (1258, 1000), (255, 0, 0), 0)
    #secondCard = cv2.rectangle(printscreen_pil2, (750, 460), (500, 360), (0, 255, 0), 0)
    #First card in hand
    #Suit
    pixel = printscreen_pil.getpixel((1183, 731))
    #print(pixel)
    if pixel == (217, 74, 50):
        #print("Hearts")
        first_card_suit = "H"
    elif pixel == (45, 49, 57):
        #print("Spades")
        first_card_suit = "S"
    elif pixel == (49, 169, 75):
        #print("Clubs")
        first_card_suit = "C"
    elif pixel == (57, 126, 203):
        #print("Diamonds")
        first_card_suit = "D"
    #Rank
    #mindre bokstaver git mer accuracy
    my_hand1 = cv2.cvtColor(printscreen_pil2[655:600+250, 1145:792+490], cv2.COLOR_BGR2RGB)
    me = cv2.cvtColor(printscreen_pil2[660:600+200, 800:1100], cv2.COLOR_BGR2RGB)
    pot = cv2.cvtColor(printscreen_pil2[250:200+230, 800:1100], cv2.COLOR_BGR2RGB)
    #call = cv2.cvtColor(printscreen_pil2[820:800+200, 645:1258], cv2.COLOR_BGR2RGB)
    #########################
    ##
    #img = get_grayscale(my_hand)
    my_hand_proc = cv2.bitwise_not(my_hand1)
    my_hand_proc = get_grayscale(my_hand_proc)
    my_hand_proc = cv2.threshold(my_hand_proc, 50, 255, cv2.THRESH_BINARY)[1] #125 - 131
    ##mindre width gir mer accuracy
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
    #call_proc = get_grayscale(call)
    #call_proc = cv2.threshold(call_proc, 170, 255, cv2.THRESH_BINARY)[1]

    img = cv2.hconcat([pot_proc, me_proc, my_hand_proc])
    cv2.rectangle(img, (1400, 95), (1680, 380), (0, 0, 0), -1)
    cv2.rectangle(img, (0, 0), (600, 130), (0, 0, 0), -1)
    #print(ocr_core(img))
    #cv2.imshow('window', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

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
    pixel = printscreen_pil.getpixel((1243, 731))
    #print(pixel)
    if pixel == (217, 74, 50):
        #print("Hearts")
        second_card_suit = "H"
    elif pixel == (45, 49, 57):
        #print("Spades")
        second_card_suit = "S"
    elif pixel == (49, 169, 75):
        #print("Clubs")
        second_card_suit = "C"
    elif pixel == (57, 126, 203):
        #print("Diamonds")
        second_card_suit = "D"
    #Rank
    #image = cv2.cvtColor(printscreen_pil2[329:329 + 19, 494:494 + 14], cv2.COLOR_BGR2RGB)
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

    #cv2.imshow('window', cv2.cvtColor(printscreen_pil2, cv2.COLOR_BGR2RGB))
    Equity = honestplayer.estimate_win_rate(first_card, second_card, nump)
    #AllIn_Loses = 0 - float(remaining)
    #AllIn_Winnings = float(total_pot) + float(remaining)
    #Fold_Winnings = float(total_pot)
    #Fold_Percent = .25
    #if to_call != '' and float(to_call):
    #Call_Amount = float(to_call)

    #expected_value.AllInExpectedValue(AllIn_Loses, AllIn_Winnings, Fold_Winnings, Fold_Percent, Equity, 0)



