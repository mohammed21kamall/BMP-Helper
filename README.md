# BMP-Helper


### Resizing and Recoloring Rug Designs

This project addresses the challenges of resizing and recoloring rug designs while maintaining their visual integrity. Rug designs, originally created in high-resolution BMP format, require resizing to fit various manufacturing specifications. The resizing process often leads to geometric distortions and a loss of design details, affecting production quality. 

The primary goal is to ensure that resized designs maintain 100% similarity to the original, preserving color accuracy and structural details. This involves using advanced image processing techniques such as K-means clustering for color analysis and KDTree or KNN algorithms for intelligent pixel mapping. These methods minimize color blending, ensuring that each pixel is recolored to match the nearest original shade.

The solution also integrates a GUI built with PyQt5 to allow dynamic user input for resizing parameters, frame processing, and design merging. The project supports multi-size scaling, automated white-space detection, and dynamic frame handling, ensuring that each step in the design process seamlessly aligns with manufacturing requirements.

By employing these techniques, the project bridges the gap between software tools like NedGraphics and the precision demanded by modern rug manufacturing, ensuring high-quality designs across diverse sizes and patterns.
