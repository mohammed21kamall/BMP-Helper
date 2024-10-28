import numpy as np
from sklearn.cluster import KMeans


def upscale_image(sr, image):
    return sr.upsample(image)


# استخراج الألوان الأصلية باستخدام K-means
def extract_original_colors(image, n_colors):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(np.uint8)
    return colors

