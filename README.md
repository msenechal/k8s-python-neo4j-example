# k8s-python-neo4j-example
Example of a FastAPI backend connecting to neo4j on k8s

Update .env with your creds

At root:

1. Build the docker image
```shell
docker build -t my_fastapi_app .
```

2. Create k8s secret with the .env variables
```shell
kubectl create secret -n neo4j generic neo4j-secrets --from-env-file=.env
```

3. Apply K8s Deployment and Service
```shell
kubectl apply -n neo4j -f k8s/deployment.yaml
kubectl apply -n neo4j -f k8s/service.yaml
```

4. Access http://localhost:30080/neo4j and that should return 5 nodes from your Neo4j DB through your fastAPI backend