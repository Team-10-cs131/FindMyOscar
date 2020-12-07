import DatabaseConnector
import ApiHitter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #  API CREDENTIALS
    api_key = '911ae236'

    #  DATABASE CREDENTIALS
    hostname = '127.0.0.1'
    user = 'root'
    password = 'carlsagan42'
    db = 'find_my_oscar'

    #  QUERY
    award_category = "'MAKEUP AND HAIRSTYLING'"
    select_query = "SELECT * FROM artifact_data WHERE category=" + award_category

    #  OPEN CONNECTION TO ARTIFACT DATABASE
    artifact_connection = DatabaseConnector.create_connection(hostname, user, password, db)

    #  READ CATEGORY FROM ARTIFACT DATABASE
    movies = DatabaseConnector.execute_read_query(artifact_connection, select_query)

    #  WRITE MOVIES TO OUR DATABASE
    for movie in movies:
        movie += ApiHitter.search_title(api_key, movie[3])
        insert_query = """
            INSERT INTO
              `our_data` (`year`, `category`, `winner`, `entity`, `released`, `plot`, `poster`)
            VALUE 
              """ + str(movie)
        DatabaseConnector.execute(artifact_connection, insert_query)

    print(len(movies))
