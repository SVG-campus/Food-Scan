import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download("mdsagorahmed/fruit-image-dataset-22-classes")

print("Dataset downloaded to:", path)
