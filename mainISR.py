from Models.book import Book

while(True):

    command = input("\n-->")
    command_parsed = command.split()
    model = command_parsed[1]
    query_type = command_parsed[0]
    body = ' '.join(command_parsed[2:])

    if model == 'book':
        Book.query(query_type, body)
