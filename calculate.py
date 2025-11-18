import argparse
from database.models.challenge import ChallengeModel
from engine.compators.simplesPocetage import ComparatorSimplePorcetage
parser = argparse.ArgumentParser()
parser.add_argument("--challenge", type=str, required=True)
args = parser.parse_args()
print(f'Get Challenge Name: {args.challenge}')
ch:ChallengeModel=ChallengeModel.get_or_none(ChallengeModel.name==args.challenge)
if ch is None:
    print('Unknown challenge')
    exit()
best=ComparatorSimplePorcetage(ch)
best.getWinner()
if not best.results:
    print('Error to get compartor results')
    exit()

print(f"---- Name: {ch.name}  ---")
print(f"---- Sample: {ch.sampleSize}  ---")
print(f"---- Is Treined: {ch.hasEnoughSample()}  ---")

for item in best.results:
    print(f"---\nId:{item.option.id}\nText: {item.option.text}\nScore:{(item.score*100):.2f}%\nSample Size: {item.passes_len}\n")

