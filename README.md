# Software-Engineering-Epidemic-Reporting-System
Software Engineering(professional elective in my 6th semester in NKUCS) 3rd programming assignments. The work is to establish an epidemic reporting system by pair programming.
## Brief intro
- a simple report system
- when it begins to run in console, it'll create data.csv if not exist, otherwise read data.csv
- type 1 for continuing operations, 2 for exit and save data in data.csv
- if input is 1, there are 5 options:
  - type 1 for adding an data item
  - type 2 for deleting an data item
  - type 3 for modifying an data item
  - type 4 for seraching for an data item
  - type 5 for outputing all data items
- each data item contains 3 not-null data: ID number(primary key), name and nucleic acid test results(positive or negative).
- before adding, deleting, modifying, searching for an data item, it'll check whether ID number is valid.
## Code intro
- main.py: system main frame
- IDNumVerification.py: to verify whether id number is legal, need to be called by main.py
- constant.py: prestored data with regular expressions for 1st and 2nd generation ID numbers and area codes.
