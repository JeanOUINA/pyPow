## pyPow
<img align="right" src="https://github.com/epy3/pyPow/blob/main/assets/logo.png" width="250">

### About
Standalone PoW server in Python using OpenCL & FastAPI.<br>
Only tested on linux platforms. (debian/ubuntu/arch)<br>
Logo <sub><sup>(why?)</sup></sub> created by my creative friend Dall-e ;)<br>

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
- [ ] Handle synchronous API calls (multithread/queue)

### Install and run

A simple tutorial with screenshots is available at https://github.com/epy3/pyPow/tree/main/howto#readme

```
git clone https://github.com/epy3/pyPow.git
cd pyPow
pip install -r requirements.txt
uvicorn main:APP --host 127.0.0.1 --port 80
change host(ip) and port if needed
```

### How to use
```
In app: set PoW Settings to your server ip and port (if not using port 80).
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

