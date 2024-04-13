# Chat_Companion

Chat companion app to chat with your custom companion.

To run this app, you have install docker on your machine from https://docs.docker.com/engine/install/



clone the git repository using 
git clone https://github.com/DhruvJari07/Chat_Companion.git

open the terminal create virtual environment and install requirements.txt using
pip install requirements.txt

run following commands in the terminal in the same directory

docker pull ollama/ollama

docker build -t ollama_test .

docker compose up

open your browser and run 
localhost:8501

Your app is ready for interaction!





