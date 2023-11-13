from application import create_app #importando a aplicação Flask que encontra-se dentro do package "website"
from application import models
from flask_pymongo import PyMongo
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #app.config["MONGO_URI"] = "mongodb+srv://root:root@cluster0.o64y1wi.mongodb.net/"
    #mongodb_cliente = PyMongo(app)
    #db = mongodb_cliente.db