__author__ = 'bhavinpatel'

class ClockTower:

    def __init__(self,inputData=None):
        if inputData is None:
            inputData = self.getInput()
        self._inputData = inputData

        self.parseInput()

    def parseInput(self):
        lines = self._inputData.split("\n")
        (N,E,K) = lines[0].split(" ")

        self.vertices = int(N)
        self.sEdges   = int(E)
        self.usageLimit = int(K)

    def ShortestTimeFromEachEdge(self):
        pass

if __name__ == "__main__":
    WaversFlight = ClockTower()
    WaversFlight.ShortestTimeFromEachEdge()

