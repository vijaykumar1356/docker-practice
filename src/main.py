from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    import ipdb; ipdb.set_trace()
    return {'message': 'hello world!'}