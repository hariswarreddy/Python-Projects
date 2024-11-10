#Model of KBC using Kalki 2898AD Movie
#Designed By : Bontha Hariswar Reddy


questions = [
    [
        "Who is the Director of Kalki?", "SS Rajamouli", "RGV", "Nag Ashwin",
        "Prashanth Neel", 3
    ],
    [
        "Who is Karna in kalki?", "Prabhas", "Amitabh", "Dulquer Salman",
        "Vijay ", 1
    ],
    [
        "Who is depicted as Parasurama in Kalki", "Prabhas", "Nani",
        "Dulquer Salman", "Vijay devarkonda", 3
    ],
    [
        "Who is Arjuna in kalki?", "Prabhas", "Amitabh", "Dulquer Salman",
        "Vijay devarkonda", 4
    ],
    [
        "Who is Sumathi in kalki?", "Anna Ben", "Deepika Padukone",
        "Mrunal takur", "Keerthi Suresh", 2
    ],
    [
        "Who is Ashwathamma in kalki?", "Prabhas", "Amitabh", "Dulquer Salman",
        "Vijay devarkonda", 2
    ],
    [
        "Who is Kyra in kalki?", "Anna Ben", "Deepika Padukone",
        "Mrunal takur", "Keerthi Suresh", 1
    ],
    [
        "Who gave Voice over to Bujji in Kalki?", "Anna Ben",
        "Deepika Padukone", "Mrunal takur", "Keerthi Suresh", 4
    ],
    [
        "Who is the Music Director of Kalki?", "Anirudh", "Rockstar DSP",
        "Santhosh Narayanan", "Kala Bhairava", 3
    ],
    [
        "Who is Roxie in Kalki?", "Disha Patani", "Deepika Padukone",
        "Mrunal takur", "Keerthi Suresh", 1
    ],
    [
        "Who is Supreme Yaskin in kalki?", "Prabhas", "Amitabh", "Nani",
        "Kamal Haasan", 4
    ],
    [
        "Who acted as  Lord Krishna in kalki?", "Mahesh Babu", "Nani",
        "Krishna Kumar", "Allu Arjun", 3
    ],
]
levels = [
    1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000,
    100000
]
money = 0
i = 0
for i in range(0, len(questions)):
  question = questions[i]
  print("------------------------------------")
  print(f"question for Rs.{levels[i]}\n")
  print(f"{question[0]}\n")
  print(f"1.{question[1]}       2.{question[2]}\n")
  print(f"3.{question[3]}       4.{question[4]}\n")
  reply = int(input("Enter the answer (1-4):"))
  if (reply == question[len(question) - 1]):
    print("\nYay!! It's Correct\n")
    if (i >= 1 and i < 3):
      money = levels[1]
    elif (i >= 3 and i < 5):
      money = levels[3]
    elif (i >= 5 and i < 7):
      money = levels[5]
    elif (i >= 7 and i < 9):
      money = levels[7]
    elif (i >= 9 and i < 11):
      money = levels[9]
    elif (i == 11):
      money = levels[11]
  elif reply != 1 and reply != 2 and reply != 3 and reply != 4:
    print("\nSelected Invalid Option")
    break
  else:
    print("Ohh Wrong answer!!\n")
    break

print("\nTake home money is: ", money)
