def validate_string(schema, value, ctx):
    if type(value) is not str:
        ctx.error(
            error_code='type',
            message='The value should be a string',
            schema=schema,
            value=value
        )
        return

    if 'max_length' in schema:
        max_length = schema['max_length']
        if len(value) > max_length:
            ctx.error(
                error_code='max_length',
                message='The value should have less or equal than {} characters'.format(max_length),
                schema=schema,
                value=value
            )
            return

    if 'min_length' in schema:
        min_length = schema['min_length']
        if len(value) < min_length:
            ctx.error(
                error_code='min_length',
                message='The value should have more or equal than {} characters'.format(min_length),
                schema=schema,
                value=value
            )
            return