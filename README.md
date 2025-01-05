# BMP-Helper


Here’s an updated version of your README description, incorporating images and examples for better clarity:

---

### Resizing and Recoloring Rug Designs

This project addresses the challenges of resizing and recoloring rug designs while preserving their visual integrity. Rug designs, originally created in high-resolution BMP format, require resizing to fit various manufacturing specifications. However, resizing often introduces geometric distortions and loss of design details, which impacts production quality.

#### Key Features:
1. **100% Design Integrity**: Maintains structural and color fidelity using advanced image processing techniques such as K-means clustering for color reduction and KDTree/KNN for precise pixel mapping.
2. **Dynamic Resizing**: Supports multi-size scaling with floating-point ratios, ensuring accurate adjustments for various manufacturing needs.
3. **Frame Processing**: A PyQt5-based GUI facilitates user input for resizing, merging, and dynamic white-space detection.
4. **Customizable Outputs**: Allows for scalable designs with editable dimensions and seamless integration with manufacturing pipelines.

---

### Example Workflow

1. **Original Design**  
   *Image of the original high-resolution rug design (e.g., 1680x799 BMP).*

2. **Resized Design (e.g., 1320x639)**  
   *Side-by-side comparison showing the resized design with retained quality.*

3. **Recolored Design**  
   *A close-up showing pixelated areas recolored to match the original palette using KNN.*

---

### Visual Examples

- **Original Design**  
  ![Original Design](path/to/resized_image.png)

- **Resized Design**  
  ![Resized Design](path/to/resized_image.png)

- **Recolored Close-Up**  
  ![Recolored Close-Up](path/to/recolored_closeup.png)

---

This approach ensures a perfect match between resized outputs and original designs, enhancing precision and efficiency in rug manufacturing.
