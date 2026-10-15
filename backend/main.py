from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from logic import (
    eq, stress, eq_tarhan, intelligence_types, cranial_nerves,
    leonhard_shmishek, gad7, phq9, stai, hads,
)

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI(title="Ruhshunos")


@app.middleware("http")
async def no_cache_static(request, call_next):
    """Statik fayllar (HTML/CSS/JS) brauzer tomonidan muddatsiz keshlanib
    qolmasligi uchun. Sayt tez-tez yangilanadi; muddatsiz kesh ba'zi
    foydalanuvchilarda eski sahifa ko'rinishiga olib kelgan edi (masalan,
    allaqachon ochiq bo'lgan sahifalarda yangi navigatsiya ko'rinmay
    qolgan holat). ETag asosida revalidatsiya hali ham ishlaydi — bu
    faqat brauzerning so'ramasdan eski nusxani ishlatishini oldini oladi.
    """
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, must-revalidate"
    return response


class AnswersRequest(BaseModel):
    answers: list[str]


class IntAnswersRequest(BaseModel):
    answers: list[int]


@app.get("/api/eq/questions")
def get_eq_questions():
    return eq.get_questions()


@app.post("/api/eq")
def post_eq(payload: IntAnswersRequest):
    try:
        return eq.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/stress/questions")
def get_stress_questions():
    return stress.get_questions()


@app.post("/api/stress")
def post_stress(payload: IntAnswersRequest):
    try:
        return stress.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/eq-tarhan/questions")
def get_eq_tarhan_questions():
    return eq_tarhan.get_questions()


@app.post("/api/eq-tarhan")
def post_eq_tarhan(payload: IntAnswersRequest):
    try:
        return eq_tarhan.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/intelligence-types/questions")
def get_intelligence_types_questions():
    return intelligence_types.get_questions()


@app.post("/api/intelligence-types")
def post_intelligence_types(payload: IntAnswersRequest):
    try:
        return intelligence_types.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/cranial-nerves/questions")
def get_cranial_nerves_questions():
    return cranial_nerves.get_questions()


@app.post("/api/cranial-nerves")
def post_cranial_nerves(payload: AnswersRequest):
    try:
        return cranial_nerves.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/leonhard-shmishek/questions")
def get_leonhard_shmishek_questions():
    return leonhard_shmishek.get_questions()


@app.post("/api/leonhard-shmishek")
def post_leonhard_shmishek(payload: IntAnswersRequest):
    try:
        return leonhard_shmishek.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/gad7/questions")
def get_gad7_questions():
    return gad7.get_questions()


@app.post("/api/gad7")
def post_gad7(payload: IntAnswersRequest):
    try:
        return gad7.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/phq9/questions")
def get_phq9_questions():
    return phq9.get_questions()


@app.post("/api/phq9")
def post_phq9(payload: IntAnswersRequest):
    try:
        return phq9.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/stai/questions")
def get_stai_questions():
    return stai.get_questions()


@app.post("/api/stai")
def post_stai(payload: IntAnswersRequest):
    try:
        return stai.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/hads/questions")
def get_hads_questions():
    return hads.get_questions()


@app.post("/api/hads")
def post_hads(payload: IntAnswersRequest):
    try:
        return hads.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
