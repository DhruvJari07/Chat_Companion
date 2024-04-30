# Chat_Companion

Chat companion app to chat with your custom companion.

## Prerequisites
To run this app, you have to install docker on your machine from https://docs.docker.com/engine/install/


## running the web app

clone the git repository.

```
git clone https://github.com/DhruvJari07/Chat_Companion.git
```


open the terminal create virtual environment and install requirements.txt.

```
pip install -r requirements.txt
```

run following commands in the terminal in the same directory

```
docker pull ollama/ollama
```
```
docker build -t ollama_test .
```
```
docker compose up
```

Now open the another terminal in the same directory and run following command
```
docker container ls -a
```

You will see two containers running. Copy the container ID of the container which is using ollama/ollama image

then apply following command using that container ID
```
docker exec -it <container_ID> ollama run phi
```
Note: If you have powerful machine and want to use best llm model (Llama2) then change 'phi' with llama2 in above command and also check app_test.py to change the model there before building a docker image aobve.

open your browser and run 
localhost:8501

Your app is ready for interaction!





