%define tarversion  1_10_0
%define packname xml-xalan
%define minor 0
%define libname %mklibname %{name} %{minor}

Name: xalan-c
Version: 1.10
Release: %mkrel 1
License: Apache License
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	An XSLT Transformation Engine in C++
URL: http://xalan.apache.org/
Source: Xalan-C_1_10_0-src.tar.gz 
Patch0: xml-xalan-lib64.patch
BuildRequires: xerces-c-devel >= 2.7.0

%description 
Xalan is an XSL processor for transforming XML documents
into HTML, text, or other XML document types. Xalan-C++ represents an
almost complete and a robust C++ reference implementation of the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath).

#------------------------------------------------------------------------

%package -n %{libname}
Group:		Development/Other
Summary:	Library for an XSLT Transformation Engine in C++
Obsoletes:	xalan-c < 1.10-1mdv2008.0
Provides: xalan-c

%description -n %{libname}
Library for xalan-c

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc c/README
%{_bindir}/*
%{_libdir}/*.so.*

#------------------------------------------------------------------------

%package -n %{libname}-devel
Requires: %libname = %version-%release
Group: Development/Other
Summary: Developpement files for XSLT Transformation Engine
Provides: xalan-c-devel = %version-%release 
Provides: libxalan-c-devel = %version-%release
Obsoletes: xalan-c-devel

%description -n %{libname}-devel
Xalan is an XSL processor for transforming XML documents
into HTML, text, or other XML document types. Xalan-C++ represents an
almost complete and a robust C++ reference implementation of the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath).

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/xalanc/*

#------------------------------------------------------------------------

%package doc
Group:		Development/Other
Summary:	Online manual for Xalan-C, XSLT Transformation Engine

%description doc
Documentation for Xalan-C, viewable through your web server, too!

%files doc
%defattr(644 root root 755)
%doc c/LICENSE c/readme.html c/xdocs/

#------------------------------------------------------------------------

%prep
%setup -q -n %{packname}

%if "%{_lib}" != "lib"
%patch0 -p1 -b .orig
%endif

%build
rm -f c/bin/*
rm -f c/lib/*

export XALANCROOT=${RPM_BUILD_DIR}/%{packname}/c/
export XERCESCROOT=%{_includedir}/xercesc
export ICUROOT=%_prefix

cd $XALANCROOT

export CXXFLAGS="$RPM_OPT_FLAGS -fexceptions"

sh ./runConfigure \
    -p linux \
    -c gcc \
    -x c++ \
    -m nls \
    -t icu \
%if "%{_lib}" != "lib"
    -b "64" \
%else
    -b "32" \
%endif
    -P /usr \
    -m inmem \
    -C --libdir -C /usr/%_lib

make
make samples
make tests

%install
rm -rf ${RPM_BUILD_ROOT}

export XALANCROOT=${RPM_BUILD_DIR}/%{packname}/c/
cd c/
%makeinstall

%clean
rm -fr %buildroot


