from database.models.challenge import ChallengeModel
from database.models.challengeoption import ChallengeOptionModel
from database.models.challengeoptionpass import ChallengeOptionPassModel
from engine.compators.simplesPocetage import ComparatorSimplePorcetage,ComparatorSimplePorcetageResult
from typing import Optional
class BestActionEngine():
    def __init__(self,challenge:ChallengeModel):
          self.challenge=challenge
          self._best_option:Optional['ChallengeOptionModel']=None
          self._hasEnoughSample=False
    def get_best_option(self)->Optional['ChallengeOptionModel']:
         if self._best_option:
               return self._best_option
         self._best_option=self._findBest() 
         return self._best_option
    def _findBest(self)->Optional['ChallengeOptionModel']:
         best=ComparatorSimplePorcetage(self.challenge)
         winn=best.getWinner()
         return winn.option if winn else None
    def pick_option(self):
         if not self._hasEnoughSample:
              self._hasEnoughSample=self.challenge.hasEnoughSample()
         if(self._hasEnoughSample and not self._best_option):
             self._best_option=self.get_best_option()
         if(self._best_option):
               return self._best_option    
         return self.challenge.getRandomOption()     
         

              
