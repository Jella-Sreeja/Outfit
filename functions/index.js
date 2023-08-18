const functions = require("firebase-functions");
/**
 * Handles the user's request based on the occasion parameter.
 * @param {WebhookClient} agent - The agent instance from dialogflow-fulfillment library.
 */
function occasionHandler(agent) {
  const occasion = agent.parameters['Occasion'];

  if (occasion === 'party') {
    agent.add('Got it! A party outfit it is. What color preferences do you have?');
  } else {
    // Handle other occasions
  }
}

  // Map your intent handlers
  const intentMap = new Map();
  intentMap.set("Occasion Intent", occasionHandler);
  // Add other intent handlers here
  agent.handleRequest(intentMap);
});
