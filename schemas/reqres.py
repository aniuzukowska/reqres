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


SchemaLoginUnsuccessful = Schema(
    {
        "error": str
    },
    required=True,
    extra=PREVENT_EXTRA
)


SchemaLoginSuccessful = Schema(
    {
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)


SchemaUpdateUser = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

