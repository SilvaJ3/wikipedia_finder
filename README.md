# Wikipedia project for technical test

## Rules

The goal of the application we would like you to develop is to find information about famous
people on wikipedia and put that information inside a simple database. Application can be a
simple “command line” python program.

1. The program will receive the full name of someone famous (example : Donald Trump)
2. It will look if the name is known by “wikipedia”.
  1. If not, it will print a message “I don’t not know this person”. If possible, it could also
  suggest another person with a similar name. (Example: if you type Bill Clanton, the
  program can suggest “Did you mean Bill Clinton?”).
  2. If the name is known by “wikipedia”, a new entry will have to be created in a table
  called “famous_people” in a database. The “famous_people” table is a table with
  three columns :
    1. an ID (starting at 1 for the first record),
    2. a “name” (containing the full name of the person)
    3. a “summary”: the summary of wikipedia’s page about the person.

## NB :

- There is a *try/except* block code to avoid the **wikipedia.exceptions.PageError** which happens when I try to search *Joe Biden*. There were a match with the **wikipedia.search** but not with the **wikipedia.page**.

- The Suggestion part works but for somes *less famous people* it seems not work. e.a. : *Dilma Roussef* doesn't give the suggestion for *Dilma Roussef**f***

- When the program try to register the famous people, it checks before if there is already one entry in the DB for the same name