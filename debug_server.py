from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/", methods=["GET", "POST"])
async def log_request(request: Request):
    auth = request.headers.get("Authorization", "No Auth")
    body = await request.body()
    print(f"Request: {request.method} {request.url.path} '{auth}' {body.decode()}")
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9999)