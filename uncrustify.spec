Summary:	Source code beautifier
Name:		uncrustify
Version:	0.75.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://downloads.sourceforge.net/uncrustify/%{name}-%{version}.tar.gz
# Source0-md5:	0bdae8a77605220e5790ee140e7a7018
URL:		http://uncrustify.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uncrustify is a configurable source code beautifier for C, C++, C#,
ObjectiveC, D, Java, Pawn and VALA.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog CODEOWNERS Comments.txt CONTRIBUTING.md COPYING HELP LIMITATIONS.txt NEWS README.md TESTING release-process.rst
%doc documentation
%attr(755,root,root) %{_bindir}/uncrustify
%{_mandir}/man1/uncrustify.1*
