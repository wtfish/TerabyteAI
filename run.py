from App import create_app

app = create_app()
# print(app.config)
# print("bisa")
if __name__ == '__main__':
    app.run(debug=True)