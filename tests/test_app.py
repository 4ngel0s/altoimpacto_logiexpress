from datetime import date

from app import Ocorrencia, Entrega, app, db

def test_health():
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json["status"] == "ok"

def test_dashboard():
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"LOGIEXPRESS" in response.data


def test_ocorrencia_crud_and_encerramento():
    app.config["TESTING"] = True
    with app.app_context():
        entrega = Entrega.query.first()
        assert entrega is not None
        client = app.test_client()

        response = client.post(
            "/ocorrencias/novo",
            data={
                "entrega_id": str(entrega.id),
                "tipo": "AVARIA",
                "descricao": "Embalagem danificada",
                "data": date.today().isoformat(),
                "status": "ABERTA",
            },
            follow_redirects=False,
        )
        assert response.status_code == 302
        ocorrencia = Ocorrencia.query.order_by(Ocorrencia.id.desc()).first()
        assert ocorrencia.status == "ABERTA"

        response = client.get(f"/ocorrencias/{ocorrencia.id}")
        assert response.status_code == 200
        assert b"Embalagem danificada" in response.data

        response = client.post(
            f"/ocorrencias/{ocorrencia.id}/editar",
            data={
                "entrega_id": str(entrega.id),
                "tipo": "ATRASO",
                "descricao": "Entrega atrasada",
                "data": date.today().isoformat(),
                "status": "ABERTA",
            },
            follow_redirects=False,
        )
        assert response.status_code == 302
        db.session.refresh(ocorrencia)
        assert ocorrencia.tipo == "ATRASO"

        response = client.post(
            f"/ocorrencias/{ocorrencia.id}/encerrar",
            follow_redirects=False,
        )
        assert response.status_code == 302
        db.session.refresh(ocorrencia)
        assert ocorrencia.status == "ENCERRADA"

        db.session.delete(ocorrencia)
        db.session.commit()
