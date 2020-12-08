from flask import Flask
from flask_restful import Api, Resource, reqparse
import DataMassager
import DatabaseConnector

app = Flask(__name__)
api = Api(app)

#  DATABASE CREDENTIALS
hostname = '127.0.0.1'
user = 'root'
password = 'carlsagan42'
db = 'find_my_oscar'

my_connection = DatabaseConnector.create_connection(hostname, user, password, db)
select_all_query = "SELECT * FROM our_data"

movies_tuple_list = DatabaseConnector.execute_read_query(my_connection, select_all_query)
movies = []
fields = ('year', 'category', 'winner', 'entity', 'released', 'plot', 'poster')
for movie_tuple in movies_tuple_list:
    movie_list_entry = DataMassager.tuple_to_dict(movie_tuple, fields)
    movies.append(movie_list_entry)


class Default(Resource):
    def get(self):
        if movies is None:
            return "Movie database is empty.", 404
        return movies, 200


class Entity(Resource):
    def get(self, entity):
        for movie in movies:
            if entity == movie["entity"]:
                return movie, 200
        return "Movie not found", 404

    def post(self, entity):
        parser = reqparse.RequestParser()
        parser.add_argument("year")
        parser.add_argument("category")
        parser.add_argument("winner")
        parser.add_argument("released")
        parser.add_argument("plot")
        parser.add_argument("poster")
        args = parser.parse_args()

        for movie in movies:
            if entity == movie["entity"]:
                return "Movie with title {} already exists".format(entity), 400

            movie = {
                        "year": args["year"],
                        "category": args["category"],
                        "winner": args["winner"],
                        "entity": entity,
                        "released": args["released"],
                        "plot": args["plot"],
                        "poster": args["poster"]
                    }
            movies.append(movie)
            return movie, 201

    def put(self, entity):
        parser = reqparse.RequestParser()
        parser.add_argument("year")
        parser.add_argument("category")
        parser.add_argument("winner")
        parser.add_argument("released")
        parser.add_argument("plot")
        parser.add_argument("poster")
        args = parser.parse_args()

        for movie in movies:
            if entity == movie["category"]:
                movie = {
                            "year": args["year"],
                            "category": args["category"],
                            "winner": args["winner"],
                            "entity": entity,
                            "released": args["released"],
                            "plot": args["plot"],
                            "poster": args["poster"]
                        }
                return movie, 200

            movie = {
                        "year": args["year"],
                        "category": args["category"],
                        "winner": args["winner"],
                        "entity": entity,
                        "released": args["released"],
                        "plot": args["plot"],
                        "poster": args["poster"]
                    }
            movies.append(movie)
            return movie, 201

    def delete(self, entity):
        global movies
        movies = [movie for movie in movies if movie["entity"] != entity]
        return "{} is deleted.".format(entity), 200


class Category(Resource):

    def get(self, category):
        parser = reqparse.RequestParser()
        parser.add_argument("year")
        parser.add_argument("winner")
        parser.add_argument("entity")
        parser.add_argument("released")
        parser.add_argument("plot")
        parser.add_argument("poster")
        args = parser.parse_args()

        select_category_query = "SELECT * FROM our_data WHERE `category`='" + category + "'"

        if args["year"] is not None:
            select_category_query += " AND `year`='" + args["year"] + "'"
        if args["winner"] is not None:
            select_category_query += " AND `winner`='" + args["winner"] + "'"

        category_tuple_list = DatabaseConnector.execute_read_query(my_connection, select_category_query)
        category_list = []

        if not category_tuple_list:
            return "No movies under category {}.".format(category), 404

        for movie in category_tuple_list:
            category_list.append(DataMassager.tuple_to_dict(movie, fields))

        return category_list, 200

    def post(self, category):
        pass

    def put(self, category):
        pass

    def delete(self, category):
        pass


if __name__ == "__main__":
    api.add_resource(Entity, "/movies/title/<string:entity>")
    api.add_resource(Category, "/movies/category/<string:category>")
    api.add_resource(Default, "/movies")

    app.run(debug=True)
