std = 'R-0,0,0,0-1,1,1,1-1,1,1,1-0,0,0,0-0-x,x,x,yR,yN,yB,yK,yQ,yB,yN,yR,x,x,x/x,x,x,yP,yP,yP,yP,yP,yP,yP,yP,x,x,x/x,x,x,8,x,x,x/bR,bP,10,gP,gR/bN,bP,10,gP,gN/bB,bP,10,gP,gB/bQ,bP,10,gP,gK/bK,bP,10,gP,gQ/bB,bP,10,gP,gB/bN,bP,10,gP,gN/bR,bP,10,gP,gR/x,x,x,8,x,x,x/x,x,x,rP,rP,rP,rP,rP,rP,rP,rP,x,x,x/x,x,x,rR,rN,rB,rQ,rK,rB,rN,rR,x,x,x'

class Parser:
    
    def fen2pos(self, fen: str):
        pass

    def pos2move(self, pos) -> str:
        pass

    # fen2pos methods #

    def __turnToPlayer(self, turn: str):
        pass

    def __castleToRight(self, kingSide: str, queenSide: str):
        pass

    def __boardToPos(self, board: str):
        pass
    
    # pos2move methods #

    def __playerToTurn(self, player) -> str:
        pass

    def __rightToCastle(self, right):
        pass

    def __posToBoard(self, pos):
        pass



def parse(fen):
    s = fen.split('-')
    return s

print(parse(std))