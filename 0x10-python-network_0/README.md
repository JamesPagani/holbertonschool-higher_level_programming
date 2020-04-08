# 0x10. Python - Network #0

Despite the name, there's only one Python file/module in this directory. Instead, it is filled with various Linux/Unix shell commands regarding the usage of `curl` to retireve the information of the HTTP messages, which are transmited when our machine's web browser tries to retireve resources with the remote server and that same server responds to the browser, either with the requested documents/files or an error.

## Contents

**0. cURL body size** (bash script): Make a request to localhost on port 5000 and retrieve the size (in bytes) of the HTTP response body.
**1. cURL to the end** (bash script): Send a *GET* request to an user-specified URL and, if it succeeds (HTTP response code 200), display the response's body.
**2. cURL Method** (bash script): Send a *DELETE* request to an user-specified URL and, if it succeeds, display the response's body.
**3. cURL only methods** (bash script): Display the HTTP methods an user-specified URL will accept.
**4. cURL headers** (bash script): Send to an user-specified URL a *GET* request and display the body of the response. The request contains an aditional header variable.
**5. cURL POST parameters** (bash script): Send a *POST* request, containing an "email" and "subject" fields (on the body) and display the response's body.
**6. Find a peak** (Python 3 module): Find the peak in a list of unsorted integers.

*Made by: Jaime Andrés Gálvez Villamarin*

