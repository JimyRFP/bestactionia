from database.models.challenge import ChallengeModel
from database.models.challengeoption import ChallengeOptionModel
from database import migration  
from params.challenge.register import ChallengeRegisterParams



class BestActionIaCreate():
    def __init__(self,params:ChallengeRegisterParams) -> None:
        self.params=params
    def create(self)->'ChallengeModel':
         has=ChallengeModel.get_or_none(ChallengeModel.name==self.params.challengeName)
         if has:
              return has
         challenge=ChallengeModel.create(name=self.params.challengeName,
                               sampleSize=self.params.challengeSample,
                               description=self.params.challengeDescription)
         for op in self.params.options:
              ChallengeOptionModel.registerOption(challenge,op.text)   
         return challenge   