from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Cloud-Native Task Management Platform is running"
    )


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Docker",
            "completed": False
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Learn Docker"
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Kubernetes",
            "completed": False
        }
    )

    task_id = response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Learn Kubernetes"


def test_update_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Old Task",
            "completed": False
        }
    )

    task_id = response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Updated Task"
    assert data["completed"] is True


def test_delete_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Task To Delete",
            "completed": False
        }
    )

    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Task deleted"
    assert data["task"]["id"] == task_id


def test_task_not_found():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"