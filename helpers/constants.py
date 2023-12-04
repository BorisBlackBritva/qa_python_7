

class Constants:

    COURIERS = {
        'valid': [
            {
                'login': 'courier_111_777',
                'password': 'password1',
                'firstName': 'Elon Lask1'
            },
            {
                'login': 'courier_112_777',
                'password': 'password1',
                'firstName': 'Elon Lask1'
            },
        ],
        'incorrect_credentials': [
            {
                'login': 'courier_1_777_777',
                'password': 'password1'
            },
            {
                'login': 'courier_1_777',
                'password': 'password1_1'
            }
        ],
        'without_mandatory': [
            {
                'password': 'password1',
            },
            {
                'login': 'specific1',
            },
            {
                "login": '',
                'password': 'password1',
            },
            {
                'login': 'specific1',
                "password": ''
            }
        ]
    }

    ORDERS = [
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]
        },
         {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "GREY"
            ]
        },
         {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK",
                "GREY"
            ]
        },
         {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
    ]
