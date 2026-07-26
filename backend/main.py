from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from logic import zodiac, life_path, love_language, temperament, eq, stress

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI(title="Ruhshunos Fun")


class ZodiacRequest(BaseModel):
    birth_date: date
    gender: Optional[str] = None
    partner_birth_date: Optional[date] = None
    partner_gender: Optional[str] = None


class LifePathRequest(BaseModel):
    birth_date: date


class AnswersRequest(BaseModel):
    answers: list[str]


class IntAnswersRequest(BaseModel):
    answers: list[int]


@app.post("/api/zodiac")
def get_zodiac(payload: ZodiacRequest):
    sign = zodiac.get_sign(payload.birth_date)
    result = {
        "sign": {
            "key": sign.key,
            "name": sign.name,
            "emoji": sign.emoji,
            "element": sign.element,
            "element_emoji": sign.element_emoji,
            "modality": sign.modality,
            "date_range": sign.date_range,
            "description": sign.description,
        },
        "compatibility": None,
    }

    if payload.partner_birth_date is not None:
        partner_sign = zodiac.get_sign(payload.partner_birth_date)
        combo = zodiac.compatibility(
            sign, partner_sign, payload.gender, payload.partner_gender
        )
        result["compatibility"] = {
            "partner_sign": {
                "key": partner_sign.key,
                "name": partner_sign.name,
                "emoji": partner_sign.emoji,
                "element": partner_sign.element,
                "element_emoji": partner_sign.element_emoji,
                "modality": partner_sign.modality,
            },
            **combo,
        }

    return result


@app.post("/api/life-path")
def get_life_path(payload: LifePathRequest):
    if payload.birth_date > date.today():
        raise HTTPException(status_code=400, detail="Tug'ilgan sana kelajakda bo'lishi mumkin emas")
    return life_path.calculate_life_path(payload.birth_date)


@app.get("/api/love-language/questions")
def get_love_language_questions():
    return love_language.get_questions()


@app.post("/api/love-language")
def post_love_language(payload: AnswersRequest):
    try:
        return love_language.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/api/temperament/questions")
def get_temperament_questions():
    return temperament.get_questions()


@app.post("/api/temperament")
def post_temperament(payload: AnswersRequest):
    try:
        return temperament.calculate(payload.answers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


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


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
