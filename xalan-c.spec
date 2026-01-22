# https://github.com/llvm/llvm-project/issues/96859
%global optflags %{optflags} -fdelayed-template-parsing

%define oname xalan_c

%define major       112
%define oldlibname  %mklibname %{name} %{major}
%define libname     %mklibname %{name}
%define develname   %mklibname %{name} -d

%define underscoreversion %(echo %{version} |sed -e 's,\\\.,_,g')_0

Name:           xalan-c
Version:        1.12
Release:        7
Summary:        Xalan XSLT processor for C

Group:          System/Libraries
License:        ASL 2.0
URL:            https://xml.apache.org/xalan-c/
Source0:        https://github.com/apache/xalan-c/releases/download/Xalan-C_%{underscoreversion}/xalan_c-%{version}.tar.gz

BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  icu-devel
BuildSystem:	cmake
BuildOption:	-Dtranscoder=icu

Requires:       %{libname} = %{version}-%{release}

%description
Xalan is an XSLT processor for transforming XML documents into HTML, text, or
other XML document types.

%package -n %{libname}
Summary:        Xalan-C++ XSLT processor
Group:          System/Libraries
# Renamed after 5.0
%rename %{oldlibname}

%description -n %{libname}
Xalan is an XSLT processor for transforming XML documents into HTML, text, or
other XML document types.

This package contains the shared xalan-c library.

%package -n %{develname}
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{develname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Group:          Development/Java
Summary:        Documentation for Xerces-C++ validating XML parser

%description doc
Documentation for %{name}.

%prep -a
# ICU headers included by Xalan are incompatible with
# the requested C++14 (they use std::is_same_v)
sed -i -e 's,CMAKE_CXX_STANDARD 14,CMAKE_CXX_STANDARD 17,g' CMakeLists.txt

rm -vf samples/configure samples/configure.in

%files
%defattr(-,root,root,-)
%doc LICENSE KEYS NOTICE
%{_bindir}/Xalan

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/xalanc
%{_libdir}/lib*.so
%{_libdir}/cmake/XalanC/*.cmake
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%defattr(-,root,root,-)
%doc readme.html samples
%doc %{_docdir}/xalan-c
