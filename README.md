## pyPowie

#### Info
Standalone pyopencl POW server for vite.

![pyPowie](https://github.com/epy3/py-pow/actions/workflows/python.yml/badge.svg?branch=main)

#### Tasks
- [x] Compute correct POW on CPU
- [x] Compute correct POW on GPU
- [x] FastAPI endpoint
- [ ] More function checks
- [ ] Multprocessing
- [ ] Multiple compute servers support

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
FastAPI docs at http://localhost/docs | http://serverip/docs
```

