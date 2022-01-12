#Calculates expeccted value of hand
def AllInExpectedValue(AllIn_Loses, AllIn_Winnings, Fold_Winnings, Fold_Percent, Equity, Call_Amount):
    FoldEV = (float(Fold_Percent) * float(Fold_Winnings))
    AllinEV = (1 - float(Fold_Percent)) * ((float(AllIn_Winnings) * float(Equity)) + (float(AllIn_Loses) * (1 - float(Equity))))
    AllInExpectedValue = round(FoldEV + AllinEV, 2)
    if AllInExpectedValue > float(Call_Amount):
        print('Raise! ' + str(AllInExpectedValue))
    else:
        print('Fold! ' + str(AllInExpectedValue))
