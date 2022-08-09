## Howto install pyPow on a fresh server (GPU)
EXAMPLE vultr.com -> Debian Cloud GPU 6144 MB NVIDIA A100<br><br>

```
connect to your server and login.
```
<img src="https://github.com/epy3/pyPow/blob/main/howto/step2.png" width=800>

```
git clone https://github.com/epy3/pyPow.git
cd pyPow
```
<img src="https://github.com/epy3/pyPow/blob/main/howto/step3.png" width=800>

```
pip install -r requirements.txt
```
<img src="https://github.com/epy3/pyPow/blob/main/howto/step4.png" width=800><br>
<img src="https://github.com/epy3/pyPow/blob/main/howto/step5.png" width=800>

```
uvicorn main:APP --host 127.0.0.1 --port 80
please change host and port if needed.

select the GPU device [0].
```
<img src="https://github.com/epy3/pyPow/blob/main/howto/step6.png" width=800>

```
server is now up and running!
results below.
```
<img src="https://github.com/epy3/pyPow/blob/main/howto/res1.png" width=800><br>
<img src="https://github.com/epy3/pyPow/blob/main/howto/res2.png" width=800>
