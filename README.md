# face labeling

auto labeling for faster-rcnn, yolo model label format

## Environment

- windows OS (Linux is not officially supported OS)
- python 3.7.9 (Recommended), Upper than 3.6.x
- requirments.txt

## Guide

Shortcut | Description | 
--- | --- |
<kbd>q</kbd> | Exit |
<kbd>w</kbd> | Capture 1 Image |
<kbd>e</kbd> | (Auto)Capture [MAX_NUM] Image |

##  Getting Started

#### 1) Install IDE

- Using Aanacond **[here](https://www.anaconda.com/)**

#### 2) Make Dir

```cmd
cd [your_dir_path]
mkdir [dir_name]
```

#### 3) Make Virtual Envs

(if you use python3 venv)

```cmd
cd [your_dir_path]
python -m venv .venv
source .venv/bin/activate
```

(if you use Anaconda3)

```cmd
conda create -n venv python=3.7.9
conda activate venv
```

#### 4) Import Sub Package

```cmd
pip install -r requirements.txt
```

#### 5) Import face_labeling Package

```cmd
python -c "import face_labeling as fl"
```

#### 6) In IDE (such as Spyder)

```python
import face_labeling as fl
fl.__version__
```
