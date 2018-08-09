# intern-matching

Ranks and pairs interns by compatibility using [Gale-Shapley Stable Marriage Algorithm](https://en.wikipedia.org/wiki/Stable_marriage_problem#Algorithm).

Compatibility is determined by measuring equality of string attributes for:
  
  - team
  - position
  - product
  - skills

I ran a *LinkedIn Endorsement Party* workshop using these matches.

Each intern submits information about their job to a Google Form.\
The data is copied into an Excel spreadsheet.\
Python reads the data from Excel into a Pandas dataframe.\
Intern objects are created using values from the dataframe.\
Each intern has their compatibility with every other intern ranked.\
The ranking is a simple count of how many similar terms are in the string attributes.\
Interns are paired up each round, beginning with their most compatible counterparts.\
All interns cannot possible be paired with their ideal counterparts in perfectly descending order (from most to least compatible).\
This is because all interns have different order of preferences.\
The Gale-Shapley Stable Marriage Algorithm is implemented to manage differences in ideal pairing preferences.

The result is:
  1) In general, interns will pair with more compatible interns earlier and less compatible interns later.
  2) At no point will there be 2 interns who would prefer to be with each other than with their current match.