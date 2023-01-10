"""Write a Python program to display a bar chart and
 pie chart of the popularity of programming Languages using matplotlib."""

import matplotlib.pyplot as plt

def bar_chart(data):
    plt.bar(data.keys(),data.values(),color="green")
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("Popularity of programming languages")
    plt.show()

def pie_chart(data):
    plt.pie(data.values(),labels=data.keys(),autopct="%1.1f%%")
    plt.title("Popularity of programming languages")
    plt.show()

data={'Python': 22.2, 'Java': 17.6, 'PHP': 8.8, 'JavaScript': 8, 'C#': 7.7, 'C++': 6.7}
bar_chart(data)
pie_chart(data)    