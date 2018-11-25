Summary:	Source code beautifier
Name:		uncrustify
Version:	0.68.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/uncrustify/%{name}-%{version}.tar.gz
# Source0-md5:	bc184fe715cf625bda6869ce2a2a2b54
URL:		http://uncrustify.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uncrustify is a configurable source code beautifier for C, C++, C#,
ObjectiveC, D, Java, Pawn and VALA.

%prep
%setup -qc

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
%doc AUTHORS BUGS ChangeLog CODEOWNERS Comments.txt CONTRIBUTING.md COPYING HELP LIMITATIONS.txt NEWS README.md TESTING release-steps.txt working.txt
%doc documentation
%attr(755,root,root) %{_bindir}/uncrustify
%{_mandir}/man1/uncrustify.1*
