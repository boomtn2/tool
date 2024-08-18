import os
from skimage import io
import numpy as np
from scipy.spatial import distance
import time
from multiprocessing import Pool, cpu_count

def remove_similar_colors(args):
    img_path, target_colors, tolerance = args
    img = io.imread(img_path)
    
    # Calculate Euclidean distances between all pixels and target colors
    color_distances = np.linalg.norm(img[:, :, np.newaxis, :] - np.array(target_colors)[np.newaxis, np.newaxis, :, :], axis=-1)
    
    # Find minimum distances and mask pixels within tolerance
    min_distances = np.min(color_distances, axis=-1)
    mask = min_distances <= tolerance
    
    # Replace masked pixels with white color
    img[mask] = [255, 255, 255]
    
    return img

input_folder = './input'
output_folder = './output'
target_colors = [
    [251, 206, 187],  # Color FBCEBB
    [255, 255, 246],  # Color FFFFF6
]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def process_image(filename):
    img_path = os.path.join(input_folder, filename)
    output_filename = os.path.splitext(filename)[0] + '_ok.jpg'
    output_path = os.path.join(output_folder, output_filename)

    args = (img_path, target_colors, 50)  # Adjust tolerance if needed
    
    start_time = time.time()
    processed_img = remove_similar_colors(args)
    io.imsave(output_path, processed_img)
    end_time = time.time()
    
    print(f"Image {filename} completed. Time: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    start = time.time()
    
    filenames = [filename for filename in os.listdir(input_folder) if filename.endswith('.jpeg')]
    num_processes = min(cpu_count(), 8)  # Use up to 8 processes

    with Pool(num_processes) as pool:
        pool.map(process_image, filenames)

    end = time.time()
    print("Total processing time:", end - start, "seconds")
    print("Processing complete.")
