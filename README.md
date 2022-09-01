# Anti-spoofing for face recognition

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=reda-maizate_anti_spoofing&metric=bugs)](https://sonarcloud.io/summary/new_code?id=reda-maizate_anti_spoofing) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=reda-maizate_anti_spoofing&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=reda-maizate_anti_spoofing) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=reda-maizate_anti_spoofing&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=reda-maizate_anti_spoofing) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=reda-maizate_anti_spoofing&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=reda-maizate_anti_spoofing) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=reda-maizate_anti_spoofing&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=reda-maizate_anti_spoofing)

This project was made to recognize if the given image is from live or a spoofed one.
The dataset is available on [Kaggle](https://www.kaggle.com/datasets/tapakah68/anti-spoofing).

*This project was also made to learn the entire fabric of Deep Learning life cycle.*

## Infrastructure

🚧 Currently working in the v1.0.0... 🚧

![anti_spoofing_pipeline_v1](./images/anti-spoofing_v1.png)

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