# This question is asked by Apple. You are serving people in a lunch line and need to ensure each person gets a “balanced” meal. A balanced meal is a meal where there exists the same number of food items as drink items. Someone is helping you prepare the meals and hands you food items (i.e. F) or a drink items (D) in the order specified by the items string. Return the maximum number of balanced meals you are able to create without being able to modify items.
# Note: items will only contain F and D characters.
def balancedMeal(s):
    balancedMeal = 0;
    cntF = 0;
    cntD = 0;
    for c in s:
        if c == 'F':
            cntF += 1;
        else:
            cntD += 1;
        if(cntF == cntD):
            balancedMeal += 1
            cntF = 0;
            cntD = 0;
    return balancedMeal

s = "F"
print(balancedMeal(s))
