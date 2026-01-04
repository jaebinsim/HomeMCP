# src/home_mcp_core/app.py
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import control, panel, status, health


def create_app() -> FastAPI:
    app = FastAPI(
        title="HomeMCP Core",
        version="0.1.0",
    )

    # Static (Admin Panel assets)
    base_dir = Path(__file__).resolve().parents[2]  # .../home-mcp-core
    static_dir = base_dir / "web" / "static"
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    # Routers
    # status / health / panel routers define their own prefixes internally.
    app.include_router(status.router)
    app.include_router(health.router)
    app.include_router(panel.router)

    # control router is mounted under /tuya
    app.include_router(control.router, prefix="/tuya", tags=["tuya"])

    return app


app = create_app()