from typing import Union
from aiohttp import web, hdrs
import os
import logging
import json

routes = web.RouteTableDef()



@routes.post('/auth')
async def verify_token(request):
    logger = logging.getLogger(__name__)
    logger.debug("help me")
    print("help me")
    # data = await request.json()
    # role = data.get('role') if data.get('role') in defined_roles else 'system'
    # action = data.get('action') if data.get('action') else 'replace'
    # temp_messages = [msg for msg in messages]
    # messages.clear()
    # message = data.get('input_text')
    # if not message:
    #     return status_bad_request(body="No message was provided")

    # if action == "add":
    #     messages.append({"role": role, "content": message})
    # else: 
        
    #     if role == 'system':
    #         for r_obj in temp_messages: 
    #             if not r_obj.get('role') == role:
    #                 messages.append(r_obj)
            
    #         messages.insert(0, {"role": role, "content": message})
    #     else:
    #         messages.append({"role": role, "content": message})

    return status_ok(body=json.dumps(messages).encode('utf-8'))





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
web.run_app(app, port=8087)