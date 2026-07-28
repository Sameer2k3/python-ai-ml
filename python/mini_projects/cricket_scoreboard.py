# take cricketers name and their score and store this in a dictionary

scores={
    "virat":90,
    "sachin":45,
    "dhoni":533,
    "bumrah":34
}

mx_score=0

for score in scores:
    if scores[score]>mx_score:
        mx_score=scores[score]

print(mx_score)