
# scatter plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# titanic = sns.load_dataset("titanic")
# sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# plt.show()
# ..............
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# boat = sns.load_dataset("titanic")
# print (titanic)

# p1=sns.countplot(x='sex', data=titanic, hue='class')
# p1.set_title("Plot for Counting")
# plt.show()
# .............



# Step-1: Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step-2: Set theme
sns.set_theme(style="ticks", color_codes=True)

# Step-3: Import data set (You can also import your own data)
boat = sns.load_dataset("titanic")
# print(boat)

# # Step-4: Plot basic graph with one variable (coount)
# p = sns.countplot(x = "sex", data = boat)
# plt.show()

# # Step-5: Plot basic graph with two variables (count plot)
# p = sns.countplot(x = "sex", data = boat, hue = "class")
# plt.show()

# Step-6: Plot basic graph with two variables (count plot) with titles
p = sns.countplot(x = "sex", data = boat, hue = "class")
p.set_title("Count plot")
plt.show()