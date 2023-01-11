# Write a Python program to create a pie chart of the popularity of programming Languages using matplotli

import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.pie(popularity, labels = languages, autopct = '%1.1f%%')
plt.axis('equal')
plt.title('Popularity of Programming Languages')
plt.show()
