def map_db_result_to_user(db_result, user):
    user.id = db_result['_id']
    user.email = db_result['email']
    user.password = db_result['password']

    return user
