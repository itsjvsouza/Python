### [Back](../../README.md)
# World 3

## Tuples:
### [072](072.py)
Create a program that has a fully populated Tuple with a count in words, from zero to twenty. Your program should read a number from the keyboard (between 0 and 20) and show it in words.

### [073](073.py)
Create a Tuple filled with the top 20 teams in the Brazilian League Table, in order of placement. Then show: a) The first 5 teams. b) The last 4 table positions. c) Teams in alphabetical order. d) In what position is the Chapecoense team.

### [074](074.py)
Create a program that generates five random numbers and puts them in a Tuple. After that, show the list of generated numbers and also indicate the smallest and largest values that are in the Tuple.

### [075](075.py)
Create a program that reads four values from the keyboard and saves them in a Tuple. At the end, show: a) How many times the value 9 appeared. b) In which position the first value 3 was entered. c) Which were the even numbers.

### [076](076.py)
Create a program that has a single Tuple with product names and their respective prices in sequence. At the end, show a price list, organizing the data in tabular form.

### [077](077.py)
Create a program that has a Tuple with several words (do not use accents). After that, you must show, for each word, what its vowels are.

## Lists:
### [078](078.py)
Write a program that reads 5 numerical values and stores them in a List. At the end, show which was the highest and lowest value typed and their respective positions in the list.

### [079](079.py)
Create a program where the user can type several numerical values and register them in a List. If the number already exists there, it will not be added. At the end, all unique values entered will be displayed in ascending order.

### [080](080.py)
Create a program where the user can type five numerical values and register them in a List, already in the correct insertion position (without using sort()). At the end, show the sorted list on the screen.

### [081](081.py)
Create a program that reads several numbers and puts them in a List. After that, show: a) How many numbers were entered. b) The list of values sorted in descending order. c) Whether the value 5 was entered and is or is not in the list.

### [082](082.py)
Create a program that reads several numbers and puts them in a List. After that, create two extra lists that will contain only the even values and the odd values entered, respectively. At the end, show the three lists generated.

### [083](083.py)
Create a program where the user types an expression that uses parentheses. Your app should analyze whether the expression passed has open and closed parentheses in the correct order.

### [084](084.py)
Create a program that reads the name and weight of several people, keeping them in a List. At the end, show: a) How many people were registered. b) A list of the heaviest people. c) A list of the lightest people.

### [085](085.py)
Create a program where the user can type seven numerical values and register them in a single List that keeps even and odd values separated. At the end, show the even and odd values in ascending order.

### [086](086.py)
Create a program that creates a 3x3 matrix and fills it with values read from the keyboard. At the end, show the matrix on the screen with the correct formatting.

### [087](087.py)
Improve the previous challenge, showing at the end: a) The sum of all even values entered. b) The sum of the values in the third column. c) The highest value in the second row.

### [088](088.py)
Write a program that helps a Mega Sena player create guesses. The program will ask how many games will be generated and will draw 6 random numbers between 1 and 60 for each game, registering everything in a composite list.

### [089](089.py)
Create a program that reads the name and two grades of several students and stores them in a composite list. At the end, show a report card containing the average of each one and allow the user to see the grades of each student individually.

## Dictionaries:
### [090](090.py)
Write a Python program that reads a student's name and average, also storing the status (Approved/Failed) in a Dictionary. At the end, show the content of the structure on the screen.

### [091](091.py)
Create a program where 4 players roll a die and have random results. Store these results in a Dictionary. At the end, put that dictionary in order, knowing that the winner rolled the highest number on the die.

### [092](092.py)
Create a program that reads name, birth year, and work card (CTPS) and registers them (with age) in a Dictionary. If the CTPS is different from ZERO, the dictionary will also receive the year of recruitment and salary. Calculate and add, besides age, at what age the person will retire.

### [093](093.py)
Create a program that manages a football player's performance. The program will read the player's name and how many matches they played. Then it will read the number of goals scored in each match. All this will be stored in a Dictionary, including the total goals scored during the championship.

### [094](094.py)
Create a program that reads the name, gender, and age of several people, storing each person's data in a Dictionary and all dictionaries in a List. At the end, show: a) How many people were registered. b) The average age of the group. c) A list with all women. d) A list with all people with age above average.

### [095](095.py)
Improve CHALLENGE 093 so that it works with several players, including a system to visualize details of each player's performance.

## Functions:
### [096](096.py)
Write a program that has a function called area(), which receives the dimensions of a rectangular land (width and length) and shows the area of the land.

### [097](097.py)
Write a program that has a function called write(), which receives any text as a parameter and shows a message with adaptable size.

### [098](098.py)
Write a program that has a function called counter(), which receives three parameters: start, end, and step, and performs the count. Your program must perform three counts through the function: a) From 1 to 10, 1 by 1. b) From 10 to 0, 2 by 2. c) A personalized count.

### [099](099.py)
Write a program that has a function called larger(), which receives several parameters with integer values. Your program has to analyze all the values and say which one is the largest.

### [100](100.py)
Write a program that has a List called numbers and two functions called draw() and sumEven(). The first function will draw 5 numbers and put them inside the list and the second function will show the sum of all the even values drawn by the previous function.

### [101](101.py)
Create a program that has a function called vote(), which receives a person's birth year as a parameter, returning a literal value indicating whether a person has a DENIED, OPTIONAL, or MANDATORY voting status in elections.

### [102](102.py)
Create a program that has a factorial() function that receives two parameters: the first that indicates the number to calculate and the second called show, which will be a logical value (optional) indicating whether or not the process of calculating the factorial will be shown on the screen.

### [103](103.py)
Write a program that has a function called player(), which receives two optional parameters: a player's name and how many goals they scored. The program should be able to show the player's data, even if some data has not been entered correctly.

### [104](104.py)
Create a program that has the readInt() function, which will work similarly to Python's input() function, but doing the validation to accept only a numerical value.

### [105](105.py)
Write a program that has a notes() function that can receive several grades from students and will return a Dictionary with the following information: quantity of grades, the highest grade, the lowest grade, the class average, and the status (optional).

### [106](106.py)
Make an interactive system that utilizes Python's Interactive Help. The user will type the command and the manual will appear. When the user types the word 'EXIT', the program will terminate.

## Modules and Packages:
### [107](107.py)
Create a module called coin.py that has incorporated functions called increase(), decrease(), double(), and half(). Also make a program that imports this module and uses some of these functions.

### [108](108.py)
Adapt the code from challenge 107, creating an additional function called coin() that manages to show the values as a formatted monetary value.

### [109](109.py)
Modify the functions that were created in challenge 107 so that they accept one more parameter, informing whether the value returned by them will be formatted or not by the function developed in challenge 108.

### [110](110.py)
Add a function called summary() to the coin.py module created in the previous challenges, which shows on the screen some information generated by the functions we already have in the module so far.

### [111](111.py)
Create a package called utilitiesCeV that has two internal modules called coin and data. Transfer all the functions used in challenges 107, 108, and 109 to the first package and keep everything working.

### [112](112.py)
Inside the utilitiesCeV package created in challenge 111, the data module has a function called readMoney() that is capable of functioning like the input() function, but with data validation to accept only values that are monetary.

## Error Handling:
### [113](113.py)
Rewrite the readInt() function from challenge 104, including the possibility of entering an invalid type of number. Also create a readFloat() function with the same functionality.

### [114](114.py)
Create a code in Python that tests whether the Pudim website is accessible from the computer being used.

### [115](115.py)
Create a small final system in Python that allows registering people by name and age in a simple text file. The system will have only two options: register a new person and list all registered people.