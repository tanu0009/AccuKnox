import requests
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

names = [user["name"] for user in data[:5]]
scores = [len(user["username"]) * 10 for user in data[:5]]

average = sum(scores) / len(scores)
print("Average Score:", average)

plt.bar(names, scores)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.show()
