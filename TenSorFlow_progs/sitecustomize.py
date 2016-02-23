import site
import os
SITEPKGS = "/usr/local/site-packages"
site.addsitedir(SITEPKGS)
site.PREFIXES += ['/usr/local']
