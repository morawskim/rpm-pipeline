Name:           fake-libuuid
Version:        0.1.0
Release:        1
License:        MIT
Summary:        Fake provider
Group:          Fake
Source:         README.md
Requires:       libuuid1
Provides:       libuuid
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	    noarch

%description
Responsively-App requires libuuid, but OpenSuSE provide only libuuid1.

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
