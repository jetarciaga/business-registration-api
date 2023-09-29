from marshmallow import Schema, fields


class BusinessSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str()