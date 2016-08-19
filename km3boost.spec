# $Id$
Name:           km3boost
Version:        1.55
Release:        2
Summary:        The Boost C++ headers and shared development libraries

Group:          System Environment/Libraries
License:        Boost
URL:            http://www.boost.org/
Source0:        boost_1_55_0.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bzip2-devel, python-devel, python-libs
Requires: bzip2, python-libs
%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%prep
%setup -q -n boost_1_55_0

%build
BOOST_ROOT=`pwd`
export BOOST_ROOT
./bootstrap.sh --prefix=$RPM_BUILD_ROOT/usr/local --with-toolset=gcc --with-icu --with-libraries=thread,chrono,random,program_options,thread,atomic,timer

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
./b2 install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,-)
/usr/local/lib/libboost_*
/usr/local/include/boost/*

%changelog
* Tue Jun 16 2015 Carmelo Pellegrino <cpellegrino@km3net.de> 0.2
- Timer library added.
* Wed Oct 29 2014 Carmelo Pellegrino <cpellegrino@km3net.de> 0.1
- First release with chrono, random, program_options, thread and atomic.
