from config import config
from utils.utils import get_png_files, load_or_create_dataframe, process_image


if __name__ == "__main__":
    df = load_or_create_dataframe(config.FILE_PATH)

    # Get the list of image files in the folder you want to process
    image_files = get_png_files(config.IMAGE_DIR)
    image_files.sort()

    print(image_files)
    print(df.head())

    for image_file in image_files:
        if image_file not in df["image_file"].values:
            process_image(image_file, df)

    # Save the DataFrame to a CSV file
    df.to_csv(config.FILE_PATH, index=False)
