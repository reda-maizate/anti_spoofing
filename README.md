# Anti-spoofing for face recognition

[![Maintainability](https://api.codeclimate.com/v1/badges/30072246ae93c8bb7c5b/maintainability)](https://codeclimate.com/github/reda-maizate/anti_spoofing/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/30072246ae93c8bb7c5b/test_coverage)](https://codeclimate.com/github/reda-maizate/anti_spoofing/test_coverage)


This project was made to recognize if the given image is from live or a spoofed one.
The dataset is available on [Kaggle](https://www.kaggle.com/datasets/tapakah68/anti-spoofing).

*This project was also made to learn the entire fabric of Deep Learning life cycle.*

## Usage

### Set up the environment

#### For conda
Use the following command to create a conda environment:

```bash
conda create -n anti_spoofing_env python=3.8 --file requirements.txt
```
Use the following command to activate the environment:

```bash
conda activate anti_spoofing_env
```

Use the following command to deactivate the environment:

```bash
conda deactivate
```

#### For virtual environment
Use the following command to create a virtual environment:

```bash
virtualenv -p python3.8 anti_spoofing_env
```
Use the following command to activate the environment:

```bash
source anti_spoofing_env/bin/activate
```

Use the following command to install all the dependencies:

```bash
pip install -r requirements.txt
```

Use the following command to deactivate the environment:

```bash
source deactivate
```