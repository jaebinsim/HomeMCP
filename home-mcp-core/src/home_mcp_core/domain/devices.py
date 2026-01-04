# src/home_mcp_core/domain/devices.py
from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Optional, Dict

import tomllib
from pydantic import BaseModel, Field


class DeviceKind(str, Enum):
    LIGHT = "light"
    SWITCH = "switch"
    AIRCON = "aircon"
    PROJECTOR = "projector"
    WINDOWS_PC = "windows_pc"


class DeviceInfo(BaseModel):
    kind: DeviceKind
    tuya_device_id: Optional[str] = None

    tuya_on_device_id: Optional[str] = None
    tuya_off_device_id: Optional[str] = None

    location: Optional[str] = None
    supports_brightness: bool = False
    supports_temperature: bool = False


# ─────────────────────────────────────────────
# TOML 로딩
# ─────────────────────────────────────────────

_CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"
_DEVICES_FILE = _CONFIG_DIR / "devices.toml"

# Keys in DEVICE_REGISTRY are logical device names (e.g. "bed_light", "living_light")
# defined in config/devices.toml under the [devices.*] tables.
def _load_device_registry() -> Dict[str, DeviceInfo]:
    if not _DEVICES_FILE.exists():
        # For Debug
        raise FileNotFoundError(f"Device config not found: {_DEVICES_FILE}")

    data = tomllib.loads(_DEVICES_FILE.read_text(encoding="utf-8"))

    devices_raw = data.get("devices", {})
    registry: Dict[str, DeviceInfo] = {}

    for logical_name, cfg in devices_raw.items():
        registry[logical_name] = DeviceInfo.model_validate(cfg)

    return registry


DEVICE_REGISTRY: Dict[str, DeviceInfo] = _load_device_registry()