## pyPowie

#### Info
Standalone pyopencl PoW server.
Only tested on Arch linux.

![pyPowie](https://github.com/epy3/py-pow/actions/workflows/python.yml/badge.svg?branch=main)

#### Requirements
- [x] Host with a GPU
- [x] OpenCL driver
- [x] Python3

#### Tasks
- [x] Compute correct POW on CPU
- [x] FastAPI endpoint
- [x] Compute correct POW on GPU
- [x] Working example
- [ ] Multithreading for CPU
- [X] Simple logging system
- [ ] Multiple GPU support
- [ ] Pool multiple instances

#### Install and run?
```
git clone https://github.com/epy3/pyPowie.git
cd pyPowie
pip install -r requirements.txt
uvicorn main:APP --port 80
```

#### How to use?
```
Set PoW Settings to your server ip and port (if not using port 80).
```

<p float="left">
  <img src="https://github.com/epy3/pyPowie/blob/main/assets/screenshot.png" width="250">
  <img src="https://github.com/epy3/pyPowie/blob/main/assets/screenshot2.png" width="250">
  <img src="https://github.com/epy3/pyPowie/blob/main/assets/screenshot1.png" width="250">
</p>

#### Docs
```
FastAPI Swagger UI docs at http://localhost:port/docs | http://serverip:port/docs
```

