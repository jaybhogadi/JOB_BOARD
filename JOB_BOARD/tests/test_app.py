import pytest
from httpx import ASGITransport, AsyncClient
from src.job_board.main import app

@pytest.mark.asyncio
async def test_read_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport,base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello world"}