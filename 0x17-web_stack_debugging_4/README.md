# Concepts to learn
- For the benchmarking, ApacheBench can be used which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. 
- Issue after checking the logs was found to be that Nginx reached the limit on the number of files it can open simultaneously.
- Open Nginx configuration file
- Set this variable after the worker_processes entry line:
- worker_rlimit_nofile 10000;
- Restart Nginx
