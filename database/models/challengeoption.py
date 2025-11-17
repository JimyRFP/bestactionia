from peewee import *
from database.connection import databaseIa
import database.models.challenge as challenge
from datetime import datetime
from typing import Optional
import uuid
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from database.models.challengeoptionpass import ChallengeOptionPassModel

class ChallengeOptionModel(Model):
    id=UUIDField(primary_key=True,default=uuid.uuid4)
    challenge_name=ForeignKeyField(model=challenge.ChallengeModel,backref='options', on_delete='CASCADE')
    text=TextField()
    passes: list['ChallengeOptionPassModel']
    created_at=DateTimeField(default=datetime.now)
    class Meta:
        database=databaseIa
    def getText(self,params:Optional[dict] = None):
        if params is None:
            return str(self.text)
        returnText:str=str(self.text)
        for key in params.keys():
            if not isinstance(params[key],str):
                continue
            returnText=returnText.replace(f"{{{key}}}",params[key])
        return returnText
    @staticmethod
    def registerOption(challenge:challenge.ChallengeModel,text:str):
        return ChallengeOptionModel.create(challenge_name=challenge.name,text=text)
