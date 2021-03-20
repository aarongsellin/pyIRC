# pyIRC
pyIRC is a _userfriendly_ TCP client and server for creating your own internet relay chat system.

* End to end encryption.
* Easy setup and customizablity.
* Both TCP and HTTP protocol.

pyIRC is easy to use, _server setup Ex_:
```
>>> import pyIRC
>>> server = pyIRC.SimpleSetup(6667)
'Server setup successfull'
>>> server.StartListener()
'Listening on port 10.10.10.10:6667'
```
_client setup Ex_:
```
>>> import pyIRC
>>> client = pyIRC.SimpleClient()
>>> client.connect("10.10.10.10",6667)
'Connected to 10.10.10.10:6667'
```

# Installing
Download with ![git](https://git-scm.com/).

```$ git clone https://github.com/mrikea4real/pyIRC```

In the future you will be able to install pyIRC with ![pip](https://pip.pypa.io/en/stable/).

# Documentation
Documentation can be found in this respository in the folder __documentation__

# Contributing
I happily accpet contributions. They can come in the form of bug fixes,  Please send me an email or add me on discord _Mr Ikea#6576_

# Maintainers
* @mrikea4real (Aaron Gotthardsson)
