## pyPowie
<img align="right" src="https://github.com/epy3/pyPowie/blob/main/assets/logo.png" width="250">

### About
No idea why this project is named pyPowie.<br>
No clue how to use github markup.<br><br>

Standalone pyopencl PoW server.<br>
Only tested on Arch linux.<br>
Logo created by my friend Dali ;)<br>

![pyPowie](https://github.com/epy3/py-pow/actions/workflows/python.yml/badge.svg?branch=main)

### Requirements
- [ ] Host with a GPU
- [ ] OpenCL driver
- [ ] Python3

### Todo
- [x] Compute correct POW on CPU
- [x] FastAPI endpoint
- [x] Compute correct POW on GPU
- [x] Working example
- [X] Simple logging system
- [ ] Pool multiple instances
- [ ] Multithreading for multiple API calls*

### Install and run
```
git clone https://github.com/epy3/pyPowie.git
cd pyPowie
pip install -r requirements.txt
uvicorn main:APP --port 80
```

### How to use
```
Set PoW Settings to your server ip and port (if not using port 80).
```

<p float="left">
  <img src="https://github.com/epy3/pyPowie/blob/main/assets/screenshot.png" width="250">
  <img src="https://github.com/epy3/pyPowie/blob/main/assets/screenshot2.png" width="250">
  <img src="https://github.com/epy3/pyPowie/blob/main/assets/screenshot1.png" width="250">
</p>

### Tests
```
run pytest in root directory.
<< pytest
```

### Docs
```
FastAPI Swagger UI docs at http://localhost:port/docs | http://serverip:port/docs
```

