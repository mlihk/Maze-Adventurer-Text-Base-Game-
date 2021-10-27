import threading
import time

def timeToHurry():
    print('unknown voice: 3 minutes has passed, quick or we are all dead!')
 
 
timer = threading.Timer(180.0, timeToHurry)
timer.start()
 
startingTimer = time.time() #constant please do not touch
 
def getTimer(): #use to get the time taken to finish the game
    usedTime = time.time() - startingTimer
    print(usedTime)
    return usedTime
 
def timeToGrade(usedTime): # converts the time into a grade
    if usedTime <= 60:
        gradeS(usedTime)
        return
    elif usedTime <= 120 and usedTime > 60:
        gradeA(usedTime)
        return
    elif usedTime <= 180 and usedTime > 120:
        gradeB(usedTime)
    elif usedTime <= 240 and usedTime > 180:
        gradeC(usedTime)
    elif usedTime > 240:
        gradeD(usedTime)
 
def gradeS(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: S')
    print('unknown voice: Well done! You have shown an amazing performance that no one has ever done!')
    sound_victory_music()
 
def gradeA(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: A')
    print('unknown voice: Good job! Impressive skills, you have saved the day!')
 
def gradeB(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: B')
    print('unknown voice: Great! The evil has now been eliminated!')
 
 
def gradeC(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: C')
    print('unknown voice: Well, we did it at last!')
 
def gradeD(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: D')
    print('unknown voice: That was a close one!')
