from peewee import *
from database.connection import databaseIa
import database.models.challengeoption as challengeoption
import database.models.challenge as challenge
from datetime import datetime
from typing import Optional
import uuid
import json
class ChallengeOptionPassModel(Model):
    id=UUIDField(primary_key=True,default=uuid.uuid4)
    challenge_option_id=ForeignKeyField(model=challengeoption.ChallengeOptionModel,backref='passes', on_delete='CASCADE')
    challenge_name=ForeignKeyField(model=challenge.ChallengeModel,backref='passes', on_delete='CASCADE')
    rewardWeight=IntegerField(default=0)
    created_at=DateTimeField(default=datetime.now)
    internal_id=TextField(null=True)
    user_meta_json=TextField(null=True)
    class Meta:
        database=databaseIa
    @staticmethod
    def registerPass(option:challengeoption.ChallengeOptionModel,
                     internal_id:Optional[str] = None,
                     user_meta_json:Optional[str] = None) -> 'ChallengeOptionPassModel':
       jsondata=''
       if isinstance(user_meta_json,str):
            jsondata=json.loads(user_meta_json)
       return ChallengeOptionPassModel.create(challenge_option_id=option.id,
                                              internal_id=internal_id,
                                              challenge_name=option.challenge_name,
                                              user_meta_json=jsondata)
    def setReward(self,weight:int)->None:
        self.rewardWeight=weight
        self.save()

