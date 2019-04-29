def validate_list(schema, value, ctx):
    if type(value) is not list:
        ctx.error(
            error_type='type',
            message='The value should be a list'
        )
        return

    # TODO: min_length
    # TODO: max_length

    item_schema = schema['item_schema']

    for index, item in enumerate(value):
        ctx.add_to_path('${}'.format(str(index)))
        validator = ctx.validators[item_schema['$type']]
        validator(
            schema=item_schema,
            value=item,
            ctx=ctx
        )
        ctx.pop_path()