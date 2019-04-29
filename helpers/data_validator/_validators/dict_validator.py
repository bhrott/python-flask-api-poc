def validate_dict(schema, value, ctx):
    if type(value) is not dict:
        ctx.error(
            error_code='type',
            message='The value should be a dict',
            schema=schema,
            value=value
        )
        return

    # TODO: strict

    schema_props = schema['props']
    value_props = value

    for schema_prop_key in schema_props:
        prop_schema = schema_props[schema_prop_key]
        prop_value = value_props[schema_prop_key]
        validator = ctx.validators[prop_schema['$type']]

        ctx.add_to_path(schema_prop_key)

        validator(prop_schema, prop_value, ctx)

        ctx.pop_path()