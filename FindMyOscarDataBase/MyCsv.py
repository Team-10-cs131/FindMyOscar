import csv

header = ['title', 'genre', 'imageurl']


def read_from_csv(filename):
    output_list = []
    with open(filename, mode='r') as input_file:
        input_reader = csv.reader(input_file, delimiter=',')
        line_count = 0
        for row in input_reader:
            if line_count != 0:
                output_list.append(row[0])
            line_count += 1
        print("Processed " + str(line_count - 1) + " lines")
        return output_list


def write_to_csv(input_data, out_file):
    with open(out_file, mode='w') as movie_file:
        movie_writer = csv.writer(movie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        movie_writer.writerow(header)

        for data in input_data:
            if len(data) != 1:
                movie_writer.writerow(data)
