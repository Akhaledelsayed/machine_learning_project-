# Multimodal Skin Lesion Classification System

This machine learning project aims to improve the early detection of skin cancer, particularly melanoma, by employing a multimodal approach that combines dermoscopic images with patient metadata for enhanced diagnostic accuracy.

## The Problem

Many automated skin cancer detection systems rely solely on dermoscopic images of skin lesions. This approach overlooks valuable patient-specific contextual information—such as age, gender, and lesion location—that dermatologists routinely use in clinical diagnosis. Consequently, image-only models may fail to account for important risk factors, potentially reducing diagnostic performance.

## The Solution

The project implements a **dual-stream multimodal system**:

1. **Visual stream**  
   Processes dermoscopic images to extract physical characteristics such as color variation, border irregularity, asymmetry, and texture.

2. **Context stream**  
   Incorporates patient metadata (tabular data) to evaluate clinical risk factors.

The primary objective is **binary classification**: determining whether a skin lesion is **benign** (non-cancerous) or **malignant** (cancerous).

## Dataset

- **Source**: International Skin Imaging Collaboration (ISIC) dataset
- **Size**: 10,480 samples
- **Features per sample**:
  - High-resolution dermoscopic RGB image
  - Tabular metadata (e.g., approximate age, sex, anatomical site, benign/malignant label)

**Preprocessing**:
- Missing values imputed
- Categorical features encoded
- Numerical features normalized
- Images resized to 128×128 pixels and pixel values scaled

## Models Developed

Several baseline models were trained and evaluated using either tabular data or image data independently.

### Tabular Data Models
| Model                          | Notes                                      | Best Accuracy |
|--------------------------------|--------------------------------------------|---------------|
| Logistic Regression            | Simple statistical baseline                | -             |
| Decision Tree                  | Interpretable rule-based model              | -             |
| Support Vector Machine (RBF)   | Best performing tabular model              | **~78.3%**    |

### Image Data Models
| Model                                      | Notes                                            | Best Accuracy |
|--------------------------------------------|--------------------------------------------------|---------------|
| Logistic Regression on flattened pixels    | Very poor performance                            | -             |
| SVM on raw pixels                          | Moderate performance                             | -             |
| Convolutional Neural Network (CNN)         | Multiple conv layers, max pooling, dropout; trained for 15 epochs with minimal overfitting | **~78.1%**    |

## Key Findings

- Tabular metadata models slightly outperformed image-only models (~78% vs. ~75–78% accuracy).
- Clinical factors such as patient age and lesion anatomical site were strong predictors.
- Traditional ML methods struggled with high-dimensional raw image data, whereas the CNN effectively learned relevant visual patterns.

## Conclusion

This project demonstrates a complete end-to-end machine learning pipeline—from data preprocessing and exploration to model training and evaluation. It highlights the value of incorporating patient context alongside visual analysis for skin lesion classification.

## Future Direction

The next phase involves developing an **ensemble model** that fuses predictions from the best tabular model (SVM) and the best image model (CNN). Early fusion, late fusion, or intermediate fusion strategies will be explored. Combining both modalities is expected to push overall accuracy beyond **85%**, resulting in a more robust and clinically useful tool for skin cancer screening.