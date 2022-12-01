# dividedBills

TODO:
Graphic UI
Testing
prepare and sanitize input csv
----

Google collab to test without installing anything:
https://colab.research.google.com/drive/1jf7Cos5YzT6CZejieC2cMgfwKXIZ_QAJ

---



pip3 install -r requirements.txt

Usage:

python3 main.py <Optional: path to people txt file> <Optional: path to bills csv file>

Two files must be created in the same directory:

people.txt -> One name in each line of all the people that will participate.
bills.csv Heading: Who paid, ammount, description, date, Person 1 excluded, ..., person n excluded (see 'test.csv')