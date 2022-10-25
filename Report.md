# Report

## Task 1

---

**Part 1 Question**

*What kind of data set is this?*

**Part 1 Answer**

We know this data set is an overview of who died on the titanic; the data contains information describing each person. E.g., Age, name, gender and which cabin on the ship they were assigned.

When starting out analyzing the data set, I'll start with checking out how the data looks and what types it contains. We have integers, floats and objects; All of which is strings.

Getting to the context, the attributes are:

### PassengerId
PassengerID is a integer. It is used as indexing for the passengers. To all fairness, I feel like this is redundant for us, and I'll probably drop this in further analyzing.

I would prefer to use ticket as an unique identifier because it should be, but when looking closer at that attribute, I clearly see that its not.

### Survived
Survived attribute is a boolean which tells us if the person died or not on the titanic.

### PClass

This is an Integer describing what socio-economic class the passenger is. 

### Name

This is an string, and is the identifier of a person / but not a unique one.

### Sex

This is a string saying what kind of gender the person has.

### Age

This is a float describing the age of the person. Ages below 1 is fractions, rest is not.

### SibSp

This is a Integer describing number of siblings and or spouse is onboard.

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


## TODOS

---

- See Corr between PClass and Survived.
- See Corr between Cabin and Survived.
- See Corr between Age and Survived.
- See Corr between SibSp and Survived: Might be harder for one to get all its siblings aboard emergency boat; and therefore die himself.
- See Corr between Parch
