"""
FastAPI application entrypoint.

Provides REST endpoints and dashboard rendering
for real-time system telemetry visualization.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.metrics import collect_metrics
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)
# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request) -> HTMLResponse:
    """
    Render telemetry dashboard.

    Args:
        request: Incoming request object.

    Returns:
        Rendered dashboard template.
    """
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "refresh_interval": settings.refresh_interval_seconds,
        },
    )

@app.get("/metrics")
async def metrics() -> dict:
    """
    Return real-time telemetry metrics.

    Returns:
        JSON dictionary of system telemetry metrics.
    """
    return collect_metrics()


@app.get("/health")
async def health_check() -> dict:
    """
    Health-check endpoint for container orchestration readiness.

    Returns:
        Health status payload.
    """
    return {"status": "healthy"}