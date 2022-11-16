Name:		texlive-verifica
Version:	56625
Release:	1
Summary:	Typeset (Italian high school) exercises
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verifica
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verifica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verifica.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verifica.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class provides various environments and commands to
produce the typical exercises contained in a test. It is mainly
intended for Italian high school teachers, as the style is
probably more in line with Italian high school tests.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/verifica
%{_texmfdistdir}/tex/latex/verifica
%doc %{_texmfdistdir}/doc/latex/verifica

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
