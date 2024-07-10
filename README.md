 QA Test

This repository contains scripts and configuration files to deploy and test the frontend-backend integration using Kubernetes.

rerequisites
- Minikube installed
- Python 3.x with `requests` library

Deployment Steps
1. Start Minikube: `minikube start`
2. Deploy backend and frontend services:
   ```bash
   kubectl apply -f backend/deployment.yaml
   kubectl apply -f backend/service.yaml
   kubectl apply -f frontend/deployment.yaml
   kubectl apply -f frontend/service.yaml

3.Run the command kubectl get SVC
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
backend-service    ClusterIP      10.98.137.104    <none>        3000/TCP       3h9m
frontend-service   LoadBalancer   10.105.128.122   127.0.0.1     80:30877/TCP   3h6m
hello              ClusterIP      10.108.20.218    <none>        80/TCP         118m
kubernetes         ClusterIP      10.96.0.1        <none>        443/TCP        3h27m

4.run the command curl http://127.0.0.1

check the message.

Write the python code to verify the message 
check the code in .py file
