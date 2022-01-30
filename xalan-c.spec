%define oname xalan_c

Name:           xalan-c
Version:        1.12
Release:        1
Summary:        Xalan XSLT processor for C

Group:          System/Libraries
License:        ASL 2.0
URL:            http://xml.apache.org/xalan-c/
Source0:         http://www.us.apache.org/dist/xalan/xalan-c/sources/xalan_c-%{version}.tar.gz

BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  icu-devel
BuildRequires:  cmake

%description
Xalan is an XSLT processor for transforming XML documents into HTML, text, or
other XML document types.

%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Group:          Development/Java
Summary:        Documentation for Xerces-C++ validating XML parser

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{oname}-%{version} -p1

rm -vf samples/configure samples/configure.in

%build
%cmake \
    -Dtranscoder=icu
%make_build

%install
%make_install -C build

rm -rf %{buildroot}%{_prefix}/share/doc/xalan-c/api


%files
%defattr(-,root,root,-)
%doc LICENSE KEYS NOTICE
%{_bindir}/Xalan
%{_libdir}/libxalan*.so.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/libxalan*.so
%{_includedir}/xalanc/


%files doc
%defattr(-,root,root,-)
%doc readme.html xdocs samples




%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 1.10.0-10
+ Revision: 734256
- rebuild
- imported package xalan-c

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - P2: fix build with xerces-c-3.x (gentoo)
    - P3: fix build with gcc-4.4.x

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.10-5mdv2009.0
+ Revision: 266068
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1.10-4mdv2009.0
+ Revision: 213156
- Recompile against current xerces-c
- Added gcc pedantic patch

* Thu Apr 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1.10-3mdv2009.0
+ Revision: 197289
- Rebuild against new xerces-c

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.10-2mdv2008.1
+ Revision: 179590
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Helio Chissini de Castro <helio@mandriva.com> 1.10-1mdv2008.0
+ Revision: 24862
- Drop old nls, using icu. Added build requires


* Wed Aug 16 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-16 15:51:22 (56379)
- New upstream stable version

* Tue Aug 15 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-15 14:34:25 (56194)
- import xalan-c-1.4-0.20040818104017.2mdk

* Mon Sep 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4-0.20040818104017.2mdk
- Rebuild to fix ticket #16486

