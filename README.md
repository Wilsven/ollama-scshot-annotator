# Screenshot Annotator with Ollama 🦙

## How to run?

### 1. Set up the virtual environment

```zsh
conda create -n <ENV_NAME> python=3.11 -y
conda activate <ENV_NAME>
```

### 2. Install required packages

```zsh
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file and copy & paste the contents from `.env.example`. Feel free to edit these to your own needs.

```.env
FILE_PATH="data/image_descriptions.csv"
IMAGE_DIR="images"
```

### 4. Add your screenshot images into `IMAGE_DIR` folder

Ensure the path of the image directory matches the one specified in your environment variables.

### 5. Edit the prompt (Optional)

Feel free to experiment with the prompt for better results.

### 6. Run

```python
python3 screenshot_annotator.py
```

## 🔧 Further works

1. Add `argparse` functionality
2. Extend functionality to RAG systems

Feel free to make pull requests if you have any suggestions or added any useful functionalities!
