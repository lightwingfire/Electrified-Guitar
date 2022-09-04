import MemoryReader
import GuitarComm
import subprocess
from time import sleep

#subprocess.Popen("D:\\Program Files (x86)\\Steam\\steamapps\\common\\Rocksmith2014\\Rocksmith2014.exe")

sleep(10)

print("opened!")

rockSmith = MemoryReader.MemoryReader()
guitar = GuitarComm.GuitarComm()

guitar.startConnect()

while(True):

    rockSmith.startReadingMemory()
    misses = 0

    while(rockSmith.isPlayingASong()):
        if guitar.pressedRestart():
            rockSmith.setPlayingASong(False)
            break
        if misses<rockSmith.getMisses():
            misses = rockSmith.getMisses()
        
        if rockSmith.getMisses()<misses:
            print(f"you missed {misses} notes, prepare for punishment!")
            guitar.shock(misses*100)
            misses = 0
            