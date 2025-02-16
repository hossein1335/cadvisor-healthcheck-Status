# MONITOR_CONTAINER

## health_check_help

### metric
- container_health_status
### Metric output
- 1=healthy
- 0=unhealthy
- 2=starting
- -1=unknown and another
## container_status_help

### metric
- container_status
### Metric output
- 3=running
- 2=restarting
- 1=created
- 0=paused
- -1=exited
- -2=another
## PORT
### cadvisor
- port=6677
### health
- port=6678

