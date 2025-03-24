def test_health_endpoint():
    """Test that the health endpoint returns a 200 status code."""
    from fastapi.testclient import TestClient
    from app.main import app
    
    client = TestClient(app)
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}