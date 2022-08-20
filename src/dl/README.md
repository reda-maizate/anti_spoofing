## Ideas for preparing the data (v2.0.0)

### Deport the data into a Scaleway object storage bucket
All the process below is done in the form of batch jobs.
1. Download the raw data from the SW bucket.
2. Run `prepare_data.py`
3. Upload the data to the SW bucket in the processed data directory.

### Add more data

You can find below some datasets that can be used to add more data to the raw data.

- [CelebA dataset](https://drive.google.com/drive/folders/1OW_1bawO79pRqdVEVmBzp8HSxdSwln_Z)
- [ReplayMobile dataset](https://www.idiap.ch/en/dataset/replay-mobile)
- [ReplayAttack dataset](https://www.idiap.ch/en/dataset/replay-attack)