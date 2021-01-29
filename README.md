# All Valid Republic of Turkey Identity Numbers Generator
This generator generates all valid "Republic of Turkey Identity numbers". But how can it does?

First things first, you need to know "how are ids created?". Ids are not created randomly, created accorrding to a rule. These rules are listed below:

* Must be 11 characters.

* All digits must be numbers.

* First digit cannot be 0 (zero).

* When we remove the sum of 2, 4, 6, 8 digits from 7 times the total of 1, 3, 5, 7, 9 digits, the number remaining from the 10th part of the result (MOD 10) should give the number in the tenth digit.

* The number remaining from the 10th part of the result from the sum of the top 10 digits (MOD 10) must give the number in the eleventh digit.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
