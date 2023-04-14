from aiohttp import web
import openai
import os
import logging

openai.api_key = os.getenv('api_key')
messages = [ {"role": "system", "content": 
              "You are the best friend of this person named Sam, he knew you James as butterfield but is a little confused these days, Sam knows know you are an AI Model so no need to tell him. If he asks you to something you can't do because of your an AI model just say no thank you or ignore him and change the topic. Sam, has amnesia and will act like he doesn't know you just answer his questions politey. His wife is Lindsey and has three kids Everly, Theo and Nora. He likes outdoors and always like camping in idaho. Hes an architech by trade. Lives in morgan utah. He is more reserved but very friendly and is originally from centerville"} ]
routes = web.RouteTableDef()

@routes.get('/voice/text-generate')
async def text_generator(request):
    logger = logging.getLogger(__name__)
    message = request.rel_url.query.get('input_text', '')
    #request.match_info('input_text')
    messages.append(
            {"role": "user", "content": message},
        )
    try:
        chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        return web.Response("what you said hurts my head, I might have a stroke")
    logging.error(f"Here is the message reply: {reply}")
    print(messages)

    return web.Response(text=reply)

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8084)