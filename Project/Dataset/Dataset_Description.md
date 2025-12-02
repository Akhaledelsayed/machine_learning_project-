### Dataset Description

**Name:** MILK10k (Multimodal Imaging-Learning Kit)
**Source:** Official ISIC Archive (International Skin Imaging Collaboration).
**Version:** Original Complete Bundle (Raw Data).

#### 1. Dataset Overview
This project utilizes the **MILK10k** dataset, acquired directly from the official ISIC Archive. We selected the original complete bundle to work with the **raw, 
unmodified data**, ensuring that no external down-sampling, cropping, or artificial resizing was applied prior to acquisition. 
This allows for a fully controlled and custom pre-processing pipeline.

#### 2. Visual Data (Images)
The visual component consists of **10,480 high-resolution images** representing 5,240 unique clinical cases.
* **Modality:** The dataset includes paired images for each case: a **Clinical** image (standard camera view) and a **Dermatoscopic** image (magnified view).
* **Resolution:** Images are provided in their native, variable resolutions.
* **Artifacts:** As raw clinical data, the images retain natural artifacts such as hair, gel bubbles, and ruler markers, 
which are handled within our processing pipeline.

#### 3. Clinical Metadata (Tabular Data)
To support the **Multi-modal** architecture of our project, the image data is complemented by a rich set of clinical attributes for each patient. 
Instead of relying solely on visual features, the dataset provides essential demographic and physiological context, including:
* **Patient Demographics:** Information regarding the patient's age and gender.
* **Anatomical Context:** Specific details about the location of the skin lesion on the body (e.g., head, neck, or extremities).
* **Linkage:** Unique identifiers that accurately map each clinical profile to its corresponding image pair.

