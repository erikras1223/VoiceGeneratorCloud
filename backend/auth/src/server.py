from typing import Union
from aiohttp import web, hdrs
import os
import logging
import json
import firebase_admin
from firebase_admin import auth, credentials, exceptions
import jwt


routes = web.RouteTableDef()
key_json_path = os.getenv('auth_key_path')
cred = credentials.Certificate("/app/service-account.json")
firebase_admin.initialize_app(cred)



@routes.get('/auth/verify')
async def verify_token(request):
    logger = logging.getLogger(__name__)
    try: 
        

        # Extract the JWT token from the Authorization header
        logger.debug("Look at me please?")
        auth_header = request.headers.get('authorization')
        token = auth_header[len('Bearer '):]
        print(f"about to verify token {token}")
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        print("Go ahead, its you budd ")
    except auth.ExpiredIdTokenError as et:
        try:

            
            logger.debug("Expired token exception")
           
            # decoded_token = jwt.decode("..-g",options={'verify_signature': False})  # Set verify to True if you want to verify the signature
            # # Extract the email claim from the decoded token
            # email = decoded_token.get('email')
            # logger.debug(f"Expired token using refresh token\n {str(email)}")
            # user = auth.get_user_by_email(email)
            # refresh_token = user.tokens.get('refresh_token')
            return status_unauthorized("Expired token exception")
        except(ValueError, auth.UserNotFoundError, exceptions.FirebaseError) as e:
            logger.debug(str(e))
            return status_forbidden(str(e))

    except Exception as e:
         logger.debug(str(e))
         return status_forbidden(str(e))
        

    response = status_ok(body=json.dumps([]).encode('utf-8'))
    response.headers['subject'] = uid
    
    
    return response





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


def status_forbidden(body=None) -> web.Response:
    """
    Returns HTTP response with status code 403 and optional body.

    :return: aiohttp.web.Response with a 403 status code.
    """
    return web.HTTPForbidden(body=body)

def status_unauthorized(body=None) -> web.Response:
    """
    Returns a newly created HTTP response object with status code 401 and optional body.

    :return: aiohttp.web.Response with a 401 status code.
    """
    return web.HTTPUnauthorized(body=body)
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