import random
import math
import pickle
import re

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def EloRating(scores, d, album1, album2):
    Ra, Rb = scores[album1], scores[album2]
    K = 30
    Pb = Probability(Ra, Rb)
    Pa = Probability(Rb, Ra)
 
    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)
 
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
 
    print("Updated Ratings:-")
    print(f"{album1} =", int(round(Ra, 6)), f" {album2} =", int(round(Rb, 6)))
    scores[album1], scores[album2] = Ra, Rb

def ChooseAlbum(scores, album1, album2):
    choice = ''
    while choice != album1.lower() and choice != album2.lower():
        print('Type "stop" to quit')
        choice = (input(f'Choose which album is better: {album1} or {album2}: ')).lower()
        #print(choice)
        if choice == 'stop':
            return 'stop'
        elif choice != album1.lower() and choice != album2.lower():
            print(f'Please select a proper album')
        else: 
            if choice == album1.lower():
                EloRating(scores, 1, album1, album2)
            else:
                EloRating(scores, 0, album1, album2)
            return 'yes'

def Updater(scores):
    stop = 'yes'
    while stop.lower() != 'stop':

        album1 = random.choice(list(scores.keys()))
        listtemp = (list(scores.keys()))
        listtemp.remove(album1)
        album2 = random.choice(listtemp)

        stop = ChooseAlbum(scores, album1, album2)
    

def saver(scores):
    with open('album_rankings.pkl', 'wb') as f:
        pickle.dump(scores, f)

def loader():
    with open('album_rankings.pkl', 'rb') as f:
        scores = pickle.load(f)
    return scores
            
def printScores(scores):
    sortedScores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i in sortedScores:
        i = str(i)
        i = re.sub(r'[()]', '', i)
        i = re.sub(r'\'', '', i)
        i = re.sub(r',', ':', i)
        print(i)

def addNewAlbum(scores):
    stop = 'yes'
    while stop.lower() == 'yes':
        newKey = input(f'What Album Would You Like to Add: ')
        scores[newKey] = 1000
        stop = input(f'Would you like to add another album? (Yes to continue, Stop to Stop): ')

def resetScores(scores):
    for i in scores.keys():
        scores[i] = 1000
    print('Scores have been reset')

def deleteAlbum(scores):
    stop = input('Do you want to delete an album from your List: ')
    while stop.lower() == 'yes':
        keys = list(scores.keys())
        print(keys)
        delAlbum = input('What album would you like to delete from your list: ')
        if delAlbum in keys:
            del scores[delAlbum]
            print('Album has been deleted')
        else:
            print('Album not found in your list, please try again')
        stop = input('Would you like to delete another album from your list (Yes to continue, Stop to Stop): ')

def main():
    try:
        scores = loader()
    except:
        scores = {}
        while len(scores.keys()) <= 1:
            print(f'Please add at least two albums to begin your album list')
            addNewAlbum(scores)
        saver(scores)
    choice = ''
    while choice != '9':
        print('1: Do album battles\n2: Print your current Rankings\n3: Add a new Album\n4: Reset your Scores\n5: Delete an Album')
        print('9: Quit and Save')
        choice = input('What do you want to do: ')
        match choice:
            case '1':
                Updater(scores)
            case '2':
                printScores(scores)
                input('Enter any key to continue: ')
            case '3':
                addNewAlbum(scores)
            case '4':
                resetScores(scores)
                input('Enter any key to continue: ')
            case '5':
                deleteAlbum(scores)
            case '9':
                saver(scores)
        saver(scores)
        
        
    
main()


