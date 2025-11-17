from database.models.challenge import ChallengeModel
from database.models.challengeoption import ChallengeOptionModel
from database import migration  
from database.models.challengeoptionpass import ChallengeOptionPassModel
from engine.bestaction import BestActionEngine
from typing import Optional

class BestActionRestun():
    def __init__(self,challenge:ChallengeModel,option:ChallengeOptionModel,passe:Optional['ChallengeOptionPassModel']):
        self.option=option
        self.challenge=challenge
        self.passe=passe


class BestActionIaGetPass():
    def __init__(self,name:str):
        self.name=name
        self.challenge=ChallengeModel.get_or_none(ChallengeModel.name==self.name)
        if not self.challenge:
            raise Exception('unknown challenge name')
        self.engine=BestActionEngine(self.challenge)
    def getActionAndSavePass(self)->'BestActionRestun':
        op=self.engine.pick_option()
        if not op:
            raise Exception("No options")
        passe=ChallengeOptionPassModel.registerPass(op)
        return BestActionRestun(self.challenge,op,passe)
    def getActionWithouSavePasse(self)->'ChallengeOptionModel':
        op=self.engine.pick_option()
        if not op:
            raise Exception("No options")
        return op
    def getActionAndSaveNotTreined(self)->'BestActionRestun':
        op=self.engine.pick_option()
        if not op:
            raise Exception("No options")
        passe=None
        if not self.engine._hasEnoughSample:
           passe=ChallengeOptionPassModel.registerPass(op)
        return BestActionRestun(self.challenge,op,passe)