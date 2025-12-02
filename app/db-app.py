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
    print("You have chosen an option that requires input information.")
    print("Please enter the desired values for each field\n")

    outputList = []
    for argument in argumentList:
        outputList += [input(argument + ": ")]
    
    print("All fields have been collected. Continuing...")
    print(ASTERISK_STRING)

    return outputList

def createMember(first_name, last_name, email, heart_rate_bpm, current_weight_lb, target_weight_lb):
    # Create the member
    db_query = "INSERT INTO Members (first_name, last_name, email) VALUES ('" + first_name + "', '" + last_name + "', '" + email + "');"
    executeQuery(db_query)

    # Initialize its HealthInfo entry
    db_query = "INSERT INTO HealthInfo (member_id, heart_rate_bpm, current_weight_lb) VALUES ((SELECT member_id FROM Members WHERE first_name = '" + first_name + "' AND last_name = '" + last_name + "'), " + heart_rate_bpm + ", " + current_weight_lb + ");"
    executeQuery(db_query)
    
    # Initialize its FitnessGoals entry
    db_query = "INSERT INTO FitnessGoals (member_id, target_weight_lb) VALUES ((SELECT member_id FROM Members WHERE first_name = '" + first_name + "' AND last_name = '" + last_name + "'), " + target_weight_lb + ");"
    executeQuery(db_query)

def updateMember(first_name, last_name, email, heart_rate_bpm, current_weight_lb, target_weight_lb):
    # Update the email
    db_query = "UPDATE Members SET email = '" + email + "' WHERE first_name = '" + first_name + "' AND last_name = '" + last_name + "');"
    executeQuery(db_query)

    # Update the HealthInfo entry
    db_query = "UPDATE HealthInfo SET heart_rate_bpm = " + heart_rate_bpm + ", current_weight_lb = " + current_weight_lb + " WHERE member_id = (SELECT member_id FROM Members WHERE first_name = '" + first_name + "' AND last_name = '" + last_name + "');"
    executeQuery(db_query)

    # Update the FitnessGoals entry
    db_query = "UPDATE FitnessGoals SET target_weight_lb = " + target_weight_lb + " WHERE member_id = (SELECT member_id FROM Members WHERE first_name = '" + first_name + "' AND last_name = '" + last_name + "');"
    executeQuery(db_query)

# Main Code
if __name__ == '__main__':
    user_role = ""

    user_has_quit = False
    while (not user_has_quit):
        print(ASTERISK_STRING)
        print("COMP 3005 Final Project")
        if (user_role == ""):
            print("\nWhat role of user are you?")
            print("\nOptions:")
            print("\t1) Member")
            print("\t2) Trainer")
            print("\t3) Administrative Staff")
        else:
            print("\nHello " + user_role + "!")
            print("\nOptions:")
            if (user_role == "Member"):
                print("\t1) User Registration")
                print("\t2) Profile Management")
                print("\t3) PT Session Scheduling")
                print("\t4) Group Class Registration")
            elif (user_role == "Trainer"):
                print("\t1) Set Availability")
                print("\t2) Schedule View")
            elif (user_role == "Administrative Staff"):
                print("\t1) Room Booking")
                print("\t2) Class Management")

        print("\tq) Quit")
        print(ASTERISK_STRING)

        user_input = input()

        if (user_input == "q"):
            print("Quitting program...")
            user_has_quit = True

            print(ASTERISK_STRING)
        elif (user_role == ""):
            if (user_input == "1"):
                user_role = "Member"
            elif (user_input == "2"):
                user_role = "Trainer"
            elif (user_input == "3"):
                user_role = "Administrative Staff"
            else:
                print(ASTERISK_STRING)

                print("Entered option is not known. Try again.")
                print(ASTERISK_STRING)
        elif (user_role == "Member"):
            if (user_input == "1"):
                print("Registering new member. Enter desired member information.")

                input_arguments = promptArguments(["first_name", "last_name", "email", "heart_rate_bpm", "current_weight_lb", "target_weight_lb"])
                createMember(input_arguments[0], input_arguments[1], input_arguments[2], input_arguments[3], input_arguments[4], input_arguments[5])

                print(ASTERISK_STRING)
            elif (user_input == "2"):
                print("Updating personal information. Enter first/last name, then enter new information.")

                input_arguments = promptArguments(["first_name", "last_name", "email", "heart_rate_bpm", "current_weight_lb", "target_weight_lb"])
                updateMember(input_arguments[0], input_arguments[1], input_arguments[2], input_arguments[3], input_arguments[4], input_arguments[5])

                print(ASTERISK_STRING)
            else:
                print(ASTERISK_STRING)

                print("Entered option is not known. Try again.")
                print(ASTERISK_STRING)
        elif (user_role == "Trainer"):
            pass
            # else:
            #     print(ASTERISK_STRING)

            #     print("Entered option is not known. Try again.")
            #     print(ASTERISK_STRING)
        elif (user_role == "Administrative Staff"):
            pass
            # else:
            #     print(ASTERISK_STRING)

            #     print("Entered option is not known. Try again.")
            #     print(ASTERISK_STRING)
        else:
            print(ASTERISK_STRING)

            print("Entered option is not known. Try again.")
            print(ASTERISK_STRING)

# Close the connection to the database
DB_CURS.close()
DB_CONN.close()
