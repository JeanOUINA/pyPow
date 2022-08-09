## pyPow
<img align="right" src="https://github.com/epy3/pyPow/blob/main/assets/logo.png" width="250">

### About
Standalone PoW server in python using OpenCL and FastAPI.<br>
Only tested on linux platform.<br>
Logo (why?) created by my creative friend Dali ;)<br>

![pyPow](https://github.com/epy3/py-pow/actions/workflows/python.yml/badge.svg?branch=main)

### Requirements
- [ ] Host with a GPU
- [ ] OpenCL driver
- [ ] Python3

### Todo
- [x] Compute correct POW on CPU
- [x] FastAPI endpoint
- [x] Compute correct POW on GPU
- [x] Working example
- [x] Simple logging system
- [ ] Pool multiple instances
- [ ] Multithreading for multiple API calls*

### Install and run
```
git clone https://github.com/epy3/pyPow.git
cd pyPow
pip install -r requirements.txt
uvicorn main:APP --port 80
```

### How to use
```
Set PoW Settings to your server ip and port (if not using port 80).
```

<p float="left">
  <img src="https://github.com/epy3/pyPow/blob/main/assets/screenshot.png" width="250">
  <img src="https://github.com/epy3/pyPow/blob/main/assets/screenshot2.png" width="250">
  <img src="https://github.com/epy3/pyPow/blob/main/assets/screenshot1.png" width="250">
</p>

### Testing
```
run pytest from root directory.
```

### Docs
```
FastAPI Swagger UI docs at http://localhost:port/docs | http://serverip:port/docs
```

