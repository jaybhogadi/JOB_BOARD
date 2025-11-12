import uvicorn

print("in run.py")
if __name__ == "__main__":
    uvicorn.run("job_board.main:app", host = "127.0.0.1", port = 8000, reload=True)
