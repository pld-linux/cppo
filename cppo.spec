#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		debug_package	%{nil}
Summary:	Preprocessor (cpp equivalent) for OCaml
Summary(pl.UTF-8):	Preprocesor (odpowiednik cpp) dla OCamla
Name:		cppo
Version:	1.6.8
Release:	1
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/ocaml-community/cppo/releases
Source0:	https://github.com/mjambon/cppo/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fed401197d86f9089e89f6cbdf1d660d
URL:		http://mjambon.com/cppo.html
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-dune >= 1.0
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamlbuild-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cppo is an OCaml-friendly implementation of cpp, the C preprocessor.
It can replace camlp4 for preprocessing OCaml files, using cpp style
and syntax. It allows defining simple macros and file inclusion.

%description -l pl.UTF-8
Cppo to przyjazna dla OCamla implementacja cpp - preprocesora języka
C. Może zastąpić preprocesor camlp4 przy przetwarzaniu plików OCamla z
wykorzystaniem stylu oraz składni cpp. Pozwala na definiowanie
prostych makr oraz włączanie plików.

%package -n ocamlbuild-cppo
Summary:	Cppo plugin for ocamlbuild
Summary(pl.UTF-8):	Wtyczka cppo dla ocamlbuilda
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# ocamlbuild resides in ocaml package, so don't require just ocaml-runtime
%requires_eq	ocaml

%description -n ocamlbuild-cppo
Cppo plugin for ocamlbuild.

%description -n ocamlbuild-cppo -l pl.UTF-8
Wtyczka cppo dla ocamlbuilda.

%package -n ocamlbuild-cppo-devel
Summary:	Development files for ocamlbuild_cppo library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki ocamlbuild_cppo
Group:		Development/Libraries
Requires:	ocamlbuild-cppo = %{version}-%{release}
%requires_eq	ocaml

%description -n ocamlbuild-cppo-devel
Development files for ocamlbuild_cppo library.

%description -n ocamlbuild-cppo-devel -l pl.UTF-8
Pliki programistyczne biblioteki ocamlbuild_cppo.

%prep
%setup -q

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --verbose --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# not needed (no cppo ocaml library)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/cppo/{META,dune-package,opam}
# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/cppo_ocamlbuild/ocamlbuild_cppo.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/{cppo,cppo_ocamlbuild}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE.md README.md
%attr(755,root,root) %{_bindir}/cppo
%{_examplesdir}/%{name}-%{version}

%files -n ocamlbuild-cppo
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/cppo_ocamlbuild
%{_libdir}/ocaml/cppo_ocamlbuild/META
%{_libdir}/ocaml/cppo_ocamlbuild/dune-package
%{_libdir}/ocaml/cppo_ocamlbuild/opam
%{_libdir}/ocaml/cppo_ocamlbuild/cppo_ocamlbuild.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/cppo_ocamlbuild/cppo_ocamlbuild.cmxs
%endif

%files -n ocamlbuild-cppo-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/cppo_ocamlbuild/ocamlbuild_cppo.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/cppo_ocamlbuild/ocamlbuild_cppo.cmx
%{_libdir}/ocaml/cppo_ocamlbuild/cppo_ocamlbuild.cmxa
%{_libdir}/ocaml/cppo_ocamlbuild/cppo_ocamlbuild.a
%endif
%{_libdir}/ocaml/cppo_ocamlbuild/ocamlbuild_cppo.mli
%{_libdir}/ocaml/cppo_ocamlbuild/ocamlbuild_cppo.cmt
%{_libdir}/ocaml/cppo_ocamlbuild/ocamlbuild_cppo.cmti
