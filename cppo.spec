#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), remove when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		debug_package	%{nil}
Summary:	cpp for OCaml
Summary(pl.UTF-8):	Wiązania cppo dla OCamla
Name:		cppo
Version:	0.9.3
Release:	3
License:	BSD
Group:		Applications
Source0:	http://mjambon.com/releases/cppo/%{name}-%{version}.tar.gz
# Source0-md5:	cfea4211ab9a7c1276537ce4fc3669b5
URL:		http://mjambon.com/cppo.html
BuildRequires:	ocaml >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cppo is an OCaml-friendly implementation of cpp, the C preprocessor.
It can replace camlp4 for preprocessing OCaml files, using cpp style
and syntax. It allows defining simple macros and file inclusion.

%description -l pl.UTF-8
Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%prep
%setup -q

%build
%{__make} -j1 all %{?with_ocaml_opt:opt} \
	CC="%{__cc} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p cppo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes LICENSE examples
%attr(755,root,root) %{_bindir}/cppo
