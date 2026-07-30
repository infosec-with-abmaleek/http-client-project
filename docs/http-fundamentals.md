##What HTTP is.
    HTTP short for Hyper Text Transfer Protocol. This is a set of rules governing how communication occurs between clients(browsers) and servers. HTTP allows transfer of various kinds of files such as: HTML, CSS, JavaScript, Images, Videos, PDFS, etc.
    
    
##The difference between a client and a server.
   * A client is resposible for asking/requesting for information/resources during HTTP communication. It mostly involves browsers (e.g Chrome, Firefox, Safari) and others like netcat.
    
   * A server on the other hand is responsible for receiving the client's request, processing it, and returning a valid response to the client's request. Server examples include: MS IIS, Nginx, Apache. 
    
##The structure of a URL.
    A URL is basically made up of the following: 
    * Protocl: http/https
    * Host: example.com
    * Port: 8080
    * Path: index.html
    * Query: get?name=john
    
##The structure of an HTTP request.
    GET / http/1.1
    Host: example.com
    User-Agent: MyClient
    Accept: */*
    
    
##The structure of an HTTP response.
    HTTP/1.1 200 OK 
    Content-Type: text/html
    Content-Length: 190
    
    <html>
    ...
    
##The difference between GET and POST.
    * GET is simply used to request contents/resource from a server.
    * POST is used to push contents to a server. E.g when submitting a form containing username and password.
    
##Five common HTTP status codes and what they mean.
    * 200: Success
    * 404: Not Found
    * 500: Internal Server Error:
    * 301: Permanent Redirect
    * 302: Temporary Redirect
