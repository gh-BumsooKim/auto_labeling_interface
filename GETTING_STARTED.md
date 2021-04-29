##  Getting Started with Python3 Virtual Envs

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

#### 4) Import 3rd-Party Packages

```cmd
pip install -r requirements.txt
```

#### 5) Import face_labeling

```cmd
python -c "import face_labeling as fl"
```

#### 6) In IDE

```python
import face_labeling as fl
fl.__version__
```
