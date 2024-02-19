abstract_schema = {
    "type": "object",
    "required": [
        "title",
        "presentation_type",
        "topic",
        "authors",
        "bio",
        "abstract",
    ],
    "properties": {
        "title": {"type": "string", "minLength": 1},
        "presentation_type": {"type": "string", "minLength": 1},
        "topic": {"type": "string", "minLength": 1},
        "bio": {"type": "string", "minLength": 1},
        "abstract": {"type": "string", "minLength": 1},
        "authors": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "title",
                    "first_name",
                    "last_name",
                    "organization",
                    "affilation",
                    "is_presenter",
                ],
                "properties": {
                    "title": {"type": "string", "minLength": 1},
                    "first_name": {"type": "string", "minLength": 1},
                    "last_name": {"type": "string", "minLength": 1},
                    "organization": {"type": "string", "minLength": 1},
                    "is_presenter": {"type": "boolean"},
                    "affilation": {
                        "type": "object",
                        "required": ["affilation", "city", "country", "state"],
                        "properties": {
                            "affilation": {"type": "string", "minLength": 1},
                            "city": {"type": "string", "minLength": 1},
                            "country": {"type": "string", "minLength": 1},
                            "state": {"type": "string"},
                        },
                    },
                },
            },
        },
    },
}
