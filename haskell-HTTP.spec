%global debug_package %{nil}
%define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module HTTP
Name:           haskell-%{module}
Version:        4000.2.6
Release:        1
Summary:        A library for client-side HTTP
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  haskell(network)
buildrequires:  haskell(parsec)
Requires(pre):  ghc
requires(pre):  haskell(network)
requires(pre):  haskell(parsec)

%description
The HTTP package supports client-side web programming in Haskell. It lets you
set up HTTP connections, transmitting requests and processing the responses
coming back, all from within the comforts of Haskell. It's dependent on the
network package to operate, but other than that, the implementation is all
written in Haskell.
.
A basic API for issuing single HTTP requests + receiving responses is provided.
On top of that, a session-level abstraction is also on offer  (the
@BrowserAction@ monad); it taking care of handling the management of persistent
connections, proxies, state (cookies) and authentication credentials required
to handle multi-step interactions with a web server.
.
The representation of the bytes flowing across is extensible via the use of a
type class, letting you pick the representation of requests and responses that
best fits your use.  Some pre-packaged, common instances are provided for you
(@ByteString@, @String@.)
.
Here's an example use:
.
>
>    do
>      rsp <- Network.HTTP.simpleHTTP (getRequest "http://www.haskell.org/")
>              -- fetch document and return it (as a 'String'.)
>      fmap (take 100) (getResponseBody rsp)
>
>    do
>      (_, rsp)
>         <- Network.Browser.browse $ do
>               setAllowRedirects True -- handle HTTP redirects
>               request $ getRequest "http://www.haskell.org/"
>      return (take 100 (rspBody rsp))

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

#% check
#% _cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



