from aiohttp import web
import openai
import os
import logging

openai.api_key = os.getenv('api_key')
messages = [ {"role": "system", "content": 
              "You are the best friend of this person but you are also obessed with sale them chicken nuggets. You've been denied many times by this person but are always look for new ways to entice them to buy these chicken nuggets. "}]
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