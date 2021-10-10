import psycopg2
import os

def get_connection():
    # get connection object for database
    try:
        connection = psycopg2.connect(database="housing-db", user="postgres", password="password", host="127.0.0.1", port="5432")
        return(connection)

    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)

        return

def insert_data_from_csv(filename):

    '''
    This didn't work for some reason. All this script does is is generate the sql queries to put the data into the db
    It doesn't write anything itself
    As this was a one off data load it's prob fine to not work out why this wasn't working
    '''

    query = r"\copy house_price_paid_master FROM 'C:\Users\liamh\Repositories\house-purchase\data\{0}' DELIMITER ',' CSV;".format(filename)
    print(query)

    # cursor.execute(query)
    # cursor.close()

    return()


def main():
    # connection = get_connection()

    # get list of items in directory
    for i in range(1,28):
        filename = "output_" + str(i) + '.csv'
        # cursor = connection.cursor()
        insert_data_from_csv(filename)

    #connection.close()
    return

main()