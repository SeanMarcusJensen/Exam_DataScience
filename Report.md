# Report

## Task 1

---

### Part 1 Question

> What kind of data set is this?

We know this data set is an overview of who died on the titanic; the data contains information describing each person. E.g., Age, name, gender and which cabin on the ship they were assigned.

When starting out analyzing the data set, I'll start with checking out how the data looks and what types it contains. We have integers, floats and objects; All of which is strings.

Getting to the context, the attributes are:

### PassengerId

PassengerID is a integer. It is used as indexing for the passengers. To all fairness, I feel like this is redundant for us, and I'll probably drop this in further analyzing.

I would prefer to use ticket as an unique identifier because it should be, but when looking closer at that attribute, I clearly see that its not.

### Survived

Survived attribute is a boolean which tells us if the person died or not on the titanic.

### PClass

This is an Integer describing what socio-economic class the passenger is. This would be Lower, Middle and Higher class.
1 = Higher
2 = Middle
3 = Lower.

### Name

This is an string, and is the identifier of a person / but not a unique one.
We can actually get a lot information just in the name, since this was in the 1910s everyone was so polite; in the names they were called Master, miss, mrs, ms and mr. With this information we know if the person is married, young, or unmarried.

### Sex

This is a string saying what kind of gender the person has.

### Age

This is a float describing the age of the person. Ages below 1 is fractions, rest is not.

### SibSp

This is a Integer describing number of siblings and spouse is onboard.

### Parch

This is a Integer describing number of parents/children onboard.

### Ticket

This is a string, and is the ticket. I Would prefer to use this as a unique identifier; since one can only have one Ticket per person ( as this gives more sense ). But I assume one family might board on one common ticket.

### Fare

this is a float, and is the price the passenger paid for its ticket onboard the titanic.
I would assume there was mostly the same prices for each PClass; but it might be a difference coming from where the passenger bought the ticket - if it was on sale or if the state the passenger lived in has different taxes?

### Cabin

this is a string, and is an unique ID for the cabin the passenger is staying in. This is not unique id(UID) for each passenger, but an UID for the cabin. Multiple passengers can have the same cabin UID.

### Embarked

This is a Character describing where the passenger mounted from. People embarked from  Southampton, Cherbourg, and Queenstown hence the chars C, S and Q.

## Task 2

> What can you use this data set for? Name at least 2 different applications, or examples of getting value out of the data set.

### Application / Example 1

Based on Sosio-economic status(Pclass), Fare and Embarkment we can analyze the wealth of each citys population, and from there decide what type of products to display on onboarding. Also if we should be more exclusive on onboarding - to accomodate the wealthier families.

When doing this, the sales of products will be sold more effectivitly; wealthier persons might be able to purchase champaign, wheras more economic unstable families can only purchase beers.

This analyzis can also be used for other application than cruises - like cities can use this analyzis to increase prices of wares etc.

### Application / Example 2

We can take a look at number of parents / children (Parch) and see if larger families death rate is larger than lonely passengers, and therefor place larger families where there are more escapeboats / better evacuation possibilities.

## Task 2b

the data need some processing. Cabin - has alot of missing values(over 60%) and since this is 'unique' its really hard for me to find values for it, We could try to map persons by name and ticket to make sense of cabin, and then fill those values - but since both my applications does not have any use of cabin, I will exclude this.

When it comes to age, theres alot of missing values there as well, but I could do some mean calculations and fill those values.

And Embarked is missing 2 values, which vill we definantly filled with the highes 2.
I could ofc do some more advanced inserts to this, and calculate the fare and pclass, and get embarked from those in same the same category. but I do not feel like the trouble is worth it for 2 values.

## TODOS

---

- See Corr between PClass and Survived.
- See Corr between Cabin and Survived.
- See Corr between Age and Survived.
- See Corr between SibSp and Survived: Might be harder for one to get all its siblings aboard emergency boat; and therefore die himself.
- See Corr between Parch
- Pie-plot on Embarked.
- See Corr on Fare and Embarked.
