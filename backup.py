import  requests
import  json
import  os
import  photocrawler
import  cryto_api

HEADER = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + '9zHtf5bVu3mjF9Kg1tvlNcL1yJwF8cCQqc6MH4MHK/q5KU/zuaO8s88k3vdBzbrVWCExxL7z3dcwiOhU4r83jNyOuXFT0NuxI+iNB3eyZieNzIPxnRXBuM6eRfpIn55d1J2BxYfa2BJFNX2J2ILdxQdB04t89/1O/w1cDnyilFU='
}

def lambda_handler(event, context):

    body = json.loads(event['body'])

    for event in body['events']:

        payload = {
            'replyToken': event['replyToken'],
            'messages': []
        }
        if event['message']['type'] == 'text':
            if len(event['message']['text'])==1 and event['message']['text'][0].lower()=='j':
                
                jphotolink = photocrawler.return_url()

                payload['messages'].append({
                'type': 'image',
                'originalContentUrl': jphotolink,
                'previewImageUrl': jphotolink
                })
            else:
                input_message = event['message']['text']
                result = cryto_api.coin_price(event['message']['text'])
                if result != False:
                    try:
                        price_message = "The price of {} is BTC {}/ USD {}/ HKD {}".format(input_message,result['BTC'],result['USD'],result['HKD'])
                    except:
                        price_message = "{} is still in pre ICO stage".format(input_message)
                    
                else:
                    
                    price_message = "Sorry your entry is invalid!"
                    

                payload['messages'].append({
                'type': 'text',
                'text': price_message
                })
        elif event['message']['type'] == 'sticker':
            payload['messages'].append({
                'type': 'sticker',
                'stickerId': event['message']['stickerId'],
                'packageId': event['message']['packageId']
            })

        if len(payload['messages']) > 0:
            response = requests.post('https://api.line.me/v2/bot/message/reply',
                headers=HEADER,
                data=json.dumps(payload))

def kickspace():
    if c[0]=='':
        c.pop(0)
        kickspace()
        