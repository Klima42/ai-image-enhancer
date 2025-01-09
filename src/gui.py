# src/gui.py
import tkinter as tk
from tkinter import filedialog, ttk
from pathlib import Path
from enhancer import ImageEnhancer

class ImageEnhancerGUI:
    def __init__(self, root):
        """Initialize the GUI for the Image Enhancer."""
        self.root = root
        self.root.title("AI Image Enhancer")
        self.enhancer = ImageEnhancer()
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface elements."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Buttons
        ttk.Button(main_frame, text="Load Image", command=self.load_image).grid(
            row=0, column=0, pady=5)
        
        ttk.Button(main_frame, text="Enhance", command=self.enhance_image).grid(
            row=1, column=0, pady=5)
        
        # Filter selection
        ttk.Label(main_frame, text="Filter:").grid(row=2, column=0, pady=5)
        self.filter_var = tk.StringVar(value='none')
        filter_menu = ttk.OptionMenu(main_frame, self.filter_var, 'none',
                                   'none', 'smoothing', 'noise_reduction', 'sharpen')
        filter_menu.grid(row=3, column=0, pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, length=200, mode='determinate')
        self.progress.grid(row=4, column=0, pady=5)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(main_frame, textvariable=self.status_var).grid(
            row=5, column=0, pady=5)

    def load_image(self):
        """Load an image file through file dialog."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
        
        if file_path:
            self.current_image_path = file_path
            self.status_var.set(f"Loaded: {Path(file_path).name}")

    def enhance_image(self):
        """Enhance the loaded image and apply selected filter."""
        if not hasattr(self, 'current_image_path'):
            self.status_var.set("Please load an image first")
            return
            
        self.status_var.set("Enhancing image...")
        self.progress['value'] = 0
        self.root.update_idletasks()
        
        # Enhance image
        enhanced_img = self.enhancer.enhance_image(self.current_image_path)
        self.progress['value'] = 50
        self.root.update_idletasks()
        
        # Apply filter if selected
        if self.filter_var.get() != 'none':
            enhanced_img = self.enhancer.apply_filter(
                enhanced_img, self.filter_var.get())
        
        self.progress['value'] = 100
        
        # Save enhanced image
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        
        if save_path:
            enhanced_img.save(save_path)
            self.status_var.set(f"Saved enhanced image to: {Path(save_path).name}")
        else:
            self.status_var.set("Enhancement cancelled")