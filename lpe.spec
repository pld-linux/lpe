Summary:	Lpe - programmer's editor.
Summary(pl):	Lpe - edytor progamisty.
Name:		lpe
Version:	1.2.5
Release:	1
Copyright:	GPL
Group:		Editors
Group(pl):	Edytory
Source0:	http://cdsmith.twu.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://cdsmith.twu.net/lpe/
#Patch0:		
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/lpe
%attr(644,root,root) %{_libdir}/lpe/*.so
%attr(644,root,root) %{_libdir}/lpe/*.la
%attr(644,root,root) %{_datadir}/lpe/*
