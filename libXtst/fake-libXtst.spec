Name:           fake-libXtst
Version:        0.1.0
Release:        1
License:        MIT
Summary:        Fake provider
Group:          Fake
Source:         README.md
Requires:       libXtst6
Provides:       libXtst
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	    noarch

%description
Responsively-App requires libXtst, but OpenSuSE provide only libXtst6.

%prep
%setup -c -T

%build
cp %{SOURCE0} README

%install

%files
%defattr(-,root,root)
%doc README

%changelog
* Thu Apr 01 2021 Marcin Morawski <marcin@morawskim.pl>
-  init package
