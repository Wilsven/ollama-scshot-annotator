import glob
import os
from io import BytesIO

import pandas as pd
from ollama import generate
from PIL import Image

from config.prompt import PROMPT


def load_or_create_dataframe(filepath: str) -> pd.DataFrame:
    """
    A function to load an existing dataframe from a file or create a
    new dataframe if the file does not exist.

    Args:
        filepath (str): The name of the file path to load or create

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded or newly created data
    """

    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
    else:
        df = pd.DataFrame(columns=["image_file", "description"])
    return df


def get_png_files(image_dir: str = "images") -> list[str]:
    """Returns a list of PNG files in the specified image directory.

    Args:
        image_dir (str, optional): The path to the directory containing the image files. Defaults to "images".

    Returns:
        list[str]: A list of file paths to the PNG files in the specified directory.
    """

    return glob.glob(os.path.join(image_dir, "*.png"))


def process_image(
    image_file: str,
    df: pd.DataFrame,
    model: str = "llava:13b-v1.6",
    prompt: str = PROMPT,
) -> None:
    """Process an image and generate a description using a given model and prompt.

    Args:
        image_file (str): The file path of the image to process.
        df (pd.DataFrame): The DataFrame to which the image file and its description will be added.
        model (_type_, optional): The model to use for generating the description. Defaults to "llava:13b-v1.6".
        prompt (str, optional): The prompt to use for generating the description.. Defaults to PROMPT.
    """

    print(f"\nProcessing {image_file}\n")
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format="PNG")
            image_bytes = buffer.getvalue()

    full_response = ""
    # Generate a description of the image
    for response in generate(
        model=model, prompt=prompt, images=[image_bytes], stream=True
    ):
        # Print the response to the console and add it to the full response
        print(response["response"], end="\n\n", flush=True)
        full_response += response["response"]

    # Add a new row to the DataFrame
    df.loc[len(df)] = [image_file, full_response]
