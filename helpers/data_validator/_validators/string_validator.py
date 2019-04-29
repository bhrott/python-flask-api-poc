def validate_string(schema, value, ctx):
    if type(value) is not str:
        ctx.error(
            error_type='type',
            message='The value should be a string'
        )
        return

    if 'max_length' in schema:
        max_length = schema['max_length']
        if len(value) > max_length:
            ctx.error(
                error_type='max_length',
                message='The value should have less than {} characters'.format(max_length)
            )
            return