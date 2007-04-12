%define tarversion  1_10_0
%define packname xml-xalan
%define major 18
%define minor 0
%define libname %mklibname %{name} %{minor}

Name: xalan-c
Version: 1.10
Release: %mkrel 0.%{tarversion}.2
License: Apache License
Group: Development/Other
Summary:	An XSLT Transformation Engine in C++
URL: http://xalan.apache.org/
Source: Xalan-C_1_10_0-src.tar.gz 
Patch0: xml-xalan-lib64.patch
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires:	xerces-c-devel >= 2.7.0

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
Obsoletes:	xalan-c <= xalan-c-1.1-4mdk

%description -n %{libname}
Library for xalan-c

#------------------------------------------------------------------------

%package -n %{libname}-devel
Requires:	%libname = %version-%release
Group:		Development/Other
Summary:	Developpement files for XSLT Transformation Engine
Provides:	xalan-c-devel = %version-%release, libxalan-c-devel = %version-%release
Obsoletes:	xalan-c-devel

%description -n %{libname}-devel
Xalan is an XSL processor for transforming XML documents
into HTML, text, or other XML document types. Xalan-C++ represents an
almost complete and a robust C++ reference implementation of the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath).

#------------------------------------------------------------------------

%package doc
Group:		Development/Other
Summary:	Online manual for Xalan-C, XSLT Transformation Engine

%description doc
Documentation for Xalan-C, viewable through your web server, too!

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
cd $XALANCROOT
export CXXFLAGS="$RPM_OPT_FLAGS -fexceptions"
sh ./runConfigure -p linux -c gcc -x c++ -m nls
make

%install
rm -rf ${RPM_BUILD_ROOT}

export XALANCROOT=${RPM_BUILD_DIR}/%{packname}/c/
cd c/
%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc c/README
%{_bindir}/*
%{_libdir}/nls/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/xalanc/*

%files doc
%defattr(644 root root 755)
%doc c/LICENSE c/readme.html c/xdocs/



