Summary:	Lpe - programmer's editor
Summary(pl):	Lpe - edytor progamisty
Name:		lpe
Version:	1.2.5
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://cdsmith.twu.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
URL:		http://cdsmith.twu.net/lpe/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	slang-devel >= 1.4.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
LPE is small, fast, full screen visual text editor designed to make
editing code easier.

%description -l pl
LPE jest ma³ym, pe³no ekranowym edytorem przeznaczonym do edycji kodu.

%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure \
    --with-modes=all
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_mandir}/cz $RPM_BUILD_ROOT%{_mandir}/cs

gzip -9nf AUTHORS BUGS CUSTOMIZE IDEAS MODES NEWS README TODO ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz data/custom.ex
%attr(755,root,root) %{_bindir}/lpe
%dir %{_libdir}/lpe
%attr(755,root,root) %{_libdir}/lpe/*.so
%attr(755,root,root) %{_libdir}/lpe/*.la
%{_datadir}/lpe

%{_mandir}/man1/lpe*
%lang(bg) %{_mandir}/bg/man1/lpe*
%lang(cs) %{_mandir}/cs/man1/lpe*
%lang(de) %{_mandir}/de/man1/lpe*
%lang(es) %{_mandir}/es/man1/lpe*
%lang(fr) %{_mandir}/fr/man1/lpe*
%lang(pl) %{_mandir}/pl/man1/lpe*
%lang(ru) %{_mandir}/ru/man1/lpe*
