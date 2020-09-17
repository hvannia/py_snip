

### docker image build -t quote:latest .


``` docker run -it c5459f99bd7d /bin/bash
    cd app
    gunicorn -b 0.0.0.0:5000 quote:app --reload
```
