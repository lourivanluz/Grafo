from http import HTTPStatus

from flask import jsonify, request

def search_router (graphId,town1,town2):
    args = request.args.get('maxStops')
    print(args)
    response = {"graphid":graphId,'townOrigin':town1,'townDestini':town2,'max':args}

    return jsonify(response),HTTPStatus.OK