# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from pprint import pprint
import json,random,re,requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from pymessenger.bot import Bot
from chintent import check_intent


PAGE_ACCESS_TOKEN = "EAABlZCeiOMsYBAAUbpBIuE0BPsyP4vmnNqb9IOOa7VZBC6zvaZAcb1eP0a44ZAs4lauQNPyxEasUItY76cVZB6ZC5NtpXkpGVtlj98AAD58ENu0ZCGiSuzsWupywYJhtqrqAEZCmlkwY2X3ZAwTnAjzE4TSvb8h52mWb8aZCxvjmenwAZDZD"
VERIFY_TOKEN = "01081996"

 
def post_getstart():
    pprint("heytuthuuuuuuuuuuuuuuuuuuu")
    

def post_facebook_message(fbid, text):
    
    string=text
    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
                            
    
    response_msg = json.dumps(
                    {
                        "recipient":
                            {
                                "id":fbid
                           }, 
                        "message":
                            {
                                "text":string,
                                "quick_replies":[
                                 {
                                
                                "title":"Emergency",
                               
                               "content_type":"text",
                               "payload":"Emergency_Payload"
                               

                               }
                                ,
                            {
                                  "content_type":"text",
                                  "title":"Disease",
                                  "payload":"Disease_Payload"
                                  },
                                

                         ]
                            }
                            })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

def send_disease_message(fbid):
    dtype="Select the type of disease"
    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
                            
    
    response_msg = json.dumps(
                    {
                        "recipient":
                            {
                                "id":fbid
                            }, 
                        "message":
                            {
                                "text":dtype,
                                "quick_replies":[
                                 {
                                
                                "title":"Multiple Sclerosis",
                               
                               "content_type":"text",
                               "payload":"d1_Payload"
                               

                               }
                                ,
                                 {
                                
                                "title":"Lupus",
                               
                               "content_type":"text",
                               "payload":"d2_Payload"
                               

                               }
                            ,
                                 {
                                
                                "title":"Heart",
                               
                               "content_type":"text",
                               "payload":"d3_Payload"
                               

                               }
                            ,
                                 {
                                
                                "title":"Cancer",
                               
                               "content_type":"text",
                               "payload":"d4_Payload"
                               

                               }
                            ,
                                 {
                                
                                "title":"Liver",
                               
                               "content_type":"text",
                               "payload":"d5_Payload"
                               

                               }
                            ,
                                 {
                                
                                "title":"Infectious",
                               
                               "content_type":"text",
                               "payload":"d6_Payload"
                               

                               },
                                 {
                                
                                "title":"Other",
                               
                               "content_type":"text",
                               "payload":"d7_Payload"
                               

                               }]
                            }
                            })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    
    
    
    # print(status.json())
    
def post_facebook_location(fbid,rlat,rlong):

    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    print(fbid)               
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())
def send_location(fbid):
    string="please share your location";
    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
                    
    response_msg = json.dumps(
                    {
                        "recipient":
                            {
                                "id":fbid
                            }, 
                        "message":
                            {
                                "text":string,
                                "quick_replies":[
                                 {
                                
                                
                               
                               "content_type":"location",
                               }
                                ,]
                            }
                            })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    
def post_emer_loc(fbid):
    
    string="please send your location"
    
    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
                    
    

    
    response_msg = json.dumps(
                    {
                        "recipient":
                            {
                                "id":fbid
                            }, 
                        "message":
                            {
                                "text":string,
                                "quick_replies":[
                                 {
                                
                                
                               
                               "content_type":"location",
                               }
                                ,]
                            }
                            })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    
def send_button_message(recipient_id):
        
    user_details_url = "https://graph.facebook.com/v2.10/%s"%recipient_id 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    text="alzeihmer"
    response_msg=json.dumps({
            'recipient': {
                'id': recipient_id
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements":[
           {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          },
          {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          },
          {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          },
          {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          },
          {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          }

        ]
        }
        }
        }
        })

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
# Create your views here.
class HEBot104View(generic.View):
    def get(self, request, *args, **kwargs):
        post_message_url ='https://graph.facebook.com/v2.10/me/messenger_profile?fields=get_started&access_token=%s'%PAGE_ACCESS_TOKEN    
        
        status = requests.get(post_message_url, headers={"Content-Type": "application/json"})

        
        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if self.request.GET.get('hub.verify_token') == VERIFY_TOKEN:             
            
            return HttpResponse(self.request.GET['hub.challenge'])   
        else:    
            return HttpResponse('Error, invalid token')        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        post_message_url ='https://graph.facebook.com/v2.10/me/messenger_profile?access_token=%s'%PAGE_ACCESS_TOKEN    
        response_msg=json.dumps({ 
    "get_started":{
    "payload":"GET_STARTED_PAYLOAD"
    }
    })
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)
                    
                    if 'quick_reply' in message['message']:

                        pload=str(message['message']['quick_reply']['payload'])
                        if pload=="Emergency_Payload":
                            post_emer_loc(message['sender']['id'])
                        else:
                            send_disease_message(message['sender']['id'])

                            
                    if 'attachments' in message['message']:
                        ar=message['message']['attachments']
                        for j in ar:
                            content_type = j['type']
                            if content_type == 'location':
                                message_coordinates = (j['payload']['coordinates'])
                                latitude = message_coordinates['lat']
                                longitude = message_coordinates['long']
                                print(latitude,longitude)
                                post_facebook_location(message['sender']['id'], str (latitude), str( longitude))    
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly. 
                    # post_facebook_message(message['sender']['id'], message['message']['text'])    
                    else:
                        help_command = (message['message']['text'])
                        if help_command == "Get started":
                            print "$$$$$$$$$$$$$$$$$$$"
                            text = check_intent(help_command)
                            print text
                            post_facebook_message(message['sender']['id'],text)
                            
                        
                        
                        else :
                            pass    
        return HttpResponse() 


