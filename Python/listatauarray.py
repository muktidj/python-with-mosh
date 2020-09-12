scores = [100, 72, 93]
scores1 = [50, 60]

# add item to the end of list
scores.append(80)

# Inserting item anywhere poisition of the list
scores.insert(2, 98)

# changing item of the list
scores[0] = "None"

# Combining list
scores.extend(scores1)

# Removing list
scores.remove('None')
scores.pop(5)
scores.pop()
# last item

# is  100 in scores list ?
scoreStudent = 100 in scores
print(scoreStudent)


# Looping list
for score in scores:
    print(score)
