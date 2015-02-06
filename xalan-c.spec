Name:           xalan-c
Version:        1.10.0
Release:        11
Summary:        Xalan XSLT processor for C

Group:          System/Libraries
License:        ASL 2.0
URL:            http://xml.apache.org/xalan-c/
Source0:        http://www.apache.org/dist/xml/xalan-c/Xalan-C_1_10_0-src.tar.gz
Patch0:         xalan-c-1.10.0-escaping.patch
Patch1:         xalan-c-1.10.0-gcc43.patch
# http://bugs.gentoo.org/attachment.cgi?id=169168
Patch2:         xalan-c-1.10.0-new-xerces-c.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  xerces-c-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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
%setup -q -n xml-xalan/c
%patch0 -p2 -b .escaping
%patch1 -p2 -b .gcc43
%patch2 -p0 -b .new-xerces-c
find -type d -name CVS -print0 | xargs -0 rm -rf
chmod 644 NOTICE


%build
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
COMMONARGS="-plinux -cgcc -xg++ -minmem -rpthreads"
%ifarch alpha ppc64 s390x sparc64 x86_64
./runConfigure ${COMMONARGS} -b64 -P %{_prefix} -C --libdir="%{_libdir}" -z '%{optflags}'
%else
./runConfigure ${COMMONARGS} -b32 -P %{_prefix} -C --libdir="%{_libdir}" -z '%{optflags}'
%endif
# _smp_mflags do not work
make


%install
rm -rf $RPM_BUILD_ROOT
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
make install DESTDIR=$RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


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

