# simple falcon application that returns an HTTPBadRequest response if there's no data provided in the request body
import falcon
import json

class Resource(object):
    def on_post(self, req, resp):
        if req.content_length:
            resp.body = json.dumps({'success': True})
        else:
            raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required.')
        
app = falcon.API()
app.add_route('/', Resource())


