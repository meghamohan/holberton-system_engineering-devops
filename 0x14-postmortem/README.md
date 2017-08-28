# 0x11. Postmortem

### Summary:
Around 7:10 AM PST 24th August 2017 an issue was reported that some of the pages of holbertonschool.com were not accessible. System admin started debugging the issue and narrowed the issue down to pages with encoded URL. Approximately 20% of users were affected. It took approximately 7 hours to debug, fix the issue and test it and at around 2.30PM PST the website was fully operational again.

### Timeline
- **7:10AM PST** - User issue logged that some 
- **8:30AM PST** - System admins starts debugging. Narrowed issue to pages with encoded URL as all other URLs seemed to be working fine
- **9:00AM PST** - Internally it was verified that taking Nginx out of the path, the requests are getting served fine.
- **11:30AM PST** - Sysadmin discovers from Nginx error.log that the root cause of the issue is because of decoding url before sending to application server.
- **12:30AM PST** - Identified that the incorrect Nginx configuration caused issuei.
- **1:00 PM PST** - Updated Nginx configuration with the fix and all services restored to normal.
- **2:00 PM PST** - Opened a case to systest to add Nginx in end2end testing scenario

### Root Cause
Root cause was misconfiguration in Nginx causing incorrect request forwarded to the app server. All the requests with encoded URI, the Nginx configured in reverse proxy using proxy_pass configuration will decode all the requests with encoded URI before sending to origin server. All non-encoded URLs will be sent as is so no issues will be seen.

### Resolution and Recovery
When Nginx was removed from the request/response path, all the requests served fine which pointed out that the issue is with introducing Nginx as reverse proxy. With Nginx as reverse_proxy to all the client requests it was also noted only URLs with encoded parameters are failing to get response from server. Upon further debugging and looking in to the error log of Nginx, it was clear that the client request with encoded URI gets decoded before it gets sent to server. Updated Nginx proxy_pass to not use URI ( ‘/‘ or $request_uri). with this change Nginx will pass the incoming client request URI as is to the server.

### Corrective and Preventive Measures
It was noted that before pushing the application changes to support for encoded URL requests, it was never tested with existing Nginx configuration as reverse proxy. SRE team to have encoded URLs as part of their sanity test after deployment and systest team to include Ngnix in their end-to-end testing cycle to capture real deployment scenario.
