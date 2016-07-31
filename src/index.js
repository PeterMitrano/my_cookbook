/**
 * @fileOverview
 * @author Peter Mitrano- mitrnanopeter@gmail.com
 */

'use strict';

var Alexa = require('./alexa');
var Core = require('./core');

var AskMakeCookbookHandlers = require('./state_handlers/ask_make_cookbook');
var AskSearchHandlers = require('./state_handlers/ask_search');
var AskTutorialHandlers = require('./state_handlers/ask_tutorial');
var IngredientsOrInstructionsHandler = require('./state_handlers/ingredients_or_instructions');
var NewRecipeHandlers = require('./state_handlers/new_recipe');
var PromptForStartHandlers = require('./state_handlers/prompt_for_start');
var TellTutorialHandlers = require('./state_handlers/tell_tutorial');

/** this can be found on the amazon developer page for the skill */
var APP_ID = 'amzn1.echo-sdk-ams.app.5e07c5c2-fba7-46f7-9c5e-2353cec8cb05';

/**
 * Handle requests from the user when we are not in any given state.
 * This usually means the first time the user launches a new session,
 * but it could be other things
 */
var StatelessHandlers = {
  'NewSession': function () {
    //shortcut to stateless Launch request
    this.handler.state = Core.states.INITIAL_STATE;
    this.emit("LaunchRequest" + Core.states.INITIAL_STATE);
  },
  /** Any intents not handled above go here */
  'SessionEndedRequest': function() {
    this.handler.state = Core.states.INITIAL_STATE;
    this.emit("SessionEndedRequest" + Core.states.INITIAL_STATE);
  }
};

var InitialStateHandlers = Alexa.CreateStateHandler(Core.states.INITIAL_STATE, {
  /** User can start off by immediately asking for a recipe */
  'StartNewRecipeIntent': function () {
    this.emit("StartNewRecipeIntent" + Core.states.NEW_RECIPE);
  },
  /** The user says something like "Open my cookbook" */
  'LaunchRequest': function () {
    let ftu = Core.firstTimeIntroductionIfNeeded(this);
    if (!ftu) {
      if (this.event.session.new) {
        this.attributes.invocations += 1;
        this.handler.state = Core.states.NEW_RECIPE;
        this.emit(":ask", "Hi again. What do you want to make?");
        this.emit(':saveState', true);
        return true;
      }
      else {
        this.emit(":tell", "I've already been launched");
      }
    }
  },
  'SessionEndedRequest': function() {
    this.emit(":tell", "Goodbye!");
  },
  /** Any intents not handled above go here */
  'Unhandled': function() {
    console.log("unhandled no state");
    let ftu = Core.firstTimeIntroductionIfNeeded(this);
    if (!ftu) {
      if (this.event.session.new) {
        this.emit(":tell", "I'm not sure what you want. Try asking for help");
      }
      else {
        this.emit(":tell", "How did you manage to get here? I have no idea what you want.");
      }
    }
  }
});

/**
 * the function that alexa will call when envoking our skill.
 * The execute method essentially dispatches to on of our session handlers
 */
exports.handler = function(event, context) {
  var alexa = Alexa.LambdaHandler(event, context);

  alexa.registerHandlers(StatelessHandlers,
    InitialStateHandlers,
    AskMakeCookbookHandlers,
    AskSearchHandlers,
    AskTutorialHandlers,
    IngredientsOrInstructionsHandler,
    TellTutorialHandlers,
    PromptForStartHandlers,
    NewRecipeHandlers
    );
  alexa.dynamoDBTableName = 'my_cookbook_users';
  alexa.appId = APP_ID;
  alexa.execute();
};
