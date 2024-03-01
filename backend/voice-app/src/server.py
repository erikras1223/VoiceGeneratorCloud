from typing import Union
from aiohttp import web, hdrs
import openai
import os
import logging
import json

openai.api_key = os.getenv('api_key')
messages = [ {"role": "system", "content": "You are taking to my wife Eryn on behalf of me. So please use my name Erik when you are address. Its our aniversary today, we've been married 52 years so please congrate. Teach her the history of marriage ritual and they evolved over time. "}]
defined_roles = ['system','assistant','user']
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
        return web.Response(text="what you said hurts my head, ouchy")
    msg = '\n'.join(map(lambda x: f"role: {x['role']} \n content: {x['content']}", messages))
    logger.error(msg)

    return web.Response(text=reply)


@routes.post('/voice/context')
async def update_context(request):
    logger = logging.getLogger(__name__)
    data = await request.json()
    role = data.get('role') if data.get('role') in defined_roles else 'system'
    action = data.get('action') if data.get('action') else 'replace'
    temp_messages = [msg for msg in messages]
    messages.clear()
    message = data.get('input_text')
    if not message:
        return status_bad_request(body="No message was provided")

    if action == "add":
        messages.append({"role": role, "content": message})
    else: 
        
        if role == 'system':
            for r_obj in temp_messages: 
                if not r_obj.get('role') == role:
                    messages.append(r_obj)
            
            messages.insert(0, {"role": role, "content": message})
        else:
            messages.append({"role": role, "content": message})

    return status_ok(body=json.dumps(messages).encode('utf-8'))


@routes.delete('/voice/context')
async def delete_context(request):
    messages.clear()
    return status_no_content()




def status_bad_request(body: bytes = None) -> web.Response:
    """
    Returns a newly created HTTP response object with status code 400 and an optional body.
    :param body: the body of the message, typically an explanation of why the request is bad.
    :return: aiohttp.web.Response with a 400 status code.
    """
    return web.HTTPBadRequest(body=body)


def status_created() -> web.Response:
    """
    Returns a newly created HTTP response object with status code 201.

    :return: aiohttp.web.Response with a 201 status code and the Location header set to the URL of the created object.
    """
    return web.HTTPCreated()


def status_ok(body: bytes, content_type: str = 'application/json') -> web.Response:
    """
    Returns a newly created HTTP response object with status code 201, the provided Content-Type header, and the
    provided body.
    :param body: the body of the response.
    :param content_type: the content type of the response (default is application/json).
    :return: aiohttp.web.Response object with a 200 status code.
    """
    if content_type is not None:
        return web.HTTPOk(headers={hdrs.CONTENT_TYPE: content_type}, body=body)
    else:
        return web.HTTPOk(body=body)


def status_no_content() -> web.Response:
    """
    Returns a newly created HTTP response object with status code 204.
    :return: aiohttp.web.Response object with a 204 status code.
    """
    return web.HTTPNoContent()



app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8084)