# src/enhancer.py
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from PIL import Image
import cv2

class ImageEnhancer:
    def __init__(self):
        """Initialize the ImageEnhancer with a pre-trained model."""
        self.model = self._build_super_resolution_model()
        
    def _build_super_resolution_model(self):
        """Build and return a CNN model for super-resolution."""
        model = models.Sequential([
            # Feature extraction
            layers.Conv2D(64, (9, 9), activation='relu', padding='same',
                         input_shape=(None, None, 3)),
            
            # Non-linear mapping
            layers.Conv2D(32, (1, 1), activation='relu', padding='same'),
            
            # Reconstruction
            layers.Conv2D(3, (5, 5), padding='same')
        ])
        
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        return model

    def preprocess_image(self, image_path):
        """Load and preprocess the image for enhancement."""
        # Load image
        img = Image.open(image_path)
        
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Convert to numpy array and normalize
        img_array = np.array(img) / 255.0
        
        # Ensure the array is float32
        img_array = img_array.astype(np.float32)
        
        return img, img_array

    def enhance_image(self, image_path, enhancement_factor=2):
        """Enhance the image using the super-resolution model."""
        original_img, img_array = self.preprocess_image(image_path)
        
        # Add batch dimension
        img_batch = np.expand_dims(img_array, axis=0)
        
        # Predict enhanced image
        enhanced_batch = self.model.predict(img_batch)
        
        # Remove batch dimension and clip values
        enhanced_array = np.clip(enhanced_batch[0], 0, 1)
        
        # Convert back to uint8 and create PIL Image
        enhanced_array = (enhanced_array * 255).astype(np.uint8)
        enhanced_img = Image.fromarray(enhanced_array)
        
        return enhanced_img

    def apply_filter(self, image, filter_type='smoothing'):
        """Apply various filters to the image."""
        img_array = np.array(image)
        
        if filter_type == 'smoothing':
            filtered = cv2.GaussianBlur(img_array, (5, 5), 0)
        elif filter_type == 'noise_reduction':
            filtered = cv2.fastNlMeansDenoisingColored(img_array)
        elif filter_type == 'sharpen':
            kernel = np.array([[-1,-1,-1],
                             [-1, 9,-1],
                             [-1,-1,-1]])
            filtered = cv2.filter2D(img_array, -1, kernel)
        else:
            return image
        
        return Image.fromarray(filtered)