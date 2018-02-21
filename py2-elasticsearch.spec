### RPM external py2-elasticsearch 1.6
## INITENV +PATH PYTHONPATH %{i}/${PYTHON_LIB_SITE_PACKAGES}

%define pip_name elasticsearch

## IMPORT build-with-pip

#%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*
