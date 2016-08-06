APP_ID = "amzn1.echo-sdk-ams.app.5e07c5c2-fba7-46f7-9c5e-2353cec8cb05"
STATE_KEY = "STATE"
DB_TABLE = 'my_cookbook_users'
LOGGER = 'my_cookbook'


class States:
    ASK_MAKE_COOKBOOK = '_ASK_MAKE_COOKBOOK'
    ASK_SEARCH = '_ASK_SEARCH'
    ASK_TUTORIAL = '_ASK_TUTORIAL'
    ASK_MAKE_SOMETHING = '_ASK_MAKE_SOMETHING'
    INGREDIENTS_OR_INSTRUCTIONS = '_INGREDIENTS_OR_INSTRUCTIONS'
    INITIAL_STATE = '_INITIAL_STATE'
    NEW_RECIPE = '_NEW_RECIPE'
    PROMPT_FOR_START = '_PROMPT_FOR_START'
    SEARCH_ONLINE = '_SEARCH_ONLINE'
    STATELESS = ''
    TELL_TUTORIAL = '_TELL_TUTORIAL'
