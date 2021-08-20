# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# from typing import Any, Text, Dict, List

# from rasa.sdk.events import SlotSet
# from rasa.sdk import Action , Tracker
# from rasa.sdk.executor import CollectingDispatcher

# def findTrain(ent):
#     return f"found"

# class ActionLookForTrain(Action):

#     def name(self) -> Text:
#         return "action_look_for_train"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         ent = tracker.latest_message['entities'][0]
#         print(ent)

#         dispatcher.utter_message(text=findTrain(ent))

#         return [SlotSet("train-destination",ent["train-destination"]),
#                 SlotSet("train-departure",ent["train-departure"]),
#                 SlotSet("train-day",ent["train-day"]),
#                 SlotSet("train-bookpeople",ent["train-bookpeople"]),
#                 SlotSet("train-arriveby",ent["train-arriveby"]),
#                 SlotSet("train-leaveat",ent["train-leaveat"]),
#         ]

# class ActionBookTrain(Action):

#     def name(self) -> Text:
#         return "action_book_train"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         ent = tracker.latest_message['entities'][0]
#         print(ent)
        
#         dispatcher.utter_message(text=findTrain(ent))

#         return [SlotSet("train-destination",ent["train-destination"]),
#                 SlotSet("train-departure",ent["train-departure"]),
#                 SlotSet("train-day",ent["train-day"]),
#                 SlotSet("train-bookpeople",ent["train-bookpeople"]),
#                 SlotSet("train-arriveby",ent["train-arriveby"]),
#                 SlotSet("train-leaveat",ent["train-leaveat"]),
#         ]

# class ActionGetTrivia(Action):

#     def name(self) -> Text:
#         return "action_get_trivia"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         #Pega entidades de trivia, descomente caso essas entidades existam
#         ent = tracker.latest_message['entities'][0] 
        
#         #Pega a ultima mensagem como uma string, descomente caso o tratamento seja por meio de if(contain())'s
#         text = tracker.latest_message['text']

#         print(ent)
#         print(text)

#         dispatcher.utter_message(text=findTrain(ent))

#         return [SlotSet("train-destination",ent["train-destination"]),
#                 SlotSet("train-departure",ent["train-departure"]),
#                 SlotSet("train-day",ent["train-day"]),
#                 SlotSet("train-bookpeople",ent["train-bookpeople"]),
#                 SlotSet("train-arriveby",ent["train-arriveby"]),
#                 SlotSet("train-leaveat",ent["train-leaveat"]),
#         ]


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

