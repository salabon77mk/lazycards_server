# LazyCards Server

This Flask based server handles requests from the
 [LazyCards](https://github.com/salabon77mk/lazycards_android) app.

## REQUIREMENTS

* A web server (Apache / nginx)
* A [WordsAPI key(it's free!)](https://www.wordsapi.com/). 

## How to set up the Server using Apache

### Linux (Arch based distros)

**\*\*NOTE:**
These directions are identical on different distros and the only
differences are the locations and names of files pertaining to Apache, e.g httpd is the package in 
Arch whereas in Ubuntu it's apache2, the httpd-vhosts.conf file in the Ubuntu package 
has a different name, etc...

1. Install httpd
2. Add a new virtual host to httpd-vhosts.conf located at _/etc/httpd/conf/extra_
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

ServerName should preferably be your current local host
Ensure that the python-path points to the location of your
LazyCards server

3. Install mod\_wsgi

4. In your httpd.conf (located at _/etc/httpd/conf_)
    1. Make sure **ServerRoot** is set to where you want to place the server. Mine is /etc/httpd
    2. Add **LoadModule wsgi\_module modules/mod\_wsgi.so** somewhere
    3. Add **Listen 80** (or the port of your choice and makesure the port in VirtualHost reflects this change)

5. Place the LazyCards server in the directory where you specified your **ServerRoot**, in the same folder:
    1. In _/wsgi_, open lazycards.wsgi and change the path in sys.change.insert(0, **some path**) to the path of the lazycards\_server
**\*\*NOTE:** if the path is somewhere in /home, make sure to chmod 755 the folders from root to the directory of lazycards
    2. In the root directory of lazycards, create a file named "apikey.txt" and place your WordsAPI key in there.

7. Start up httpd (sudo systemctl start httpd)

8. Start up Anki

9. Go ahead and use the Android app to start sending some requests!
