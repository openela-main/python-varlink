Name:           python-varlink
Version:        29.0.0
Release:        1%{?dist}
Summary:        Python implementation of Varlink
License:        ASL 2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros

%global _description \
An python module for Varlink with client and server support.

%description %_description

%package -n python3-varlink
Summary:       %summary
%{?python_provide:%python_provide python3-varlink}
# The varlink copr had this package under the "python-varlink"
# name. Add Obsoletes to make it easy to upgrade.
Obsoletes:     python-varlink <= 3-1.git.61.1bc637d.fc27

%description -n python3-varlink %_description

%prep
%autosetup -n python-%{version}

%build
%py3_build

%check
CFLAGS="%{optflags}" %{__python3} %{py_setup} %{?py_setup_args} check

%install
%py3_install

%files -n python3-varlink
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*

%changelog
* Wed Oct 10 2018 Harald Hoyer <harald@redhat.com> - 29.0.0-1
- fixed grammar for interface and field names
- Resolves: rhbz#1638237

* Mon Aug 06 2018 Harald Hoyer <harald@redhat.com> - 27.1.1-1
- python-varlink-27.1.1-1
- fixed varlink.cli bridge

* Fri Jul 20 2018 Harald Hoyer <harald@redhat.com> - 27.1.0-1
+ python-varlink-27.1.0-1
- add "varlink.cli bridge" support

* Fri Jul 20 2018 Harald Hoyer <harald@redhat.com> - 27.0.0-1
- python-varlink-27.0.0-1

* Thu Jun 14 2018 Harald Hoyer <harald@redhat.com> - 26.1.0-1
- python-varlink 26.1.0

* Fri May 25 2018 Harald Hoyer <harald@redhat.com> - 26.0.2-1
- python-varlink 26.0.2

* Mon May 14 2018 Harald Hoyer <harald@redhat.com> - 26-1
- python-varlink 26

* Fri May 11 2018 Harald Hoyer <harald@redhat.com> - 25-1
- python-varlink 25

* Mon May 07 2018 Harald Hoyer <harald@redhat.com> - 23-1
- python-varlink 23

* Wed Apr 25 2018 Harald Hoyer <harald@redhat.com> - 22-1
- python-varlink-22

* Wed Apr 18 2018 Harald Hoyer <harald@redhat.com> - 19-1
- python-varlink 19

* Thu Apr 12 2018 Harald Hoyer <harald@redhat.com> - 18-1
- python-varlink 18

* Wed Apr 11 2018 Harald Hoyer <harald@redhat.com> - 17-1
- python-varlink 17

* Fri Mar 23 2018 Harald Hoyer <harald@redhat.com> - 15-1
- python-varlink 15

* Mon Mar 19 2018 Harald Hoyer <harald@redhat.com> - 14-1
- python-varlink 14

* Mon Feb 26 2018 Harald Hoyer <harald@redhat.com> - 13-1
- python-varlink 13

* Wed Feb 14 2018 Harald Hoyer <harald@redhat.com> - 12-1
- python-varlink 12

* Fri Feb 09 2018 Harald Hoyer <harald@redhat.com> - 11-1
- python-varlink 11

* Fri Feb 09 2018 Harald Hoyer <harald@redhat.com> - 10-1
- python-varlink 10

* Fri Feb 09 2018 Harald Hoyer <harald@redhat.com> - 9-1
- python-varlink 9

* Thu Feb 08 2018 Harald Hoyer <harald@redhat.com> - 8-1
- python-varlink 8

* Thu Feb 08 2018 Harald Hoyer <harald@redhat.com> - 7-1
- python-varlink 7

* Thu Feb 08 2018 Harald Hoyer <harald@redhat.com> - 4-1
- python-varlink 4

* Fri Feb 02 2018 Harald Hoyer <harald@redhat.com> - 3-2
- bump release

* Fri Feb  2 2018 Harald Hoyer <harald@redhat.com> - 3-1
- python-varlink 3

* Thu Dec 14 2017 Harald Hoyer <harald@redhat.com> - 2-1
- python-varlink 2

* Tue Aug 29 2017 <info@varlink.org> 1-1
- python-varlink 1
