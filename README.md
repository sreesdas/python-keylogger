# python-keylogger
A key-logger written in python using pyHook and pyWin32 modules.


## Getting Started

Download the zip or Clone the repo to start working with this project. 

This keylogger has 2 variants (online and offline).
The offline version can be found inside the archive folder, which simply outpus the keystrokes into a text file
Whereas the online variant, makes POST requests to a remote server which stores the input data.

If you have any feedback or run into issues, please file an issue on this repository.

### Prerequisites

* Python (2.7.13, 32 bit)
* PyHook <https://sourceforge.net/projects/pyhook/>
* PyWin32 <https://sourceforge.net/projects/pywin32/>
* requests 


### Installing

Download and Install Python

After installing, add _C:\Python27\_ and _C:\Python27\Scripts_ to the _Path_ env variable

Download and Install pyHook and pyWin32 from the links provided

To install requests, clone their repo and use pip command for installation

```
$ git clone git://github.com/requests/requests.git
$ cd requests
$ pip install .
 
```

For the online variant, you can either start a free web hosting account with [Hostinger](https://www.hostinger.in/) or [000WebHost] (https://in.000webhost.com/cpanel-login)
You can also use **xampp** or **wamp** to test it out in your local machine.
After you setup your server, copy the contents of _server_side_scripts_ to _C:\xampp\htdocs\_ or the _root_ folder in your hosting website.

*** Note that for the offline variant, these steps are not needed***

Once everything is set, run the _keylogger.py_ file

Now all your keystrokes will be logged into the server with a _<ipaddr>.txt_ format
You can view the file from the link <http://<your_server_name>/post/view.php>

## Compatability with Linux

Since we are using Windows specific libraries for hooking the keystrokes, this won't work 
with linux. But same code can be reused for other operating systems with minor modifications.


## Authors

* **Sreenath Sivadas** - *Initial work* - [sreesdas](https://github.com/sreesdas)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

