%define module HTTP

Name: haskell-%{module}
Version: 4000.0.8
Release: %mkrel 1
Summary: A library for client-side HTTP
Url: http://www.haskell.org/http
Group: Development/Other
License: BSD3
Source: http://www.haskell.org/http/download/%{module}-%{version}.tar.gz
BuildRequires: ghc hugs98 ghc-prof
BuildRequires: haddock haskell-macros
BuildRoot: %_tmppath/%name-%version-%release-root
Requires(post): ghc
Requires(preun): ghc

%description
A library for client-side HTTP

%prep
%setup -q -n %{module}-%{version}

%build
%define _cabal_setup Setup.lhs
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -rf %buildroot%{_datadir}/%{module}-%{version}/doc

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_libdir/%{module}-%{version}
%_docdir/%{module}-%{version}
%_cabal_rpm_files

%clean
rm -fr %buildroot


