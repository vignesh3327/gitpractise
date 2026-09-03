from kubernetes import client, config

# Load in-cluster config
config.load_incluster_config()

# Create API client
v1 = client.CoreV1Api()

# List pods in current namespace
pods = v1.list_namespaced_pod(namespace="dieloitte")

for pod in pods.items:
    # (The rest of the loop is cut off in the video, but typically you would print the pod name here, e.g.:)
    print(pod.metadata.name)
