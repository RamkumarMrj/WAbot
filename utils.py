import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "jokes-vsdt-bb75c4a45345.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "jokes-vsdt"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply():
    response = detect_intent_from_text("say joke", 12314)
    return response.fulfillment_text

response.intent.display_name
response.intent_detection_confidence