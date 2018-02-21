### RPM external py2-dxr 2.0
## INITENV +PATH PYTHONPATH %i/${PYTHON_LIB_SITE_PACKAGES}
Requires: python 
BuildRequires: py2-setuptools llvm

%define dxrCommit 11844e0
%define branch master

Source0: git+https://github.com/mozilla/dxr.git?obj=%{branch}/%{dxrCommit}&export=dxr-%{dxrCommit}&module=dxr-%dxrCommit&output=/dxr-%{dxrCommit}.tgz
Patch0: py2-dxr
%define keep_archives true

%prep
%setup -n dxr-%dxrCommit
%patch0 -p1

%build
make plugins

%install
#export PYTHONUSERBASE=%{i}
#python setup.py install --user --nodeps --record=/dev/null
python setup.py install --prefix=%{i}  --single-version-externally-managed --record=/dev/null
for f in `find %{i} -type f` ;do
    perl -p -i -e "s|^#!%{cmsroot}/.*|#!/usr/bin/env python|" $f
done
