import pytest

def make_station(code="S1", name="Gare", capacity=10, status="open"):
    return {"code": code, "name": name, "capacity": capacity, "status": status}

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_then_read(client):
    created = client.post("/stations", json=make_station())
    assert created.status_code == 201
    station = created.json()
    response = client.get(f"/stations/{station['id']}")
    assert response.status_code == 200
    assert response.json() == station

def test_filter_status(client):
    client.post("/stations", json=make_station(code="A", status="open"))
    client.post("/stations", json=make_station(code="B", status="closed"))
    client.post("/stations", json=make_station(code="C", status="open"))
    response = client.get("/stations", params={"status": "open"})
    assert response.status_code == 200
    stations = response.json()
    assert len(stations) == 2
    assert all(s["status"] == "open" for s in stations)

def test_patch_name(client):
    station = client.post("/stations", json=make_station()).json()
    response = client.patch(f"/stations/{station['id']}", json={"name": "Nouveau nom"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["name"] == "Nouveau nom"
    assert updated["code"] == station["code"]
    assert updated["capacity"] == station["capacity"]
    assert updated["status"] == station["status"]

def test_get_unknown_id(client):
    response = client.get("/stations/999")
    assert response.status_code == 404
    assert "detail" in response.json()

@pytest.mark.parametrize(
    "bad_data",
    [
        make_station(capacity=0),
        make_station(status="flying"),
    ],
)
def test_invalid_input(client, bad_data):
    response = client.post("/stations", json=bad_data)
    assert response.status_code == 422
    assert client.get("/stations").json() == []

def test_duplicate_code(client):
    first = client.post("/stations", json=make_station(code="DUP"))
    second = client.post("/stations", json=make_station(code="DUP", name="Autre"))
    assert first.status_code == 201
    assert second.status_code == 409
    assert len(client.get("/stations").json()) == 1
