#!/usr/bin/env python3
import connexion
from connexion import RestyResolver
from adapters import sql_interface

app = connexion.App(__name__)
app.add_api('swagger.yaml', resolver=RestyResolver('api'))
application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='gevent')
