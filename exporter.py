from prometheus_client import start_http_server, Gauge
import docker
import time
import socket

HEALTH_STATUS = Gauge('container_health_status', 'Container health status', ['container_name'])
UPTIME = Gauge('container_uptime_seconds', 'Container uptime in seconds', ['container_name'])
CONTAINER_STATUS = Gauge('container_status', 'Container status', ['container_name']) 

client = docker.from_env()

def collect_metrics():
    containers = client.containers.list(all=True)  
    for container in containers:

        state = container.attrs.get('State', {})
        health = state.get('Health', {}).get('Status', 'unknown')
        status = state.get('Status', 'unknown')  
        uptime = state.get('StartedAt', 0)

      
        container_status = 3 if status == 'running' else 2 if status == 'restarting' else 1 if status == 'created' else 0 if status == 'paused' else -1 if status == 'exited' else -2  

       
        HEALTH_STATUS.labels(container_name=container.name).set(1 if health == 'healthy' else 0 if health == 'unhealthy' else 2 if health == 'starting' else -1)
        UPTIME.labels(container_name=container.name).set(time.time() - time.mktime(time.strptime(uptime[:19], "%Y-%m-%dT%H:%M:%S")))
        CONTAINER_STATUS.labels(container_name=container.name).set(container_status) 

if __name__ == "__main__":
  
    start_http_server(6678)
    while True:
        collect_metrics()
        time.sleep(10)

