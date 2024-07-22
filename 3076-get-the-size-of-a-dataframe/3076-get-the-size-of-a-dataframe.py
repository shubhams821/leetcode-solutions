import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    print(players.shape)
    return [i for i in players.shape]
