# LazyCards Server

This Flask based server handles requests from the
 [LazyCards](https://github.com/salabon77mk/lazycards_android) app.

## REQUIREMENTS

* A web server (Apache / nginx)

## How to set up the Server using Apache

### Linux (Arch based distros)

**\*\*NOTE:**
These directions are identical on different distros and the only
differences are the location and name pertaining to Apache, e.g httpd is the package in 
Arch whereas in Ubuntu it's apache2, the virtualhosts file in the Ubuntu package 
has a different name, etc...

1. Install httpd
2. Add a new virtual host to httpd-vhosts.conf located at /etc/httpd/conf/extra. \n
EXAMPLE
```
<VirtualHost *:80>

    ServerName 192.168.1.207 
    ErrorLog "/var/log/httpd/lazycards/error_log"
    CustomLog "/var/log/httpd/lazycards/access_log" common
    
    WSGIProcessGroup lazycards_server
    WSGIDaemonProcess lazycards_server python-path=/srv/http/lazycards_server 
    WSGIApplicationGroup %{GLOBAL} 

    WSGIScriptAlias /lazycards /srv/http/lazycards_server/wsgi/lazycards.wsgi     
    <Directory /srv/http/lazycards_server/>
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

```
\n

ServerName should preferably be your current local host
Ensure that the python-path points to the location of your
LazyCards server

3. Install mod\_wsgi

4. In your httpd.conf (located at /etc/httpd/conf)
1. Make sure **ServerRoot** is set to where you want to place the server. Mine is /etc/httpd
2. Add **LoadModule wsgi\_module modules/mod\_wsgi.so**
3. Add **Listen 80** (or the port of your choice)

5. Place the LazyCards server in the directory where you specified your **ServerRoot**

6. In lazycards\_server/wsgi, open lazycards.wsgi
and change the path in sys.change.insert(0, **some path**) to 
**ServerRoot**/lazycards\_server
**\*\*NOTE:** if the path is somewhere in /home, make sure to chmod 755 the folders from root to where you placed the server

7. Start up httpd (sudo systemctl start httpd)

8. Start up Anki

9. Go ahead and use the Android app to start sending some requests!
