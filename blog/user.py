def todo_serializer(todo) -> dict:
    return {
        "_id": str(todo["_id"]),
        "title": todo["title"],
        "body": todo["body"],
    }


def todos_serializer(todos) -> list:
    return [todo_serializer(todo) for todo in todos]
