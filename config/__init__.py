"""Configuration module for RP Binder"""

import yaml
import os
from pathlib import Path

CONFIG_DIR = Path(__file__).parent
DEFAULT_CONFIG = CONFIG_DIR / "default_config.yaml"

def load_config(config_path=None):
    """Load configuration from YAML file"""
    if config_path is None:
        config_path = DEFAULT_CONFIG
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        return load_default_config()

def load_default_config():
    """Load default configuration"""
    with open(DEFAULT_CONFIG, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_config(config, config_path):
    """Save configuration to YAML file"""
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False)