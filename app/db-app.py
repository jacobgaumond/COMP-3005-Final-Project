import psycopg2

ASTERISK_STRING = "**********************"

# Create the db connection
DB_CONN = psycopg2.connect("host=localhost dbname=postgres user=postgres password=assignment-password")

# Create a db cursor object for executing commands
DB_CURS = DB_CONN.cursor()

"""
Helper function used to facilitate the execution of commands on the psql server
"""
def executeQuery(db_query):
    DB_CURS.execute(db_query)

    print("Query complete. Printing result(s)...\n")
    try: # Try to retrieve a response
        for result in DB_CURS.fetchall():
            print(result)
    except: # Handle no response
        print("No response was provided.")

    # Ripple changes out to database after executing commands
    DB_CONN.commit()

"""
Helper function used to prompt a user for function argument values.
"""
def promptArguments(argumentList):
    print("You have chosen an option that calls a function requiring arguments.")
    print("Please enter the desired values for each argument\n")

    outputList = []
    for argument in argumentList:
        outputList += [input(argument + ": ")]
    
    print("All arguments have been collected. Continuing...")
    print(ASTERISK_STRING)

    return outputList

# Main Code
if __name__ == '__main__':
    user_has_quit = False
    while (not user_has_quit):
        print(ASTERISK_STRING)
        print("COMP 3005 Final Project")
        print("\nOptions:")
        
        print("\tq) Quit")
        print(ASTERISK_STRING)

        user_input = input()
        
        if (user_input == "q"):
            print("Quitting program...")
            user_has_quit = True

            print(ASTERISK_STRING)
        else:
            print(ASTERISK_STRING)

            print("Entered option is not known. Try again.")
            print(ASTERISK_STRING)

# Close the connection to the database
DB_CURS.close()
DB_CONN.close()
