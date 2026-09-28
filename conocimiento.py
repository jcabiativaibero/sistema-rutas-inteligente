# Base de conocimiento del sistema de transporte

conexiones = {
    "Portal Norte": [
        "Toberín",
        "Calle 100"
    ],

    "Toberín": [
        "Portal Norte",
        "Calle 100"
    ],

    "Calle 100": [
        "Portal Norte",
        "Toberín",
        "Calle 72"
    ],

    "Calle 72": [
        "Calle 100",
        "Calle 63"
    ],

    "Calle 63": [
        "Calle 72",
        "Universidades"
    ],

    "Universidades": [
        "Calle 63",
        "Museo del Oro"
    ],

    "Museo del Oro": [
        "Universidades",
        "Las Aguas"
    ],

    "Las Aguas": [
        "Museo del Oro"
    ]
}