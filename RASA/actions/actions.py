# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import json
import random
import datetime as dt

from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action , Tracker
from rasa_sdk.executor import CollectingDispatcher


with open ('db.json', 'r') as read_file:
    trains_in_db = json.load(read_file)

entities = {}

def select_trains(train):
    train_leave_at = dt.datetime.strptime(train["leaveAt"], '%H:%M')
    train_arrive_by = dt.datetime.strptime(train["arriveBy"], '%H:%M')

    entity_leave_at = dt.datetime.strptime(entities['leaveat'], '%H:%M') 
    entity_arrive_by = dt.datetime.strptime(entities['arriveby'], '%H:%M')

    return train["departure"] == entities['departure'] and train["destination"] == entities['destination'] and train["day"] == entities['day'] and train_leave_at >= entity_leave_at and train_arrive_by <= entity_arrive_by

def get_trains(): 
    options = [x for x in filter(select_trains, trains_in_db)] 

    random.shuffle(options) 
    options = options[:min(5, len(options))] 

    # print(options)

    return options

class ActionFoundYourTrainWithHour(Action):

    def name(self) -> Text:
        return "action_found_your_train_with_hour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global entities
        entities = {}
        entities['departure'] = tracker.get_slot('train-departure').lower()
        entities['destination'] = tracker.get_slot('train-destination').lower()
        entities['day'] = tracker.get_slot('train-day').lower()
        entities['arriveby'] = tracker.get_slot('train-arriveby')
        entities['leaveat'] = tracker.get_slot('train-leaveat')
        

        train_results = get_trains()

        buttons = [{"title":'train code: ' + x["trainID"] + ' - ' + 'Arrive by: ' + x["arriveBy"] + ', Leave at: ' + x['leaveAt'], "payload": '/book_train{"trainID":"' + x["trainID"] + '"}'} for x in train_results] + [{"title": "Finished", "payload": "/finish_query"}]
        dispatcher.utter_message(text="here's what I found:", buttons=buttons)

        return []

class ActionResetAllSlots(Action):

    def name(self) -> Text:
        return "action_reset_all_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]



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
