test_recipe = {
    'id': 0,
    "category": {
        "name": "breakfast",
        "subcategory": {
            "attributes": "buttermilk",
            "name": "pancakes"
        }
    },
    "cook_time": "10 minutes",
    "ingredients": [
        {
            "name": "flour"
        }, {
            "name": "salt"
        }, {
            "name": "baking soda"
        }, {
            "name": "baking powder"
        }, {
            "name": "egg"
        }, {
            "name": "buttermilk"
        }, {
            "name": "butter"
        }
    ],
    "instructions": [
        {
            "speech": [
                "mix", {
                    "name": "flour",
                    "quantity": 0.5,
                    "units": "cups"
                }, "with", {
                    "name": "salt",
                    "quantity": 0.25,
                    "units": "teaspoon"
                }, ",", {
                    "name": "baking soda",
                    "quantity": 0.25,
                    "units": "teaspoon"
                }, ", and", {
                    "name": "baking powder",
                    "quantity": 0.5,
                    "units": "teaspoon"
                }
            ]
        }, {
            "speech": [
                "beat in an", {
                    "name": "egg",
                    "quantity": 1,
                    "units": "None"
                }, "and", {
                    "name": "buttermilk",
                    "quantity": 0.5,
                    "units": "cups"
                }
            ]
        }, {
            "speech": [
                "melt the", {
                    "name": "butter",
                    "quantity": 1,
                    "units": "tablespoon"
                }, "and beat into the batter"
            ]
        }
    ],
    "main_ingredient": "buttermilk",
    "name": "classic buttermilk pancakes",
    "nutrition": {
        "fat": {
            "unit": "g",
            "value": 2
        },
        "sodium": {
            "unit": "g",
            "value": 1
        }
    },
    "prep_time": "10 minutes",
    "tags": [
        "sweet", "buttery", "warm"
    ],
    "total_time": "20 minutes"
}

test_online_recipes = [
    test_recipe,  # all we know how to make is pancakes
]
