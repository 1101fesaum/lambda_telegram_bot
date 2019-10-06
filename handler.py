import json
import os
import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
ADMIN_CHAT_ID = os.environ['BOT_ID']
URL = f"https://api.telegram.org/bot{TOKEN}/"


def send_message(text, chat_id):
    """ Send back the same message the bot received and its chat id"""
    bot_response = f"I received: {text} from: {chat_id}" 
    url = URL + f"sendMessage?text={bot_response}&chat_id={chat_id}"
    requests.get(url)


def lambda_handler(event, context):
    """ Receive a telegram bot message or a message from other sources
    To receive from other sources the message most contain a json object with
    a 'form_msg' key with the content of the message and it will send 
    this information to the bot admin (admin_chat_id)"""

    try:
        if isinstance(event['body'], str):
            message = json.loads(event['body'])
        else:
            message = event['body']

        if message.get('message', False):
          chat_id = message['message']['chat']['id']
          reply = message['message']['text']
          send_message(reply, chat_id)
        elif message.get('form_msg', False):
          reply = message['form_msg']['info']
          send_message(reply, ADMIN_CHAT_ID)
        else:
          return {
            'statusCode': 403
          }
        return {
            'statusCode': 200
        }
    except KeyError:
        return {
            'statusCode': 400
          }
    except Exception:
        return {
            'statusCode': 500
          }
