import wikipedia
import sqlite3



def register(entry):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS famous_people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            summary TEXT
        )
        """)
    # Get the last id of the table
    c.execute("SELECT id FROM famous_people")
    record = c.fetchall()
    # if not record => first entry id must be 1
    if not record:
        id = 1
    else:
        id = record[-1][0] + 1
    
    famous_people = {"id": id ,"name": entry["name"], "summary": entry["summary"]}
    # Check if already exist in the table
    c.execute("SELECT name FROM famous_people WHERE name = (:name)", famous_people)
    alreay_exist = c.fetchall()
    if alreay_exist:
        print(f"{famous_people['name']} is already register in the database")
    else:
        c.execute("INSERT INTO famous_people VALUES (:id, :name, :summary)", famous_people)
        print(f"{famous_people['name']} has been registered in your database")
    conn.commit()
    conn.close()


def search_people(famous_people: str):
    # Check if there is a match
    if wikipedia.search(famous_people):
        # Check if it's exactly the same name
        if wikipedia.search(famous_people)[0].lower() == famous_people.lower():
            # This block code check if there's a name but no page (example: Joe Biden => match name but no page)
            try:
                search = wikipedia.page(famous_people)
                summary = wikipedia.summary(famous_people, sentences=1)
                entry = {
                    "name": search.title,
                    "summary": summary
                }
                register(entry)
            except wikipedia.exceptions.PageError:
                print("It seems that we found the name you are looking for but not his page. Try again with someone else.")
        else:
            print("I don’t know this person")
            suggestion = wikipedia.suggest(famous_people)
            # if there is a match && a suggestion, the program give the suggestion
            if suggestion:
                print(f"Did you mean {suggestion.title()}?")
    else:
        print("I don't know this person")


if __name__ == "__main__":
    search = input("Which famous people would you like to add to the database ? ")
    search_people(search)