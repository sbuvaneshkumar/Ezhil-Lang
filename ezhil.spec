%define name ezhil
%define version 0.99
%define unmangled_version 0.99
%define unmangled_version 0.99
%define release 1

Summary: Ezhil - Tamil programming language implemented in Python; Ezhil works on both Python 2 and Python 3
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Muthiah Annamalai <ezhillang@gmail.com>
Url: https://github.com/Ezhil-Language-Foundation/Ezhil-Lang

%description
Ezhil is a Tamil programming language for early education

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
