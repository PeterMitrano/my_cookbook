import random

from my_cookbook.util import core
from my_cookbook.util import responder
from my_cookbook.util import recipes_helper


class NewRecipeHandler():
    def StartNewRecipeIntent(self, handlers, persistant_attributes, attributes, slots):
        if 'RecipeName' not in slots:
            attributes[core.STATE_KEY] = core.States.NEW_RECIPE
            return responder.ask(
                "I couldn't figure what recipe you wanted. Try saying, How do I make pancakes?",
                'Try saying, How do I make pancakes?', attributes)
        else:
            recipe_name = slots['RecipeName']['value']

            # search the users recipes to find appropriate recipes.
            # the value here is a (possibly empty) list of recipes in order
            # of some ranking I have yet to devise.
            recipes = recipes_helper.search_my_recipes(persistant_attributes, recipe_name)

            if len(recipes) == 0:
                attributes[core.STATE_KEY] = core.States.ASK_SEARCH
                return responder.ask("I didn't find any recipe for " + recipe_name +
                                     ", In your cookbook. Should I find one online?",
                                     "Do you want to find another recipe?", attributes)
            elif len(recipes) == 1:
                attributes[core.STATE_KEY] = core.States.ASK_MAKE_COOKBOOK
                best_guess_recipe_name = recipes[0]['name']
                attributes['current_recipe'] = recipes[0]
                return responder.ask("I found a recipe for " + best_guess_recipe_name +
                                     ", In your cookbook. Do you want to use that?", None,
                                     attributes)
            elif len(recipes) < 3:
                attributes[core.STATE_KEY] = core.States.ASK_WHICH_RECIPE
                recipe_names = ','.join([recipe['name'] for recipe in recipes])
                return responder.ask(
                    "I found a recipes for " + recipe_names +
                    ", In your cookbook. Do you want the first one, the second one, or the third one?",
                    None, attributes)
            else:
                # here would be a good spot to ask questions to narrow down
                # which recipe the user wants to make
                # for now just say how many we found I guess
                return responder.tell("I found " + len(recipes) + " recipes")

    def Unhandled(self, handlers, persistant_attributes, attributes, slots):
        persistant_attributes[core.STATE_KEY] = attributes[core.STATE_KEY]
        return responder.tell("I'm confused. Try asking me what you want to make.")


handler = NewRecipeHandler()
state = core.States.NEW_RECIPE
