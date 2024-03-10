from typing import Union
from aiohttp import web, hdrs
import os
import logging
import json
import firebase_admin
from firebase_admin import auth, credentials


routes = web.RouteTableDef()
key_json_path = os.getenv('auth_key_path')
cred = credentials.Certificate("/app/service-account.json")
firebase_admin.initialize_app(cred)



@routes.get('/auth/verify')
async def verify_token(request):
    logger = logging.getLogger(__name__)
    try:    
        logger.debug("Look at me please?")
        print("about to verify token ")
        decoded_token = auth.verify_id_token("eyJhbGciOiJSUzI1NiIsImtpZCI6IjNiYjg3ZGNhM2JjYjY5ZDcyYjZjYmExYjU5YjMzY2M1MjI5N2NhOGQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaG9qcG9qLTI0YjMwIiwiYXVkIjoiaG9qcG9qLTI0YjMwIiwiYXV0aF90aW1lIjoxNzA5ODgxNTI5LCJ1c2VyX2lkIjoiUmwxWEhWRFBBd09WQ3FISjNGVTBCbTk4SVo0MyIsInN1YiI6IlJsMVhIVkRQQXdPVkNxSEozRlUwQm05OElaNDMiLCJpYXQiOjE3MDk4ODE1MzAsImV4cCI6MTcwOTg4NTEzMCwiZW1haWwiOiJlcmlrcmFzMTIyM0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZXJpa3JhczEyMjNAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.UkAhY9P0HINFdLSWzjHTCUtsvg8OpfUyobJTPT8kOwj4BVs3Z4YBDOBJDKI1pBCwvrvd0KeLdtJNOmtJfvFIH3GbZwp1Fz2rHbUf5t-YMwJtEMcQtmCfza3pSC-r53JGIRL8IXWhhkZ6-whYzFRwZ2bBuffwQ6eOJBKU3oTA7wRhZ0pmCTXiGoHW9iNlXaNpemfotdxlTXmNxVXxsmSOc9rar9cAdonCqs-L2C1sWvbOe-kQQQNunn5lxsmPJN6fhsXhq8g9f5tg1hXi-89VlKICExjE1cR8gjlsNMYDhyaKJpgca9QLgibtZnTLmNgaHU5l9iaBBKo18G1lj29xPg")
        uid = decoded_token['uid']
        print("Go ahead, its you budd ")
        logger.debug(decoded_token)
    except Exception as e:
        print("invalid ")
        logger.debug("Invalid")
        return status_unauthorized("Invalid token, deny")

    
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

    return status_ok(body=json.dumps([]).encode('utf-8'))





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


def status_unauthorized(body=None) -> web.Response:
    """
    Returns a newly created HTTP response object with status code 201.

    :return: aiohttp.web.Response with a 201 status code and the Location header set to the URL of the created object.
    """
    return web.HTTPForbidden(body=body)

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

def main():
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=8085)

if __name__ == "__main__":
    main()