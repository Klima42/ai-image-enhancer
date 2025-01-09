# AI Image Enhancer

An AI-powered desktop application that enhances image quality using deep learning techniques. The tool uses a convolutional neural network (CNN) to improve image resolution and provides additional filters for further enhancement.

## 🌟 Features

- **Super Resolution**: Enhance image quality using deep learning
- **Multiple Filters**: 
  - Smoothing
  - Noise reduction
  - Sharpening
- **User-friendly GUI**: Simple and intuitive interface
- **Format Support**: Works with common image formats (JPG, PNG, BMP, etc.)
- **Real-time Progress**: Visual feedback during enhancement process

## 🛠️ Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 📦 Installation

1. Clone the repository:
```bash
git clone git@github.com:yourusername/ai-image-enhancer.git
cd ai-image-enhancer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the application:
```bash
python src/main.py
```

2. Using the GUI:
   - Click "Load Image" to select your input image
   - Choose an enhancement filter (optional)
   - Click "Enhance" to process the image
   - Select a location to save the enhanced image

## 📁 Project Structure

```
ai-image-enhancer/
├── src/
│   ├── main.py          # Application entry point
│   ├── enhancer.py      # Core enhancement logic
│   ├── gui.py           # GUI implementation
│   └── utils.py         # Utility functions
├── models/
│   └── saved_models/    # Trained model storage
├── data/
│   ├── input/           # Input images
│   └── output/          # Enhanced images
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Technical Details

### Neural Network Architecture
- Input Layer: Accepts RGB images of any size
- Feature Extraction: Conv2D layer (64 filters, 9x9 kernel)
- Non-linear Mapping: Conv2D layer (32 filters, 1x1 kernel)
- Reconstruction: Conv2D layer (3 filters, 5x5 kernel)

### Supported Image Formats
- JPEG/JPG
- PNG
- BMP
- GIF
- TIFF

## ⚙️ Configuration

Default settings are suitable for most use cases. Advanced users can modify:
- Model architecture in `enhancer.py`
- Filter parameters in `enhancer.py`
- GUI layout in `gui.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- TensorFlow team for the deep learning framework
- OpenCV community for image processing capabilities
- Python Tkinter for GUI components

## 📫 Contact

- Your Name - email@example.com
- Project Link: [https://github.com/yourusername/ai-image-enhancer](https://github.com/yourusername/ai-image-enhancer)

## 🐛 Known Issues

- Processing very large images may require significant memory
- Some filters may take longer on high-resolution images

## 🔜 Planned Features

- Batch processing capability
- Additional enhancement filters
- Custom model training options
- Preview window for real-time filter viewing
