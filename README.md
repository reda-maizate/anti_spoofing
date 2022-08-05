# Anti-spoofing for face recognition

[![Maintainability](https://api.codeclimate.com/v1/badges/30072246ae93c8bb7c5b/maintainability)](https://codeclimate.com/github/reda-maizate/anti_spoofing/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/30072246ae93c8bb7c5b/test_coverage)](https://codeclimate.com/github/reda-maizate/anti_spoofing/test_coverage)


This project was made to recognize if the given image is from live or a spoofed one.
The dataset is available on [Kaggle](https://www.kaggle.com/datasets/tapakah68/anti-spoofing).

*This project was also made to learn the entire fabric of Deep Learning life cycle.*

[[_TOC_]]

## Usage

### Set up the environment

**DISCLAIMER**: If you are not using an M1 macOS, you need to update the files below.
- `enviroment.yml`
- `requirements.txt`

After updated this files, use the following command to create the conda environment:

```bash
conda env create -f environment.yml
```

### Set up the development environment

**DISCLAIMER**: If you are not using an M1 macOS, you need to update the files below.
- `enviroment-dev.yml`
- `requirements-dev.txt`

After updated this files, use the following command to create the conda environment:

```bash
conda env create -f environment-dev.yml
```