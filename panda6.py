#pandas visulization
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# if you want to check the available styles
print(plt.style.available)
#output
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

# to select the style
plt.style.use('seaborn-deep')




df = pd.read_csv(r'C:\Users\HP\Downloads\Ice Cream Ratings.csv')
print(df)
df.set_index('Date')
# to visualize data in pandas we use what we cal plot
# visual = df.plot()  # default it will print out a line plot
# print(visual)

# now to select what design to output use kind =
visual = df.plot(kind = 'line')


# if you want to break it into  each columns
visual1 = df.plot(kind= 'line',subplots = True)


# some of the arguments we can use to make it look nice
#1.putting a title
df.plot(kind = 'line',title = 'Ice Cream Ratings')
# adding label to the x axis the bottom and y axis the  left beginning of column
df.plot(kind = 'line',title = 'Ice Cream Ratings',xlabel = 'Daily Ratings',ylabel='Scores')

# now we are using a bar plot
df.plot(kind = 'bar')
# now to put data on top of each other like the flavor rating,texture,overall in one column d
df.plot(kind = 'bar',stacked = True)

# if we only one column to be displayed in this case flavor rating
df['Flavor Rating'].plot(kind = 'bar',stacked = True)

# normally it would default to vertical bar chart if selected in kind is bar
# to change it to horizontal, no need to add kind since barh already
df.plot.barh(stacked = True)

# now using scatter plot,note you need to indicate the x and y axis
# choosing any of the columns
df.plot.scatter(x = 'Texture Rating',y = 'Overall Rating')

#deciding the size of the dots
df.plot.scatter(x='Texture Rating',y= 'Overall Rating',s= 100)

#choosing the color of the dots
df.plot.scatter(x = 'Texture Rating ',y= 'Overall Rating',s=100,c= 'Yellow')

#Using a histogram(you can choose the bins = how many columns will be shown for the data) similar to a bar chart
df.plot.hist(bins = 2)

# box plot or chat whiskers
df.boxplot()

# area
df.plot.area()
#controling the size of the image=figuresize
df.plot.area(figsize = (10,5))# length and width

#pie
df.plot.pie(y= 'Flavor Rating',figsize = (10,6))
# you need the y as basis (width)

