Summary:	Lpe - programmer's editor.
Summary(pl):	Lpe - edytor progamisty.
Name:		lpe
Version:	1.2.5
Release:	1
Copyright:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source0:	http://cdsmith.twu.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://cdsmith.twu.net/lpe/
BuildRequires:	slang-devel >= 1.4.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
LPE is small, fast, full screen visual text editor designed to make 
editing code easier.

%description -l pl
LPE jest ma³ym, pe³no ekranowym edytorem przeznaczonym do edycji 
kodu.

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix} \
    --with-modes=all
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

mv -f %{_mandir}/cz %{_mandir}/cs

gzip -9nf AUTHORS BUGS CUSTOMIZE IDEAS MODES NEWS README TODO ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,ChangeLog,CUSTOMIZE,IDEAS,MODES,NEWS,README,TODO}.gz data/custom.ex
%attr(755,root,root) %{_bindir}/lpe
%attr(644,root,root) %{_libdir}/lpe/*.so
%attr(644,root,root) %{_libdir}/lpe/*.la
%attr(644,root,root) %{_datadir}/lpe/*

%{_mandir}/man1/lpe*
%lang(bg) %{_mandir}/bg/man1/lpe*
%lang(cs) %{_mandir}/cs/man1/lpe*
%lang(de) %{_mandir}/de/man1/lpe*
%lang(es) %{_mandir}/es/man1/lpe*
%lang(fr) %{_mandir}/fr/man1/lpe*
%lang(pl) %{_mandir}/pl/man1/lpe*
%lang(ru) %{_mandir}/ru/man1/lpe*
