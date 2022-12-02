from voluptuous import Schema, PREVENT_EXTRA, All, Length, Any


SchemaCreateUser = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA
)

