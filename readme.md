# Using miniconda for a local chatbot

### Creating a conda enviroment

```bash
conda create -n llm_chatbot
```

```bash 
conda activate llm_chatbot
```

If there is problems with the activation of conda you can use:

```bash
sourve activate base
```


## Install dependencies

These are the following dependencies you must install to properly execute a local LLM model:

```bash 
conda install conda-forge::ollama
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install groq
pip install chromadb
pip install python-dotenv


```