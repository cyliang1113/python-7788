from dice import Dice
import matplotlib.pyplot as plt
import pygal


dice = Dice()

res = []
for i in range(1000):
    r = dice.roll()
    res.append(r)
print(type(res))

# 计算每个点出现的次数
count = []
for i in range(1, dice.num_sides + 1):
    c = res.count(i)
    count.append(c)
print(count)

# plt.scatter(range(1, dice.num_sides + 1), count)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()

hist = pygal.Bar()
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.add('D6', count)
hist.render_to_file('dice_visual.svg')


