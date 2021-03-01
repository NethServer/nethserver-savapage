===================
nethserver-savapage
===================

Install and configure SavaPage: https://www.savapage.org/

SavaPage is installed inside ``/opt/savapage`` and creates a ``savapage`` system user.

Database: ::

 savapage=service
    PaperSize=a4
    TCPPorts=8631,8632,8639,5222
    UDPPort=5353
    access=green
    status=enabled

Login
=====

Go to https://NETHSERVER:8632/admin and login with username ``admin`` and password ``admin``.

User sync
=========

User sync is enabled to sync AD/LDAP users. The AD needs a valid certificate.

Links
=====

Official documentation: https://www.savapage.org/docs/manual/
