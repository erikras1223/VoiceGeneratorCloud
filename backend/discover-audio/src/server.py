from typing import Union
from aiohttp import web, hdrs
import jwt
import logging
import json
from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount

routes = web.RouteTableDef()
debugger = True


@routes.get('/discover')
async def text_generator(request):
    logger = logging.getLogger(__name__)
    message = request.rel_url.query.get('input_text', '')
    
    account = MyPlexAccount('razmat2', 'two1243@seatHSense++','fwyz9qfAKY17y3tWzdba&')
    plex = account.resource('<SERVERNAME>').connect()

    # Get the Plex server
    plex = PlexServer(baseurl="http://localhost:32400", token="fwyz9qfAKY17y3tWzdba&")
    #request.match_info('input_text')
    
    return web.Response(text="helloword")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=8086)