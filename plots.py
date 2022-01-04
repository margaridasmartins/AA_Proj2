"""

Project 2 Advanced Algorithmts 2021/22
Margarida Martins

"""

import matplotlib.pyplot as plt
import numpy as np

#English
f_exact_english= open("Tests/Don_Quixote/eng_exact", "r")
f_exact_english.readline()
f_fixed_english= open("Tests/Don_Quixote/eng_fixed", "r")
f_fixed_english.readline()
f_decreasing_english=open("Tests/Don_Quixote/eng_decreasing", "r")
f_decreasing_english.readline()

#Spanish
f_exact_spanish= open("Tests/Don_Quixote/spa_exact", "r")
f_exact_spanish.readline()
f_fixed_spanish= open("Tests/Don_Quixote/spa_fixed", "r")
f_fixed_spanish.readline()
f_decreasing_spanish=open("Tests/Don_Quixote/spa_decreasing", "r")
f_decreasing_spanish.readline()

#French
f_exact_french= open("Tests/Don_Quixote/fre_exact", "r")
f_exact_french.readline()
f_fixed_french= open("Tests/Don_Quixote/fre_fixed", "r")
f_fixed_french.readline()
f_decreasing_french=open("Tests/Don_Quixote/fre_decreasing", "r")
f_decreasing_french.readline()

#Deutch
f_exact_deutch= open("Tests/Don_Quixote/deu_exact", "r")
f_exact_deutch.readline()
f_fixed_deutch= open("Tests/Don_Quixote/deu_fixed", "r")
f_fixed_deutch.readline()
f_decreasing_deutch=open("Tests/Don_Quixote/deu_decreasing", "r")
f_decreasing_deutch.readline()

#Hungarian
f_exact_hungarian= open("Tests/Don_Quixote/hun_exact", "r")
f_exact_hungarian.readline()
f_fixed_hungarian= open("Tests/Don_Quixote/hun_fixed", "r")
f_fixed_hungarian.readline()
f_decreasing_hungarian=open("Tests/Don_Quixote/hun_decreasing", "r")
f_decreasing_hungarian.readline()


avg_fixed_values=dict()
avg_exact_values=dict()
avg_decreasing_values= dict()

avg_relative_exact_values_english=dict()
avg_relative_fixed_values_english=dict()
avg_relative_decreasing_values_english=dict()

avg_relative_exact_values_spanish=dict()
avg_relative_fixed_values_spanish=dict()
avg_relative_decreasing_values_spanish=dict()

avg_relative_exact_values_hungarian=dict()
avg_relative_fixed_values_hungarian=dict()
avg_relative_decreasing_values_hungarian=dict()

avg_relative_exact_values_french=dict()
avg_relative_fixed_values_french=dict()
avg_relative_decreasing_values_french=dict()

avg_relative_exact_values_deutch=dict()
avg_relative_fixed_values_deutch=dict()
avg_relative_decreasing_values_deutch=dict()

#English
for line in f_exact_english:
    line=line.split(" ")
    avg_exact_values[line[0]]=round(float(line[1]))
    avg_relative_exact_values_english[line[0]]=round(float(line[2]),2)

for line in f_fixed_english:
    line=line.split(" ")
    avg_fixed_values[line[0]]=round(float(line[1]))
    avg_relative_fixed_values_english[line[0]]=round(float(line[2]),2)

for line in f_decreasing_english:
    line= line.split(" ")
    avg_decreasing_values[line[0]] = round(float(line[1]))
    avg_relative_decreasing_values_english[line[0]]=round(float(line[2]),2)
    

#Spanish
for line in f_exact_spanish:
    line=line.split(" ")
    avg_relative_exact_values_spanish[line[0]]=round(float(line[2]),2)

for line in f_fixed_spanish:
    line=line.split(" ")
    avg_relative_fixed_values_spanish[line[0]]=round(float(line[2]),2)

for line in f_decreasing_spanish:
    line= line.split(" ")
    avg_relative_decreasing_values_spanish[line[0]]=round(float(line[2]),2)

#French
for line in f_exact_french:
    line=line.split(" ")
    avg_relative_exact_values_french[line[0]]=round(float(line[2]),2)


for line in f_fixed_french:
    line=line.split(" ")
    avg_relative_fixed_values_french[line[0]]=round(float(line[2]),2)

for line in f_decreasing_french:
    line= line.split(" ")
    avg_relative_decreasing_values_french[line[0]]=round(float(line[2]),2)

#Deutch
for line in f_exact_deutch:
    line=line.split(" ")
    avg_relative_exact_values_deutch[line[0]]=round(float(line[2]),2)

for line in f_fixed_deutch:
    line=line.split(" ")
    avg_relative_fixed_values_deutch[line[0]]=round(float(line[2]),2)

for line in f_decreasing_deutch:
    line= line.split(" ")
    avg_relative_decreasing_values_deutch[line[0]]=round(float(line[2]),2)

