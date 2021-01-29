# All Valid Republic of Turkey Identity Numbers Generator
This generator generates all valid "Republic of Turkey Identity numbers". But how can it does?

First things first, you need to know "how are ids created?". Ids are not created randomly, created accorrding to a rule. These rules are listed below:

* Must be 11 characters.

* All digits must be numbers.

* First digit cannot be 0 (zero).

* When we remove the sum of 2, 4, 6, 8 digits from 7 times the total of 1, 3, 5, 7, 9 digits, the number remaining from the 10th part of the result (MOD 10) should give the number in the tenth digit.

* The number remaining from the 10th part of the result from the sum of the top 10 digits (MOD 10) must give the number in the eleventh digit.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This program is generating id in 3 steps:

Step 1 - Generating all 9-digit numbers: I used a while loop for this. This loop's variables is taking all numbers from 100000000 to 999999999.

Step 2 - Generating last 2 digits: You can ask "We are generating all 9-digit numbers, but how is that help? An id needs to be 11-digit? But we have only 9.". Actually ids are 9-digit, but we need to verify it. And last 2 digits are meets this need. But how to generate last 2-digit? Last two id rules are answering this. You can look and find an answer to this question.

Step 3 - Verifying generated id: We generated id, but we need to trust it. So we need to "test" it. And program checking id according to this 5 rules.

And, we did it! Generated a working id. After this, we writing it to a text file and doing all this 3 steps until all ids are created. And program closes.

