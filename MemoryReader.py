from pymeow import *

class MemoryReader:
    
    def __init__(self):
        print("starting Memory Reader")

    #gets the offsets for data pointer to find the real data
    def read_offsets(self,proc, base_address, offsets):
        
        basepoint = read_int(proc, base_address)

        current_pointer = basepoint

        for i in offsets[:-1]:
            print(f"pointer:{hex(current_pointer)}, plus {i}")
            current_pointer = read_int(proc, current_pointer+i)
        
        return current_pointer + offsets[-1]

    def startReadingMemory(self):
        self.isPlaying = False
        try:
            process = process_by_name("Rocksmith2014.exe")

            base_address = process["baseaddr"] + 0x00F5C4CC

            print("base " + hex(base_address))
            print("holds " + hex(read_int(process,base_address)))

            offsets = [ 0x10, 0x28, 0x38, 0x18, 0x4, 0x84, 0x104]
            missAddr = self.read_offsets(process, base_address, offsets)

            self.process = process
            self.missAddr = missAddr
            self.isPlaying = True
            
        except:
            print("waiting for song to start")
            self.isPlaying = False
        else:
            self.isPlaying = True

    def isPlayingASong(self):
            return self.isPlaying

    def setPlayingASong(self, setter):
        self.isPlaying = setter

    def getMisses(self):
        try:
            misses = read_int(self.process, self.missAddr)
            if  misses > 1:
                        # print(f"miss {misses}x")
                        return misses
        except:
            self.isPlaying = False

        return 0


    # while(True):
    #     try:
    #         process = process_by_name("Rocksmith2014.exe")

    #         base_address = process["baseaddr"] + 0x00F5C4CC

    #         print("base " + hex(base_address))
    #         print("holds " + hex(read_int(process,base_address)))

    #         offsets = [ 0x10, 0x28, 0x38, 0x18, 0x4, 0x84, 0x104]
    #         missAddr = read_offsets(process, base_address, offsets)
            
    #         while(True):
    #             if read_int(process, missAddr) > 1:
    #                 print(f"miss {read_int(process, missAddr)}x")

    #     except:
    #         print("waiting for song to start")

