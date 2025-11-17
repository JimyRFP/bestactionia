from database.models.challenge import ChallengeModel
from database.models.challengeoption import ChallengeOptionModel
from database.models.challengeoptionpass import ChallengeOptionPassModel
from operator import attrgetter
from typing import cast
from typing import Optional, List
class ComparatorSimplePorcetage():
    def __init__(self,challenge:ChallengeModel):
       self.challenge=challenge
       self.results: Optional[List[ComparatorSimplePorcetageResult]] = None
       
    def getWinner(self)->Optional['ComparatorSimplePorcetageResult']:
        passes=list(self.challenge.passes)
        if len(passes)==0:
              return None
        greater=max(passes,key=attrgetter('rewardWeight')).rewardWeight
        assert isinstance(greater, int)
        if greater==0:
              return None
        options=list(self.challenge.options)
        self.results=[]
        for op in options:
            op_passes=list(op.passes)
            passes_len=len(op_passes)
            if(passes_len==0):
                 self.results.append(ComparatorSimplePorcetageResult(op,0,0,greater))
                 continue
            score=0
            for op_passe in op_passes:
                 score+=(cast(int,op_passe.rewardWeight)/greater)/passes_len
            self.results.append(ComparatorSimplePorcetageResult(op,score,passes_len,greater))     
        return max(self.results,key=attrgetter('score'))      

class ComparatorSimplePorcetageResult():
     def __init__(self,option:ChallengeOptionModel,
                  score:float,
                  passes_len:int,
                  challenge_grater_pass:int):
          self.option=option
          self.score=score
          self.passes_len=passes_len
          self.challenge_grater_pass=challenge_grater_pass
    