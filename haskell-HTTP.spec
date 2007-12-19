%define module HTTP
%define srcname http-20060707

Name: haskell-%{module}
Version: 2006.7.7
Release: %mkrel 2
Summary: A library for client-side HTTP
Url: http://www.haskell.org/http
Group: Development/Other
License: BSD3
Source: http://www.haskell.org/http/download/%{srcname}.tar.gz
BuildRequires: ghc hugs98 ghc-prof
BuildRequires: haddock
Requires(post): ghc
Requires(preun): ghc

%description
A library for client-side HTTP

%prep
%setup -q -n %{srcname}

%build
runhaskell Setup.lhs configure --prefix=%{_prefix}
runhaskell Setup.lhs build
runhaskell Setup.lhs haddock

runhaskell Setup.lhs   register --gen-script
runhaskell Setup.lhs unregister --gen-script

%install
runhaskell Setup.lhs copy --destdir=%{buildroot}

rm -rf %buildroot%{_datadir}/%{module}-%{version}/doc

%check
runhaskell Setup.lhs test

%post -f register.sh

%preun -f unregister.sh

%files
%defattr(-,root,root)
%doc dist/doc/html
%doc README
%_libdir/%{module}-%{version}

%clean
rm -fr %buildroot


