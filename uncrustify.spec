Summary:	Reformat Source
Name:		uncrustify
Version:	0.60
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/uncrustify/%{name}-%{version}.tar.gz
# Source0-md5:	0467a60b7c6f108259e69a90120afd4a
URL:		http://uncrustify.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Source Code Beautifier for C, C++, C#, D, Java, and Pawn.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING AUTHORS README NEWS
%doc documentation
%attr(755,root,root) %{_bindir}/uncrustify
%{_mandir}/man1/uncrustify.1*
%{_datadir}/%{name}
