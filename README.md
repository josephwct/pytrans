# pytrans - transcript in python

## Installation steps (only need once)

1. download project from github 

```sh
git clone git@github.com:josephwct/pytrans.git
```

2. install required package

```sh
pip install faster-whisper ffmpeg-python
```

or 

```sh
pip3 install faster-whisper ffmpeg-python
```

## Generate subtitle

1. save your mp4 video file in the project folder

2. edit main.py , update filename to the following line

```
input_video = "RQRZo-z19u4.mp4"
````

3. open a terminal , execute the following command

```
python main.py
```

or 

```
python3 main.py
```