#Hungarian
for line in f_exact_hungarian:
    line=line.split(" ")
    avg_relative_exact_values_hungarian[line[0]]=round(float(line[2]),2)

for line in f_fixed_hungarian:
    line=line.split(" ")
    avg_relative_fixed_values_hungarian[line[0]]=round(float(line[2]),2)

for line in f_decreasing_hungarian:
    line= line.split(" ")
    avg_relative_decreasing_values_hungarian[line[0]]=round(float(line[2]),2)


#Absolute count
letters=sorted(avg_exact_values.keys())

x = np.arange(len(letters))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, [avg_exact_values[l] for l in letters], width, label='Exact counter')
rects2 = ax.bar(x, [avg_fixed_values[l] for l in letters], width, label='Fixed probability counter')
rects3 = ax.bar(x + width, [avg_decreasing_values[l] for l in letters], width, label='Decreasing probability counter')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_title('Exact and estimated counts for the different counters')
ax.set_xticks(x, letters)
ax.legend()

ax.bar_label(rects1,labels=["" for l in letters], padding=3)
ax.bar_label(rects2, labels=["" for l in letters], padding=3)
ax.bar_label(rects3, labels=["" for l in letters], padding=3)

fig.tight_layout()

plt.savefig(f'Images/count_plot.png')


#Relative count
x = np.arange(len(letters))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, [avg_relative_exact_values_english[l] for l in letters], width, label='Exact counter')
rects2 = ax.bar(x, [avg_relative_fixed_values_english[l] for l in letters], width, label='Fixed probability counter')
rects3 = ax.bar(x + width, [avg_relative_decreasing_values_english[l] for l in letters], width, label='Decreasing probability counter')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Relative Count (%)')
ax.set_title('Exact and estimated relative counts for the different counters')
ax.set_xticks(x, letters)
ax.legend()

ax.bar_label(rects1,labels=["" for l in letters], padding=3)
ax.bar_label(rects2, labels=["" for l in letters], padding=3)
ax.bar_label(rects3, labels=["" for l in letters], padding=3)

fig.tight_layout()

plt.savefig(f'Images/count_relative_plot.png')

fig = plt.figure()

#Exact
letters=sorted(avg_relative_exact_values_english.keys())

plt.scatter(letters,[avg_relative_exact_values_english.get(l,0) for l in letters], s=6, label="english")
plt.scatter(letters,[avg_relative_exact_values_spanish.get(l,0) for l in letters], s=6, label="spanish")
plt.scatter(letters,[avg_relative_exact_values_french.get(l,0) for l in letters], s=6, label="french")
plt.scatter(letters,[avg_relative_exact_values_hungarian.get(l,0) for l in letters], s=6, label="hungarian")
plt.scatter(letters,[avg_relative_exact_values_deutch.get(l,0) for l in letters], s=6, label="dutch")
plt.legend()
plt.savefig(f'Images/count_relative_languages_plot.png')

fig = plt.figure()

#Fixed
letters=sorted(avg_relative_fixed_values_english.keys())

plt.scatter(letters,[avg_relative_fixed_values_english.get(l,0) for l in letters], s=6, label="english")
plt.scatter(letters,[avg_relative_fixed_values_spanish.get(l,0) for l in letters], s=6, label="spanish")
plt.scatter(letters,[avg_relative_fixed_values_french.get(l,0) for l in letters], s=6, label="french")
plt.scatter(letters,[avg_relative_fixed_values_hungarian.get(l,0) for l in letters], s=6, label="hungarian")
plt.scatter(letters,[avg_relative_fixed_values_deutch.get(l,0) for l in letters], s=6, label="dutch")
plt.legend()
plt.savefig(f'Images/count_relative_languages_fixed_plot.png')

fig = plt.figure()

#Decreasing
letters=sorted(avg_relative_decreasing_values_english.keys())

plt.scatter(letters,[avg_relative_decreasing_values_english.get(l,0) for l in letters], s=6, label="english")
plt.scatter(letters,[avg_relative_decreasing_values_spanish.get(l,0) for l in letters], s=6, label="spanish")
plt.scatter(letters,[avg_relative_decreasing_values_french.get(l,0) for l in letters], s=6, label="french")
plt.scatter(letters,[avg_relative_decreasing_values_hungarian.get(l,0) for l in letters], s=6, label="hungarian")
plt.scatter(letters,[avg_relative_decreasing_values_deutch.get(l,0) for l in letters], s=6, label="dutch")
plt.legend()
plt.savefig(f'Images/count_relative_languages_decreasing_plot.png')



f_exact_english.close()
f_fixed_english.close()
f_decreasing_english.close()

f_exact_spanish.close()
f_fixed_spanish.close()
f_decreasing_spanish.close()

f_exact_deutch.close()
f_fixed_deutch.close()
f_decreasing_deutch.close()

f_exact_french.close()
f_fixed_french.close()
f_decreasing_french.close()

f_exact_hungarian.close()
f_fixed_hungarian.close()
f_decreasing_hungarian.close()