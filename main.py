from application import create_app #importando a aplicação Flask que encontra-se dentro do package "website"

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)