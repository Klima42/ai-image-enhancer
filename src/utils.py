# src/utils.py
import os
from pathlib import Path

def ensure_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        'data/input',
        'data/output',
        'models/saved_models'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

def get_input_files():
    """Get list of input image files."""
    input_dir = Path('data/input')
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    return [f for f in input_dir.glob('*') if f.suffix.lower() in image_extensions]

def get_output_path(input_path, prefix='enhanced_'):
    """Generate output path for enhanced image."""
    output_dir = Path('data/output')
    return output_dir / f"{prefix}{input_path.name}"