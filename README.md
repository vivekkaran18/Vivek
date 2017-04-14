docker build -t Ansible/Dockersfile .

docker run -p 8080:8080 -td Ansible/Dockersfile

curl http://127.0.0.1:8080/hello
