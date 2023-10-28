import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
counter = os.getenv("COUNTER", 0)


@app.get("/")
def read_root():
    return JSONResponse({"Hello": "World"})


@app.get("/count")
def main():
    global counter
    counter = int(counter)
    counter += 1
    return JSONResponse(
        {
            "status": 200,
            "response": "I have been seen {} times.".format(
                str(counter),
            ),
        },
    )


@app.get("/color")
def get_color():
    color = os.getenv("COLOR", "DEFUALT")
    return JSONResponse(
        {
            "status": 200,
            "response": "My Color is {}.".format(
                str(color),
            ),
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=2010,
        reload=False,
    )
