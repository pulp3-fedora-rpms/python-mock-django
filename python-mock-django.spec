# Created by pyp2rpm-3.3.2
%global pypi_name mock-django

Name:           python-%{pypi_name}
Version:        0.6.10
Release:        1%{?dist}
Summary:        UNKNOWN

License:        Apache License 2.0
URL:            http://github.com/dcramer/mock-django
# Upstream doesn't include runtests.py On PyPi
# And they forgot to tag 0.6.10 on github
#Source0:        https://files.pythonhosted.org/packages/source/m/%%{pypi_name}/%%{pypi_name}-%%{version}.tar.gz
Source0:        https://github.com/dcramer/mock-django/tarball/1168d3255e0d67fbf74a9c71feaccbdafef59d21
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(django) >= 1.4
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(unittest2)

# Manually added dependencies so it builds successfully
BuildRequires:  python3dist(runtests)

%description
mock-django
~~~~~~~~~~~

A simple library for mocking certain Django behavior,
such as the ORM.

Using mock-django objects
-------------------------
Inside
your virtualenv:

.. code:: python

   >>> from django.conf import settings
>>> settings.configure() # required to convince Django it's properly configured
>>> from mock_django.query import QuerySetMock
   >>> class Post(object):...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(django) >= 1.4
Requires:       python3dist(mock)
%description -n python3-%{pypi_name}
mock-django
~~~~~~~~~~~

A simple library for mocking certain Django behavior,
such as the ORM.

Using mock-django objects
-------------------------
Inside
your virtualenv:

.. code:: python

   >>> from django.conf import settings
>>> settings.configure() # required to convince Django it's properly configured
>>> from mock_django.query import QuerySetMock
   >>> class Post(object):...


%prep
#%%autosetup -n %{pypi_name}-%{version}
%autosetup -n dcramer-mock-django-1168d32
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/mock_django
%{python3_sitelib}/mock_django-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.6.10-1
- Initial package.
