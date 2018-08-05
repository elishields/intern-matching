# intern-matching

Built this for a LinkedIn Endorsement workshop.
Interns endorse each other for their compatible skills.

Each intern submits Google form with their information.
Data is aggregated into Excel spreadsheet.
Data is read from Excel into Pandas dataframe.
Each intern is an object with string attributes for:
  - team
  - position
  - product
  - skills

Each intern has their compatibility with every other intern ranked.
The ranking is a simple count of how many similar terms are in their string attributes.
Interns are paired up each round, like speed dating.
Interns begin with their most compatible partner.
Their future pairs are in descending order of compatibility.

The Gale-Shapley Stable Marriage Algorithm is implemented to manage different ideal pairing preferences.

This was fun.
